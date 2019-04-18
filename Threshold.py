import numpy as np
from sympy import *
import EMG
from scipy.stats.distributions import chi2
#Reference paper is Xu & Adler (2004)
#At least for now...
#All variable names come from there

#Need an ndarray of trials
#Set-up in EMG class or here?
#NOTE: This class might actually be useless,
#as I believe it is for offline detection
def Gen_Zi(data):
    """Generates Zi for a given trial"""
    Zi = np.empty(len(data),1)
    
    for rowNum in range(len(data)):
        xi_sqr = np.power(data[rowNum,:],2)
        Zi[rowNum] = np.sum(xi_sqrt)

    return Zi

def Cal_PZeta(m,LowerL,Pfa):
    """Calculates probability that noise will cross the threshold
    given the number of sampls, m, smallest number of consecutive
    crossings, LowerL, and a user set probability of false activation,
    PZeta."""

    #Define Symbols
    k, P = symbols('k P')

    #Define probability term
    prob_term = (P**k)*(1 - P)**(m - k)

    #Define binomial term
    B_coef = binomial(m,k)

    #Define term for sum
    Sum_term = prob_term * B_coef

    #Define Sum
    Final_eqn = Sum(Sum_term,(k,LowerL,m))

    #Create polynomial
    poly = Poly(Final_eqn.doit() - Pfa)

    #Create list of real roots
    real_roots = np.roots(np.array(poly.coeffs()))
    real_roots = real_roots[np.isreal(real_roots)]

    #Return this?
    #Write another function to evaluate inv. chi^2 as a funciton of data
    #And a third to evalute the threshold as a function of this value and chi^2
    return np.real(real_roots[real_roots < 1][0])


#DF comes from the number of noise samples?
def DetermineThresh(DF,NoiseVar,Pzeta):

    return NoiseVar * chi2.ppf(1 - Pzeta,DF)

#TODO: Keep this as a separate module?
#Make a separate module for actual detection of motion?


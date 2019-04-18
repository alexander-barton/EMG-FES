import serial
import numpy as np
from scipy.signal import hilbert

#Do I want the EMG object to just be an object or an array?
#Also do I want EMG to be an abstract class?  Probably
#Add sampling frequency?  Whether or not it needs filtering?
class EMG(object):
    """A live instance of EMG data.  Continually reads input from ports
    every 50 ms and updates.

    Attributes:
    #TODO"""

    #TODO: Make eType be a binary category
    #Unsure if sampling frequency of the device can be read from port
    def __init__(self,portNum,eType,Freq):
        """Opens an EMG connection to *portNum* with type **eType**
        eType is weather it is a template OR live EMG recording.."""
        self.portNum = portNum
        self.eType = eType
        self.Freq = Freq
        #Set data size depending on type of template
        if self.eType == 'TEMPLATE':
            self.data = np.empty(1,10*Freq)
        else:
            self.data = np.empty(1,np.floor(0.05*Freq))

            
    def read(self):
        """Opens the connection to the port and reads the data.
        Returns 10 seconds of data for template, returns 50 ms
        of data for live recording."""
        port = serial.Serial(portNum)
        if self.eType == 'TEMPLATE':
            self.data = port.read(timeout=10)
        else:
            self.data = port.read(timeout=0.050)

    def rectify(self):
        """Rectifies the recorded EMG signal.  Returns <<ERROR>>?
        if data is empty"""
        mew = np.mean(self.data)
        self.data = self.data - mew
        self.data = np.abs(self.data)
        #Got rid of this as we want zero meaned data
        #self.data = self.data + mew


    def envelope(self):
        """Returns a numpy array of the envelope of the data"""
        return np.abs(hilbert(self.data))


    #Temp Function to set for test data
    def setData(self,input):
        self.data = input

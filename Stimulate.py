import numpy as np

#TODO: should it take the EMG objects or just the data?
def Determine_Level(Goal,Current):
    """Determines the stimulation level to apply based on difference in 
    EMG signals.  'Goal' and 'Current' are both EMG objects."""

    Env_Goal = Goal.envelope()
    Env_Current = Current.envelope()

    return np.mean(Env_Goal - Env_Current)


"""
functions for data io
"""

from scipy.io.wavfile import read as WAV_read
from scipy.io.wavfile import write as WAV_write
import os
import re
import numpy as np



# --------------------------------------------------------------------------------------------
# Classes
# --------------------------------------------------------------------------------------------

class WaverIn():
    """A class to load waves into np.arrays"""

    __slots__ = ['dirpath', 'size', 'samples', 'n']

    def __init__(self, dirpath, size, n):
        """initialize the wave reader"""
        self.dirpath = dirpath
        self.size = size
        self.n = n
        self.samples = None

    
    def load_samples(self):
        """Method to load .wavs into numpy arrays from a 
        directory path. Depends on attributes on instaniation.

        Returns:
            - wavs
        """

        for f in os.listdir(dirpath):
            print(f)


        # try:
        #     wav_array = WAV_read(dirpath)
        #     return wav_array
        # except ValueError as ve:
        #     print(f"Error for `{dirpath}`: {ve}")
        #     return None, None




# --------------------------------------------------------------------------------------------
# Functions
# --------------------------------------------------------------------------------------------


def load_wav(filepath):
    """A function to load a given filepath into
    a np.array

    Args:
        - filepath (str): DUH
    Returns:
        - tuple: sample rate and amplitude matrix
    """
    try:
        wav_array = WAV_read(filepath)
        return wav_array
    except ValueError as ve:
        print(f"Error for `{filepath}`: {ve}")
        return None, None


def write_wav(filepath, wav_array, bit_type="int16", sr=44100):
    """A function to load a given filepath into
    a np.array

    Args:
        - filepath (str): DUH
    Returns:
        - tuple: sample rate and amplitude matrix
    """
    wav_array = wav_array.astype(bit_type)
    print ("about to save wav array")
    print (wav_array)
    return WAV_write(filepath, sr, wav_array)

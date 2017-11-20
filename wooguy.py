from scipy.io import wavfile
from scipy import fftpack
import numpy as np
import matplotlib.pyplot as plt
import math


# Import wav file
(rate, data) = wavfile.read('wooguy.wav') # stereo wavfile
(data_rows, data_cols) = data.shape
duration = data_rows / rate

data = data[:, 0] # left channel
#data = data[:, 1] # right channel


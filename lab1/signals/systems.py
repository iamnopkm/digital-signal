import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack as fft
from signals.given_info import *


def impulse_response():
    plt.plot(Impulse_response)
    plt.title ('impulse respone')
    
def convert():
    plt.subplot(2, 3, 1)
    freqency = fft.fft(Impulse_response)
    plt.plot(freqency)
    
    plt.subplot(2, 3, 2)
    real = np.real(freqency)
    plt.plot(real)
    
    plt.subplot(2, 3, 3)
    imag = np.imag(freqency)
    plt.plot(imag)
    
    plt.subplot(2, 3, 4)
    mag = np.abs(freqency)
    plt.plot(mag)
    
    plt.subplot(2, 3, 5)
    phase = np.angle(freqency)
    plt.plot(phase)
    
def output():
    
    # output1 is the output using time convolution
    plt.subplot(1, 2, 1)
    output1 = np.convolve(Impulse_response, Input_1kHz_15kHz, mode='full')
    plt.plot(output1)
   
   # output2 is the output using frequency multiplication
    plt.subplot(1, 2, 2)
    output2 = np.multiply(np.fft.fft(Impulse_response), np.fft.fft(Input_1kHz_15kHz))
    output2 = fft.ifft(output2)
    plt.plot(output2)
    
    
def convert_output():
    output1 = np.convolve(Impulse_response, Input_1kHz_15kHz, mode='full')
    
    plt.subplot(2, 3, 1)
    freqency = fft.fft(output1)
    plt.plot(output1)
    
    plt.subplot(2, 3, 2)
    real = np.real(freqency)
    plt.plot(real)
    
    plt.subplot(2, 3, 3)
    imag = np.imag(freqency)
    plt.plot(imag)
    
    plt.subplot(2, 3, 4)
    mag = np.abs(freqency)
    plt.plot(mag)
    
    plt.subplot(2, 3, 5)
    phase = np.angle(freqency)
    plt.plot(phase)
    

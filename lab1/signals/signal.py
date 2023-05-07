import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack as fft
from .given_info import Input_1kHz_15kHz


def time_domain():
    plt.plot(Input_1kHz_15kHz)
    plt.title ('Time Domain Signal')
    plt.xlabel ('Time')
    plt.ylabel ('Amplitude')
    
    
def frequency_domain():
    frequency = fft.fft(Input_1kHz_15kHz)
    plt.title ('Frequency Domain Signal')
    plt.xlabel ('Frequency')
    plt.ylabel ('Amplitude')
    plt.plot(frequency)
    
def real_domain():
    real = np.real(fft.fft(Input_1kHz_15kHz))
    plt.xlabel ('Frequency')
    plt.ylabel ('Amplitude')
    plt.title ('Real Domain Signal')
    plt.xlabel ('Real')
    plt.ylabel ('Amplitude')
    plt.plot(real)
    
    
def imaginary_domain():
    imag = np.imag(fft.fft(Input_1kHz_15kHz))
    plt.xlabel ('Imaginary')
    plt.ylabel ('Amplitude')
    plt.title ('Imaginary Domain Signal')
    plt.plot(imag)
    
def magnitude_domain():
    mag = np.abs(fft.fft(Input_1kHz_15kHz))
    plt.xlabel ('Magnitude')
    plt.ylabel ('Amplitude')
    plt.title ('Magnitude Domain Signal')
    plt.plot(mag)
    
def phase_domain():
    phase = np.angle(fft.fft(Input_1kHz_15kHz))
    plt.xlabel ('Phase')
    plt.ylabel ('Amplitude')
    plt.title ('Phase Domain Signal')
    plt.plot(phase)
    
def inverse():
    inverse = fft.ifft(fft.fft(Input_1kHz_15kHz))
    plt.title ('Time Domain Signal')
    plt.xlabel ('Time')
    plt.ylabel ('Amplitude')
    plt.plot(inverse)
    

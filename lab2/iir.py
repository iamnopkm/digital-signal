import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack as fft
import scipy.signal as sgl
from given_info import Input_1kHz_15kHz



def chebyshev():
    b, a = sgl.cheby1(10, 1, 15, "low", fs=len(Input_1kHz_15kHz))
    w, h = sgl.freqs(b, a)

    plt.semilogx(w, 20 * np.log10(abs(h)))
    plt.xlabel("Frequency representation of Chebyshev filter")
    plt.show()

    output = sgl.filtfilt(b, a, Input_1kHz_15kHz)

    plt.subplot(2, 2, 1)
    plt.plot(Input_1kHz_15kHz, "r.", ms=2)
    plt.xlabel("Input in time domain")

    plt.subplot(2, 2, 2)
    plt.plot(np.abs(fft.fft(Input_1kHz_15kHz)))
    plt.xlabel("Input in frequency domain")

    plt.subplot(2, 2, 3)
    plt.plot(output, "r.", ms=2)
    plt.xlabel("Output in time domain")

    plt.subplot(2, 2, 4)
    plt.plot(np.abs(fft.fft(output)))
    plt.xlabel("Output in frequency domain")

    plt.show()


def butterworth():
    b, a = sgl.butter(10, 15, "low", fs=len(Input_1kHz_15kHz))
    w, h = sgl.freqs(b, a)

    plt.semilogx(w, 20 * np.log10(abs(h)))
    plt.xlabel("Frequency representation of Butterworth filter")
    plt.show()

    output = sgl.filtfilt(b, a, Input_1kHz_15kHz)

    plt.subplot(2, 2, 1)
    plt.plot(Input_1kHz_15kHz, "r.", ms=2)
    plt.xlabel("Input in time domain")

    plt.subplot(2, 2, 2)
    plt.plot(np.abs(fft.fft(Input_1kHz_15kHz)))
    plt.xlabel("Input in frequency domain")

    plt.subplot(2, 2, 3)
    plt.plot(output, "r.", ms=2)
    plt.xlabel("Output in time domain")

    plt.subplot(2, 2, 4)
    plt.plot(np.abs(fft.fft(output)))
    plt.xlabel("Output in frequency domain")

    plt.show()


def bessel():
    b, a = sgl.bessel(10, 15, "low", fs=len(Input_1kHz_15kHz))
    w, h = sgl.freqs(b, a)

    plt.semilogx(w, 20 * np.log10(abs(h)))
    plt.xlabel("Frequency representation of Bessel filter")
    plt.show()

    output = sgl.filtfilt(b, a, Input_1kHz_15kHz)

    plt.subplot(2, 2, 1)
    plt.plot(Input_1kHz_15kHz, "r.", ms=2)
    plt.xlabel("Input in time domain")

    plt.subplot(2, 2, 2)
    plt.plot(np.abs(fft.fft(Input_1kHz_15kHz)))
    plt.xlabel("Input in frequency domain")

    plt.subplot(2, 2, 3)
    plt.plot(output, "r.", ms=2)
    plt.xlabel("Output in time domain")

    plt.subplot(2, 2, 4)
    plt.plot(np.abs(fft.fft(output)))
    plt.xlabel("Output in frequency domain")

    plt.show()

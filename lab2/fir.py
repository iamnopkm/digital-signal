import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack as fft
import scipy.signal as sgl
from given_info import Input_1kHz_15kHz




def bartlett():
    window = sgl.windows.bartlett(50)

    plt.subplot(2, 1, 1)
    plt.plot(window)
    plt.xlabel("Time representation of Bartlett window")

    norm = fft.fft(window, 2000) / (len(window) / 2.0)
    freq = np.linspace(-0.5, 0.5, len(norm))
    response = np.abs(fft.fftshift(norm / abs(norm).max()))

    plt.subplot(2, 1, 2)
    plt.plot(freq, response)
    plt.xlabel("Frequency representation of Bartlett window")
    plt.show()

    output = np.convolve(Input_1kHz_15kHz, window)

    plt.subplot(2, 2, 1)
    plt.plot(Input_1kHz_15kHz, "r.", ms=2)
    plt.xlabel("Input in time domain")

    freq_input = np.abs(fft.fft(Input_1kHz_15kHz))
    plt.subplot(2, 2, 2)
    plt.plot(freq_input)
    plt.xlabel("Input in frequency domain")

    plt.subplot(2, 2, 3)
    plt.plot(output, "r.", ms=2)
    plt.xlabel("Output in time domain")

    plt.subplot(2, 2, 4)
    plt.plot(np.abs(fft.fft(output)))
    plt.xlabel("Output in frequency domain")

    plt.show()


def hamming():
    window = sgl.windows.hamming(50)

    plt.subplot(2, 1, 1)
    plt.plot(window)
    plt.xlabel("Time representation of Hamming window")

    norm = fft.fft(window, 2000) / (len(window) / 2.0)
    freq = np.linspace(-0.5, 0.5, len(norm))
    response = np.abs(fft.fftshift(norm / abs(norm).max()))

    plt.subplot(2, 1, 2)
    plt.plot(freq, response)
    # plt.plot(fft.fft(window), markerfmt=" ")
    # plt.axis([-0.5, 0.5, -120, 0])
    plt.xlabel("Frequency representation of Hamming window")
    plt.show()

    output = np.convolve(Input_1kHz_15kHz, window)

    plt.subplot(2, 2, 1)
    plt.plot(Input_1kHz_15kHz, "r.", ms=2)
    plt.xlabel("Input in time domain")

    freq_input = np.abs(fft.fft(Input_1kHz_15kHz))
    plt.subplot(2, 2, 2)
    plt.plot(freq_input)
    plt.xlabel("Input in frequency domain")

    plt.subplot(2, 2, 3)
    plt.plot(output, "r.", ms=2)
    plt.xlabel("Output in time domain")

    plt.subplot(2, 2, 4)
    plt.plot(np.abs(fft.fft(output)))
    plt.xlabel("Output in frequency domain")

    plt.show()


def blackman():
    window = sgl.windows.blackman(50)

    plt.subplot(2, 1, 1)
    plt.plot(window)
    plt.xlabel("Time representation of Blackman window")

    norm = fft.fft(window, 2000) / (len(window) / 2.0)
    freq = np.linspace(-0.5, 0.5, len(norm))
    response = np.abs(fft.fftshift(norm / abs(norm).max()))

    plt.subplot(2, 1, 2)
    plt.plot(freq, response)
    # plt.plot(fft.fft(window), markerfmt=" ")
    # plt.axis([-0.5, 0.5, -120, 0])
    plt.xlabel("Frequency representation of Blackman window")
    plt.show()

    output = np.convolve(Input_1kHz_15kHz, window)

    plt.subplot(2, 2, 1)
    plt.plot(Input_1kHz_15kHz, "r.", ms=2)
    plt.xlabel("Input in time domain")

    freq_input = np.abs(fft.fft(Input_1kHz_15kHz))
    plt.subplot(2, 2, 2)
    plt.plot(freq_input)
    plt.xlabel("Input in frequency domain")

    plt.subplot(2, 2, 3)
    plt.plot(output, "r.", ms=2)
    plt.xlabel("Output in time domain")

    plt.subplot(2, 2, 4)
    plt.plot(np.abs(fft.fft(output)))
    plt.xlabel("Output in frequency domain")

    plt.show()
    
    

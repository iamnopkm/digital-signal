import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack as fft
from signals.given_info import *
from scipy import signal


sampling_rate = 300
    

# Define the sampling frequency
fs = 1000 

# Define the lowpass filter parameters
cutoff_freq = 50
filter_order = 20


def modify_impulse_respone():
    

    # Create the lowpass filter
    nyquist_freq = 0.5 * fs
    normalized_cutoff_freq = cutoff_freq / nyquist_freq
    b, a = signal.butter(filter_order, normalized_cutoff_freq, btype='lowpass')

    # Apply the filter to the ECG signal
    filtered_signal = signal.filtfilt(b, a, ECG)

    # Plot the original and filtered signals
    t = np.arange(len(ECG)) / fs
    fig, ax = plt.subplots()
    ax.plot(t, ECG, label='Original Signal')
    ax.plot(t, filtered_signal, label='Filtered Signal')
    ax.legend()
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Amplitude')
    ax.set_title('ECG Signal with Lowpass Filter')
    plt.show()
    
def ecg():
    
    # Generate white noise with mean 0 and standard deviation 0.1
    noise = np.random.normal(0, 0.1, len(ECG))
    # Add noise to the ECG signal
    noisy_ecg_signal = ECG + noise

    # Define a low-pass filter with a cutoff frequency of 100 Hz
    cutoff_freq = 100
    nyquist_freq = 0.5 * sampling_rate
    normalized_cutoff_freq = cutoff_freq / nyquist_freq
    filter_order = 4
    b, a = signal.butter(filter_order, normalized_cutoff_freq, btype='lowpass')

    # Apply the filter to the noisy ECG signal
    filtered_ecg_signal = signal.filtfilt(b, a, noisy_ecg_signal)

    t = np.arange(len(ECG)) / fs
    fig, ax = plt.subplots()
    ax.plot(t, noisy_ecg_signal, label='Noisy Signal')
    ax.plot(t, filtered_ecg_signal, label='Filtered Signal')
    ax.legend()
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Amplitude')
    ax.set_title('ECG Signal with Noise and with Filter')
    plt.show()




    
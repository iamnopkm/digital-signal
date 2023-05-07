import matplotlib.pyplot as plt
from .signal import *


def run_plot(option: int):
    if option == 1:
        time_domain()
        plt.show()
    elif option == 2:
        frequency_domain()
        plt.show()
    elif option == 3:
        real_domain()
        plt.show()
    elif option == 4:
        imaginary_domain()
        plt.show()
    elif option == 5:
        magnitude_domain()
        plt.show()
    elif option == 6:
        phase_domain()
        plt.show()
    else:
        print("\nYour option is not in the list")
    

def plot_signal():
    while True:
        print(f'''Choose 1 option:
                1. plot time domain signal
                2. plot frequency domain signal
                3. plot real signal
                4. plot imaginary siganl
                5. plot magnitude signal
                6. plot phase signal
              ''')
        
        option: int = int(input("Option: "))
        run_plot(option)
        
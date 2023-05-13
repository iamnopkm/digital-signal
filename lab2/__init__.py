from fir import *
from iir import *
import matplotlib.pyplot as plt

def fir():
    while True:
        print("1 - Bartlett window")
        print("2 - Hamming window")
        print("3 - Blackman window")
        print("4 - exit")

        choice = int(input("choice: "))

        match choice:
            case 1:
                bartlett()
            case 2:
                hamming()
            case 3:
                blackman()
            case 4:
                break
            case _:
                print("\nYour option is not in the list")   
                
def iir():
    while True:
        print("1 - Chebyshev filter")
        print("2 - Butterworth filter")
        print("3 - Bessel filter")
        print("4 - exit")

        choice = int(input("choice: "))

        match choice:
            case 1:
                chebyshev()
            case 2:
                butterworth()
            case 3:
                bessel()
            case 4:
                break
            case _:
                print("\nYour option is not in the list")   
                
def run_menu(option: int):
    if option == 1:
        fir()
    elif option == 2:
        iir()
    else:
        print("\nYour option is not in the list")   
        
if __name__ == "__main__":
    print(f'''Choose 1 option:
                1. fir
                2. iir
              ''')
    option: int = int(input("What is your choice: "))
    run_menu(option)
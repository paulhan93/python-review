# Date: Apr. 9, 2026
# Author: Paul Han
# Celsius to Fahrenheit converter

import sys

def celsius_to_fahrenheit(temp: float):
    return (temp * 1.8) + 32

def main(temp: float):
    f_temp = celsius_to_fahrenheit(temp)
    print(f"{temp} Celsius -> {f_temp:.2f} Fahrenheit")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            main(float(sys.argv[1]))
        except ValueError:
            print("Please ensure the input is a number")
    else:
        print("Usage: python celsius_converter.py <temperature in celsius>")

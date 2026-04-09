# Date: Apr. 9, 2026
# Author: Paul Han
# Celsius to Fahrenheit converter

import sys

def celsius_to_fahrenheit(temp: float):
    return (temp * 1.8) + 32

def main(temp: float):
    f_temp = celsius_to_fahrenheit(temp)
    print(f"{temp} Celsius -> {f_temp} Fahrenheit")

if __name__ == "__main__":
    main(float(sys.argv[1]))

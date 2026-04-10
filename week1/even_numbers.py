# Date: Apr. 9, 2026
# Author: Paul Han
# Return even numbers from a list

import sys

def is_even(num: int):
    return num % 2 == 0

def main(nums: list):
    return [n for n in nums if is_even(n)]

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            numbers = [int(x) for x in sys.argv[1:]]
            print(main(numbers))
        except ValueError:
            print("Please ensure all inputs are integers.")
    else:
        print("Usage: python even_numbers.py <list of numbers>")

# from aoc2025 import readInput as r
import math

def main():
    filename = "day2.txt"
    # filename = "practice.txt"
    productIdRange = []

    total = 0

    try:
        with open(filename, "r") as f:
            productIDs = f.read()
    except FileNotFoundError:
        print(f"Error the file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    productIdRange = productIDs.split(',')

    for id in productIdRange:
        total = checkValue(id, total)
    
    print(total)

def checkValue(productRange, total):
    start, end = productRange.split('-')
    for i in range(int(start), (int(end) + 1)):
        digits = []
        # divide by 10 to separate out the values
        while i > 0:
            remainder = i % 10
            digits.append(remainder)
            i //= 10
        # find the midpoint of the number
        halfLength = math.ceil(len(digits) / 2)
        # check first and second halves, add total 
        if(digits[:int(halfLength)] == digits[int(halfLength):]):
            # print(digits)
            string_numbers = [str(n) for n in digits[::-1]]
            joined_string = "".join(string_numbers)
            total += int(joined_string)

    return total

main()

    
# from aoc2025 import readInput as r

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
        
        # Check if the number has a repeating pattern (invalid IDs)
        if hasRepeatingPattern(digits):
            total += joinArrayAsInt(digits)

    return total

def joinArrayAsInt(array):
    string_numbers = [str(n) for n in array[::-1]]
    joined_string = "".join(string_numbers)
    value = int(joined_string)

    return value

def hasRepeatingPattern(digits):

    n = len(digits)
    # Try all possible pattern lengths (from 1 to n//2)
    for pattern_length in range(1, n // 2 + 1):
        # Only check if the pattern length divides evenly into total length
        if n % pattern_length == 0:
            pattern = digits[:pattern_length]
            # Check if repeating this pattern recreates the entire digit array
            is_repeating = True
            for i in range(pattern_length, n, pattern_length):
                if digits[i:i+pattern_length] != pattern:
                    is_repeating = False
                    break
            if is_repeating:
                return True
    return False


main()

    
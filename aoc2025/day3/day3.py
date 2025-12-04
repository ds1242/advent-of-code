

def main() -> None:
    filename:str = "input.txt"
    # filename: str = "sample-input.txt"
    input_list:list = read_input(filename)
    
    total: int = 0

    for row in input_list:
        result = find_largest(row)
        print(f"{row} -> {result}")
        total += result

    print(f"\nTotal: {total}")
    
def find_largest(digits: str) -> int:
    """
    Keep exactly 12 digits to create the largest possible number.
    Uses a monotonic stack approach.
    """
    digits = list(digits)
    keep_count = 12
    removals_left = len(digits) - keep_count
    stack = []
    
    for digit in digits:
        # While we can still remove digits AND
        # the top of stack is smaller than current digit,
        # remove from stack (this makes room for larger digit)
        while removals_left > 0 and stack and stack[-1] < digit:
            stack.pop()
            removals_left -= 1
        
        stack.append(digit)
    
    # If we haven't removed enough yet, remove from the end
    # (these are the smallest/least significant digits)
    while removals_left > 0:
        stack.pop()
        removals_left -= 1
    
    # Convert back to integer
    return int(''.join(stack))

def read_input(filename: str) -> list:
    inputList = []

    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                inputList.append(line.strip())
    except FileNotFoundError:
        print(f"Error the file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return inputList





main()
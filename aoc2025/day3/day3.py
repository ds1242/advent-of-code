

def main() -> None:
    # filename = "input.txt"
    filename: str = "input.txt"
    input_list:list = read_input(filename)
    
    output: int = 0

    for row in input_list:
        output += (find_largest(list(row)))

    print(output)
    
def find_largest(row: list):
    largest: int = 0

    for i in range(0, len(row)):
        for j in range(i, len(row)):
            if(int(row[i] + row[j]) > largest and j != i):
                largest = int(row[i] + row[j])

    return largest

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
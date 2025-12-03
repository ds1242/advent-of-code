

def main() -> None:
    # filename = "input.txt"
    filename = "sample-input.txt"
    input_list = read_input(filename)
    
    for row in input_list:
        find_largest(list(row))

    
def find_largest(row: list):
    largest: int = int(row[0])
    second_largest: int = int(row[1])
    for i in range(2, len(row)):
        print(row[i])

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
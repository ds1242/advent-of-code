

def main():
    # filename = "input.txt"
    filename = "sample-input.txt"
    input_list = readInput(filename)
    print(input_list)

    

def readInput(filename):
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
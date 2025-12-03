

def main() -> None:
    # filename:str = "input.txt"
    filename: str = "sample-input2.txt"
    input_list:list = read_input(filename)
    
    output: int = 0

    for row in input_list:
        output += (find_largest(list(row)))

    # print(output)
    
def find_largest(row: list):
    largest: int = 0
    smallest_three_count:int = 3
    count_dict:dict = {}
    output:list = []
    # dump count of characters into a dictionary
    for i in range(0, len(row)):
        count_dict[row[i]] = count_dict.get(row[i], 0) + 1

    count_dict = dict(sorted(count_dict.items()))

    for key, _ in count_dict.items():
        if smallest_three_count == 0:
            break

        while smallest_three_count > 0:
            if key in count_dict and count_dict[key] > 0:
                count_dict[key] -= 1
                smallest_three_count -= 1


    for i in range(0, len(row)):
        if row[i] in count_dict and count_dict[row[i]] > 0:
            output.append(row[i])
            count_dict[row[i]] -= 1

    print(output)
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
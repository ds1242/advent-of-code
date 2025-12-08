
def day5() -> None:
    filename:str = "input.txt"
    # filename:str = "sample-input.txt"
    input_list:str = read_input(filename)

    input_list = input_list.split()
    input_range: list = []
    value_list: list = []
    for row in input_list:
        if '-' in row:
            input_range.append(row.split('-'))
        else:
            value_list.append(row)

    # for input_value in input_range:
    #     split_value(input_value)
    count: int = 0

    # print(input_range)
    # print(value_list)
    for value in value_list:
        for range_value in input_range:
            if int(value) >= int(range_value[0]) and int(value) <= int(range_value[1]):
                count += 1
                break

    print(count)


def read_input(filename: str) -> str:

    try:
        with open(filename, "r") as f:
            productIDs:str = f.read()
    except FileNotFoundError:
        print(f"Error the file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return productIDs


def split_value(input: str) -> tuple[int, int]:
    # values:list = 
    print(input.split('-'))

day5()

# read input
# split into ranges and values
# check if value falls into any of the ranges
# return count of values
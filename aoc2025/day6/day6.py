
def day6() -> None:
    filename:str = "input.txt"
    # filename:str = "sample-input.txt"

    input_list:str = read_input(filename)

    data_rows:list = input_list[:-1]
    operations:list = input_list[-1]

    num_cols:int = len(operations)
    total: int = 0


    for col_idx in range(num_cols):
        operation:str = operations[col_idx]
        col_total:int 

        if operation =='+':
            col_total = 0
        elif operation == '*':
            col_total = 1
        else:
            continue

        for row in data_rows:
            value = int(row[col_idx])
            if operation == '+':
                col_total += value
            elif operation == "*":
                col_total *= value

        total += col_total

    print(f"Total: {total}")
    


def read_input(filename: str) -> list:
    inputList = []

    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                inputList.append(line.split())
    except FileNotFoundError:
        print(f"Error the file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return inputList


day6()
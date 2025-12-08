
def day6() -> None:
    # filename:str = "input.txt"
    filename:str = "sample-input.txt"

    input_list:str = read_input(filename)


    total: int = 0
    for i in range(0, len(input_list)):
        col_total: int
        if input_list[-1][i] == '+':
            col_total = 0
        elif input_list[-1][i] == '*':
            col_total = 1

        for j in range(0, len(input_list[i]) - 1):
            # print(input_list[-1][i])
            if input_list[-1][i] == '+':
                col_total += int(input_list[j][i])
                # print('add')
            elif input_list[-1][i] == '*':
                col_total *= int(input_list[j][i])
                # print('multi')
            # print(col_total)
        total += col_total

    print(total)
    


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
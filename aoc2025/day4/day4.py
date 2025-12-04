

def day4():
    # filename = "input.txt"
    filename:str = "sample-input.txt"
    input_list:list = read_input(filename)


    
    for i in range(0, len(input_list)):
        for j in range(0, len(input_list[i])):
            print(input_list[i][j])
            # set count to 0
            count:int = 0
            
            # check row above

            # check left

            # check right

            # check row below
    #     for j in range(0, len(input_list[i])):
    #         matrix[i][j] = input_list[i][j]
    
    # print(matrix[0][3])


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

day4()
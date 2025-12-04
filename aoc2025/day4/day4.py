

def day4():
    # filename:str = "input.txt"
    filename:str = "sample-input.txt"
    input_list:list = read_input(filename)


    rolls_removed:int = 0
    able_to_remove:bool = True

    matrix:list = []

    for row in input_list:
        matrix.append(list(row))

    
    while able_to_remove == True:
        # reset rolls to be removed list
        rolls_to_remove:list = []

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                curr_count:int = 0
                # up and left
                if matrix[i][j] == '@':
                    if i > 0 and j > 0 and matrix[i - 1][j - 1] == '@':
                        curr_count += 1
                    # above
                    if i > 0 and matrix[i - 1][j] == '@':
                        curr_count += 1
                    # up and right
                    if i > 0 and j < len(matrix[i]) - 1 and matrix[i - 1][j + 1] == '@':
                        curr_count += 1
                    # left
                    if j > 0 and matrix[i][j - 1] == '@': 
                        curr_count += 1
                    # right
                    if j < len(matrix[i]) - 1 and matrix[i][j + 1] == '@':
                        curr_count += 1
                    # below and left
                    if i < len(matrix[i]) - 1 and j > 0 and matrix[i + 1][j - 1] == '@':
                        curr_count += 1
                    # below
                    if i < len(matrix[i]) - 1 and matrix[i + 1][j] == '@':
                        curr_count += 1
                    # below and right
                    if i < len(matrix[i]) - 1 and j < len(matrix[i]) - 1 and matrix[i + 1][j + 1] == '@':
                        curr_count += 1

                    if curr_count < 4 and curr_count > 0:
                        rolls_removed += 1
                        rolls_to_remove.append((i, j))
        if len(rolls_to_remove) == 0:
            able_to_remove = False

        matrix = remove_rolls(rolls_to_remove, matrix)

    print(rolls_removed)
    
    
    
    # print(matrix)
    

def remove_rolls(rolls_to_remove:list, matrix: list) -> list:
    for roll in rolls_to_remove:
        matrix[roll[0]][roll[1]] = '.'
    
    return matrix

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


def day4():
    filename:str = "input.txt"
    # filename:str = "sample-input.txt"
    input_list:list = read_input(filename)


    available_rolls:int = 0
    for i in range(0, len(input_list)):
        for j in range(0, len(input_list[i])):
            # print(input_list[i][j])
            # set count to 0
            curr_count:int = 0

            # up and left
            if input_list[i][j] == '@':
                if i > 0 and j > 0 and input_list[i - 1][j - 1] == '@':
                    curr_count += 1
                # above
                if i > 0 and input_list[i - 1][j] == '@':
                    curr_count += 1
                # up and right
                if i > 0 and j < len(input_list[i]) - 1 and input_list[i - 1][j + 1] == '@':
                    curr_count += 1
                # left
                if j > 0 and input_list[i][j - 1] == '@': 
                    curr_count += 1
                # right
                if j < len(input_list[i]) - 1 and input_list[i][j + 1] == '@':
                    curr_count += 1
                # below and left
                if i < len(input_list[i]) - 1 and j > 0 and input_list[i + 1][j - 1] == '@':
                    curr_count += 1
                # below
                if i < len(input_list[i]) - 1 and input_list[i + 1][j] == '@':
                    curr_count += 1
                # below and right
                if i < len(input_list[i]) - 1 and j < len(input_list[i]) - 1 and input_list[i + 1][j + 1] == '@':
                    curr_count += 1

                if curr_count < 4:
                    available_rolls += 1

            # print(f"found at i:{i} j:{j}")

    print(available_rolls)

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

def day6() -> None:
    # filename:str = "input.txt"
    filename:str = "sample-input.txt"

    input_list:str = read_input(filename)


    total: int = 0
    flat_list:list = []
    for row in input_list:
        print(row)
      
    


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

def day5() -> None:
    # filename:str = "input.txt"
    filename:str = "sample-input.txt"
    input_list:str = read_input(filename)

    print(input_list.split('\n\n'))


def read_input(filename: str) -> str:

    try:
        with open(filename, "r") as f:
            productIDs:str = f.read()
    except FileNotFoundError:
        print(f"Error the file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return productIDs


day5()


def main():
    #  filename = "day2.txt"
    filename = "practice2.txt"
    productId = []

    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                productId.append(line.strip())
    except FileNotFoundError:
        print(f"Error the file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    
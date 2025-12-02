

def main():
     filename = "day1.txt"
    # filename = "practice1.txt"
    instructions = []

    dial = 50

    password = 0

    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                instructions.append(line.strip())
    except FileNotFoundError:
        print(f"Error the file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
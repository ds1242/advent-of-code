# from aoc2025 import readInput as r

def main():
    filename = "day2.txt"
    # filename = "practice.txt"
    productIdRange = []
    print("start")
    try:
        with open(filename, "r") as f:
            productIDs = f.read()
    except FileNotFoundError:
        print(f"Error the file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    productIdRange = productIDs.split(',')

    print(productIdRange)

main()

    
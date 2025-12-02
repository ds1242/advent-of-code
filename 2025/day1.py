
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

    
    for i in instructions:
        direction, distance = split_instruction(i)
        # print(f"direction: {direction} distance: {distance}")
        if direction == 'L':
            dial = turn_left(dial, int(distance))
        if direction == 'R':
            dial = turn_right(dial, int(distance))
        if dial == 0:
            password += 1
    
    print(password)


def split_instruction(instruction):
    direction = instruction[0]
    distance = instruction[1:]

    return direction, distance


def turn_left(dial, distance):
    for _ in range(distance):
        if dial - 1 == -1:
            dial = 99
        else:
            dial -= 1
    
    return dial


def turn_right(dial, distance):
    for _ in range(distance):
        if dial + 1 == 100:
            dial = 0
        else:
            dial += 1
    
    return dial

main()

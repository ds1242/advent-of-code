
import os
from aoc2025 import readInput as r

def main():
    script_dir = os.path.dirname(__file__)
    filename = "day1.txt"
    filename = os.path.join(script_dir, filename)
    # filename = "practice1.txt"
    instructions = []

    dial = 50

    password = 0

    instructions = r.readInput(filename)

    
    for i in instructions:
        direction, distance = split_instruction(i)
        # print(f"direction: {direction} distance: {distance}")
        if direction == 'L':
            dial, password = turn_left(dial, int(distance), password)
        if direction == 'R':
            dial, password = turn_right(dial, int(distance), password)
    
    print(password)


def split_instruction(instruction):
    direction = instruction[0]
    distance = instruction[1:]

    return direction, distance


def turn_left(dial, distance, count):
    for _ in range(distance):
        if dial - 1 == -1:
            dial = 99
        else:
            dial -= 1
        
        if dial == 0:
            count += 1
    
    return dial, count


def turn_right(dial, distance, count):
    for _ in range(distance):
        if dial + 1 == 100:
            dial = 0
        else:
            dial += 1

        if dial == 0:
            count += 1
    
    return dial, count

main()

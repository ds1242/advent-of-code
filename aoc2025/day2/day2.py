import os
from aoc2025 import readInput as r

def readInput():
    script_dir = os.path.dirname(__file__)
    #  filename = "day2.txt"
    filename = "practice.txt"
    filename = os.path.join(script_dir, filename)
    productIdRange = []

    productIdRange = r.readInput(filename)

    print(productIdRange)

    
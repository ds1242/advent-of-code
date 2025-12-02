
import readInput as r

def readInput():
    #  filename = "day2.txt"
    filename = "practice2.txt"
    productIdRange = []

    productIdRange = r.readInput(filename)

    for range in productIdRange:
        print(range)

    
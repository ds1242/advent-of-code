

def day4_optimized():
    filename = "input.txt"
    input_list = read_input(filename)
    
    # Store occupied positions as a set of (row, col) tuples
    rolls = set()
    rows = len(input_list)
    cols = len(input_list[0]) if input_list else 0
    
    for i, row in enumerate(input_list):
        for j, char in enumerate(row):
            if char == '@':
                rolls.add((i, j))
    
    total_removed = 0
    
    while True:
        to_remove = set()
        
        for (i, j) in rolls:
            # Count neighbors using set lookups
            neighbors = sum(1 for di in [-1, 0, 1] 
                          for dj in [-1, 0, 1] 
                          if (di, dj) != (0, 0) and (i + di, j + dj) in rolls)
            
            if neighbors < 4:
                to_remove.add((i, j))
        
        if not to_remove:
            break
        
        rolls -= to_remove
        total_removed += len(to_remove)
    
    print(total_removed)

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


day4_optimized()
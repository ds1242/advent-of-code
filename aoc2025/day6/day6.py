
def day6() -> None:
    filename:str = "input.txt"
    # filename:str = "sample-input.txt"

    input_list:str = read_input(filename)

    data_rows:list = input_list[:-1]
    operations:list = input_list[-1]

    num_cols:int = len(operations)
    total: int = 0


    for col_idx in range(num_cols):
        operation = operations[col_idx].strip()
        
        if operation == '+':
            col_total = 0
        elif operation == '*':
            col_total = 1
        else:
            continue

        # Get all cell values for this column
        numbers = []
        for row in data_rows:
            cell_value = row[col_idx]
            # Check if it contains only spaces (fixed-width format)
            if cell_value.strip():  # Only process non-empty values
                # For fixed-width with spaces, need to parse right-to-left
                if ' ' in cell_value:
                    # Fixed-width format - use the complex parsing
                    col_lists = [list(row[col_idx]) for row in data_rows]
                    numbers = count_right_to_left(col_lists)
                    break
                else:
                    # Space-delimited format - just convert to int
                    numbers.append(int(cell_value))
        
        # Apply the operation
        for num in numbers:
            if operation == '+':
                col_total += num
            elif operation == '*':
                col_total *= num
        
        # if col_idx < 5:  # Debug first 5 columns
        #     print(f"Column {col_idx}: {operation} with {numbers} = {col_total}")
        total += col_total

    print(f"Total: {total}")
    

def count_right_to_left(col_lists: list):
    output_list = []
    
    while True:
        output_val = ""
        for lst in col_lists:
            if len(lst) > 0:
                char = lst.pop()
                # Only include non-space characters
                if char != ' ':
                    output_val += char
        
        if len(output_val) > 0:
            output_list.append(int(output_val))
        else:
            break
    
    return output_list

def read_input(filename: str) -> list:
    inputList = []

    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            
            # Check if it's fixed-width (sample) or space-delimited (input)
            first_line = lines[0].rstrip('\n')
            if len(first_line) < 100:  # Sample file is short
                # Fixed-width parsing for sample
                for line in lines:
                    line = line.rstrip('\n')
                    row = []
                    for i in range(0, len(line), 4):
                        col = line[i:i+3]  # Get exactly 3 chars (skip the 4th which is separator)
                        row.append(col)
                    inputList.append(row)
            else:
                # Space-delimited parsing for full input
                for line in lines:
                    inputList.append(line.split())
    except FileNotFoundError:
        print(f"Error the file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return inputList


day6()
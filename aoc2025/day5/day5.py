
def day5() -> None:
    filename:str = "input.txt"
    # filename:str = "sample-input.txt"
    input_list:str = read_input(filename)

    input_list = input_list.split()
    input_range: list = []
    value_list: list = []
    for row in input_list:
        if '-' in row:
            split_row: list = row.split('-')
            input_range.append([int(split_row[0]), int(split_row[1])])
        else:
            value_list.append(row)

    sorted_list = sorted(input_range, key=lambda x: x[0])
    compressed_list: list = compress_input(sorted_list)
    
    # count the values in the range
    # for value in value_list:
    #     for range_value in input_range:
    #         if int(value) >= int(range_value[0]) and int(value) <= int(range_value[1]):
    #             count += 1
    #             break

    # count total values in list
    total = sum(end - start + 1 for start, end in compressed_list)
    print(total)


    # print(count)

def compress_input(ranges: list) -> list:
    merged = []
    current_start, current_end = ranges[0]
    
    for start, end in ranges[1:]:
       # Check if this range overlaps or is adjacent to current
        if start <= current_end + 1:  # +1 handles adjacent ranges like [3-5] and [6-8]
            # Merge: extend the current range
            current_end = max(current_end, end)
        else:
            # No overlap: save current range and start a new one
            merged.append((current_start, current_end))
            current_start, current_end = start, end
    
    # Don't forget the last range!
    merged.append((current_start, current_end))
    
    return merged

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

# read input
# split into ranges and values
# check if value falls into any of the ranges
# return count of values
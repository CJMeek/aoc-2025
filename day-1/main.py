def readInput():
    with open("day-1/input.txt") as f:
        return [str(line.strip()) for line in f.readlines()]
    

#For each line go left or right and output how many times after we finish a sequence we are pointing at 0
def part1(data):

    position = 50
    zero_pointing = 0
    
    for line in data:
        
        #each line is either LXX or RXX where XX is a number
        #we need to split the line into an array
        line_arr = [line[0], int(line[1:])]
        
        if line_arr[0] == "L":
            position -= line_arr[1]
        elif line_arr[0] == "R":
            position += line_arr[1]
            
        position = position % 100
        
        if position == 0:
            zero_pointing += 1
    

    return zero_pointing

# how many times we cross over zero in total
def part2(data):
    
    position = 50
    zero_crossings = 0
    
    for line in data:
        
        line_arr = [line[0], int(line[1:])]
        
        if line_arr[0] == "L":
            for _ in range(line_arr[1]):
                position -= 1
                position = position % 100
                if position == 0:
                    zero_crossings += 1
        elif line_arr[0] == "R":
            for _ in range(line_arr[1]):
                position += 1
                position = position % 100
                if position == 0:
                    zero_crossings += 1

    return zero_crossings

if __name__ == "__main__":
    data = readInput()
    result = part1(data)
    result2 = part2(data)
    print(f"Part 1: {result}")
    print(f"Part 2: {result2}")
    
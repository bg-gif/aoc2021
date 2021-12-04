def sum():
    input = [int(x) for x in open('aoc-dayone-input.txt', 'r').readlines()]
    count = 0
    for i in range(len(input)):
        if input[i] > 0 and input[i] > input[i-1]:
            count+=1
    return count

print(sum())

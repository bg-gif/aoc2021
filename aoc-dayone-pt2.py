def output():
    input = [int(x) for x in open('aoc-dayone-input.txt', 'r').readlines()]
    count = 0
    prev = 0
    for i in range(len(input)):
        x = slice(i-2,i+1)
        if i > 1 and i <= len(input):
            total = sum(list(input[x]))
            if total > prev and prev != 0:
                count+=1
            prev = total
    return count

print(output())

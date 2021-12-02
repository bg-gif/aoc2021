with open('aoc-dayone-input.txt') as f:
    input = f.read()
arr = input.split('\n')
ints = [int(x) for x in arr]
count = 0
prev = 0
for i in range(len(ints)):
    x = slice(i-2,i+1)
    if i > 1 and i <= len(ints):
        total = sum(list(ints[x]))
        if total > prev and prev != 0:
            count+=1
        prev = total
print(count)
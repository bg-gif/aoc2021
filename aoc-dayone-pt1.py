with open('aoc-dayone-input.txt') as f:
    input = f.read()
arr = input.split('\n')
ints = [int(x) for x in arr]
count = 0
for i in range(len(ints)):
    if ints[i] > 0 and ints[i] > ints[i-1]:
        count+=1
print(count)

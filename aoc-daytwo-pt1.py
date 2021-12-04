input = open('aoc-daytwo-input.txt', 'r').readlines()
location = {"horizontal": 0, "depth": 0}
for instruction in input:
    split_instructions = instruction.strip('\n').split(' ')
    direction = split_instructions[0]
    move_val = int(split_instructions[1])
    if direction == 'forward':
        location['horizontal'] += move_val
    if direction == 'up':
        location['depth'] -= move_val
    if direction == 'down':
        location['depth'] += move_val
print(location)
print(location['horizontal'] * location['depth'])
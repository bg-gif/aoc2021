with open('aoc-daytwo-input.txt') as f:
    input = f.read()
instructions = input.split('\n')
location = {"horizontal": 0, "depth": 0}
for instruction in instructions:
    split_instructions = instruction.split(' ')
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
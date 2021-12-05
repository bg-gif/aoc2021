class Gamma_Epsilon:

    def __init__(self, input_file):
        self.input = [x.strip('\n') for x in open(input_file, 'r').readlines()]
        self.counter = self.declare_counter()

    def update_obj(self, index, counter):
        counter[index] = {'1':0, '0':0}
        return 

    def declare_counter(self):
        counter = {}
        for x in range(len(self.input[0])):
            self.update_obj(x, counter)
        self.count_characters(counter)
        return counter

    def count_characters(self, counter):
        for x in self.input:
            binary_array = [y for y in x]
            for index in range(len(binary_array)):
                counter[index][binary_array[index]] += 1
    
    def get_gamma(self):
        key = ''
        for x in range(len(self.counter)):
            if self.counter[x]['1'] > self.counter[x]['0']:
                key =  key + '1'
            else:
                key = key + '0'
        return int(key, 2)

    def get_epsilon(self):
        key = ''
        for x in range(len(self.counter)):
            if self.counter[x]['0'] > self.counter[x]['1']:
                key =  key + '1'
            else:
                key = key + '0'
        return int(key, 2)

    def get_power(self):
        power = self.get_epsilon() * self.get_gamma()
        return power

counter = Gamma_Epsilon('aoc-daythree-input.txt')
print('Gamma: ' + str(counter.get_gamma()))
print('Epsilon: ' + str(counter.get_epsilon()))
print('Power: ' + str(counter.get_power()))
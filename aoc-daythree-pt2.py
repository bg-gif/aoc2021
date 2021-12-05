class Rating_Finder:

    def __init__(self, input_file):
        self.input = [x.strip('\n') for x in open(input_file, 'r').readlines()]

    def update_obj(self, index, counter):
        counter[str(index)] = {'1':0, '0':0}
        return 

    def declare_counter(self, input):
        counter = {}
        for x in range(len(input[0])):
            self.update_obj(x, counter)
        self.count_characters(counter, input)
        return counter

    def count_characters(self, counter, input):
        for x in input:
            binary_array = [y for y in x]
            for index in range(len(binary_array)):
                counter[str(index)][binary_array[index]] += 1
    
    def find_most_common(self, index, changer):
        if changer[index]['1'] >= changer[index]['0']:
            return 1
        else:
            return 0
    
    def find_least_common(self, index, changer):
        if changer[index]['1'] >= changer[index]['0']:
            return 0
        else:
            return 1

    def find_oxygen_rating(self):
        candidates = list(self.input)
        for x in range(len(candidates[0])):
            changer = self.declare_counter(candidates)
            common = self.find_most_common(str(x), changer)
            if len(candidates) > 1:
                candidates = [y for y in candidates if y[x] == str(common)]
        return int(candidates[0],2)

    def find_co2_rating(self):
        candidates = list(self.input)
        for x in range(len(candidates[0])):
            changer = self.declare_counter(candidates)
            not_common = self.find_least_common(str(x), changer)
            if len(candidates) > 1:
                candidates = [y for y in candidates if y[x] == str(not_common)]
        return int(candidates[0],2)       


readout = Rating_Finder('aoc-daythree-input.txt')
print('Oxygen Rating: ' + str(readout.find_oxygen_rating()))
print('CO2 Rating: ' + str(readout.find_co2_rating()))
print('Life Support Rating: ' + str(readout.find_co2_rating() * readout.find_oxygen_rating()))


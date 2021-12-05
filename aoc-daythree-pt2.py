class Rating_Finder:

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
    
    def get_most_common(self):
        most_common = []
        for index in range(len(self.counter)):
            most_common.append(self.find_most_common(self.counter[index]))
        return most_common
    
    def find_most_common(self, obj):
        if obj['1'] >= obj['0']:
            return 1
        else:
            return 0
    
    def get_least_common(self):
        least_common = []
        for index in range(len(self.counter)):
            least_common.append(self.find_least_common(self.counter[index]))
        return least_common
    
    def find_least_common(self, obj):
        if obj['1'] >= obj['0']:
            return 0
        else:
            return 1
    
    def find_oxygen_rating(self):
        candidates = list(self.input)
        accepted = list(self.input)
        most_common = self.get_most_common()
        for x in range(len(most_common)):
            index = range(len(candidates))
            for y in index:
                if int(candidates[y][x]) != most_common[x] and len(accepted) > 1 and candidates[y] in accepted:
                    accepted.remove(candidates[y])
        print(accepted, most_common)
        return int(accepted[0], 2)

    def find_co2_rating(self):
        candidates = list(self.input)
        accepted = list(self.input)
        least_common = self.get_least_common()
        for x in range(len(least_common)):
            index = range(len(candidates))
            for y in index:
                if int(candidates[y][x]) != least_common[x] and len(accepted) > 1 and candidates[y] in accepted:
                    accepted.remove(candidates[y])
        print(accepted, least_common)
        return int(accepted[0], 2)

    def find_lifesupport_rating(self):
        return self.find_co2_rating() * self.find_oxygen_rating()
                    
        

    
    # def get_oxygen_generator_rating(self):
      




counter = Rating_Finder('aoc-daythree-input.txt')
# print(counter.counter)
# print(counter.most_common)
print('Oxygen Rating: ' + str(counter.find_oxygen_rating()))
print('CO2 Rating: ' + str(counter.find_co2_rating()))
print('Life Support Rating: ' + str(counter.find_lifesupport_rating()))


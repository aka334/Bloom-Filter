import hashlib
import random

class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * self.size
    
    def __len__(self):
        return self.size

    def add(self, string):
        for seed in range(self.hash_count):
            result = int(hashlib.sha256(f"{seed}{string}".encode()).hexdigest(), 16) % self.size
            self.bit_array[result] = 1
    
    def lookup(self, string):
        for seed in range(self.hash_count):
            result = int(hashlib.sha256(f"{seed}{string}".encode()).hexdigest(), 16) % self.size
            if self.bit_array[result] == 0:
                return False 
        return True 

def generate_random_elements(num_elements, element_size=10):
    elements = set()
    while len(elements) < num_elements:
        elements.add(''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=element_size)))
    return elements

def main():
    num_sets = 7
    num_elements = 1000
    num_filters = 3
    filter_size = 30000
    hash_count = 7
    
    filters = [BloomFilter(filter_size, hash_count) for _ in range(num_filters)]
    all_sets = [generate_random_elements(num_elements) for _ in range(num_sets)]
    codes = [format(i, '03b') for i in range(1, 8)]
    for set_idx, element_set in enumerate(all_sets):
        code = codes[set_idx]
        for element in element_set:
            for filter_idx, bit in enumerate(code):
                if bit == '1':
                    filters[filter_idx].add(element)
    
    correct_lookups = 0
    
    for set_idx, element_set in enumerate(all_sets):
        code = codes[set_idx]
        for element in element_set:
            lookup_result = [filters[filter_idx].lookup(element) for filter_idx in range(num_filters)]
            lookup_code = ''.join(['1' if result else '0' for result in lookup_result])
            if lookup_code == code:
                correct_lookups += 1
    
    with open("coded_bloom.txt", "w") as f:
        f.write(f"{correct_lookups}\n")

if __name__ == "__main__":
    main()

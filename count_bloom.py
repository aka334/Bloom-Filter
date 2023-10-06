import hashlib
import random

class CountingBloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.counters = [0] * self.size
    
    def add(self, string):
        indices = []
        for seed in range(self.hash_count):
            result = int(hashlib.sha256(f"{seed}{string}".encode()).hexdigest(), 16) % self.size
            indices.append(result)
            self.counters[result] += 1
        return indices  
    
    def remove(self, string, indices=None):
        if indices is None: 
            indices = []
            for seed in range(self.hash_count):
                result = int(hashlib.sha256(f"{seed}{string}".encode()).hexdigest(), 16) % self.size
                indices.append(result)
        for index in indices:
            if self.counters[index] > 0:  
                self.counters[index] -= 1
    
    def lookup(self, string):
        for seed in range(self.hash_count):
            result = int(hashlib.sha256(f"{seed}{string}".encode()).hexdigest(), 16) % self.size
            if self.counters[result] == 0:
                return False  
        return True  

def generate_random_elements(num_elements, element_size=10):
    elements = set()
    while len(elements) < num_elements:
        elements.add(''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=element_size)))
    return elements

def main():
    num_elements = 1000
    num_to_remove = 500
    num_to_add = 500
    
    cbf = CountingBloomFilter(size=10000, hash_count=7)
    
    elements_a = generate_random_elements(num_elements)
    
    
    indices_a = {element: cbf.add(element) for element in elements_a}
    
    elements_to_remove = set(random.sample(elements_a, num_to_remove))
    for element in elements_to_remove:
        cbf.remove(element, indices_a[element])
    
    elements_to_add = generate_random_elements(num_to_add)
    for element in elements_to_add:
        cbf.add(element)

    count_found_a = sum(1 for element in elements_a if cbf.lookup(element))
    
    with open("count_bloom.txt", "w") as f:
        f.write(f"{count_found_a}\n")

if __name__ == "__main__":
    main()

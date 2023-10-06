import hashlib
import random

class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * self.size
    
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
    elements_a = generate_random_elements(1000)
    elements_b = generate_random_elements(1000)
    
    bloom_filter = BloomFilter(size=10000, hash_count=7)
    
    for element in elements_a:
        bloom_filter.add(element)
    
    count_a = sum(1 for element in elements_a if bloom_filter.lookup(element))
    count_b = sum(1 for element in elements_b if bloom_filter.lookup(element))
    
    with open("bloom_filter.txt", "w") as f:
        f.write(f"{count_a}\n")
        f.write(f"{count_b}\n")

if __name__ == "__main__":
    main()

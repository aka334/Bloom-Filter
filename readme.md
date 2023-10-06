
# Bloom Filter Implementations

This repository contains implementations of three variations of Bloom Filters:

1. **[Standard Bloom Filter](./bloom_filter.py)**
2. **[Counting Bloom Filter](./count_bloom.py)**
3. **[Coded Bloom Filter](./coded_bloom.py)**

## 1. [Standard Bloom Filter](./bloom_filter.py)

A standard Bloom Filter which allows for adding elements and checking membership with the possibility of false positives.

- **File**: [`bloom_filter.py`](./bloom_filter.py)
- **Usage Example**: Instantiating the filter, adding elements, and checking membership.

## 2. [Counting Bloom Filter](./count_bloom.py)

An extension of the standard Bloom Filter, providing the capability to remove elements and to decrement the count of false positives accordingly.

- **File**: [`count_bloom.py`](./count_bloom.py)
- **Usage Example**: Instantiating the filter, adding elements, removing elements, and checking membership.

## 3. [Coded Bloom Filter](./coded_bloom.py)

A specialized Bloom Filter which allows elements to be mapped to multiple sets and verifies the mappings through binary codes.

- **File**: [`coded_bloom.py`](./coded_bloom.py)
- **Usage Example**: Creating filters, adding elements, and validating membership across multiple sets.

---
## Dependencies

Ensure you have the following dependencies installed to use these implementations:

- Python 3.x
- hashlib (Standard library in Python)
- random (Standard library in Python)

---
## Auhor

- Aayush Karki
---
## How to Run
```bash
python3 bloom_filter.py
python3 coded_bloom.py
python3 count_bloom.py
```
---
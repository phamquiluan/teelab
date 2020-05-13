import random
import time
from example_lib import get_random_int

# random.seed(1)

for _ in range(10):
    # random.seed(1)
    print(get_random_int())

"""
READING:
    - https://softwareengineering.stackexchange.com/questions/221632/testing-deterministic-or-non-deterministic
    - https://www.geeksforgeeks.org/random-seed-in-python/
"""

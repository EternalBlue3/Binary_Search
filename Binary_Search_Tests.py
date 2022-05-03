import time, random
from Binary_Search import *

# Test array
arr = []
for x in range(1,100000000,3):
    arr.append(x)

x = random.choice(arr)
print(f"X: {x}\n")

# Function call
vanilla_1 = time.time()
result = recursive_search(arr,x)
print("Element is present at index", str(result))
vanilla_2 = time.time()
print(f"Vanilla function took: {vanilla_2-vanilla_1}\n")

binary_1 = time.time()
result = binary_search(arr,x)
print("Element is present at index", str(result))
binary_2 = time.time()
print(f"Binary function took: {binary_2-binary_1}\n")

binary_cython_1 = time.time()
result = Cython_Binary_Search(arr,x)
print("Element is present at index", str(result))
binary_cython_2 = time.time()
print(f"Cython function took: {binary_cython_2-binary_cython_1}\n")

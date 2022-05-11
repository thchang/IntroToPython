from sorting import *
from random import randint
from time import time

LENGTH = 10000

# Create an unsorted list
myList = []
for i in range(LENGTH):
    myList.append(randint(0, LENGTH))
#print(f"Original list: {myList}")
#print()

# Time bubble sort
myCopy = myList.copy()
start = time()
BubbleSort(myCopy)
end = time()
print(f"Bubble sort completed in: {end - start} seconds")
#print(myCopy)
print()

# Time selection sort
myCopy = myList.copy()
start = time()
SelectionSort(myCopy)
end = time()
print(f"Selection sort completed in: {end - start} seconds")
#print(myCopy)
print()

# Time insertion sort
myCopy = myList.copy()
start = time()
InsertionSort(myCopy)
end = time()
print(f"Insertion sort completed in: {end - start} seconds")
#print(myCopy)
print()

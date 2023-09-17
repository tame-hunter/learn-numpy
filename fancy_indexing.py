import numpy as np

a = np.array([10, 25, 89, 102, 57, 66]) # Create 1d array

indexes = [1, 3, 5] # Use python list for indexing array
print(a[indexes]) # It returns only 1, 3, 5 index elements of array

even = np.argwhere(a%2==0).flatten() # We use n-array method argwhere to find only even elements of array and also flatten array(it means that we do array 1d)
print(a[even]) # And it returns only even elements of array



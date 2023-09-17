import numpy as np
print(np.__version__) # Version of NumPy

a = np.array([1, 2, 3]) # Create a numpy array
print(a)

print(a.shape) # Shape of n-array for ex (2, 2) it means 2 elements in 2 dimention
print(a.dtype) # Type of the elements of n-array
print(a.ndim) # Dimention of n-array
print(a.size) # Size (counts of elements) of n-array
print(a.itemsize) # Size of elements(in bytes)

print(a[1]) # We also can use index in n-arrays
a[0] = 10 # We can change the elements with index in n-array
print(a)

b = a * np.array([2, 0, 5]) # It's possible to multiple two n-arrays
print(b)
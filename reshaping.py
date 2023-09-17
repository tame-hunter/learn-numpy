import numpy as np

a = np.arange(1, 7) # Use the method to create 1d arrays in certain range.
print(a)

b = a.reshape((2, 3)) # Reshape the array with set values. We create from 1d array 2x3 array
print(b)
print(b.shape)

c = a.reshape((3, 2)) # Reshape the array with set values. We create from 1d array 3x2 array
print(c)
print(c.shape)

d = a[np.newaxis, :] # Create a newaxis (ось) for the array. Before shape was (6,) after became (1, 6)
print(d)
print(d.shape)

e = a[:, np.newaxis] # Create a newaxis (ось) for the array. Before shape was (6,) after became (6, 1)
print(e)
print(e.shape)
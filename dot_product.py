import numpy as np

l1 = [1, 2, 3]
l2 = [4, 5, 6]

a1 = np.array(l1)
a2 = np.array(l2)

dot = 0
for i in range(len(l1)):  # For getting dot product of lists we use this code and it's immense 
    dot += l1[i] * l2[i]
print(dot)    

print(a1 @ a2) # But in n-arrays we can use only this code with @ symbol

print((a1 * a2).sum()) # Or we can multiple two n-array and with method sum find dot product

print(np.dot(a1, a2)) # Or we also can use the method dot to find the dot product
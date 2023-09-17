import numpy as np

l = [1, 2, 3]
a = np.array([1, 2, 3])

print(l, '\n', a)

l.append(4) # We can add element in list with append
print(l)

#a.append(4) # But we can't add element in n-array with append. It'll cause to error

l = l + [5] # We can also add element by this way in list
print(l)

a = a + np.array([4]) # But with n-array it works differently. It will in 'Broadcasting'
print(a)

print(l * 2) # We can also multiple list with digits
print(a * 2) # But with n-arrays it also works differently
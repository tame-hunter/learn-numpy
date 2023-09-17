import numpy as np

a  = np.array([[1, 2], [3, 4], [5, 6]]) # It's a 3x2 array, it means that it has 3 rows and 2 columns

bool_idx = a > 2 # It's a boolean index. It return also 3x2 array but if the condition is true then the el'll be True, else False
print(bool_idx)

print(a[a > 2]) # We also can use bool_idx here. And that returns the elements which condition is true.

b = np.where(a>2, a, -1) # It's method where. With that we can use condition and if the condition is false , it uses default value
print(b)
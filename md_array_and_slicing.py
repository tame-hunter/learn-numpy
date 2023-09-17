import numpy as np

a = np.array([[1, 2], [3, 4]]) # Create a 2 dimensional n-array
print(a) 
print(a.shape) # Shape is (2, 2), it means that array has 2 rows(строки) and 2 columns(столбцы)
print(a.ndim) # Dimension is 2

print(a[0]) # The result is first row of array
print(a[0, 0]) # First column of first row in array
print(a[1, 1]) # Column in index 1 of row in index 1 in array

print(np.linalg.det(a)) # We also can use linear algebra function with n-arrays. We found determinant of square array
print(np.linalg.inv(a)) # We found inversion of array(Обратная матрица)
print(a.T) # Мы также можем транспанировать матрицу(тоесть поменять строки со столбцами)

a2 = np.array([[1, 2, 3], [4, 5, 6]])

print(a2[:, 0:2]) # We use slicing. In all rows we found the columns between 0 and 2(not included)
print(a2[-2, -2]) # We also can use the negative indexes
print(a2[-1, -1])

print(a2[1, :]) # Here we found in the row index 2 all columns




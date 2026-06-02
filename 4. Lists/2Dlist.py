## 2D lista are like 2d arrays in other programming languages. They are lists of lists, where each inner list represents a row of the 2D list. The basic syntax for creating a 2D list is as follows:
# 2D_list = [[row1], [row2], [row3], ...
# Example of a 2D list
matrix = [
    [1, 2, 3],
    [4, 5, 6],  
    [7, 8, 9]
]
print(matrix)
print(type(matrix))  # Output: <class 'list'>
print (matrix[0][0])  # Output: 1 (first element of the first row)

## Accessing elements in a 2D list
print(matrix[1][2])  # Output: 6 (third element of the second row)
print(matrix[2][1])  # Output: 8 (second element of the third row)

## Modifying elements in a 2D list
matrix[0][1] = 20
print(matrix)  # Output: [[1, 20, 3], [4, 5, 6], [7, 8, 9]]   
matrix[2][0] = 70
print(matrix)  # Output: [[1, 20, 3], [4, 5, 6], [70, 8, 9]]

## Iterating through a 2D list
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()  # for a new line after each row
    
    
## other important functions of 2D list
# finding the number of rows and columns in a 2D list
rows = len(matrix)
columns = len(matrix[0]) if rows > 0 else 0
print(f"Number of rows: {rows}")
print(f"Number of columns: {columns}")

## finding the largest element in a 2D list
largest = matrix[0][0]
for row in matrix:
    for element in row:
        if element > largest:
            largest = element
print("The largest element is:", largest)  # Output: The largest element is: 70


## finding the sum of all elements in a 2D list
total_sum = 0
for row in matrix:
    for element in row:
        total_sum += element    
print("The sum of all elements is:", total_sum)  # Output: The sum of all elements is: 123

    # finding the average of all elements in a 2D list
total_elements = rows * columns
average = total_sum / total_elements if total_elements > 0 else 0
print("The average of all elements is:", average)  # Output: The average of all


## finding the transpose of a 2D list
transpose = [[matrix[j][i] for j in range(rows)] for i in range(columns)]
print("The transpose of the matrix is:")
for row in transpose:
    print(row)
    
    
    ## finding the diagonal elements of a 2D list
diagonal = [matrix[i][i] for i in range(min(rows, columns))] ## this will return the diagonal elements of the matrix, which are 1, 5, and 9 in this case. it uses a list comprehension to iterate through the indices of the matrix and access the elements at those indices. The min function is used to ensure that we don't go out of bounds if the matrix is not square.
print("The diagonal elements are:", diagonal)  # Output: The diagonal elements are: [1, 5, 9]


## finding the anti-diagonal elements of a 2D list
anti_diagonal = [matrix[i][columns - 1 - i] for i in range(min(rows, columns))] ## this will return the anti-diagonal elements of the matrix, which are 3, 5, and 7 in this case. it uses a list comprehension to iterate through the indices of the matrix and access the elements at those indices. The min function is used to ensure that we don't go out of bounds if the matrix is not square.
print("The anti-diagonal elements are:", anti_diagonal)  # Output: The anti-diagonal elements are: [3, 5, 70]

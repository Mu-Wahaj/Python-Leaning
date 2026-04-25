## nested loops are loops inside another loop. They are used to perform more complex iterations, such as iterating over a 2D array or creating patterns. The inner loop will complete all its iterations for each iteration of the outer loop.
# Example of nested loops
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")
    
    ##simple syntax of nested loops
    
    ## drwng F pattern using nested looops
    numbers=[5,2,5,2,2]
for number in numbers:   
    output = ""
    for count in range(number):
        output += "x"
    print(output)
    
    
    ## A pattern using nested loops
for i in range(5):
    for j in range(5):
        if (i == 0 or i == 2) and j < 4:
            print("x", end="")
        elif j == 0 or j == 4:
            print("x", end="")
        else:
            print(" ", end="")
    print()  
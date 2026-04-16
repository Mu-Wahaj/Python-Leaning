#loops in  python are used to execute a block of code repeatedly until a certain condition is met. The two main types of loops in python are for loops and while loops.
# for loop is used to iterate over a sequence (such as a list, tuple, or string) or other iterable object. The basic syntax of a for loop is as follows:
# for variable in sequence:
#     # code to execute for each item in the sequence
# Example of a for loop 


## c ++ code for a for loop
#for (int i = 0; i < 10; i++) {
    #   cout << i;
#}
for i in range(10):
    print(i)
# while loop is used to execute a block of code repeatedly as long as a certain condition is true. The basic syntax of a while loop is as follows:
# while condition:
#     # code to execute as long as the condition is true
# Example of a while loop

# c++ code for a while loop
# int i = 0;
# while (i < 10) {
#     cout << i;
#     i++;
# }
i = 0
while i < 10:
    print(i)
    i += 1
print("Loop has ended.")

#nested loops are loops inside another loop. They are used to perform more complex iterations, such as iterating over a 2D array or creating patterns. The inner loop will complete all its iterations for each iteration of the outer loop.
# Example of nested loops
for i in range(3):
    for j in range(3):
        print(f"i: {i}, j: {j}")
    
    ##simple syntax of nested loops
# for variable1 in sequence1:
#     for variable2 in sequence2:
#         # code to execute for each combination of variable1 and variable2

   
    
    


    
    

    
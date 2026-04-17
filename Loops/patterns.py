#patterns using for loops and while nad do while llosp 

# pattern 1
for i in range(5):
   print("*" * (i))
   
# pattern 2
for i in range(5, 0, -1):
    print("*" * (i))
    
# pattern 3
for i in range(1, 6):
    print(" " * (5 - i) + "*" * (i))
    
    
    #pattern 4 diamond pattern
n = 5
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
    
    
# pattern 5 butterfly pattern
n = 5
for i in range(n):
    print("*" * (i + 1) + " " * (2 * (n - i - 1)) + "*" * (i + 1))
for i in range(n - 2, -1, -1):
    print("*" * (i + 1) + " " * (2 * (n - i - 1)) + "*" * (i + 1))
    
# pattern 6 hollow square pattern
n = 5
for i in range(n):
    if i == 0 or i == n - 1:
        print("*" * n)
    else:
        print("*" + " " * (n - 2) + "*")
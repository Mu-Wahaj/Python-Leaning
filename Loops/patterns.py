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
    
    
    ##in cpp its the dimaond pattern 
# int n = 5;
# for (int i = 0; i < n; i++) {
#     for (int j = 0; j < n - i - 1; j++) {
#         cout << " ";
#     }
#     for (int j = 0; j < 2 * i + 1
#     cout << "*";
#     cout << endl;
# }
# for (int i = n - 2; i >= 0; i--) {
#     for (int j = 0; j < n - i - 1;
#     cout << " ";
#     for (int j = 0; j < 2 * i + 1
#     cout << "*";
#     cout << endl;


    
    
    
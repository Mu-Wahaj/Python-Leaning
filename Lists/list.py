## list are a collection of items that are ordered and changeable. They are one of the most commonly used data structures in Python. Lists are defined using square brackets [] and can contain items of different types, including other lists.
# Example of a list


my_list = [1, "Hello", 3.14, [1, 2, 3]]
print(my_list)
print(type(my_list))  # Output: <class 'list'>
names = ["Alice", "Bob", "Charlie"]
print(names)
print(type(names))  # Output: <class 'list'>
# Accessing list items
print(names[0])  # Output: Alice
names[1] = "Robert"
print(names)  # Output: ['Alice', 'Robert', 'Charlie']
# List methods
names.append("David")
print(names)  # Output: ['Alice', 'Robert', 'Charlie', 'David']

names.insert(1, "Eve")
print(names)  # Output: ['Alice', 'Eve', 'Robert', 'Charlie', 'David']
names.remove("Charlie")
print(names)  # Output: ['Alice', 'Eve', 'Robert', 'David']
names.pop()
print(names)  # Output: ['Alice', 'Eve', 'Robert']
names.clear()
print(names)  # Output: []



## findng the length of a list
my_list = [1, 2, 3, 4, 5]
print(len(my_list))  # Output: 5


## largest number in a list
numbers = [3, 1, 4, 1, 5, 9]
largest = numbers[0]
for number in numbers:
    
    if number > largest:
        largest = number    
        
print("The largest number is:", largest)  # Output: The largest number is: 9

## basic other function of list
my_list = [1, 2, 3, 4, 5]
print(min(my_list))  # Output: 1
print(max(my_list))  # Output: 5
print(sum(my_list))  # Output: 15
print(sorted(my_list))  # Output: [1, 2, 3, 4, 5]
print(sorted(my_list, reverse=True))  # Output: [5, 4, 3, 2, 1]
print(my_list)  # Output: [1, 2, 3, 4, 5] (original list remains unchanged)
print(my_list.count(2))  # Output: 1 (counts the occurrences of 2 in the list)
print(my_list.index(3))  # Output: 2 (returns the index of the first occurrence of 3 in the list)
## reruns te indexes and the valuesof the list 
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")
    
    ## returning th indexes of acuurences of a value in a list
    newlist = [1, 2, 3, 2, 4, 2, 5]
value_to_find = 2
indexes = [index for index, value in enumerate(newlist) if value == value_to_find] ##what it does is it creates a list of indexes where the value in the newlist is equal to the value_to_find. It uses a list comprehension to iterate through the newlist with enumerate, which provides both the index and the value for each element. If the value matches the value_to_find, the index is added to the indexes list.
print(f"Indexes of {value_to_find} in the list: {indexes}")  #
    

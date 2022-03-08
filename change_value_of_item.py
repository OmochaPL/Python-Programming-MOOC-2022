'''
Please write a program which initialises a list with the values [1, 2, 3, 4, 5]. 
Then the program should ask the user for an index and a new value, replace the value at the given index, and print the list again. 
This should be looped over until the user gives -1 for the index. 
You can assume all given index values will fall within your list.
'''


# Write your solution here

my_list = [1, 2, 3, 4, 5]
i = 5
while i > 0:
    index = int(input("Which index?: "))
    if index != -1:
        value = int(input("What value?: "))
        my_list[index] = value
        print(my_list)
    else:
        i = i - 10
    

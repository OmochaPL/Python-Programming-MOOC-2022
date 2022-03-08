''' Please write a program which first asks the user for the number of items to be added. 
Then the program should ask for the given number of values, one by one, and add them to a list in the order they were typed in. 
Finally, the list is printed out. '''

# Write your solution here

my_list = []
times = int(input("How many times?: "))
while times > 0:
    i = int(input("Item: "))
    my_list.append(i)
    times = times - 1 
print(my_list)

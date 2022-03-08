''' Please write a program which asks the user to type in values and adds them to a list. 
After each addition, the list is printed out in two different ways:
in the order the items were added
ordered from smallest to greatest
The program exits when the user types in 0.

'''

my_list = []

while True:
    i = int(input("New item: "))
    if i != 0:
        my_list.append(i)
        print("The list now:", my_list)
        print("The list in order:", sorted(my_list))
        continue
    else: 
        print("Bye!")
        break

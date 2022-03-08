''' Please write a program which asks the user to choose between addition and removal. 
Depending on the choice, the program adds an item to or removes an item from the end of a list. 
The item that is added must always be one greater than the last item in the list. 
The first item to be added must be 1. '''

# Write your solution here

mylis = []

i = 1
print(f"The list is now {mylis}")
while True:
    operation = input("a(d)d, (r)emove or e(x)it: ")
    if operation == "d":
        mylis.append(i)
        i += 1
        print(f"The list is now {mylis}")
        continue
    elif operation == "r":
        mylis.remove(i-1)
        i -= 1
        print(f"The list is now {mylis}")
        continue
    else:
        print("Bye!")
        break

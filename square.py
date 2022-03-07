'''
Please write a function named square, which prints out a square of characters, and takes two arguments. 
The first parameter specifies the length of the side of the square. The second parameter specifies the character used to draw the square.

'''

# Copy here code of line function from previous exercise
def line(number, character):
    print(character * (number))

def square(size, character):
    # You should call function line here with proper parameters
    i = 0
    while i < size:
        line(size, character)
        i = i + 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "o")

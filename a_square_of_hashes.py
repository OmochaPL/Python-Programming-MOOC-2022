''' Please write a function named square_of_hashes, which draws a square of hash characters. 
The function takes one argument, which determines the length of the side of the square.
'''

# Copy here code of line function from previous exercise
def line(number, character):
    print(character * (number))        

def square_of_hashes(size):
    # You should call function line here with proper parameters
    i = 0
    while i < size:
        line(size, "#")
        i = i + 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)

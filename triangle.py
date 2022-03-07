''' Please write a function named triangle, which draws a triangle of hashes, and takes one argument. 
The triangle should be as tall and as wide as the value of the argument. '''

# Copy here code of line function from previous exercise

def line(number, character):
    i = 1
    while i <= number:
        print( i * character)
        i += 1

def triangle(size):
    line(size, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)

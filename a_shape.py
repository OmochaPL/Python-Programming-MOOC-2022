''' Please write a function named shape, which takes four arguments. 
The first two parameters specify a triangle, as above, and the character used to draw it. 
The first parameter also specifies the width of a rectangle, while the third parameter specifies its height. 
The fourth parameter specifies the filler character of the rectangle. 
The function prints first the triangle, and then the rectangle below it.
'''

# Copy here code of line function from previous exercise and use it in your solution

def line(width, char1, height, char2):
    i = 1
    while i <= width:
        print( i * char1)
        i += 1

    j = 1
    while j <= height:
        print (width * char2)
        j += 1

def shape(width, char1, height, char2):
    line(width, char1, height, char2)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")

''''
Please write a function named box_of_hashes, which prints out a rectangle of hash characters. 
The function takes one argument, which specifies the height of the rectangle. 
The rectangle should be ten characters wide.
''''

# Copy here code of line function from previous exercise
def line(size, character):
    if character == "":
        character = "*"
    print(character[0] * size)
        

def box_of_hashes(height):
    # You should call function line here with proper parameters
    i = 0
    while i < height:
        line(10, "#")
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
    

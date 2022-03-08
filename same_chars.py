''' 
Please write a function named same_chars, which takes one string and two integers as arguments. 
The integers refer to indexes within the string. The function should return True if the two characters at the indexes specified are the same. 
Otherwise, and especially if either of the indexes falls outside the scope of the string, the function returns False.
'''

# Write your solution here
from itertools import count


def same_chars(string, no1, no2):
    if no2 > (len(string) -1):
        return False
    elif no1 > (len(string)-1):
        return False
    else:
        if string[no1] == string[no2]:
            return True
        elif string[no1] != string[no2]:
            return False

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("abc", 0, 3))

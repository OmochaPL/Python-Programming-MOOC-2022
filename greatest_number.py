''' Please write a function named greatest_number, which takes three arguments. The function returns the greatest in value of the three.

'''


from re import A


def greatest_number(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    elif c >= a and c >= b: 
        return c


# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)

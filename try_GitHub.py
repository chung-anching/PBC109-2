import math

x_limit = int(input('Enter the type: '))
y_limit = int(input('Enter a number: '))

def cal(t, n):
    if x_limit == 1:
        print(math.log(y_limit, 2))

    elif x_limit == 2:
        print(math.log(y_limit))
    elif x_limit == 3:
        print(y_limit**3)
cal(x_limit,y_limit)

class Food:
    def __init__(selfself,price):
        self.price = price
# the first pattern is half right sides triangle which is hallow

# square of stars
def square(height):
    print("*" * height)
    for _ in range(0, height-2):
        print(f"*{' ' * (height -2)}*")
    print("*" * height)

def hallow_right_tri1(height):
    print("*")
    for i in range(0, height-2):
        print(f"*{' ' * i}*")
    print("*" * height)


# rectangle of stars
def hallow_rec(height, width):
    print("*" * width)
    for _ in range(height-2):
        print(f"*{' ' * (width -2)}*")
    print("*" * width)


# left_side_triangle

def left_tri(height):
    print(f"{' ' * (height - 1)}*")
    for i in range(2, height):
        print(f"{' ' * (height - i)}", end="")
        print(f"*{' ' * (i - 2)}*")
    print('*' * height)


# hallow pyramid

def hallow_pyramid(height):
    num_spaces = 1
    print(f"{' ' * (height - 1)}*")

    for i in range(2, height):
        print(f"{' ' * (height - i)}", end="")
        print(f"*{' ' * (num_spaces + i - 2)}*")
        num_spaces += 1
    print("*" * (height * 2 -1))



def hallow_diamond(height):
    spaces_num1 = 1
    spaces_num2 = height * 2 - 3

    i1 = 1
    i2 = 0
    print(f"{' ' * (height - 1)}*")
    while i2 < height-1:

        if i1 < height-1:
            print(f"{' ' * (height - i1 - 1)}", end="")
            print(f"*{' ' * (spaces_num1 + i1-1)}*")
            spaces_num1 += 1
            i1 += 1
        else:
            print(f"{' ' * i2}", end="")
            print(f"*{' ' * (spaces_num2 - i2)}*")
            spaces_num2 -= 1
            i2 += 1
    print(f"{' ' * (height-1)}*")

def hallow_diamond2(height):
    width = height * 2 - 1
    print(" " * (height - 1) + "*")
        
    for i in range(1, width-1):
        left_spaces = abs(height - i - 1)
        stars = width - 2 * left_spaces
        print(" " * left_spaces + "*" + " " * (stars - 2) + "*") 
    print(" " * (height - 1)+ "*")
hallow_diamond2(5)



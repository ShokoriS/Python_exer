# the first pattern is half right sides triangle which is hallow

# square of stars
def square(height):
    print("*" * height)
    for _ in range(0, height-2):
        print(f"*{' ' * (height -2)}*")
    print("*" * height)
square(5)

def hallow_right_tri1(height):
    print("*")
    for i in range(0, height-2):
        print(f"*{' ' * i}*")
    print("*" * height)

hallow_right_tri1(5)

# rectangle of stars
def rec(height, width):
    print("*" * width)
    for _ in range(height-2):
        print(f"*{' ' * (width -2)}*")
    print("*" * width)

rec(5, 20)

# left_side_triangle

def left_tri(height):
    print(f"{' ' * (height - 1)}*")
    for i in range(2, height):
        print(f"{' ' * (height - i)}", end="")
        print(f"*{' ' * (i - 2)}*")
    print('*' * height)

left_tri(5)


# hallow pyramid

def hallow_pyramid(height):
    num_spaces = 1
    print(f"{' ' * (height - 1)}*")

    for i in range(2, height):
        print(f"{' ' * (height - i)}", end="")
        print(f"*{' ' * (num_spaces + i - 2)}*")
        num_spaces += 1
    print("*" * (height * 2 -1))

hallow_pyramid(5)


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

hallow_diamond(5)
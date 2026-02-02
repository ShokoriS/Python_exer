"""
To print pattrens using code...
like:
*
**
***
****
*****
"""
from oauthlib.uri_validate import hier_part

#======================================================================
#======================================================================

height = 5
weight = 6

# square of stars
def print_square(height):
    for _ in range(height):
        print("*" * height)


# rectangle of stars

def print_rec(height, weight):
    for _ in range(height):
        print("*" * weight)

# left side triangle

def print_left_side_tri(height):
    for i in range(1, height+1):
        print("*" * i)


# right side triangle

def print_right_side_tri(height):
    for i in range(1, height+1):
        print(f"{' ' * (height - i)}{'*' * i}")

# square stars inside empty

def print_square_stars(height):

    print(height * "*  " )
    for _ in range(height):
        print(f"*{" " * ((height * 2))} *")
    print(height * "*  ")
    
# pyramid
"""
  *
 ***
*****
  
"""

def pyramid(height):

    stars_num = 1

    for i in range(height):
        print(f"{' ' * (height - i-1)}", end="")
        print(f"{'*' * (stars_num + i)}")
        stars_num += 1



# upside down pyramid
"""
*****
 ***
  *
"""


def face_down_pyramid(height):

    stars_num = height * 2 - 1
    for i in range(height):
        print(f"{' ' * i}", end="")
        print(f"{'*' * (stars_num - i)}")
        stars_num -= 1




# diamond pattern printing
"""
   *
  ***
 *****
  ***
   *

"""
def diamond(height):

    stars_num = 1
    for i in range(height-1):
        print(f"{' ' * (height-i-1)}", end="")
        print(f"{'*' * (stars_num + i)}")
        stars_num += 1
    stars_num = height * 2 - 1
    for i in range(height):
        print(f"{' ' * i}", end="")
        print(f"{'*' * (stars_num - i)}")
        stars_num -= 1

def diamond2(height):
    """
    this uses one loop to create a diamond style but uses two ifs to decide which part to create
    -> while the second part is not done
    ->if we haven't created the entire top side yet, we will keep making that
    ->else we are done with the first part we will start with the second part
    :param height: the height of the diamond which the real height becomes height * 2 - 1
    :return: a diamond shape made of symbols
    """

    stars_num1 = 1 # the num of stars for the first half
    stars_num2 = height * 2 - 1 # the num of stars for the second half
    i1 = 0 # the num of spaces for the first half + the num of previous stars created
    i2 = 0 # the num of spaces + the num of previous stars for second half created

    while i2 < height:

        # this is the first part of the diamond
        if i1 < height -1:
            print(f"{' ' * (height - i1 -1)}", end="") # the number of spaces that we created
            print(f"{'*' * (stars_num1 + i1)}") # the number of symbols; if stars num is 2 and i1 is 1
            # that will give us 3;the correct num of symbols
            stars_num1 += 1 # the num of stars + 1 so we can add one more to the previous ones
            i1 += 1 # we should add one more to spaces and the stars
        # this is the second part of the diamond
        else:
            # the same idea as previous one but only this time we start with the height * 2 - 1 stars num
            print(f"{' ' * i2}", end="") # number of spaces
            print(f"{'*' * (stars_num2 - i2)}") # number of stars starting with height * 2 -1
            stars_num2 -= 1 # making the stars - 1
            i2 += 1 # making the spaces more so we get less spaces
            
"""
#
##
####
####
##
#
"""

def special(height):

    i = 1
    num_stars = 1

    second_half = ""
    while i < height:
        print("#" * num_stars if num_stars != 0 else "#" * 1)

        if i >= height // 2:
            
            break
        i += 1
        num_stars *=2


 


def num_triangle(height):

    pre_nums = ""

    for i in range(1, height + 1):
        print(*(i for _ in range(i)))





def invertered_right_triangle(height):


    for i in range(height, 0, -1):
        print("*" * i)

def gen_symbols(num):

    if num == 1:
        return "1"

    nums = "".join(f"{i} " for i in range(1, num+1))
    
    return f"{nums}{nums[::-1][3:]}"




def num_pyramid(height):
    
    for j in range(1, height+1):
        print(f"{'  ' * (height - j)}", end="")
        print(gen_symbols(j))

    
        

def binary_triangle(height):
    pattern = "1"
    switch = True

    for _ in range(height):
        print(pattern) 
        switch = not switch
        pattern = f"{int(switch)}{pattern}"   


def binary_right_triangle(height):
    pattern = '1'
    switch = True

    for spaces in range(1, height+1):
        print(f"{' ' * (height - spaces)}", end="")
        print(pattern)
        switch = not switch
        pattern = f"{int(switch)}{pattern}"


def binary_pyramid(height):
    
    pattern = "1"

    for space in range(1, height+1):
        print(f"{' ' * (height - space)}", end="")
        print(pattern)
        pattern = f"10{pattern}"
        


upper_case = lambda x: x.upper()

words = ["hello", "world", "python"]

output = ",".join(upper_case(x) for x in words)
print(output)

double = lambda x: x **2
output2 = ",".join(str(double(x)) for x in [2, 4, 5, 1])
print(output2)

multi = lambda x : f"{x * 10}"
nums = [1, 2, 3, 4, 5, 6]
output3 = "|".join(multi(x) for x in nums if x % 2 == 0)
print(output3)

firs_letter = lambda x: str(x[0])
names = ["Alice", "Bob", "Charlie"]
output4 = "".join(firs_letter(name) for name in names)
print(output4)

even_odd = lambda x: "E" if x % 2 == 0 else "O"
nums = [1, 2, 3, 4, 5]

output5 = " ".join(even_odd(num) for num in nums)
print(output5)


output6 = ", ".join(str((lambda x : x ** 3)(x)) for x in nums)
print(output6)

words1 = ["apple", "banana", "pear", "kiwi"]

words1.sort(key=lambda x: x[-1])

print(words1)

names = ["Alice", "Bob", "Charlie"]

name_length = lambda x: str(len(x))
name_lengths = ", ".join(str(len(x)) for x in names)
print(name_lengths)


nums = [1, 2, 3, 4, 5, 6]

odd_even = " ".join(map(lambda x: "odd" if x % 2 == 1 else "even", nums))
print(odd_even)

add = lambda x, y: str(x + y)
points = [(1, 6), (1, 1), (0, 2)]

points.sort(key=lambda x: x[0] + x[1])

print(points)

make_multiplier = lambda x: lambda y: x * y

times3 = make_multiplier(3)
print(times3(5))




"""
10101
10101
10101
10101
"""

def generate_01(widht):
    
    result = ""
    switch = True
    for _ in range(widht):
        result += str(int(switch))
        switch = not switch
    return result


def stacks_01(height, widht=5):
    pattern = generate_01(widht)
    for _ in range(height):
        print(pattern)


stacks_01(5)




def num_triangle(height):
    num_pattern = 1
    for row in range(1, height+1):
        for _ in range(row):
            print(f"{num_pattern} ", end="")
            num_pattern += 1
        print()

       

num_triangle(5)
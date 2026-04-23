"""I have to print a shape of alternating symbols
#####
 #####
#####
 #####
here the symbols are space and the hash I will allow it so it could be anything....
"""


#to solve this problem I will try to use a switch technique to give it the same shape

def alternating_symbols(height):
    # I have used a tuple to indicated as to should I add a space or not...(really avoiding an if here)
    switch_symbols = ('a', 'b')
    # writing the each_line for code readability... 
    
    shape = "\n".join("".join(f'{switch_symbols[(i+j) % 2]}' for j in range(height)) for i in range(height))
    return shape

print(alternating_symbols(9))



def alternating_symbols2(height):
    symbols = "ab"

    print("\n".join(f"{symbols[0]}{symbols[1]}" * height if i % 2 else "symbols[0]symbols[1]" * height for i in range(height)))


def alternating_symbols_custom(height, width, block_length, symbols=(' ', '#')):

    shape = "\n".join("".join(f"{symbols[(i + j) % 2] * block_length}" for j in range(width)) for i in range(height))
    return shape

print(alternating_symbols_custom(5, 6, 3))



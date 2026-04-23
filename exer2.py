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

def each_line(height, width,line_width, symbols, i):
    # we have to decide which symbol should we start with 

    pattern = f"{(f"{symbols[1] * width}{symbols[0]*width}" if i % 2 else f"{symbols[0]*width}{symbols[1]*width}") * line_width}"
    return "\n".join(pattern for _ in range(height))

def alternating_symbols_custom(height, width, block_height, block_width, symbols=('a', 'b')):
    # here we are going to return the entire pattern 

    return "\n".join(each_line(block_height, block_width, width, symbols, i) for i in range(height))
print(alternating_symbols_cus

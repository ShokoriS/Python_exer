def alternating_symbols(height):
    # I have used a tuple to indicated as to should I add a space or not...(really avoiding an if here)
    switch_symbols = ('a', 'b')
    # writing the each_line for code readability... 
    
    shape = "\n".join("".join(f'{switch_symbols[(i+j) % 2]}' for j in range(height)) for i in range(height))
    return shape

print(alternating_symbols(9))


def each_line(height, width,line_width, lines, i):
    
    # I decided to create each first part of the block 
    # we have to decide which symbol should we start with 
    return "\n".join("".join(lines[(j+i) % 2] for j in range(line_width))for _ in range(height))


    

def alternating_symbols_custom(height=9, width=9, block_height= 3, block_width= 3,  symbols=('a', 'b')):
    # the size will be for you to chose I left it so you can freely choose the block's size and the total size....
      
    lines = (symbols[0] * block_width, symbols[1] * block_width)

    return "\n".join(each_line(block_height, block_width, width, lines, i) for i in range(height))

print(alternating_symbols_custom(symbols=('#', ' ')))

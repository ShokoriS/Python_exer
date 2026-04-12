"""I have to print a shape of alternating symbols
#####
 #####
#####
 #####
here the symbols are space and the hash I will allow it so it could be anything....
"""


#to solve this problem I will try to use a switch technique to give it the same shape

def alternating_symbols(height, symbol='#'):
    # I have used a tuple to indicated as to should I add a space or not...(really avoiding an if here)
    switch_symbols = ('', ' ')
    # writing the each_line for code readability... 
    each_line = symbol * height
    
    shape = "\n".join(f"{switch_symbols[i % 2]}{each_line}" for i in range(height))
    return shape

print(alternating_symbols(5))

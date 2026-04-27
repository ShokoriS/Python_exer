

def X_shape(height):
    
    remainder = height % 2
    half_height = height // 2
    extra_spaces = len(str(height)) -1
    print("\n".join(
            f"{'*' * (i - 1 + extra_spaces) }{i}{' ' * (height - i * 2 - (not remainder))}{'' if i == (half_height + remainder) else i}"
            for i in range(1, 1 + half_height + remainder)))
    

    print("\n".join(
        f"{'*' * (j - 1)}{height - j + 1}{'*' * (height - j * 2 + (not remainder))}{height - j + 1}" for j in range(half_height, 0, -1)
        ))

X_shape(7)


def X_shape2(height):
    
    remainder = height % 2
    half_height = height // 2
    extra_spaces =1 if remainder == 0 else 0 
    get_len_number = lambda number: len(str(number)) -1
    # Top half
    for i in range(1, 1 + half_height + remainder):
        
        left_spaces = ' ' * (i - 1 + extra_spaces)
        
        middle_spaces = ' ' * (height - i * 2 - (not remainder) - get_len_number(i))
        
        right_number = '' if i == (half_height + remainder) else i
        
        line = f"{left_spaces}{i}{middle_spaces}{right_number}"
        
        print(line)

    # Bottom half
    for j in range(half_height, 0, -1):
         
        left_spaces = ' ' * (j - 1)
        
        number = height - j + 1
        

        middle_spaces = ' ' * (height - j * 2 + (not remainder) - get_len_number(number))
        
        line = f"{left_spaces}{number}{middle_spaces}{number}"
        
        print(line)


X_shape2(7)




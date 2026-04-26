

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

X_shape(19)



print(int(True))



def X_shape(height):
    width = len(str(height))

    print("\n".join(
        "".join(
            f"{i:>{width}}" if j == i else
            f"{height - i + 1:>{width}}" if j == height - i + 1 else
            " " * width
            for j in range(1, height + 1)
        )
        for i in range(1, height + 1)
    ))

X_shape(10)

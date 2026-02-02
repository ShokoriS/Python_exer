# we have to take a text as input and make a triangle with it taking each letter one time. Then adding new
# letters to the previous letters.


def text_pattern(text):

    pattern = ""

    for letter in text:
        if letter.isspace():
            continue
        pattern += letter
        print(pattern)


text_pattern("Python")

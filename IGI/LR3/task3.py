import string

def count_spaces_punctuation():
    """
    Count spaces and punctuation symbols in text.
    """
    text = input("Enter text: ")

    spaces = 0
    punctuation = 0

    for ch in text:
        if ch == ' ':
            spaces += 1
        if ch in string.punctuation:
            punctuation += 1

    print("Spaces:", spaces)
    print("Punctuation:", punctuation)

def analyze_string():
    """
    Analyze predefined text (Variant 9).
    """
    text = """So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her."""

    vowels = "aeiou"
    words = text.replace(",", "").replace(".", "").split()

    # a) words starting or ending with vowel
    count_vowel_words = 0
    for word in words:
        w = word.lower()
        if w[0] in vowels or w[-1] in vowels:
            count_vowel_words += 1

    print("Words starting or ending with vowel:", count_vowel_words)

    # b) count each symbol
    symbols = {}
    for ch in text:
        symbols[ch] = symbols.get(ch, 0) + 1

    print("\nSymbol frequencies:")
    for k, v in symbols.items():
        print(k, ":", v)

    # c) words after comma sorted alphabetically
    parts = text.split(",")
    after_comma_words = []

    for part in parts[1:]:
        after_comma_words.extend(part.strip().split())

    after_comma_words.sort()
    print("\nWords after comma sorted:")
    print(after_comma_words)

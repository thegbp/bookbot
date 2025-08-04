def get_number_of_words(text):
    """
    Returns the number of words in the text.
    """
    length = len(text.split())
    return f"Found {length} total words"

def get_book_text(book):
    """
    Returns the text of the book.
    """
    with open(book, "r", encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents

def get_character_frequencies(text):
    """
    Returns a dictionary with the frequency of each character (case-insensitive) in the text.
    """
    freq = {}
    for char in text.lower():
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq


def print_bookbot_analysis(book_path):
    """
    Prints a formatted analysis of the book, including word and character counts.
    """
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    text = get_book_text(book_path)
    print("----------- Word Count ----------")
    print(get_number_of_words(text))
    print("--------- Character Count -------")
    char_freq = get_character_frequencies(text)
    import re
    filtered = {k: v for k, v in char_freq.items() if k.isalpha()}
    for char, count in sorted(filtered.items(), key=lambda item: (-item[1], item[0])):
        print(f"{char}: {count}")
    print("============= END ===============")

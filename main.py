def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(character_count(text))

def get_book_text(path):
    with open(path) as f:
        return f.read()


def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    text_lowercase = text.lower()
    char_count = {}
    for char in text_lowercase:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

        



main()
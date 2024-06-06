def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print_report(book_path, text)

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
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    return char_count

def print_report(book, text):
    print(f"--- Begin report of {book} ---")
    print(f"{word_count(text)} words found in the document")
    character_count_results = character_count(text)
    sorted_chars = sorted(character_count_results.items(), key=lambda item: item[1], reverse=True)
    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")

main()
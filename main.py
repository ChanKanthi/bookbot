from stats import number_of_words, number_of_characters, sorting_to_list
import sys

def number_of_words(book_text):
    word_count = 0
    array_of_text = book_text.split()
    for i in range(0, len(array_of_text)):
        word_count += 1
    return word_count


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if (len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    book_text = get_book_text(path)
    word_number = number_of_words(book_text)
    char_count = number_of_characters(book_text)
    sorted_char_count = sorting_to_list(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {word_number} total words")
    print(f"--------- Character Count -------")
    for dictionary in sorted_char_count:
        for char, count in dictionary.items():
            if char.isalpha():
                print(f"{char}: {count}")
    print("============= END ===============")


main()

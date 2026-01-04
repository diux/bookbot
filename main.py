import sys
from stats import get_num_words, get_num_char


def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

def sort_characters_count(char_count):
    result = []
    for key in char_count:
        result.append({"character" : key, "count" : char_count[key]})
    
    def sort_on(count):
        return count["count"]

    result.sort(reverse=True, key=sort_on) 
    return result

def print_report_for_book_in(file_path):
    book = get_book_text(file_path)
    num_words = get_num_words(book)
    num_chars = sort_characters_count(get_num_char(book))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(F'Found {num_words} total words')
    print("--------- Character Count -------")
    for char in num_chars:
        print(f'{char["character"]}: {char["count"]}')
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1] # "./books/frankenstein.txt"
    print_report_for_book_in(book_path)
    


main()



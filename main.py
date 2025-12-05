import sys
from stats import *

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_path = sys.argv[1]
    content = get_book_text(book_path)
    counter = count_words(content)
    character_dict = count_characters(content)
    sorted_list = dict_into_sort_list(character_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {counter} total words")
    print("--------- Character Count -------")

    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()
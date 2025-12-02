from stats import count_words, count_characters, dict_into_sort_list

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_path = "books/frankenstein.txt"
    content= get_book_text(book_path)
    counter = count_words(content)
    print(f"")
    character_dict = count_characters(content)
    #print(character_dict)
    sorted_list = dict_into_sort_list(character_dict)
    print(sorted_list)
    print(f"""
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------)
Found {counter} total words
--------- Character Count -------

""")
main()
from stats import count_words, count_characters

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_path = "books/frankenstein.txt"
    content= get_book_text(book_path)
    counter = count_words(content)
    print(f"Found {counter} total words")
    character_dict = count_characters(content)
    print(character_dict)
    #sort_counter(counter)

main()
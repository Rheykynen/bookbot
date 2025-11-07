from stats import count_words

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    book_path = "books/frankenstein.txt"
    content= get_book_text(book_path)
    counter = count_words(content)
    #sort_counter(counter)

main()
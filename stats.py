def count_words(content):
    num_words = 0
    words = content.split()
    for word in words: 
        num_words += 1
    print(f"Found {num_words} total words")
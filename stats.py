def count_words(content):
    num_words = 0
    words = content.split()
    for word in words: 
        num_words += 1
    return num_words

def count_characters(content):
    character_count = {}
    words = content.split()
    for word in words:
        for character in word:
            character = character.lower()
            if character not in character_count:
                character_count[character] = 1
            else:
                character_count[character] += 1
    return character_count

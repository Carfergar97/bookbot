def count_words(book):
    words = book.split()
    return  len(words)

def count_characters(book):
    words = book.split()
    character_count = { }
    for word in words:
        for char in word.lower():
            if (char in character_count) == False:
                character_count[char] = 1
            else:
                character_count[char] += 1
    return character_count

def get_book_text(book_filepath):
    with open(book_filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text("books/frankestein.txt")

    words_count = count_words(book_text)
    
    characters_count = count_characters(book_text)

    print(f"The number of words in the book is {words_count}")
    print(f"The number ocurrences of each character is {characters_count}")


main()
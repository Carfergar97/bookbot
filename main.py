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

def sort_on(val):
    return val[1]
def get_book_text(book_filepath):
    with open(book_filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text("books/frankestein.txt")

    words_count = count_words(book_text)
    
    characters_count = count_characters(book_text)


    print("--- Begin Report of books/frankestein.txt ---")
    print(f"{words_count} words found in the document")
    print(" ")
    characters_count = list(characters_count.items())
    characters_count.sort(key = sort_on, reverse = True)
    for pair in characters_count:
        if pair[0].isalpha():
            print(f"The '{pair[0]}' character was found {pair[1]} times")
    print("--- End Report ---")

main()
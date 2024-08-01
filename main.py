def count_words(book):
    words = book.split()
    return  len(words)

def get_book_text(book_filepath):
    with open(book_filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text("books/frankestein.txt")

    words_count = count_words(book_text)
    
    print(f"The number of words in the book is {words_count}")

main()
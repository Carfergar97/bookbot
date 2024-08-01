def count_words(book):
    words = book.split()
    word_count = len(words)
    return word_count
def main():
    with open("books/frankestein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        print(f"The word count is : {word_count}")

main()
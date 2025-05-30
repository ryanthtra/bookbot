import sys
from stats import get_word_count
from stats import get_char_count_dict
from stats import get_sorted_dict_arr

def get_book_text(fp):
    with open(fp) as f:
        file_contents = f.read()
        return file_contents
    

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    #print(get_book_text("./books/frankenstein.txt"))
    book_text = get_book_text(sys.argv[1])
    num_words = get_word_count(book_text)
    #print(f"{num_words} words found in the document")
    print(f"Found {num_words} total words")
    num_per_char = get_char_count_dict(book_text)
    #print(f"{num_per_char}")
    print("--------- Character Count -------")
    dict_arr = get_sorted_dict_arr(num_per_char)
    for dict in dict_arr:
        if dict["char"].isalpha():
            print(f"{dict['char']}: {dict['num']}")
    print("============= END ===============")

main()
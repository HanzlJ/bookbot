import sys
from stats import get_num_words, count_characteds,generate_report

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:    
        book_content = get_book_text(sys.argv[1])
        num_words = get_num_words(book_content)
        char_dic = count_characteds(book_content)
        report = generate_report(char_dic)
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for rep in report:
            if rep["char"].isalpha():
                print(f"{rep["char"]}: {rep["num"]}")
        print("============= END ===============")

main()
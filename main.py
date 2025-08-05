import sys
from stats import count_words, count_letters, conver_letter_count_dict_to_list, sort_letter_count_dict

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def generate_book_report(filepath: str, word_count: int, letter_count: dict) -> str:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in letter_count:
        print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
        # file_path = "./books/frankenstein.txt"
        word_count = count_words(get_book_text(file_path))
        letter_count = sort_letter_count_dict(conver_letter_count_dict_to_list(count_letters(get_book_text(file_path))))

        generate_book_report(file_path, word_count, letter_count)

main()
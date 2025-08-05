def count_words(book: str) -> int:
    num_words = len(book.split())
    # return f"{num_words} words found in the document"
    return num_words

def count_letters(book: str) -> dict:
    stat_dict = {}
    for char in book.lower():
        if char.isalpha():
            stat_dict[char] = stat_dict.get(char, 0) + 1
    
    return stat_dict

def conver_letter_count_dict_to_list(letter_count: dict) -> list:
    letter_count_ls = []
    for k, v in letter_count.items():
        letter_count_ls.append({"char" : k, "num" : v})
    return letter_count_ls

def sort_letter_count_dict(letter_count: list) -> list:
    letter_count.sort(reverse=True, key=lambda x: x["num"])
    return letter_count
def get_book_text(path):
    with open(path, encoding="utf-8") as f:
        file_contents = f.read()
        return file_contents

def get_num_words(text):
    return len(text.split())

def get_num_chars(text):
    chars = dict()
    for char in text.lower():
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    return chars

def sort_dict(dict):
    list = []
    for key in dict:
        list.append({"name": key, "num" : dict[key]})
    list.sort(reverse=True, key=sort_on)
    return list

def sort_on(dict):
    return dict["num"]

def print_report(path):
    text = get_book_text(path)
    num_words = get_num_words(text)
    chars = get_num_chars(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    list = sort_dict(chars)
    for char in list:
        if char["name"].isalpha():
            print(f"{char['name']}: {char['num']}")
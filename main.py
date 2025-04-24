def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        num_words = word_count(file_contents)
        chars_dict = get_char_num(file_contents)
        chars_sorted_list = sorted_list(chars_dict)

        print('--- Begin report of books/frankenstein.txt ---')
        print(f'{num_words} words found in the document')
        print()

        for c in chars_sorted_list:
            if not c["char"].isalpha():
                continue
            print(f"The '{c["char"]}' was found {c["num"]} times")

        print('--- End report ---')

def get_char_num(text):
    char_dict = {}
    for word in text:
        string = list(word.lower())
        for char in string:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def word_count(text):
    words = text.split()
    return len(words)

def sort_on(d):
    return d["num"]

def sorted_list(chars_dict):
    sorted_list = []
    for ch in chars_dict:
        sorted_list.append({"char": ch, "num": chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()

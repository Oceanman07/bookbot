import sys


def get_book_text(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chrs(text, target_chr='a'):
    count = 0
    for i in text:
        lower_case = i.lower()
        if lower_case == target_chr:
            count = count + 1
    return count

def get_chrs_dict(text):
    chrs = {}
    for chr in text:
        lowerer = chr.lower()
        if lowerer.isalpha():
            if lowerer in chrs:
                chrs[lowerer] = chrs[lowerer] + 1
            else:
                chrs[lowerer] = 1
    return chrs

def sort_on(d):
    return d['num']

def get_chrs_dict_sorted(chrs_dict):
    sorted_list = []
    for chr in chrs_dict:
        sorted_list.append(
            {'char': chr, 'num': chrs_dict[chr]}
        )
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list

def main():
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    chrs_dict = get_chrs_dict(book_text)
    sorted_chrs_dict = get_chrs_dict_sorted(chrs_dict)

    print(f'--- Begin report of {book_path}')
    print(f'{num_words} words found in the document')

    for i in sorted_chrs_dict:
        print(f"The '{i['char']}' character was found {i['num']} times")

    print('--- End report ---')

if __name__ == '__main__':
    main()

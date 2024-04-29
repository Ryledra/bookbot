def sort_on(dict):
    return dict["count"]

def sort_dic(dic):
    lst = list([ {"letter":key, "count":dic[key]} for key in dic ])
    lst.sort(reverse=True, key=sort_on)
    return lst
     

def print_report(book):
    book = "books/frankenstein.txt"
    file_contents = get_book_contents(book)
    word_count = get_word_count(file_contents)
    character_dict = get_character_dictionary(file_contents)

    print( f"--- Begin report of {book} ---" )
    print( f"{word_count} words found in the document\n" )
    for dic in sort_dic(character_dict):
        if dic["letter"].isalpha():
            print( f"The '{dic["letter"]}' character was found {dic["count"]} times" )
    
    print( "--- End report ---" )

def get_character_dictionary(f_string):
    dic = {}
    for c in f_string.lower():
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1
    return dic

def get_book_contents(path):
    with open(path) as f:
        return f.read()

def get_word_count(f_string):
    return len(f_string.split())

def main():
    book = "books/frankenstein.txt"
    print_report(book)

main()
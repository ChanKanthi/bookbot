def sorting_to_list(dictionary):
    new_list = []
    for key, value in dictionary.items():
        new_dict = {key:value}
        new_list.append(new_dict)

    def help_sort(unsorted_dict):
        return list(unsorted_dict.values())
    new_list.sort(reverse=True, key=help_sort)
    
    return new_list

def number_of_words(book_text):
    word_count = 0
    array_of_text = book_text.split()
    for i in range(0, len(array_of_text)):
        word_count += 1
    return word_count

def number_of_characters(book_text):
    dict = {}
    for i in book_text:
        if i.lower() in dict:
            dict[i.lower()] += 1
        else:
            dict[i.lower()] = 1
    return dict


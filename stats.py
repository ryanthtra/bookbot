def get_word_count(str):
    arr = str.split()
    return len(arr)

def get_char_count_dict(str):
    chars_dict = {}
    lowers = str.lower()    
    for i in range(0, len(lowers)):
        if lowers[i] not in chars_dict:
            chars_dict[lowers[i]] = 0
        chars_dict[lowers[i]] += 1
    return chars_dict

def sort_on(dict):
    return dict["num"]

def get_sorted_dict_arr(dict):
    dict_arr = []
    for char in dict:
        new_dict = {}
        new_dict["char"] = char
        new_dict["num"] = dict[char]
        dict_arr.append(new_dict)
    dict_arr.sort(reverse=True, key=sort_on)
    return dict_arr
    
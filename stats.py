def get_num_words(file_content):
    count = len(file_content.split())
    return count

def count_characteds(file_content):
    low_file_content = file_content.lower()
    character_dict = dict()
    for char in low_file_content:
        if char in character_dict:
            character_dict[char] = character_dict[char] + 1
        else:
            character_dict[char] = 1
    return character_dict

def sort_on(items):
    return items["num"]

def generate_report(char_dic):
    list_of_dics = []
    for char in char_dic:
        list_of_dics.append({"char": char, "num": char_dic[char]})
    list_of_dics.sort(reverse=True, key=sort_on)
    return list_of_dics

def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    lowercase_text = text.lower()
    char_dic = {}

    for t in lowercase_text:
        if t in char_dic:
            char_dic[t] += 1
        else:
            char_dic[t] = 1
    return char_dic

def sort_on(items):
    return items["num"]

def sorting(char_dict):
    pair_dict = []
    for c in char_dict:
        pair_dict.append({"char": c, "num": char_dict[c]})
    pair_dict.sort(reverse=True, key=sort_on)

    return pair_dict


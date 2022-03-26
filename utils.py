def dict_to_int(old_dict):
    result = dict()
    for key in old_dict.keys():
        result[int(key)] = int(old_dict[key])
    return result

def pick_from_list_dict(list_dict, key, value):
    return list(filter(lambda item: item[key] == value, list_dict))[0]

def uppercase_string(string):
    result = ''
    for letter in string:
        o = ord(letter)
        if o >= 65 and o <= 92:
            result += chr(o)
        else:
            result += chr(o - 32)
    return result

def is_uppercase_string(string):
    is_ok = True
    for letter in string:
        o = ord(letter)
        if o < 65 or o > 92:
            is_ok = False
            break
    return is_ok
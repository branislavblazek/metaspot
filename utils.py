def dict_to_int(old_dict):
    result = dict()
    for key in old_dict.keys():
        result[int(key)] = int(old_dict[key])
    return result

def pick_from_list_dict(list_dict, key, value):
    return list(filter(lambda item: item[key] == value, list_dict))[0]
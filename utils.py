def dict_to_int(old_dict):
    result = dict()
    for key in old_dict.keys():
        result[int(key)] = int(old_dict[key])
    return result
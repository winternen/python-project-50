import json


def normalize_string(value):
    return str(value).lower()


def generate_diff(first_file, second_file):
    first_dict = json.load(open(first_file))
    second_dict = json.load(open(second_file))

    diff_list = []
    keys = sorted(set(first_dict.keys()) | set(second_dict.keys()))

    for key in keys:
        if key not in first_dict:
            diff_list.append(f'+ {key}: {normalize_string(second_dict[key])}')
        elif key not in second_dict:
            diff_list.append(f'- {key}: {normalize_string(first_dict[key])}')
        elif first_dict[key] == second_dict[key]:
            diff_list.append(f'  {key}: {normalize_string(first_dict[key])}')
        else:
            diff_list.append(f'- {key}: {normalize_string(first_dict[key])}')
            diff_list.append(f'+ {key}: {normalize_string(second_dict[key])}')
    
    diff_string = '\n'.join(diff_list)
    return '{\n' + diff_string + '\n}'

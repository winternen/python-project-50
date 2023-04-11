import json


def normalize_string(value):
    return str(value).lower()


def generate_diff(first_file, second_file):
    first_dict = json.load(open(first_file))
    second_dict = json.load(open(second_file))
    diff = []
    keys = sorted(set(first_dict.keys()) | set(second_dict.keys()))
    for key in keys:
        if key not in first_dict:
            diff.append(f'+ {key}: {normalize_string(second_dict[key])}')
        elif key not in second_dict:
            diff.append(f'- {key}: {normalize_string(first_dict[key])}')
        elif first_dict[key] == second_dict[key]:
            diff.append(f'  {key}: {normalize_string(first_dict[key])}')
        else:
            diff.append(f'- {key}: {normalize_string(first_dict[key])}')
            diff.append(f'+ {key}: {normalize_string(second_dict[key])}')
    return '{\n' + '\n'.join(diff) + '\n}'

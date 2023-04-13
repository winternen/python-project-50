import json


def make_diff(key, first_dict, second_dict):
    diff = str()
    if key not in first_dict:
        diff = f'+  {key}: {normalize_str(second_dict[key])}'
    elif key not in second_dict:
        diff = f'-  {key}: {normalize_str(first_dict[key])}'
    elif first_dict[key] == second_dict[key]:
        diff = f'   {key}: {normalize_str(first_dict[key])}'
    else:
        diff = f'-  {key}: {normalize_str(first_dict[key])}\n'
        diff += f'+  {key}: {normalize_str(second_dict[key])}'
    return diff


def generate_diff(first_file, second_file):
    first_dict = json.load(open(first_file))
    second_dict = json.load(open(second_file))
    keys = sorted(first_dict.keys() | second_dict.keys())
    diff = [make_diff(key, first_dict, second_dict) for key in keys]
    return '{\n' + '\n'.join(diff) + '\n}'


def normalize_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)

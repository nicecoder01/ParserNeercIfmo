from parse_materials import get_dict_with_links, write_to_json, get_from_json


if __name__ == '__main__':
    data = get_dict_with_links()
    write_to_json('result_data.json', data)
    data_from_file = get_from_json('result_data.json')
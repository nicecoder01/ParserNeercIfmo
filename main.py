from parse_materials import get_dict_with_links, write_to_json, load_from_json, get_link_topic


if __name__ == '__main__':
    # data = get_dict_with_links()
    # write_to_json('result_data.json', data)
    # data_from_file = get_from_json('result_data.json')
    print(get_link_topic('Машинное обучение', 'Трансформер'))

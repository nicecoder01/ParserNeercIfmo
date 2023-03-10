from parse_package.simple_parser_tool import ScrapSession
from parse_package.config import link, params, cookies, headers
import json


def write_to_json(name_of_file, data):
    json_data = json.dumps(data, indent=4, ensure_ascii=False)
    with open(name_of_file, 'w', encoding='UTF-8') as file:
        file.write(json_data)


def get_from_json(name_of_file):
    with open(name_of_file, 'r', encoding='UTF-8') as file:
        dict = json.load(file)
    return dict


def get_link_and_name(list_summary):
    data = []
    root = 'http://neerc.ifmo.ru'
    for summary in list_summary:
        try:
            name = summary.find('a').text.strip()
            link = f"{root}{summary.find('a').get('href')}"
            data.append({
                'nameOfSummary': name,
                'linkOfSummary': link,
            })
        except AttributeError:
            continue
    return data


def get_dict_with_links():
    session = ScrapSession()
    response_soup = session.get(link).soup
    # response_soup = response_soup.find('li', class_='toclevel-1 tocsection-1')
    list_with_summary = response_soup.find_all('span', class_='mw-headline')
    data = get_link_and_name(list_with_summary[1:])
    return data


if __name__ == '__main__':
    pass


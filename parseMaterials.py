from parse_package.multypurpose_parser import ScrapSession
from parse_package.config import link, params, cookies, headers
import json


def write_to_json(data):
    json_data = json.dumps(data, indent=4, ensure_ascii=False)
    with open('result_data.json', 'w', encoding='UTF-8') as file:
        file.write(json_data)


def get_link_and_name(list_summary):
    data = []
    root = 'http://neerc.ifmo.ru/wiki/index.php?title=Заглавная_страница'
    for summary in list_summary:
        name = summary.find('span', class_='toctext').text.strip()
        link = f"{root}{summary.find('a').get('href')}"
        data.append({
            'name_of_summary': name,
            'link_of_summary': link,
        })
    return data


def get_dict_with_links():
    session = ScrapSession()
    response_soup = session.get(link).soup
    response_soup = response_soup.find('li', class_='toclevel-1 tocsection-1')
    list_with_summary = response_soup.find_all('li')
    data = get_link_and_name(list_with_summary)
    return data


if __name__ == '__main__':
    data = get_dict_with_links()
    write_to_json(data)

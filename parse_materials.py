from parse_package.simple_parser_tool import ScrapSession
from parse_package.config import link, params, cookies, headers
import json

session = ScrapSession()


def write_to_json(name_of_file, data):
    json_data = json.dumps(data, indent=4, ensure_ascii=False)
    with open(name_of_file, 'w', encoding='UTF-8') as file:
        file.write(json_data)


def get_from_json(name_of_file):
    with open(name_of_file, 'r', encoding='UTF-8') as file:
        dict = json.load(file)
    return dict


def get_topics(summary_link):
    data = []
    root = 'http://neerc.ifmo.ru'
    chapters_response = session.get(summary_link).soup
    list_of_chapters = chapters_response.find('div', class_='mw-parser-output').find_all('ul')
    for chapter in list_of_chapters:
        topics = chapter.find_all('a')
        for topic in topics:
            try:
                name = topic.get('title')
                if name is None:
                    continue
                link = f"{root}{topic.get('href')}"
                data.append({
                    'nameOfTopic': name,
                    'linkOfTopic': link,
                })
            except AttributeError:
                continue
    return data

def get_link_and_name(list_summary):
    data = []
    root = 'http://neerc.ifmo.ru'
    for summary in list_summary:
        try:
            name = summary.find('a').text.strip()
            link = f"{root}{summary.find('a').get('href')}"
            topics = get_topics(link)
            data.append({
                'nameOfSummary': name,
                'linkOfSummary': link,
                'topicsOfSummary': topics,
            })
        except AttributeError:
            continue
    return data


def get_dict_with_links():
    response_soup = session.get(link).soup
    list_with_summary = response_soup.find_all('span', class_='mw-headline')
    data = get_link_and_name(list_with_summary[1:])
    return data


if __name__ == '__main__':
    pass


from parse_package.simple_parser_tool import ScrapSession
from parse_package.config import link, params, cookies, headers
from json_package.json_tool import load_from_json, write_to_json

session = ScrapSession()


def get_link_topic(name_of_summary, name_of_topic):
    data = load_from_json('json_package/result_data.json')
    for summary in data:
        if summary['nameOfSummary'] == name_of_summary:
            for topic in summary['topicsOfSummary']:
                if topic['nameOfTopic'] == name_of_topic:
                    return topic['linkOfTopic']


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


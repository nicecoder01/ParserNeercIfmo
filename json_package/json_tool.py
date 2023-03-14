import json
import difflib

count_of_elements = 3
delta_summary = 0.05
delta_topic = 0.05


def similarity(s1: str, s2: str):
  normalized1 = s1.lower()
  normalized2 = s2.lower()
  matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
  return matcher.ratio()


def write_to_json(name_of_file: str, data: dict):
    json_data = json.dumps(data, indent=4, ensure_ascii=False)
    with open(name_of_file, 'w', encoding='UTF-8') as file:
        file.write(json_data)


def load_from_json(name_of_file: str):
    with open(name_of_file, 'r', encoding='UTF-8') as file:
        dict = json.load(file)
    return dict


def get_topics_from_json(name_of_summary: str, name_of_file: str):
    data = load_from_json(name_of_file)
    answer = []
    for summary in data:
        answer.append([similarity(summary['nameOfSummary'], name_of_summary), summary['nameOfSummary']])
        if len(answer) == count_of_elements + 1:
            answer.sort(reverse=True)
            answer.pop()
    for index in range(len(answer) - 1, 0, -1):
        if answer[0][0] - answer[index][0] > delta_summary:
            answer.pop(index)
    return answer


def get_link_from_topic_list(name_of_summary: str, name_of_topic: str):
    answer = []
    data = load_from_json('result_data.json')
    for summary in data:
        if summary['nameOfSummary'] == name_of_summary:
            for topic in summary['topicsOfSummary']:
                answer.append([similarity(topic['nameOfTopic'], name_of_topic), topic['linkOfTopic']])
                if len(answer) == count_of_elements + 1:
                    answer.sort(reverse=True)
                    answer.pop()
    for index in range(len(answer) - 1, 0, -1):
        if answer[0][0] - answer[index][0] > delta_summary:
            answer.pop(index)
    return answer


if __name__ == '__main__':
    probable_summary = get_topics_from_json(name_of_summary='дискретка', name_of_file='result_data.json')
    if len(probable_summary) == 1:
        probable_topic = get_link_from_topic_list(name_of_summary=probable_summary[0][1],
                                                  name_of_topic='отношение порядка')
        if len(probable_topic) == 1:
            print(probable_topic[0][1])
        else:
            print(probable_topic)
            # действие, если под запрос пользователя подходит несколько вариантов
    else:
        print(probable_summary)
        # действие, если под запрос пользователя подходит несколько вариантов





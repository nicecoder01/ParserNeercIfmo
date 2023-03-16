import re


def get_group_name(text: str):
    regex = r'\b[PRLDVNTKMUGZH]\d+\b'
    matches = re.findall(regex, text)
    return matches


if __name__ == '__main__':
    print(get_group_name('расписание у группы R32362, пожалуйста')) #['R32362'] - вернёт список со всеми вхождениями



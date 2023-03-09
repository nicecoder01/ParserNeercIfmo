# link = 'http://neerc.ifmo.ru/wiki/index.php'
link = 'http://neerc.ifmo.ru/wiki/index.php?title=Заглавная_страница#.D0.9D.D0.B5.D0.BF.D1.80.D0.BE.D0.B2.D0.B5.D1.80.D1.8F.D0.B5.D0.BC.D1.8B.D0.B5_.D0.BA.D0.BE.D0.BD.D1.81.D0.BF.D0.B5.D0.BA.D1.82.D1.8B'
cookies = {
    '_ga': 'GA1.2.223701308.1673545655',
    'GUEST_LANGUAGE_ID': 'en_US',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ru,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': '_ga=GA1.2.223701308.1673545655; GUEST_LANGUAGE_ID=en_US',
    'If-Modified-Since': 'Sun, 04 Sep 2022 16:51:58 GMT',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.4.778 Yowser/2.5 Safari/537.36',
}

params = {
    'title': 'Заглавная_страница',
}

#response = requests.get('http://neerc.ifmo.ru/wiki/index.php', params=params, cookies=cookies, headers=headers, verify=False)
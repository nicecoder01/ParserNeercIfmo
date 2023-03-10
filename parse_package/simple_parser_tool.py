from bs4 import BeautifulSoup
import requests


class ScrapResponse:
    def __init__(self,
                 page_source: str):
        self.__page_source = page_source

    @property
    def html(self) -> str:
        return self.__page_source


    @property
    def soup(self) -> BeautifulSoup:
        return BeautifulSoup(self.__page_source, 'lxml')


class ScrapSession:
    def __init__(self):
        self.pure_session = requests.Session()

    def get(self,
            url: str,
            **kwargs) -> ScrapResponse:
        return ScrapResponse(self.pure_session.get(url=url, proxies=None, **kwargs).text)

    def post(self,
             url: str,
             **kwargs) -> ScrapResponse:
        return ScrapResponse(self.pure_session.post(url=url, proxies=None, **kwargs).text)


if __name__ == '__main__':
    pass

import requests
from bs4 import BeautifulSoup


class Requester:
    def __init__(self):
        self.url = 'https://finance.ua/ru/currency'
        self.__HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0',
                          'accept': '*/*'}
        self.request = requests.get(url=self.url, headers=self.__HEADERS, params=None)

    def get_page(self):
        if self.request.status_code == 200:
            print("[OK] Connection successful.")
        else:
            print("[X] Connection failed.")
            return 0
        soup = BeautifulSoup(self.request.text, "html.parser")
        cards = soup.find_all('tr')
        parsed_data = []
        for card in cards:
            parsed_data.append(
                {
                    'title': card.find('td', class_='c1').get_text() if
                    card.find('td', class_='c1') is not None else '-',
                    'buy': card.find('td', class_='c2').get_text() if
                    card.find('td', class_='c2') is not None else '-',
                    'sell': card.find('td', class_='c3').get_text() if
                    card.find('td', class_='c3') is not None else '-'
                }
            )
        parsed_data = [i for i in parsed_data if i['title'] != '-'][:3]
        print("[OK] Data parsing successful.")
        return parsed_data


a = Requester()
a.get_page()

import requests
from bs4 import BeautifulSoup

class Steam:
    def __init__(self, link):
        self.link = link

    def get_images(self) -> list:
        result = {}

        response = requests.get(self.link)
        soup = BeautifulSoup(response.content, "html.parser")
        stats = soup.find_all('div', {'class': 'screenshot_holder'})

        print(stats)

    @staticmethod
    def validate_url():
        pass
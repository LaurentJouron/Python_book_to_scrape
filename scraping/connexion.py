import requests
from bs4 import BeautifulSoup


class Connexion:
    def __init__(self, url):
        self.url = url
        self.response = requests.get(self.url)
        self.soup = BeautifulSoup(self.response.content, "html.parser")

    def get_soup(self):
        return self.soup

    def get_response(self):
        return self.response.status_code

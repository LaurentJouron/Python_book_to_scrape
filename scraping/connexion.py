# connexion.py

import requests
from bs4 import BeautifulSoup


class Connexion:
    def __init__(self, url):
        """
        Initialize the Connexion class with a URL,
        send a GET request to the URL, and parse the HTML content.

        Parameters:
            url (str): The target URL to retrieve data from.
        """
        self.url = url
        self.response = requests.get(
            self.url
        )  # Send GET request to the specified URL
        self.soup = BeautifulSoup(
            self.response.content, "html.parser"
        )  # Parse HTML content

    def get_soup(self):
        """
        Retrieve the parsed HTML content as a BeautifulSoup object.

        Returns:
            BeautifulSoup: Parsed HTML of the requested page.
        """
        return self.soup

    def get_response(self):
        """
        Retrieve the status code of the HTTP response.

        Returns:
            int: HTTP status code of the response.
        """
        return self.response.status_code

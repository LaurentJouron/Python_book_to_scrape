# book.py

from bs4 import BeautifulSoup
import requests

from category import Category
from files import File
from constants import WEBSITE

files = File()


class Book(Category):
    def _get_title(self, book):
        """
        Extract the title of a book from the HTML structure.

        Parameters:
            book (Tag): A BeautifulSoup tag object representing a book item.

        Returns:
            str: The cleaned title of the book.
        """
        return book.find("h3").find("a").text.strip()

    def _get_link(self, book):
        """
        Construct the full URL for the book's detail page.

        Parameters:
            book (Tag): A BeautifulSoup tag object representing a book item.

        Returns:
            str: The absolute URL of the book's detail page.
        """
        search_link = (
            book.find("div", class_="image_container").find("a").get("href")
        )
        return (WEBSITE + search_link).replace("../../..", "catalogue")

    def _get_image_link(self, book):
        """
        Construct the full URL for the book's image.

        Parameters:
            book (Tag): A BeautifulSoup tag object representing a book item.

        Returns:
            str: The absolute URL of the book's thumbnail image.
        """
        link = book.find("img", class_="thumbnail")["src"]
        return (WEBSITE + link).replace("../../../..", "")

    def _get_next_button(self, soup, url):
        """
        Find the URL for the 'next' page if available, indicating pagination.

        Parameters:
            soup (BeautifulSoup): The parsed HTML content of the current page.
            url (str): The current URL, used as a base to form the next page URL.

        Returns:
            str or None: The URL of the next page, or None if there are no more pages.
        """
        next_button = soup.find("li", class_="next")
        if next_button is not None:
            if next_link := next_button.find("a"):
                split_next = url.split("/")
                return "/".join(split_next[:7]) + "/" + next_link.get("href")
        return None

    def get_information(self):
        """
        Retrieve information about books across all categories, including title,
        detail page link, and image link. Handles pagination if available.

        Returns:
            list: A list of tuples, each containing category name, category URL,
                  book title, book detail link, and book image link.
        """
        books = []
        categories = self.get_categories()  # Get all available categories
        for name, url in categories:
            exist = True
            while exist:
                response = requests.get(url)
                soup = BeautifulSoup(response.content, "html.parser")

                try:
                    for book in soup.find("ol", class_="row").find_all(
                        "li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3"
                    ):
                        title = self._get_title(book=book)
                        links = self._get_link(book=book)
                        image = self._get_image_link(book=book)
                        # Add the book's details to the list
                        books.append((name, url, title, links, image))

                    # Check if there's a 'next' page; update URL if present, otherwise end loop
                    if next_button := self._get_next_button(
                        soup=soup, url=url
                    ):
                        url = next_button
                    else:
                        exist = False

                except Exception as e:
                    print(f"Error in category {name}: {e}")
                    exist = False
        return books

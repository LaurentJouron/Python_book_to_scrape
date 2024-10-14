from bs4 import BeautifulSoup
import requests

from category import Category
from constants import WEBSITE


class Book(Category):

    def _get_title(self, book):
        return book.find("h3").find("a").text.strip()

    def _get_link(self, book):
        search_link = (
            book.find("div", class_="image_container").find("a").get("href")
        )
        return (WEBSITE + search_link).replace("../../..", "catalogue")

    def _get_price(self, book):
        return book.find("p", class_="price_color").text

    def _get_image_link(self, book):
        link = book.find("img", class_="thumbnail")["src"]
        return (WEBSITE + link).replace("../../../..", "")

    def _get_next_button(self, soup, url):
        next_button = soup.find("li", class_="next")
        if next_button is not None:
            next_link = next_button.find("a")
            if next_link:
                split_next = url.split("/")
                return (
                    ("/".join(split_next[0:7])) + "/" + next_link.get("href")
                )
        return None

    def get_information(self):
        books = []
        categories = self.get_categories()
        for category_name, url in categories:
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
                        price = self._get_price(book=book)
                        image = self._get_image_link(book=book)
                        books.append((title, links, price, image))
                        # files = File()
                        # files.save_image(
                        #     category_name=category_name,
                        #     title=title,
                        #     image=image,
                        # )
                    next_button = self._get_next_button(soup=soup, url=url)
                    if next_button:
                        url = next_button
                    else:
                        exist = False

                except Exception as e:
                    print(f"Erreur de la catégorie {category_name}: {e}")
                    exist = False
        return books

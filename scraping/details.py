from bs4 import BeautifulSoup
import requests

from constants import HEADERS
from book import Book
from files import File
from category import Category

files = File()


class Details(Book):
    def __init__(self):
        super().__init__()
        self.book = Book()
        self.category = Category()
        self.file = File()

    def get_details(self, book_link):
        response = requests.get(book_link)
        soup = BeautifulSoup(response.content, "html.parser")
        details = []
        for tr in soup.find_all("tr"):
            th = tr.find("th").text
            td = tr.find("td").text
            details.append((th + " : " + td + " ,"))
        synopsis = soup.find_all("p")[3].text
        details.append((synopsis))
        return details

    def run(self):
        files = File()

        for name, url, title, link, image in self.book.get_information():
            details = self.get_details(link)
            (
                UPC,
                product_type,
                HT_price,
                TTC_price,
                tax,
                in_stock,
                number_of_review,
                synopsis,
            ) = details

            # Créer et alimenter le fichier CSV
            csv_writer, f = files.make_csv(category=name, headers=HEADERS)
            if csv_writer:
                csv_writer.writerow(
                    [
                        name,
                        url,
                        title,
                        link,
                        image,
                        UPC,
                        product_type,
                        HT_price,
                        TTC_price,
                        tax,
                        in_stock,
                        number_of_review,
                        synopsis,
                    ]
                )
                # Ferme le fichier après écriture
                f.close()

            # Sauvegarder l'image dans le dossier Media
            files.save_image(category=name, image=image, title=title)

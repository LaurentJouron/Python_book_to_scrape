# details.py

from bs4 import BeautifulSoup
import requests

from constants import HEADERS
from book import Book
from files import File
from category import Category

files = File()


class Details(Book):
    def __init__(self):
        """
        Initialize the Details class by setting up instances of Book, Category, and File.
        """
        super().__init__()
        self.book = Book()
        self.category = Category()
        self.file = File()

    def get_details(self, book_link):
        """
        Extract detailed information for a book from its dedicated page.

        Parameters:
            book_link (str): The URL of the book's detail page.

        Returns:
            list: A list containing various details about the book, including synopsis.
        """
        response = requests.get(book_link)
        soup = BeautifulSoup(response.content, "html.parser")
        details = []

        # Gather all book specifications from table rows
        for tr in soup.find_all("tr"):
            th = tr.find("th").text
            td = tr.find("td").text
            details.append(f"{th} : {td} ,")

        # Extract the synopsis from the fourth <p> tag
        synopsis = soup.find_all("p")[3].text
        details.append(synopsis)

        return details

    def run(self):
        """
        Main function to gather book information, create CSV files, and save images.

        For each book:
            - Extract details and write them to a CSV file.
            - Save the book's image to the specified folder.
        """
        files = File()  # Instantiate File for CSV and image handling

        # Loop through all gathered book information
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

            # Create and populate the CSV file with book details
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
                # Close the file after writing
                f.close()

            # Save the book's image in the Media folder categorized by book category
            files.save_image(category=name, image=image, title=title)

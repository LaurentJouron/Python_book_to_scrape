# constants.py

# Base URL of the website to scrape
WEBSITE = "https://books.toscrape.com/"

# CSV headers corresponding to the extracted information for each book
HEADERS = [
    "Name categories",
    "Links categories",
    "Title of the book",
    "Book link",
    "Cover of the book",
    "UPC",
    "product_type",
    "price_excl_tax",
    "price_incl_tax",
    "tax",
    "available_in_stock",
    "number_of_review",
    "synopsis",
]

# Path for the folder where downloaded images will be saved
MEDIA = "./media"

# Path for the folder where generated CSV files will be saved
CSV = "./csv"

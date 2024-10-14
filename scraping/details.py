from book import Book


class Details(Book):
    def __init__(self):
        super().__init__()
        self.book = Book()

    def run(self):
        for title, link, price, image in self.book.get_information():
            print(title, link, price, image)
        # for category in self.get_categories():
        #     self.make_child(category[0])
        #     self.create_csv(category[0], HEADERS)

from constants import WEBSITE
from connexion import Connexion


class Category(Connexion):

    def __init__(self):
        super().__init__(WEBSITE)
        self.categories = self.soup.find("ul", class_="nav nav-list").find_all(
            "a"
        )
        self.category: list = []

    def _get_name(self, category):
        return category.text.strip()

    def _get_url(self, category):
        return WEBSITE + category.get("href").strip()

    def get_categories(self):
        if self.get_response() == 200:
            for category in self.categories:
                name = self._get_name(category)
                url = self._get_url(category)
                if name != "Books":
                    self.category.append((name, url))
            return self.category
        else:
            print("Erreur de connexion")

# category.py

from constants import WEBSITE
from connexion import Connexion


class Category(Connexion):
    def __init__(self):
        """
        Initialize the Category class by inheriting from Connexion.
        Retrieves and stores category links from the website's navigation list.
        """
        super().__init__(WEBSITE)
        # Find all category links within the navigation list (ul element)
        self.categories = self.soup.find("ul", class_="nav nav-list").find_all(
            "a"
        )
        self.category: list = []  # List to store category names and URLs

    def _get_name(self, category):
        """
        Extract the category name by stripping extra whitespace.

        Parameters:
            category (Tag): A BeautifulSoup tag object representing a category link.

        Returns:
            str: The cleaned category name.
        """
        return category.text.strip()

    def _get_url(self, category):
        """
        Construct the full URL for a category by combining the base URL with the relative path.

        Parameters:
            category (Tag): A BeautifulSoup tag object representing a category link.

        Returns:
            str: The full URL of the category.
        """
        return WEBSITE + category.get("href").strip()

    def get_categories(self):
        """
        Retrieve all categories from the website, excluding the main 'Books' category.

        Returns:
            list: A list of tuples, each containing a category name and URL.
        """
        if self.get_response() == 200:
            for category in self.categories:
                name = self._get_name(category)
                url = self._get_url(category)
                if name != "Books":  # Exclude the main 'Books' category
                    self.category.append((name, url))
            return self.category
        else:
            print("Connection error")

# files.py

import requests
import csv
from folder import Folder
from constants import MEDIA, CSV


class File(Folder):
    def make_csv(self, category, headers):
        """
        Create or open a CSV file for a given category and write headers if the file is empty.

        Parameters:
            category (str): The category name to create a CSV for, used in the folder structure.
            headers (list): A list of header names for the CSV file.

        Returns:
            tuple: A tuple containing the CSV writer object and the file object.
                   Returns (None, None) if there is an error in file creation.
        """
        category = category.replace(
            " ", "_"
        )  # Ensure category name is filename-friendly

        # Create or retrieve the child folder for CSV files
        if csv_folder := self.make_child(folder=CSV, category=category):
            try:
                csv_name = f"{csv_folder}/{category}.csv"
                f = open(csv_name, "a", newline="", encoding="utf8")
                csv_writer = csv.writer(f)

                # If the file is new (empty), write the headers
                if f.tell() == 0:
                    csv_writer.writerow(headers)

                # Return the writer and the opened file for further usage
                return csv_writer, f
            except Exception as e:
                print(f"Error creating the CSV file: {e}")
                return None, None
        return None, None

    def save_image(self, category, image, title):
        """
        Save an image from a given URL to a specific folder structure based on category and title.

        Parameters:
            category (str): The category under which the image should be saved.
            image (str): The URL of the image to download and save.
            title (str): The title of the book or item, used as the image filename.

        Returns:
            bool: True if the image was saved successfully, False otherwise.
        """
        category = category.replace(
            " ", "_"
        )  # Format category name for folder structure

        # Create or retrieve the child folder for image storage
        if media_folder := self.make_child(folder=MEDIA, category=category):
            try:
                # Fetch the image content
                response = requests.get(image, allow_redirects=True)

                # Format and save the image file
                image_name = f"{media_folder}/{title.replace(' ', '_')}.jpg"
                with open(image_name, "wb") as f:
                    f.write(response.content)
                print(f"Image saved at: {image_name}")
                return True
            except Exception as e:
                print(f"Error saving image: {e}")
                return False
        return False

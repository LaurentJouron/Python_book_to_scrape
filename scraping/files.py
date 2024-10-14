import requests
import csv
from folder import Folder
from constants import MEDIA, CSV


class File(Folder):
    def make_csv(self, category, headers):
        category = category.replace(" ", "_")

        # Dossier CSV pour chaque catégorie
        csv_folder = self.make_child(folder=CSV, category=category)
        if csv_folder:
            try:
                csv_name = f"{csv_folder}/{category}.csv"
                f = open(csv_name, "a", newline="", encoding="utf8")
                csv_writer = csv.writer(f)

                # Si le fichier est vide, écrire les headers
                if f.tell() == 0:
                    csv_writer.writerow(headers)

                # Retourne le fichier ouvert et le writer
                return (csv_writer, f)
            except Exception as e:
                print(f"Erreur lors de la création du fichier CSV : {e}")
                return None, None
        return None, None

    def save_image(self, category, image, title):
        category = category.replace(" ", "_")
        # Dossier Media pour chaque catégorie
        media_folder = self.make_child(folder=MEDIA, category=category)
        if media_folder:
            try:
                response = requests.get(image, allow_redirects=True)
                image_name = f"{media_folder}/{title.replace(' ', '_')}.jpg"
                with open(image_name, "wb") as f:
                    f.write(response.content)
                print(f"Image sauvegardée dans : {image_name}")
                return True
            except Exception as e:
                print(f"Erreur lors de la sauvegarde de l'image : {e}")
                return False
        return False

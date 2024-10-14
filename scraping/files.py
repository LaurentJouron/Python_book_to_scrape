import os
import requests
import csv
from folder import Folder


class File(Folder):
    def make_csv(self, category, headers):
        category = category.replace(" ", "_")
        folder = self.make_child(category)
        if folder:
            try:
                csv_name = f"{folder}/{category}.csv"
                with open(csv_name, "w", newline="", encoding="utf8") as f:
                    csv_writer = csv.writer(f)
                    csv_writer.writerow(headers)
                return True
            except Exception as e:
                print(f"Erreur lors de la création du fichier CSV : {e}")
                return False
        return False

    def save_image(self, category_name, title, image):
        category_name = category_name.replace(" ", "_")
        title = title.replace(" ", "_")

        # Créer un dossier catégorie à l'intérieur de MEDIA
        category_folder = self.make_child(category_name)

        if category_folder:
            response = requests.get(image, allow_redirects=True)
            if response.status_code == 200:
                # Chemin complet de l'image dans le dossier catégorie
                image_path = os.path.join(category_folder, f"{title}.jpg")
                try:
                    with open(image_path, "wb") as f:
                        f.write(response.content)
                    print(f"Image enregistrée : {image_path}")
                except Exception as e:
                    print(f"Erreur lors de l'enregistrement de l'image : {e}")
            else:
                print(
                    f"Erreur de téléchargement de l'image : {response.status_code}"
                )
        else:
            print("Erreur : Impossible de créer le dossier catégorie.")

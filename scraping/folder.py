import os
from constants import MEDIA, CSV


class Folder:
    def _make_parent(self, parent_name):
        try:
            if not os.path.exists(parent_name):
                os.makedirs(parent_name)
            return True
        except Exception as e:
            print(f"Erreur : {e}")
            return False

    def _make_media(self):
        return self._make_parent(MEDIA)

    def _make_csv(self):
        return self._make_parent(CSV)

    def make_child(self, category_name):
        category_name = category_name.replace(" ", "_")
        try:
            if self._make_media():
                # Création du dossier catégorie à l'intérieur de MEDIA
                category_folder = os.path.join(MEDIA, category_name)
                if not os.path.exists(category_folder):
                    os.makedirs(category_folder)
                return (
                    category_folder  # Retourne le chemin du dossier catégorie
                )
            else:
                return None
        except Exception as e:
            print(f"Erreur : {e}")
            return None

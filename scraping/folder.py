import os


class Folder:
    def make_parent(self, folder_name):
        try:
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
                return True
            return True
        except Exception as e:
            print(f"Erreur : {e}")
            return False

    def make_child(self, folder, category):
        category = category.replace(" ", "_")
        try:
            if self.make_parent(folder):
                child = os.path.join(folder, category)
                if not os.path.exists(child):
                    os.makedirs(child)

                # Retourne le chemin du sous-dossier créé
                return child
            else:
                return False
        except Exception as e:
            print(f"Erreur lors de la création du sous-dossier : {e}")
            return False

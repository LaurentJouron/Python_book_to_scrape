# folder.py

import os


class Folder:
    def make_parent(self, folder_name):
        """
        Create a parent directory if it does not already exist.

        Parameters:
            folder_name (str): The name or path of the directory to create.

        Returns:
            bool: True if the directory was created or already exists;
                  False if an error occurred during creation.
        """
        try:
            # Check if the directory exists, if not, create it
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)  # Create the parent directory
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    def make_child(self, folder, category):
        """
        Create a child directory within a given parent directory.

        Parameters:
            folder (str): The path of the parent directory.
            category (str): The name of the child directory to create within the parent.
                            Spaces in the category name are replaced with underscores.

        Returns:
            str: The path of the created child directory if successful.
            bool: False if an error occurred during creation.
        """
        # Replace spaces in category name to make it suitable for filenames
        category = category.replace(" ", "_")
        try:
            # Ensure the parent directory exists or is created
            if self.make_parent(folder):
                # Define the path for the child directory
                child = os.path.join(folder, category)
                if not os.path.exists(child):
                    os.makedirs(child)  # Create the child directory

                # Return the path of the created child directory
                return child
            else:
                return False
        except Exception as e:
            print(f"Error creating subdirectory: {e}")
            return False

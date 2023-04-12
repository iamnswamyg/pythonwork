import os
import random
import string
import time


def create_random_files(folder_path, num_files):
    """
    Creates the specified number of random files with random names in the given folder path.
    """
    for i in range(num_files):
        # generate a random file name
        file_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        # create the file with the random name in the given folder path
        with open(os.path.join(folder_path, file_name), 'w') as f:
            f.write("")


def create_folders(folder_path, depth, breadth, max_depth):
    """
    Recursively creates folders with random files in both breadth and depth levels.
    """
    # create random files in the current folder
    create_random_files(folder_path, breadth)

    # recursively create subfolders up to the specified maximum depth
    if depth < max_depth:
        for i in range(breadth):
            subfolder_path = os.path.join(folder_path, f"folder_{i}")
            os.makedirs(subfolder_path)
            create_folders(subfolder_path, depth + 1, breadth, max_depth)





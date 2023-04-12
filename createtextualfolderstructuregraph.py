import os

def create_tree_structure(folder_path, output_path, prefix=''):
    """
    Recursively creates a textual tree structure for all files and folders within a given folder path.
    """
    if not os.path.isdir(folder_path):
        return

    # get list of files and folders within the given folder path
    items = os.listdir(folder_path)

    # iterate over the list of items
    with open(output_path, 'a') as f:
        for index, item in enumerate(sorted(items)):
            # get the full path of the item
            item_path = os.path.join(folder_path, item)

            # check if the item is a file or a folder
            if os.path.isfile(item_path):
                # write the file name with a prefix indicating its position in the tree structure
                f.write(f"{prefix}├── {item}\n")
            elif os.path.isdir(item_path):
                # write the folder name with a prefix indicating its position in the tree structure
                f.write(f"{prefix}├── {item}/\n")
                # recursively call the function to create the tree structure for the subfolder
                if index == len(items)-1:
                    create_tree_structure(item_path, output_path, prefix + "    ")
                else:
                    create_tree_structure(item_path, output_path, prefix + "│   ")



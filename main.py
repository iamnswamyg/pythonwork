from createfilesandfolders import *
from createtextualfolderstructuregraph import *

'''
timestamp = time.strftime("%Y%m%d-%H%M%S")
folder_path = f"/home/swamyg/Workspaces/Tests/Python-{timestamp}"
depth = 2  # n level depth
breadth = 1  # m level breadth
max_depth = 2  # maximum depth
os.makedirs(folder_path)
create_folders(folder_path, 0, breadth, max_depth)
'''


folder_path = "/home/swamyg/repos/saltstack"
output_path = "/home/swamyg/Workspaces/Tests/saltstack.txt"
# folder_path = "/home/swamyg/Workspaces/Tests"
# output_path = "/home/swamyg/Workspaces/Tests/output.txt"
with open(output_path, 'w') as f:
    f.write(f"{folder_path}/\n")
create_tree_structure(folder_path, output_path)
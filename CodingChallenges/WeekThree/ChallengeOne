import os

root_path = "C:\Empty_Dir1"
os.mkdir(root_path)

first_level = ["draft_code", "includes", "layouts", "site"]

for folder in first_level:
    os.mkdir(os.path.join(root_path, folder))


second_level = ["pending", "complete"]

for folder in second_level:
    os.mkdir(os.path.join(root_path, "draft_code", folder))

os.mkdir(os.path.join(root_path, "layouts", "default"))
os.mkdir(os.path.join(root_path, "layouts", "post"))
os.mkdir(os.path.join(root_path, "layouts", "post", "posted"))

# delete all folders, find by Googling "delete files and folders python"
# import shutil
# shutil.rmtree(root_path)

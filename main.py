import os
import pathlib


def organize(path, dir_list, files_list):
    for file in files_list:
        dir_name = ""
        for x in pathlib.Path(file).suffixes:
            dir_name += x
        dir_name = dir_name.replace(".", "")
        if (path + dir_name + "/" in dir_list):
            os.system(f"mv {file} {path + dir_name}/")
        else:
            os.mkdir(path + dir_name + "/")
            os.system(f"mv {file} {path + dir_name}/")


path = "/home/kaiky/Downloads/"
dir_list = []
files_list = []

for target in os.listdir(path):
    if os.path.isdir(path + target):
        dir_list.append(path + target + "/")

for target in os.listdir(path):
    if os.path.isfile(path + target):
        files_list.append(path + target)

print("Before:")
os.system(f"ls {path}")
organize(path, dir_list, files_list)
print("*" * 80)
print("After:")
os.system(f"ls {path}")

import os
import PyQt6
import HashCodeHandler
import shutil
import time
from tqdm import tqdm
import json

# q = hash.hashData(r"E:\TestFile\test1\source")
# print(q.dir_in)
# print(q.path_list)
# print(q.subpath_list)
# print(q.code_list)
# print(q.dict)
#
# oa = r"E:\TestFile\test2\a"
# ob = r"E:\TestFile\test2\b"
# a = r"E:\TestFile\test2\a\folder001\foder002\test003.txt"
# try:
#     b = ob + os.sep + a[len(oa):]
#     shutil.copy2(a, b)
#     print("文件複製成功！")
# except FileNotFoundError as e:
#     print("文件複製失敗：", e)
#     try:
#         c = a[len(oa):]
#         print(c)
#         ab = ob + os.sep +c[:c.rindex(os.sep)]
#         print(ab)
#         os.makedirs(ab)
#         print("資料夾創建成功！")
#         b = ob + os.sep + a[len(oa):]
#         shutil.copy2(a, b)
#         print("文件複製成功！")
#
#     except Exception as e:
#         print("錯誤:",e)


# src_dir_in = r"E:\TestFile\test2\a"
# dest_dir_in = r"E:\TestFile\test2\b"
#
# copy_list = [r"test001.txt", r"folder001\test002.txt", r"folder001\foder002\test003.txt", r"folder001\foder003\test004.txt"]
#
# for subpath in copy_list:
#     try:
#         if os.sep in subpath:
#             print(f"{os.path.join(dest_dir_in, subpath[:subpath.rindex(os.sep)])}=={os.path.exists(os.path.join(dest_dir_in, subpath[:subpath.rindex(os.sep)]))}")
#             if not os.path.exists(os.path.join(dest_dir_in, subpath[:subpath.rindex(os.sep)])):
#                 os.makedirs(os.path.join(dest_dir_in, subpath[:subpath.rindex(os.sep)]))
#         shutil.copy2(os.path.join(src_dir_in, subpath), os.path.join(dest_dir_in, subpath))
#         print(f"{subpath}=>複製成功")
#     except Exception as e:
#         print("複製錯誤=>", e)
#
# os.makedirs(r"E:\TestFile\test2\b")

with open(r"D:\program\FileManager\config.json") as f:
    data = json.load(f)
    print(data["test"]["b"])
with open(r"D:\program\FileManager\config.json", "w") as f:
    data = {"test": {"a": 3, "b": 4}}
    data["test"]["b"] = 0
    data["test"]["a"] = 2
    data = json.dump(data, f, indent=2)
    print()
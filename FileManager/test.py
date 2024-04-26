import hash
import shutil
import time
from tqdm import tqdm

q = hash.hashData(r"E:\TestFile\test1\source")
print(q.dir_in)
print(q.path_list)
print(q.subpath_list)
print(q.code_list)
print(q.dict)

#
# a = r"E:\TestFile\test2\a"
# b = r"E:\TestFile\test2\b\a"
# try:
#     shutil.copytree(a, b, copy_function=shutil.copy2)
#     print("文件複製成功！")
# except Exception as e:
#     print("文件複製失敗：", e)

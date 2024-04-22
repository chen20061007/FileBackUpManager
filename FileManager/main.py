import shutil
import hashlib
import os
import hash
import time
import math
from concurrent.futures import ThreadPoolExecutor


path001 = "D:/cameraFile-editing/馬"
path01 = r"E:\TestFile\test1\source"
path02 = r"E:\TestFile\test1\destination"

path03 = r"E:\TestFile\test2\a"
path04 = r"E:\TestFile\test2\b"

########(位置,code)還是(位置,code)?
########雙for要用位置記還是code記?

def is_hash_same(hash_dict1, hash_dict2):
    #整體一致性
    a = list(hash_dict1.keys()) == list(hash_dict2.keys())
    l1 = []
    l2 = []
    for path_src in hash_dict1.values():
        path_suffix_src_list.append(path_src[len(in_path_src):])
    for path_dest in hash_dict2.values():
        path_suffix_dest_list.append(path_dest[len(in_path_dest):])
    b = l1 == l2
    return a and b


start_time = time.time()

#輸入路徑
in_path_src = path001
in_path_dest = path02

#get文件全路徑+code的字典
hash_dict_src = hash.get(in_path_src)#path:coed
hash_dict_dest = hash.get(in_path_dest)#path:coed
print(f"{hash_dict_dest}==={hash_dict_src}")


hashcode_list_src = list(hash_dict_src.values())   #哈西列表
path_list_src = list(hash_dict_src.keys())         #完整路徑列表

hashcode_list_dest = list(hash_dict_dest.values()) #哈西列表
path_list_dest = list(hash_dict_dest.keys())       #完整路徑列表

path_suffix_src_list = []                          #後路徑列表
path_suffix_dest_list = []                         #後路徑列表
for path_src in path_list_src:
    path_suffix_src_list.append(path_src[len(in_path_src)+1:])
for path_dest in path_list_dest:
    path_suffix_dest_list.append(path_dest[len(in_path_dest)+1:])

print(f"{hashcode_list_src}==={hashcode_list_dest}")
print(f"{path_list_src}==={path_list_dest}")
print(f"{path_suffix_src_list}==={path_suffix_dest_list}")


#1有2有 1有2沒有 1沒有2有
copy_dict = {}
index = 0
overwrite = True
for path_suffix_src in path_suffix_src_list:
    if path_suffix_src in path_suffix_dest_list and hashcode_list_src[index] in hashcode_list_dest:
        print(f"1有2有,原位置{path_suffix_src},一致,=>{hashcode_list_src[index]}")
    elif path_suffix_src in path_suffix_dest_list:
        print(f"1有2有,原位置{path_suffix_src},不一致,新內容=>{hashcode_list_src[index]}")
        if overwrite:
            copy_dict[path_list_src[index]] = os.path.join(in_path_dest, path_suffix_src)
    else:
        print(f"1有2沒有,原位置{path_suffix_src},新內容=>{hashcode_list_src[index]}")
        copy_dict[path_list_src[index]] = os.path.join(in_path_dest, path_suffix_src)
    index += 1


print(copy_dict)
print(is_hash_same(hash_dict_src, hash_dict_dest))





end_time = time.time()
print(f"time:{1000 * round(end_time-start_time,7)}ms")

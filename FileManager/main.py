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

def hash_check(dict1, dict2):
    #整體一致性
    a = (list(dict1.keys()) == list(dict2.keys()))
    b = (list(dict1.values()) == list(dict2.values()))
    return a and b


start_time = time.time()

#輸入路徑
dir_in_src = path01
dir_in_dest = path01

hash_src = hash.hashData(dir_in_src)
hash_dest = hash.hashData(dir_in_dest)

copy_dict = {}

is_same = hash_check(hash_src.dict, hash_dest.dict)
if not is_same:
    print("檔案不一致，進行檢查")
    for i, subpath_src in enumerate(hash_src.subpath_list):
        if subpath_src in hash_dest.subpath_list:  # 有同名檔案
            if hash_src.code_list[i] in hash_dest.code_list:
                # 內容相同
                print("同檔案,同內容")
            else:
                # 內容不同
                print("同檔案,不同內容")
        else:
            # 沒同名檔案
            print("沒同檔案")
else:
    print("檔案一致")

print(copy_dict)





end_time = time.time()
print(f"time:{1000 * round(end_time-start_time,7)}ms")

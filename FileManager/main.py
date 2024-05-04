import FileHandler
import HashCodeHandler
import json
import time


path001 = "D:/cameraFile-editing/馬"
path01 = r"E:\\TestFile\test1\source"
path02 = r"E:\TestFile\test1\destination"

path03 = "E:\\TestFile\\test2\\a"
path04 = "E:\\TestFile\\test2\\b"

overwrite = True

def file_check(dict1, dict2):
    #整體一致性
    a = (list(dict1.keys()) == list(dict2.keys()))
    b = (list(dict1.values()) == list(dict2.values()))
    all_equal = a and b
    copy_equal = True
    for key1, value1 in dict1.items():
        if key1 not in dict2.keys():
            copy_equal = False
            break
        elif value1 not in dict2.values():
            copy_equal = False
            break
    return all_equal, copy_equal #完全相同, 複製的相同(目標地有其他的檔案但要複製的都有)
#
# start_time = time.time()
#
# #輸入路徑
# dir_in_src = path03
# dir_in_dest = path04
#
# hash_src = HashCodeHandler.hashData(dir_in_src)
# hash_dest = HashCodeHandler.hashData(dir_in_dest)
#
# all_equal, copy_equal = file_check(hash_src.dict, hash_dest.dict) #完全相同, 複製的相同(目標地有其他的檔案但要複製的都有)
# copyer = FileHandler.copyer(hash_src, hash_dest, overwrite)
# print(copyer.find())
# if not copy_equal:
#     print("檔案不一致，進行檢查")
#     copyer.copy()
# else:
#     print("檔案一致")
# if not all_equal:
#     print("目標資料夾有多餘的檔案:")
#     print(copyer.drift_file_dict.keys())
#
#
#
#
#
#
# end_time = time.time()
# print(f"time:{1000 * round(end_time-start_time,7)}ms")

if __name__ == "__main__":
    with open(r"D:\program\FileManager\config.json", encoding="utf-8") as f:
        config = json.load(f)
    print(f"{config["resource"]["introduction"]}\n{config["resource"]["help"]}")
    while True:
        command = input("=>")

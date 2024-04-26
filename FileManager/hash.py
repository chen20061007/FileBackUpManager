import hashlib
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm


def _hash(file_path):
    hashcode = hashlib.md5()
    hashcode.update(os.path.basename(file_path).encode())
    with open(file_path, "rb") as file_data:
        while True:
            data = file_data.read(100 * 1024 * 1024)
            if not data:
                break
            hashcode.update(data)
    return hashcode.hexdigest()

class hashData:
    def __init__(self, dir_in):
        #輸入
        self.dir_in = dir_in

        #完整路徑列表
        self.path_list = [os.path.join(root, file) for root, _, files in os.walk(dir_in) for file in files]

        #子路徑列表
        self.subpath_list = [path[len(dir_in):] for path in self.path_list]

        #讀取以及計算的線程池
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(_hash, file_path) for file_path in self.path_list]  # 進度顯示用列表

            #進度顯示
            bar = tqdm(total=len(self.path_list))

            for _, _ in enumerate(as_completed(futures), 1):
                bar.update(1)

        #哈希值列表
        self.code_list = [future.result() for future in futures]

        #位置與哈希值的字典
        self.dict = dict(zip(self.subpath_list, self.code_list))



#
# def get(foder_path):
#
#     #取得目標資料夾內以及所有子資料夾內的所有文件
#     file_path_list = []
#     for root, _, files in os.walk(foder_path):
#         for file in files:
#             file_path_list.append(os.path.join(root, file))
#     all_file_count = len(file_path_list)
#
#     #線程池創建
#     with ThreadPoolExecutor() as executor:
#         futures = {executor.submit(hash, file_path): file_path for file_path in file_path_list}#進度顯示用列表
#         # for file_path in file_path_list:
#         #     futures = executor.submit(hash, file_path)
#         hash_code_list = {}
#         bar = tqdm(total = len(file_path_list))
#         #進度顯示
#         completed_counter = 0
#         for future in tqdm(as_completed(futures)):
#             bar.update(1)
#             try:
#                 file_path = futures[future]
#                 # completed_counter += 1
#                 # print(f"{completed_counter}/{all_file_count} from:{file_path:<60} =>{future.result()}")
#             except Exception as e:
#                 print(f"計算 {file_path} 的 hash 時出錯: {e}")
#
#         for future in futures:
#             hash_code_list[futures[future]] = future.result()# 回傳列表
#
#     return hash_code_list

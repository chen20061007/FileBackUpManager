import hashlib
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
class hashData:
    def __init__(self, dir_in):
        #輸入
        self.dir_in = dir_in

        #完整路徑列表
        self.path_list = [os.path.join(root, file) for root, _, files in os.walk(self.dir_in) for file in files]

        #子路徑列表
        self.subpath_list = [path[len(self.dir_in)+1:] for path in self.path_list]

        #讀取以及計算的線程池
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(self._hash, file_path) for file_path in self.path_list]  # 進度顯示用列表

            #進度顯示
            bar = tqdm(total=len(self.path_list), desc="hash encoding...")

            for _, _ in enumerate(as_completed(futures), 1):
                bar.update(1)

        #哈希值列表
        self.code_list = [future.result() for future in futures]

        #位置與哈希值的字典
        self.dict = dict(zip(self.subpath_list, self.code_list))

    def _hash(self, file_path):
        hashcode = hashlib.md5()
        hashcode.update(os.path.basename(file_path).encode())
        with open(file_path, "rb") as file_data:
            while True:
                data = file_data.read(100 * 1024 * 1024)
                if not data:
                    break
                hashcode.update(data)
        return hashcode.hexdigest()
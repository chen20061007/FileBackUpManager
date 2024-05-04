import os
import shutil
from concurrent.futures import ThreadPoolExecutor, as_completed
from shutil import copy2
from tqdm import tqdm

class copyer:
    def __init__(self, hash_src, hash_dest, overwrite):
        self.hash_src = hash_src
        self.hash_dest = hash_dest

        self.overwrite = overwrite
        self.copy_dict= {} #要複製的檔案路徑
        self.drift_file_dict = {} #src沒有但dest有的檔案路徑
        self.same_file_count = 0
        self.modified_file_count = 0
        self.unique_file_count = 0

    def find(self):
        for i, subpath_src in enumerate(self.hash_src.subpath_list):
            # 有同名檔案
            if (subpath_src in self.hash_dest.subpath_list) and (self.hash_src.code_list[i] in self.hash_dest.code_list):
                # print("同檔案,同內容")
                self.same_file_count += 1

            # 內容不同
            elif subpath_src in self.hash_dest.subpath_list:
                # print("同檔案,不同內容")
                self.modified_file_count += 1
                if self.overwrite:
                    self.copy_dict[self.hash_src.path_list[i]] = self.hash_src.subpath_list[i]

            # 沒同名檔案
            else:
                # print("沒同檔案")
                self.unique_file_count += 1
                self.copy_dict[self.hash_src.path_list[i]] = self.hash_src.subpath_list[i]
        for i, subpath_dest in enumerate(self.hash_dest.subpath_list):
            if subpath_dest not in self.hash_src.subpath_list:
                self.drift_file_dict[self.hash_dest.path_list[i]] = subpath_dest

        return self.copy_dict, self.drift_file_dict, self.same_file_count, self.modified_file_count, self.unique_file_count

    def copy(self):
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(self._do_copy, path_src, subpath_src) for path_src, subpath_src in self.copy_dict.items()]

            #進度顯示
            bar = tqdm(total=len(self.hash_src.subpath_list), desc="copying...")

            for _, _ in enumerate(as_completed(futures), 1):
                bar.update(1)

    def _do_copy(self, path_src, subpath_src):
        try:
            if os.sep in subpath_src:
                dir_make = os.path.join(self.hash_dest.dir_in + os.sep, subpath_src[:subpath_src.rindex(os.sep)])  # 目標資料夾(不含文件)
                if not os.path.exists(dir_make):
                    os.makedirs(dir_make) #新增資料夾
            # print('資料夾ok')
            copy2(path_src, os.path.join(self.hash_dest.dir_in + os.sep, subpath_src)) #複製
            # print(f"{subpath_src}=>複製成功")
            return 0
        except Exception as e:
            print("錯誤=>", e)
            return -1



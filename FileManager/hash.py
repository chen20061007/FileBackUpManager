import hashlib
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

def get(foder_path):

    #取得目標資料夾內以及所有子資料夾內的所有文件
    file_path_list = []
    for root, _, files in os.walk(foder_path):
        for file in files:
            file_path_list.append(os.path.join(root, file))
    all_file_count = len(file_path_list)

    #線程池創建
    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(hash, file_path): file_path for file_path in file_path_list}#進度顯示用列表
        # for file_path in file_path_list:
        #     futures = executor.submit(hash, file_path)
        hash_code_list = {}
        bar = tqdm(total = len(file_path_list))
        #進度顯示
        completed_counter = 0
        for future in tqdm(as_completed(futures)):
            bar.update(1)
            try:
                file_path = futures[future]
                # completed_counter += 1
                # print(f"{completed_counter}/{all_file_count} from:{file_path:<60} =>{future.result()}")
            except Exception as e:
                print(f"計算 {file_path} 的 hash 時出錯: {e}")

        for future in futures:
            hash_code_list[futures[future]] = future.result()# 回傳列表

    return hash_code_list


def hash(file_path):
    hashcode = hashlib.md5()
    hashcode.update(os.path.basename(file_path).encode())
    with open(file_path, "rb") as file_data:
        while True:
            data = file_data.read(100 * 1024 * 1024)
            if not data:
                break
            hashcode.update(data)
    return hashcode.hexdigest()

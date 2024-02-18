"""
Created on Feb.17 2024
@author: Blake Jia

This is creating test data sets for each device
../Project/data/sampled_readings.csv
"""
import os
import pandas as pd

# 创建一个名为 "test_dataset_by_device_id" 的文件夹
os.makedirs("../lib/test_dataset_by_device_id", exist_ok=True)

# 遍历 "dataset_by_device_id" 文件夹中的每个 CSV 文件
for filename in os.listdir("../lib/dataset_by_device_id"):
    # 构造完整的文件路径
    filepath = os.path.join("../lib/dataset_by_device_id", filename)

    # 读取当前 CSV 文件的前 10 行数据
    df = pd.read_csv(filepath, nrows=100)

    # 构造新的文件路径
    new_filepath = os.path.join("../lib/test_dataset_by_device_id", filename)

    # 将前 10 行数据写入新的 CSV 文件
    df.to_csv(new_filepath, index=False)

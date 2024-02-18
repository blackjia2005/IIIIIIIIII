"""
Created on Feb.17 2024
@author: Blake Jia

This is spliting up data into small datas by device_id
../Project/data/sampled_readings.csv
"""
import os
import pandas as pd

# 创建一个名为 "dataset_by_device_id" 的文件夹
os.makedirs("../lib/dataset_by_device_id", exist_ok=True)

# 读取原始 CSV 文件
df = pd.read_csv("../Project/data/sampled_readings.csv")

# 根据 "device_id" 进行分组
grouped = df.groupby("device_id")

# 遍历每个分组，并将数据写入新的 CSV 文件
for device_id, group_df in grouped:
    # 构造文件路径
    filename = f"../lib/dataset_by_device_id/{device_id}.csv"
    # 将分组数据写入 CSV 文件
    group_df.to_csv(filename, index=False)

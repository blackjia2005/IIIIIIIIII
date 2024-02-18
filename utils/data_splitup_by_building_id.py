"""
Created on Feb.17 2024
@author: Blake Jia

This program is providing a sketch of the data we have -- which is essential for us to read.
../Project/data/sampled_readings.csv
"""
import os
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

# 创建一个名为 "dataset_by_building_id" 的文件夹
os.makedirs("../lib/dataset_by_building_id", exist_ok=True)

# 读取 devices.csv
devices_df = pd.read_csv("../Project/data/devices.csv")

# 读取 sampled_readings.csv
readings_df = pd.read_csv("../Project/data/sampled_readings.csv")

# 将 devices_df 和 readings_df 根据 "device_id" 进行合并
merged_df = pd.merge(devices_df, readings_df, on="device_id")

# 根据 "building_id" 进行分组
grouped = merged_df.groupby("building_id")

def write_group_to_csv(building_id, group_df):
    # 构造文件路径
    filename = f"../lib/dataset_by_building_id/{building_id}.csv"
    # 将分组数据写入 CSV 文件
    group_df.to_csv(filename, index=False)

# 使用多线程加速文件写入操作
with ThreadPoolExecutor() as executor:
    for building_id, group_df in grouped:
        executor.submit(write_group_to_csv, building_id, group_df)

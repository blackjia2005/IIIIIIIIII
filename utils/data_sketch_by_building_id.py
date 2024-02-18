"""
Created on Feb.17 2024
@author: Blake Jia

This program is providing a sketch of the data we have -- which is essential for us to read.
../Project/data/sampled_readings.csv
"""
import pandas as pd
import os
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor

# 读取 CSV 文件
data = pd.read_csv('../Project/data/sampled_readings.csv')
reading_types = pd.read_csv('../Project/data/reading_types.csv')
devices = pd.read_csv('../Project/data/devices.csv')

# 合并数据，以便获取 reading_type_name 和 building_id
data_merged = pd.merge(data, reading_types, left_on='value_type_id', right_on='reading_type_id')
data_merged = pd.merge(data_merged, devices, on='device_id')

# 按照 building_id 和 reading_type_id 分组
grouped = data_merged.groupby(['building_id', 'value_type_id'])

# 创建 sketches 文件夹
sketches_folder = 'sketches'
os.makedirs(sketches_folder, exist_ok=True)


# 多线程处理文件生成任务
def generate_plots(building_id, reading_type_name, group):
    folder_name = os.path.join(sketches_folder, f'{building_id}_{reading_type_name}')
    os.makedirs(folder_name, exist_ok=True)  # 创建文件夹，如果存在则不创建

    # 在每个文件夹中创建设备文件并绘制散点图
    for device_id, device_data in group.groupby('device_id'):
        plt.figure()
        plt.scatter(device_data['date'], device_data['value'])
        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.title(f'Device ID: {device_id}')
        plt.savefig(os.path.join(folder_name, f'{device_id}.png'))  # 保存图片
        plt.close()


print("开始生成图表...")

# 使用线程池执行任务
with ThreadPoolExecutor() as executor:
    futures = []
    for (building_id, value_type_id), group in grouped:
        reading_type_name = group['reading_type_name'].iloc[0]  # 获取 reading_type_name
        futures.append(executor.submit(generate_plots, building_id, reading_type_name, group))

    # 等待所有任务完成
    for future in futures:
        future.result()

print("图表生成完毕。")


import csv
import random

# 生成随机数据并写入到 CSV 文件中
with open('train_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["device_id","date","value_type_id", "value"])  # 写入表头

    # 生成随机数据
    for _ in range(50000):  # 生成1000行数据，你可以根据需要调整行数
        feature1 = random.randint(0, 10)
        feature2 = random.randint(0, 10)
        feature3 = random.randint(0, 10)
        target = feature1 + 2 * feature2 - 3 * feature3 + random.gauss(0, 0.2)  # 使用线性关系生成目标值，加入随机噪声
        writer.writerow([feature1, feature2, feature3, target])

# 生成测试数据并写入到 CSV 文件中
with open('test_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["device_id","date","value_type_id", "value"])  # 写入表头

    # 生成测试数据
    for _ in range(100):  # 生成10行数据，你可以根据需要调整行数
        feature1 = random.randint(0, 10)
        feature2 = random.randint(0, 10)
        feature3 = random.randint(0, 10)
        target = feature1 + 2 * feature2 - 3 * feature3
        writer.writerow([feature1, feature2, feature3, target])

with open('predict_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["device_id","date","value_type_id"])  # 写入表头

    # 生成测试数据
    for _ in range(100):  # 生成10行数据，你可以根据需要调整行数
        feature1 = random.randint(0, 10)
        feature2 = random.randint(0, 10)
        feature3 = random.randint(0, 10)
        writer.writerow([feature1, feature2, feature3])
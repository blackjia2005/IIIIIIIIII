"""
Created on Feb.17 2024
@author: Blake Jia

Three csv are provided.
1. devices.csv -> alias the device to the buildings ["device_id","building_id"]
2. reading_types.csv -> alias `value_type_id` to `reading_type_name` ["reading_type_id","reading_type_name"]
3. sampled_readings.csv -> ["device_id","date","value_type_id","value"]
One csv is required to fill
test.csv -> ["device_id","date","value_type","value"(unknown)] ==>> "value"

--> possible deductions
S1 devices in the same building should have similar values
"""

import keras
import pandas as pd

column_names = ["device_id", "date", "value_type_id"]
label_name = "value"

def test(train_data_path, test_data_path, predict_data_path, batch_size, num_epochs, model):
    '''
        train_data_path String: location of train file;
        test_data_path String: location of test file;
        batch_size Integer: 32-128;
        num_epochs Integer: number of epochs, 1-10;
        model: keras.Model (input_shape=3), output_layer_dense=1;
    '''
    # 处理CSV
    data = pd.read_csv(train_data_path)
    X = data[column_names].values
    y = data[label_name].values
    # fit the model
    model.compile(optimizer='adam',
                  loss='mean_squared_error',  # 回归任务常用的损失函数
                  metrics=['mse'])  # 评估指标为均方误差
    model.fit(X, y, epochs=num_epochs, batch_size=batch_size)

    # test: -------------------------------------
    test_data = pd.read_csv(test_data_path)
    test_features = test_data[column_names].values
    test_target = test_data[label_name].values  # 提取目标值
    print(test_features.shape)
    print(test_target.shape)
    score = model.evaluate(test_features, test_target)
    print("Test loss:", score[0])
    print("Test mse:", score[1])

    # save_model ----------------------------
    model.save("models/my.model")
    return model
def predict (predict_data_path, model):
    # predict ------------------------------------
    predict = pd.read_csv(predict_data_path)
    predict = predict[column_names].values
    test_data = model.predict(predict)
    predicted_test_data = pd.DataFrame(test_data)  # 将 NumPy 数组转换为 DataFrame
    predicted_test_data.to_csv('predicted_test_data.csv', index=False)

# model1 失败案例
model1 = keras.Sequential([
    keras.layers.Dense(32, activation='relu', input_shape=(3,)),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])
# model2 成功案例 最后可能over-fit
model2 = keras.Sequential([
    keras.layers.Dense(1, input_shape=(3,), activation='linear')
])

model = test(r"../Example/train_data.csv", r"Example/Example.csv", r"Example/predict_data.csv", 32, 10, model2)
predict("../Example/predict_data.csv", model)

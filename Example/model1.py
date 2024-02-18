import keras
from utils.testing_engine import *

# model1 失败案例
myModel = keras.Sequential([
    keras.layers.Dense(32, activation='relu', input_shape=(3,)),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])


#查看传入参数的阐述可以看test_engine.py中的注释
model = test(r"lib/train_data.csv", r"lib/test_data.csv", r"Example/lib/predict_data.csv", 32, 10, myModel)
predict("lib/predict_data.csv", model)

# 执行结束会在当前目录下生成 predicted_test_data.csv，和model，分别是我们会交的东西，和model的副本，免得好不容易训练好了结果弄丢了

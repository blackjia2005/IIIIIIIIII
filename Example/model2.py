import keras
from utils.testing_engine import *

# model2 成功案例 num_epochs太多可能over-fit
myModel = keras.Sequential([
    keras.layers.Dense(1, input_shape=(3,), activation='linear')
])

model = test(r"../Example/src/train_data.csv", r"../Example/src/test_data.csv", r"Example/src/predict_data.csv", 32, 10, myModel)
predict("../Example/src/predict_data.csv", model)

# 执行结束会在当前目录下生成 predicted_test_data.csv，和model，分别是我们会交的东西，和model的副本，免得好不容易训练好了结果弄丢了

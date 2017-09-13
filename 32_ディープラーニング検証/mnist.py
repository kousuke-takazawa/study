# http://qiita.com/ash8h/items/29e24fc617b832fba136

import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop

batch_size = 128 # ミニバッチのサイズ
num_classes = 10 # クラス数（０～９まで）
epochs = 20 # 訓練データを何回繰り返して学習させるか

# MNISTのデータをロード
# トレーニング画像が6万枚、テスト画像が1万枚
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(60000, 784) # 28*28の画像を784の一次元に変換
x_test = x_test.reshape(10000, 784)
x_train = x_train.astype('float32') # int型をfloat32型に変換
x_test = x_test.astype('float32')
x_train /= 255 # 白黒の255階調を０～１に変換
x_test /= 255
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# クラスを2値に変換（例えば5であれば[0, 0, 0, 0, 0, 1, 0, 0, 0, 0]）
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

# モデル構築
# relu>dropout>relu>dropout>softmax
model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(784,)))
model.add(Dropout(0.2))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(10, activation='softmax'))

model.summary() # モデルの要約を出力

model.compile(loss='categorical_crossentropy', # 損失関数
              optimizer=RMSprop(), # 最適化アルゴリズム
              metrics=['accuracy'])

# モデルの学習
history = model.fit(x_train, y_train, # 訓練用の画像とクラス
                    batch_size=batch_size, # ミニバッチの数
                    epochs=epochs, # エポック（繰り返し）の数
                    verbose=1, # ログ出力のフラグ
                    validation_data=(x_test, y_test))  # バリデーションデータ(テスト用を使っていいの？)

# モデルの評価
score = model.evaluate(x_test, y_test, verbose=0)

print('Test loss:', score[0])
print('Test accuracy:', score[1])
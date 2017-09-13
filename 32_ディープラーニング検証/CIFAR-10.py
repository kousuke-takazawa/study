# http://aidiary.hatenablog.com/entry/20161127/1480240182

import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import toimage
from keras.datasets import cifar10

# if __name__ == '__main__':
# CIFAR-10データセットをロード
(X_train, y_train), (X_test, y_test) = cifar10.load_data()
print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)

# 画像を描画
nclasses = 10 # クラス数
pos = 1
for targetClass in range(nclasses): # クラス数だけ繰り返し
    targetIdx = []
    for i in range(len(y_train)): # クラスに合致する画像のインデックスを取得
        if y_train[i][0] == targetClass:
            targetIdx.append(i)

    # 各クラスからランダムに選んだ最初の10個の画像を描画
    np.random.shuffle(targetIdx)
    for idx in targetIdx[:10]:
        img = toimage(X_train[idx])
        plt.subplot(10, 10, pos)
        plt.imshow(img)
        plt.axis('off')
        pos += 1

plt.show()

# --------------

img_rows, img_cols = 32, 32 # 入力画像の次元
img_channels = 3 # チャネル数（RGBなので3）

# (nb_samples, nb_rows, nb_cols, nb_channel) = tf
(X_train, y_train), (X_test, y_test) = cifar10.load_data() # CIFAR-10データをロード

plot_cifar10(X_train, y_train, result_dir) # ランダムに画像をプロット

# 画素値を0-1に変換
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255.0
X_test /= 255.0

# クラスラベル（0-9）をone-hotエンコーディング形式に変換
Y_train = np_utils.to_categorical(y_train, nb_classes)
Y_test = np_utils.to_categorical(y_test, nb_classes)


# CNNを構築
model = Sequential()

# 畳み込み>relu>畳み込み>relu>Maxプーリング>ドロップアウト＞（2回繰り返し）>全結合>relu>ドロップアウト>ソフトマックス
model.add(Convolution2D(32, 3, 3, border_mode='same', input_shape=X_train.shape[1:]))
model.add(Activation('relu'))
model.add(Convolution2D(32, 3, 3))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Convolution2D(64, 3, 3, border_mode='same'))
model.add(Activation('relu'))
model.add(Convolution2D(64, 3, 3))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))

model.add(Dense(nb_classes))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# モデルのサマリを表示
model.summary()
plot(model, show_shapes=True, to_file=os.path.join(result_dir, 'model.png'))

# 訓練
history = model.fit(X_train, Y_train,
                    batch_size=batch_size,
                    nb_epoch=nb_epoch,
                    verbose=1,
                    validation_split=0.1)

# 学習履歴をプロット
plot_history(history, result_dir)

# 学習したモデルと重みと履歴の保存
model_json = model.to_json()
with open(os.path.join(result_dir, 'model.json'), 'w') as json_file:
    json_file.write(model_json)
model.save_weights(os.path.join(result_dir, 'model.h5'))

# モデルの評価
loss, acc = model.evaluate(X_test, Y_test, verbose=0)
print('Test loss:', loss)
print('Test acc:', acc)
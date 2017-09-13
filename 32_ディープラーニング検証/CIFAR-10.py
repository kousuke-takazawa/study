# http://aidiary.hatenablog.com/entry/20161127/1480240182

import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import toimage
from keras.datasets import cifar10

# if __name__ == '__main__':
# CIFAR-10�f�[�^�Z�b�g�����[�h
(X_train, y_train), (X_test, y_test) = cifar10.load_data()
print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)

# �摜��`��
nclasses = 10 # �N���X��
pos = 1
for targetClass in range(nclasses): # �N���X�������J��Ԃ�
    targetIdx = []
    for i in range(len(y_train)): # �N���X�ɍ��v����摜�̃C���f�b�N�X���擾
        if y_train[i][0] == targetClass:
            targetIdx.append(i)

    # �e�N���X���烉���_���ɑI�񂾍ŏ���10�̉摜��`��
    np.random.shuffle(targetIdx)
    for idx in targetIdx[:10]:
        img = toimage(X_train[idx])
        plt.subplot(10, 10, pos)
        plt.imshow(img)
        plt.axis('off')
        pos += 1

plt.show()

# --------------

img_rows, img_cols = 32, 32 # ���͉摜�̎���
img_channels = 3 # �`���l�����iRGB�Ȃ̂�3�j

# (nb_samples, nb_rows, nb_cols, nb_channel) = tf
(X_train, y_train), (X_test, y_test) = cifar10.load_data() # CIFAR-10�f�[�^�����[�h

plot_cifar10(X_train, y_train, result_dir) # �����_���ɉ摜���v���b�g

# ��f�l��0-1�ɕϊ�
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255.0
X_test /= 255.0

# �N���X���x���i0-9�j��one-hot�G���R�[�f�B���O�`���ɕϊ�
Y_train = np_utils.to_categorical(y_train, nb_classes)
Y_test = np_utils.to_categorical(y_test, nb_classes)


# CNN���\�z
model = Sequential()

# ��ݍ���>relu>��ݍ���>relu>Max�v�[�����O>�h���b�v�A�E�g���i2��J��Ԃ��j>�S����>relu>�h���b�v�A�E�g>�\�t�g�}�b�N�X
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

# ���f���̃T�}����\��
model.summary()
plot(model, show_shapes=True, to_file=os.path.join(result_dir, 'model.png'))

# �P��
history = model.fit(X_train, Y_train,
                    batch_size=batch_size,
                    nb_epoch=nb_epoch,
                    verbose=1,
                    validation_split=0.1)

# �w�K�������v���b�g
plot_history(history, result_dir)

# �w�K�������f���Əd�݂Ɨ����̕ۑ�
model_json = model.to_json()
with open(os.path.join(result_dir, 'model.json'), 'w') as json_file:
    json_file.write(model_json)
model.save_weights(os.path.join(result_dir, 'model.h5'))

# ���f���̕]��
loss, acc = model.evaluate(X_test, Y_test, verbose=0)
print('Test loss:', loss)
print('Test acc:', acc)
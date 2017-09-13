# http://qiita.com/ash8h/items/29e24fc617b832fba136

import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop

batch_size = 128 # �~�j�o�b�`�̃T�C�Y
num_classes = 10 # �N���X���i�O�`�X�܂Łj
epochs = 20 # �P���f�[�^������J��Ԃ��Ċw�K�����邩

# MNIST�̃f�[�^�����[�h
# �g���[�j���O�摜��6�����A�e�X�g�摜��1����
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(60000, 784) # 28*28�̉摜��784�̈ꎟ���ɕϊ�
x_test = x_test.reshape(10000, 784)
x_train = x_train.astype('float32') # int�^��float32�^�ɕϊ�
x_test = x_test.astype('float32')
x_train /= 255 # ������255�K�����O�`�P�ɕϊ�
x_test /= 255
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# �N���X��2�l�ɕϊ��i�Ⴆ��5�ł����[0, 0, 0, 0, 0, 1, 0, 0, 0, 0]�j
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

# ���f���\�z
# relu>dropout>relu>dropout>softmax
model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(784,)))
model.add(Dropout(0.2))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(10, activation='softmax'))

model.summary() # ���f���̗v����o��

model.compile(loss='categorical_crossentropy', # �����֐�
              optimizer=RMSprop(), # �œK���A���S���Y��
              metrics=['accuracy'])

# ���f���̊w�K
history = model.fit(x_train, y_train, # �P���p�̉摜�ƃN���X
                    batch_size=batch_size, # �~�j�o�b�`�̐�
                    epochs=epochs, # �G�|�b�N�i�J��Ԃ��j�̐�
                    verbose=1, # ���O�o�͂̃t���O
                    validation_data=(x_test, y_test))  # �o���f�[�V�����f�[�^(�e�X�g�p���g���Ă����́H)

# ���f���̕]��
score = model.evaluate(x_test, y_test, verbose=0)

print('Test loss:', score[0])
print('Test accuracy:', score[1])
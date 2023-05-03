# 8. Write a Python program to recognize handwritten numbers from the MNIST dataset using Tensorflow.

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt
import numpy as np
import random

(X_train, y_train), (X_test, y_test) = mnist.load_data()
num_examples = 1
rand_indices = np.random.randint(len(X_train), size=num_examples)
tem = random.randint(1, 1000)
images = X_train[tem]
labels = y_train[tem]
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)
X_train = X_train.astype('float32') / 255.
X_test = X_test.astype('float32') / 255.

model = Sequential([
    Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D(pool_size=(2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(10, activation='softmax')
])

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X_train, y_train, batch_size=128, epochs=5, verbose=1, validation_data=(X_test, y_test))
score = model.evaluate(X_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
predictions = model.predict(X_test)
x = model.predict(images.reshape(1, 28, 28, 1))
plt.imshow(images)
plt.show()
np.argmax(x, axis=1)
number = np.where(x==1.)[1]
number = str(number).lstrip('[').rstrip(']')
print(f'The model has predicted that the image is of the number {number}.')
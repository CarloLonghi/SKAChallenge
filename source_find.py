import pandas as pd
import numpy as np
import keras
from keras.layers import Input, Dense, Conv2D, Dropout
from keras.models import Model
from astropy.io import fits
from keras import optimizers
import matplotlib.pyplot as plt

dir_path = "./SKAData/"

cutout_size = 218
image_size = 32700

# Define the model
input_layer = Input(shape=(50, 50, 1))
x = Conv2D(16, (7, 7), strides=1, activation='relu', padding='same')(input_layer)
x = Dropout(0.25)(x)
x = Conv2D(32, (5, 5), strides=1, activation='relu', padding='same')(x)
x = Conv2D(64, (3, 3), strides=1, activation='relu', padding='same')(x)
output_layer = Dense(1,activation='sigmoid')(x)

myCNN = Model(input_layer,output_layer)
#es=keras.callbacks.EarlyStopping(monitor='val_loss', patience=5)
adadelta = optimizers.Adadelta(lr=1.0, decay=0.0, rho=0.99)
myCNN.compile(optimizer=adadelta, loss='binary_crossentropy')

print(myCNN.summary())

# load images
img_array = []
for i in range(image_size//cutout_size):
    print(i)
    for j in range(image_size//cutout_size):
        img = np.load(dir_path+"/img_div/img_"+str(i)+"_"+str(j)+".png.npy")
        img_array.append(img)


# load data
data_array = []
for i in range(image_size//cutout_size):
    print(i)
    for j in range(image_size//cutout_size):
        data = np.load(dir_path+"/data_cutouts/data_array_{:d}_{:d}.npy".format(i,j))
        data_array.append(data)


# Divide images and data in training and testing set
# # proportion = 80% train / 20% test
train_X = img_array[0:int(0.8*len(img_array))]
test_X = img_array[int(0.8*len(img_array)):len(img_array)]
train_Y = data_array[0:int(0.8*len(data_array))]
test_Y = data_array[int(0.8*len(data_array)):len(data_array)]

# Training
base_history = myCNN.fit(train_X, train_Y, epochs=10, batch_size=128, shuffle=True, validation_data=(test_X, test_Y))

print(base_history.history.keys())

def plot_history(model_history,keys):
    m,val_m = keys
    plt.plot(model_history.history[m])
    plt.plot(model_history.history[val_m])
    plt.ylabel(m)
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()

plot_history(base_history,['accuracy','val_accuracy'])
plot_history(base_history,['loss','val_loss'])
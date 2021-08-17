import numpy as np
from astropy.io import fits
import pandas as pd
import os

dir_path = "./SKAData/"

cutout_size = 218
image_size = 32700

# Get the data from the training set 
TrainingSet=pd.read_csv(dir_path + "filtered_training_set.csv")
data=np.zeros((image_size,image_size), dtype=np.uint8 )
for i in range(0,len(TrainingSet)):
	    data[int(TrainingSet['y'][i]),int(TrainingSet['x'][i])] = 1

# divide data in 218x218 matrix

if not os.path.isdir(dir_path+"data_cutouts/"):
    os.mkdir(dir_path+"data_cutouts/")

for i in range(0,image_size,cutout_size):
    print(i//cutout_size)
    for j in range(0,image_size,cutout_size):
        #data_array = np.append(data_array,[data[i:i+cutout_size,j:j+cutout_size]], axis=0)
        data_array = data[i:i+cutout_size,j:j+cutout_size]
        np.save(dir_path + "data_cutouts/data_array_{:d}_{:d}.npy".format(i//cutout_size,j//cutout_size),data_array)


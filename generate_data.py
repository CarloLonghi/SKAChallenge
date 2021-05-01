import numpy as np
from astropy.io import fits
import pandas as pd

dir_path = "/home/carlo/SKAData/"

# Divide the fits image in 50x50 images
fits_img = fits.open(dir_path + "SKAMid_B1_8h_v3.fits")
#print(fits_img.info())
fits_img=fits_img[0].data[0,0,16300:20300,16300:20300]

img_array = np.empty((0,50,50))

a = -1
b = -1

# Perché 4000??
for i in range(0,4000,50):
    a+=1
    for j in range(0,4000,50):
        b+=1
        #print(a,b)
        img_array = np.append(img_array,[fits_img[i:i+50,j:j+50]], axis=0)

# Save the generated images
np.save(dir_path + "img_array.npy",img_array)


# Get the data from the training set 
TrainingSet=pd.read_csv(dir_path + "TrainingSet_B1_v2.txt",skiprows=17,delimiter='\s+')
TrainingSet=TrainingSet[TrainingSet.columns[0:15]]
TrainingSet.columns=['ID','RA (core)','DEC (core)','RA (centroid)','DEC (centroid)','FLUX','Core frac','BMAJ','BMIN','PA','SIZE','CLASS','SELECTION','x','y']
TrainingSet['x']=TrainingSet['x'].astype(int)
TrainingSet['y']=TrainingSet['y'].astype(int)
TrainingSet['x']=TrainingSet['x']-16300
TrainingSet['y']=TrainingSet['y']-16300

data=np.zeros((4000,4000,1), dtype=np.uint8 )
for i in range(0,len(TrainingSet)):
	    data[int(TrainingSet['y'][i:i+1]),int(TrainingSet['x'][i:i+1])] = 1

# divide data in 50x50 matrix
a = -1
b = -1

data=data.reshape(data.shape[0],data.shape[1])
data_array = np.empty((0,50,50))

for i in range(0,4000,50):
    a+=1
    for j in range(0,4000,50):
        b+=1
        data_array = np.append(data_array,[data[i+0:i+50,j+0:j+50]], axis=0)

# save the generated data
np.save(dir_path + "data_array.npy",data_array)

import pandas as pd
import numpy as np
import math
from astropy.io import fits

cutout_size = 218
image_size = 32700

def calculate_noise_level(cutout):
    mean = np.mean(cutout**2)
    noise = math.sqrt(mean)
    return noise

# Get the data from the training set 
TrainingSet=pd.read_csv("./TrainingSet_B1_v2.txt",skiprows=17,delimiter='\s+')
TrainingSet=TrainingSet[TrainingSet.columns[0:15]]
TrainingSet.columns=['ID','RA (core)','DEC (core)','RA (centroid)','DEC (centroid)','FLUX','Core frac','BMAJ','BMIN','PA','SIZE','CLASS','SELECTION','x','y']
TrainingSet['x']=TrainingSet['x'].astype(int)
TrainingSet['y']=TrainingSet['y'].astype(int)
#TrainingSet['x']=TrainingSet['x']-16350
#TrainingSet['y']=TrainingSet['y']-16350
TrainingSet = TrainingSet.set_index('ID')
initial_len = len(TrainingSet)
print(initial_len) # === 274883

counter = 0
FilteredTrainingSet = TrainingSet

# Divide the fits image in cutout_size x cutout_size images
fits_img = fits.open("./SKAMid_B1_8h_v3.fits")
#print(fits_img.info())
fits_img=fits_img[0].data[0,0,:,:]

img = np.empty((cutout_size,cutout_size))
img_array = []

a,b = (0,0)
for i in range(0,image_size,cutout_size):
    b = 0
    for j in range(0,image_size,cutout_size):
        img = fits_img[i:i+cutout_size,j:j+cutout_size]
        b += 1
        img_array.append(img)
    a += 1

noise_matrix = []
for i in range(image_size//cutout_size):
    noises = []
    for j in range(image_size//cutout_size):
        cutout = img_array[i*(image_size//cutout_size)+j]
        rms_noise = calculate_noise_level(cutout)
        noises.append(rms_noise)
    noise_matrix.append(noises)

for i in range(len(TrainingSet)):
    print(i)
    x = int(TrainingSet.iloc[i]['x'])
    y = int(TrainingSet.iloc[i]['y']) 
    if y < image_size and x < image_size:
        rms_noise = noise_matrix[y//cutout_size][x//cutout_size]

        flux = TrainingSet.iloc[i]['FLUX'] 
        if  flux < rms_noise:
            FilteredTrainingSet = FilteredTrainingSet.drop(TrainingSet.index[i])
            counter += 1


final_len = len(FilteredTrainingSet)
print(str(initial_len)+" and "+str(final_len)) #274883 and 28470

print(counter)

FilteredTrainingSet.to_csv("./filtered_training_set.csv")
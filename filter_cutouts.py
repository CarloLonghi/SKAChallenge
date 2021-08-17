import pandas as pd
import numpy as np
import math

cutout_size = 218
image_size = 32700

dir_path = "./SKAData/"


# Get the data from the training set 
TrainingSet=pd.read_csv(dir_path + "TrainingSet_B1_v2.txt",skiprows=17,delimiter='\s+')
TrainingSet=TrainingSet[TrainingSet.columns[0:15]]
TrainingSet.columns=['ID','RA (core)','DEC (core)','RA (centroid)','DEC (centroid)','FLUX','Core frac','BMAJ','BMIN','PA','SIZE','CLASS','SELECTION','x','y']
TrainingSet['x']=TrainingSet['x'].astype(int)
TrainingSet['y']=TrainingSet['y'].astype(int)
TrainingSet['x']=TrainingSet['x']-16350
TrainingSet['y']=TrainingSet['y']-16350
TrainingSet = TrainingSet.set_index('ID')
initial_len = len(TrainingSet)
print(initial_len) # === 274883


def calculate_noise_level(cutout):
    mean = np.mean(cutout**2)
    noise = math.sqrt(mean)
    return noise

counter = 0
FilteredTrainingSet = TrainingSet

noise_matrix = []
for i in range(image_size//cutout_size):
    noises = []
    for j in range(image_size//cutout_size):
        cutout = np.load(dir_path+"/img_div/img_"+str(i)+"_"+str(j)+".png.npy")
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

FilteredTrainingSet.to_csv(dir_path+"filtered_training_set.csv")
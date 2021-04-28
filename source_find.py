import pandas as pd
import numpy as np
import keras

# Get the data from the training set 
TrainingSet=pd.read_csv("~/TrainingSet_B1_v2.txt",skiprows=17,delimiter='\s+')
TrainingSet=TrainingSet[TrainingSet.columns[0:15]]
TrainingSet.columns=['ID','RA (core)','DEC (core)','RA (centroid)','DEC (centroid)','FLUX','Core frac','BMAJ','BMIN','PA','SIZE','CLASS','SELECTION','x','y']

print(TrainingSet)



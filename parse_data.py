import pandas as pd
import numpy as numpy
from keras.layers import Conv2D, MaxPooling2D


TrainingSet=pd.read_csv("TrainingSet_B1_v2.txt",skiprows=17,delimiter='\s+')

TrainingSet=TrainingSet[TrainingSet.columns[0:15]]

TrainingSet.columns=['ID','RA (core)','DEC (core)','RA (centroid)','DEC (centroid)','FLUX','Core frac','BMAJ','BMIN','PA','SIZE','CLASS','SELECTION','x','y']

print(TrainingSet)
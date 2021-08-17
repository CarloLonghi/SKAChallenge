import numpy as np
from astropy.io import fits
from numpy.lib.function_base import _calculate_shapes
import pandas as pd
import os

dir_path = "./SKAData/"

cutout_size = 218
image_size = 32700
num_cutout_per_row = image_size // cutout_size  

# Divide the fits image in cutout_size x cutout_size images
fits_img = fits.open(dir_path + "SKAMid_B1_8h_v3.fits")
#print(fits_img.info())
fits_img=fits_img[0].data[0,0,:,:]

if not os.path.isdir(dir_path+"img_div/"):
    os.mkdir(dir_path+"img_div/")

img_array = np.empty((cutout_size,cutout_size))

a,b = (0,0)
for i in range(0,image_size,cutout_size):
    b = 0
    for j in range(0,image_size,cutout_size):
        img_array = fits_img[i:i+cutout_size,j:j+cutout_size]
        np.save(dir_path + "img_div/img_{:d}_{:d}.png".format(a,b),img_array)
        b += 1
    a += 1
    print(a)

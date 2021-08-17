# SKAChallenge
Square Kilometre Array Science Data Challenge

Instructions
- Download this repository
- In the same folder of the repository, create the folder SKAData
- From https://astronomers.skatelescope.org/ska-science-data-challenge-1/ download the Training Set at 560 MHz and the Data at 560 MHz, 8 hours and put them in the SKAData folder
- Run generate_cutouts.py to divide the fits image in smaller images
- Run filter_cutouts.py to filter the noisy data -> the filtered dataset is stored in filtered_training_set.csv
- Run generate_data.py to geenerate the images from the training set
- Run source_find.py to train the network



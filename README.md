# SKAChallenge
Square Kilometre Array Science Data Challenge

Instructions
- Download this repository
- From https://astronomers.skatelescope.org/ska-science-data-challenge-1/ download the Training Set at 560 MHz and the Data at 560 MHz, 8 hours and put them in the folder of the repository
- Run filter_trainingset.py to filter the noisy data: the filtered dataset is stored in filtered_training_set.csv
- Open the notebook localization.ipynb in Colab and run it to train the network on localization data only
- Run the notebook classification.ipynb in Colab to train the network on classificaion data
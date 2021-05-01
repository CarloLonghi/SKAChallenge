# SKAChallenge
Square Kilometre Array Science Data Challenge

Instructions
-From https://astronomers.skatelescope.org/ska-science-data-challenge-1/ download the Training Set at 560 MHz and the Data at 560 MHz, 8 hours 
-Put in the variable dir_path the path to the directory where you have put the data and training set, both in generate_data.py and source_find.py 
-Run generate_data.py to divide the Data and Training Set in 50x50 pixel images
-Run source_find.py to train the network

Per ora ho solo fatto il train della rete ma non l'ho nemmeno testata quindi non sono sicuro che stia effettivamente imparando qualcosa
Però almeno non dà errori lol
La rete fa viene allenata per imparare solo le "pixel coordinates of the centroid" e nessun altro dato.
ConvoSource impara pure a distinguire tra le "categorie di sorgenti". Non penso ci vorrebbe molto a prendere da loro pure quello.
Nella challenge però viene detto di trovare anche altre categorie, quindi dobbiamo guardare come fanno ICRAR.

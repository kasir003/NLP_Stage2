##Author : Nirav Sharda

#!/bin/sh

# Variable to store input file
INPUTFILE='./inputfiles/pmss-noun-4senses.txt'


# Variable to store location of senseclusterscorer.sh
SENSE_CLUSTERS_SCORER_LOCATION='./senseclusters_scorer'

# python3 command line argument
python3 main.py -i $INPUTFILE



# move key files to sensecluster scorer location
mv inputkey.key $SENSE_CLUSTERS_SCORER_LOCATION
mv outputkey.key $SENSE_CLUSTERS_SCORER_LOCATION

# Change directory to senseclustersscorer.sh location
cd $SENSE_CLUSTERS_SCORER_LOCATION

# Run senseclusters_scorer.sh
./senseclusters_scorer.sh outputkey.key inputkey.key

# Print confusion matrix
cat report.out









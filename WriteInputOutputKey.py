# Author : Preethi Chimerla
# Team : Rome
## This function is used to generate the input and output key files
# which is used in senesecluster scorer script to generate
# the precision and other values
import sys

class WriteInputOutputKey(object):
    def __init__(self):
        self.data = []

    # This function generates input key file
    # The idea is to generate a file in the format
    # (word, word.instance, word.sense)
    def WriteInput(self,filename,targetword):
        # A variable to generate a filename based on targetword
        outputfilename='inputkey.key'
        # Open the input file
        f=open(filename,'r')
        f1=open(outputfilename,'w')
        # Get the instance id and sense id from the input file
        # and use them to generate input key file
        for line in f:
            a=[];
            if '<answer' in line:
                a=line.split('"')
                b=targetword+'.'+a[1]
                c=targetword+'.'+a[3]
                f1.write('%s   %s   %s\n' % (targetword,b,c))


    # This function generates the output key file
    # It uses the output of our clusters to
    # generate the output key file
    # Format is <word, word.instance, word.senseidentified>
    def WriteOutput(self,clusters,targetword):
        # Create a filename based on target word
    	filename='outputkey.key'
        # open that file
    	f=open(filename,'w')
    	# Write the instance and the cluster id based on our output
    	# to this file
    	for x in range(len(clusters)):
                b=targetword+'.'+str(x+1)
                c=targetword+'.'+str(clusters[x])
                f.write('%s   %s   %s \n' % (targetword,b,c))



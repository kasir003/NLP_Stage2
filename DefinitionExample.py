#  Author : Preethi Chimerla
#  Team : Rome
#
# This script based on the context vectors picks the example based on dimension words and the instances which are part of the clusters.
# System looks for the dimension words in every instance of the every cluster, it then selects instance in every cluster which has the highest dimension words in it and generates it as the example for the cluster from which the instance is selected.
# After selecting the example it writes both definition and example of each cluster to the output folder
# Input : Context vector matrix
#
# Output : file with definition and example of each sense
# Sample file name : word-defintion_and_examplefile
# example file content : Defintion is :
# either course or said
# Example is:
# And the distinction is not quite so much against the candour and common sense of the world as appears at first ; for a very narrow income has a tendency to contract the mind , and sour the temper . Those who can barely <head>live</head> , and who live perforce in a very small , and generally very inferior , society , may well be illiberal and cross . This does not apply , however , to Miss Bates ; she is only too good natured and too silly to suit me ; but , in general , she is very much to the taste of every body , though single and though poor .
#
import sys
import collections
import nltk
import random
from nltk import pos_tag
from collections import defaultdict

class DefinitionExample(object):
    
    # Constructor
    
    def __init__(self):
        self.data = []
        self.rule = defaultdict(list)
    
    # generates the cluster information based on context vectors
    def ClusterInstances(self,clusters,contextvec):
        clusterinformation=[]
        for x in range(1,max(clusters)+1):
            c=[]
            for y in range(len(clusters)):
                if(clusters[y]==x):
                    c.append(y)
            
        clusterinformation.append(c)
        
        
        return clusterinformation

# picks the instance which has the most dimension words
    def PickExample(self,clusterinformation,contextvec):
        result=[]
        for x in range(len(clusterinformation)):
            maxcount=0
            a=0
            for y in range(len(clusterinformation[x])):
                count=list(contextvec[y]).count(1)
                if(count>maxcount):
                    maxcount=count
                    a=clusterinformation[x][y]
        
            result.append(a)
            
        return result
    # returns the dimension words of each cluster to the Generate Definition class
    def GetWordsDefinition(self,clusterinformation,contextvec,dimensionwords):
        wordsforeachcluster=[]
        for x in range(len(clusterinformation)):
            words=[]
            for y in range(len(clusterinformation[x])):
                for z in range(len(contextvec[clusterinformation[x][y]])):
                    if(contextvec[clusterinformation[x][y]][z]==1):
                        words.append(dimensionwords[z])
        
            wordsforeachcluster.append(collections.Counter(words).most_common(25))
            
        return wordsforeachcluster
    # Writes the definition and example of each word to single file
    def WriteDefinitionExample(self,exampleinstances,filename,targetword,sentence):
        f=open(filename,'r')
        examplefilename=targetword+'-defintion_and_examplefile'
        f1=open(examplefilename,'w')
        count=-1
        for line in f:
            if '<head>' in line:
                count=count+1
                if count in exampleinstances:
                    f1.write('Defintion is :\n')
                    f1.write(sentence[exampleinstances.index(count)])
                    f1.write('\n')
                    f1.write('Example is: \n')
                    f1.write(line)
                    f1.write('\n')








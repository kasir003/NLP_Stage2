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


    def ClusterInstances(self,clusters,contextvec):
        clusterinformation=[]
        for x in range(1,max(clusters)+1):
            c=[]
            for y in range(len(clusters)):
                if(clusters[y]==x):
                    c.append(y)

            clusterinformation.append(c)


        return clusterinformation


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

    def WriteDefinitionExample(self,exampleinstances,filename,targetword,sentence):
        f=open(filename,'r')
        examplefilename=targetword+'defintion_and_examplefile'
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






            

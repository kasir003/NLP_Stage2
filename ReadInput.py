#!bin/usr/python
import sys
import nltk
import numpy
import scipy
import collections
import re
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from numpy import matrix
from scipy.cluster.hierarchy import linkage
from scipy import spatial

class ReadInput(object):

        # Constructor
        def __init__(self):
                self.data =[]

        # This function looks if the word has only alphabets or not
        # and it return true only if it has alphabets.
        def isalpha(self,w):
            return w.replace('_','').isalpha()


        def GetNumberOfSentences(self,filename):
            count=0
            f=open(filename,'r')
            for line in f:
                    if '<context>' in line:
                        count+=1

            return count
        
        def GetWordsFromSentences(self,filename):
            listofsentences=[]
            f=open(filename,'r')
            stop=set(stopwords.words('english'))
            stop.update(['mr','i','mrs','could','would','must','upon','miss'])
            for line in f:
                if '<head>' in line:
                    a=[word for word in nltk.word_tokenize(line) if word.lower() not in stop]
                    a=[word for word in a if self.isalpha(word)]
                    listofsentences.append(a)

            return listofsentences
        
        def GetIndexOfTargetWord(self,listofsent):
            indexes=[]
            for x in range(len(listofsent)):
                index=listofsent[x].index('head')
                indexes.append(index)
                del listofsent[x][index]

            return indexes
        
        def GetFeatureWords(self,listofsent,targetword,number_of_dimensions):
            all_words=[]
            for x in range(len(listofsent)):
                for y in range(len(listofsent[x])):
                        all_words.append(listofsent[x][y])        

            counts=collections.Counter(all_words)
            del counts[targetword]
            words_counts=counts.most_common(number_of_dimensions)
            words_without_count=[]
            dimension_words=[]
            for x in range(0,number_of_dimensions):
                words_without_count.append(words_counts[x][0])

##            print(words_without_count) for x in
##            range(len(words_without_count)):
##            words_without_count[x]=words_without_count[x].lower()
##                           
##            pos_tagged_words=pos_tag(words_without_count)
##
##            print(pos_tagged_words)
##
##            for x in range(len(pos_tagged_words)):
##                if(pos_tagged_words[x][1]!='NNP' and pos_tagged_words[x][1]!='DT' and pos_tagged_words[x][1]!='EX' ):
##                        dimension_words.append(pos_tagged_words[x])
##                           
            return words_without_count

     
                
                
            

                


        


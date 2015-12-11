# Author : Nirav Sharda
# Team : Rome
# This class is used to read the input file from the user and
# pre-process it for further use. It create a list of words in
# each sentences and then removes stop words and punctuation
# marks. It also picks the top words from all sentences as
# feature words or dimensions to the context vectors.

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


        # This function is used to get the number of sentences
        # in the input file
        def GetNumberOfSentences(self,filename):
            # initialize count to 0
            count=0
            # open the file
            f=open(filename,'r')
            # A sentence in the file has the context tag
            # so as long as you see the context tag increment
            # the count
            for line in f:
                    if '<context>' in line:
                        count+=1

            return count

        # This function is used to get a list of words in
        # each sentence. It returns the list of words in
        # each sentence after removing stop-words and
        # punctuation marks
        def GetWordsFromSentences(self,filename):
            # An empty list for storing the output
            listofsentences=[]
            # Open the file
            f=open(filename,'r')
            # It uses nltk stop words
            # So generate a set of words included in nltk.
            stop=set(stopwords.words('english'))
            # Adding some custom words
            stop.update(['mr','i','mrs','could','would','must','upon','miss,shall,O'])

            # Each sentence has a head tag, so look for that tag
            # then tokenize the sentence using nltk word_tokenize
            # and see if it is not a stop word, also check for
            # punctuations and remove them.
            for line in f:
                if '<head>' in line:
                    a=[word for word in nltk.word_tokenize(line) if word.lower() not in stop]
                    a=[word for word in a if self.isalpha(word)]
                    listofsentences.append(a)

            return listofsentences

        # This function is used to get the index of the
        # target word in each sentence.
        def GetIndexOfTargetWord(self,listofsent):
            # An empty list for storing the indexes
            indexes=[]
            # The target word is the word after head
            # in the list of words for each sentence.
            # The idea is to get the index of head and
            # use that as the index of targetword, because
            # the word head is deleted from the list, so
            # the index of head is the index of the target word
            for x in range(len(listofsent)):
                index=listofsent[x].index('head')
                indexes.append(index)
                del listofsent[x][index]

            return indexes

        # This function gives us the feature words or the dimension of
        # the contextvectors. It goes through all the words in all sentences
        # and picks the top words with most counts.
        def GetFeatureWords(self,listofsent,targetword,number_of_dimensions):
            # An empty list for storing all words
            all_words=[]
            # For each sentence add all words to the list
            for x in range(len(listofsent)):
                for y in range(len(listofsent[x])):
                        all_words.append(listofsent[x][y])        

            # Use python collections to count all words
            # and then use most_common to pick most_common words
            # After that the counts are removed and the output
            # is the top words
            counts=collections.Counter(all_words)
            del counts[targetword]
            words_counts=counts.most_common(number_of_dimensions)
            # List for storing words without counts
            words_without_count=[]
            for x in range(0,number_of_dimensions):
                words_without_count.append(words_counts[x][0])
                           
            return words_without_count

     
                
                
            

                


        


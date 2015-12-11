# This class generates the context vectors for each sentence
# and then uses scipy toolkit available in python to cluster
# those context vectors. We use the idea of local context
# vectors as suggested in one of our papers, and use values
# 1 and 0 , 1 to represent if the word is present in the sentence
# and 0 to specify otherwise. We use hierarchical clustering
# to cluster the context vectors.

#!bin/usr/python
import sys
import nltk
import numpy
import scipy
from numpy import matrix
from scipy.cluster.hierarchy import linkage,fcluster,dendrogram
from scipy import spatial
from scipy.spatial.distance import pdist
from matplotlib import pyplot as plt
from numpy.linalg import svd


class ClusterSentences(object):

    # Constructor
    def __init__(self):
        self.data = []


    # This function removes the target word from the list
    # containing words for all sentences
    def RemoveTargetWord(self,listofsent,indexes):
        for x in range(len(listofsent)):
            del listofsent[x][indexes[x]]

        return listofsent

    # This function generates the local context vectors
    def GetLocalContextVector(self,listofsent,dimension_words,number_of_sentences):
            # Create a matrix with zeros whose rows are equal to the number_of_sentences
            # and the columns represent dimension_words.
            contextvector=numpy.zeros((number_of_sentences,len(dimension_words)), dtype=int)
            # Check if the dimension word exists in the current sentence and if it is
            # present represent is by a 1 in the matrix.
            for x in range(number_of_sentences):
                for y in range(len(dimension_words)):
                        if dimension_words[y] in listofsent[x]:
                                contextvector[x][y]=1

            return contextvector

    # This function generates the clusters
    def GetClusters(self,contextvector,number_of_sentences):

          # Adding scipy singular value decomposition
          U,s,v = svd(contextvector,full_matrices=False)
          assert numpy.allclose(contextvector,numpy.dot(U,numpy.dot(numpy.diag(s),v)))
          s[2:]=0
          new_result = numpy.dot(U,numpy.dot(numpy.diag(s),v))

          # We use the linkage function in scipy for hierarchical clustering
          # The method used is the ward, which represents ward variance mimimization
          # algorithm. Also the distance metric used is euclidean which is by default
          # selected.
          result=linkage(new_result,'ward')
          # Then fcluster is used to cluster them.
          # The threshold is selected from the dendrogram
          # Code for plotting the dendrogram has been removed
          # The criterion used is distance
          if(number_of_sentences<300):
              threshold=4
          else:
              threshold=10    
              
          clusters=fcluster(result,threshold,criterion='distance')
          return clusters
    

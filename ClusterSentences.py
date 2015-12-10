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


    def RemoveTargetWord(self,listofsent,indexes):
        for x in range(len(listofsent)):
            del listofsent[x][indexes[x]]

        return listofsent

    def GetLocalContextVector(self,listofsent,dimension_words,number_of_sentences):
            contextvector=numpy.zeros((number_of_sentences,len(dimension_words)), dtype=int)
            for x in range(number_of_sentences):
                for y in range(len(dimension_words)):
                        if dimension_words[y] in listofsent[x]:
                                contextvector[x][y]=1

            return contextvector

    def GetClusters(self,contextvector):
          result=linkage(contextvector,'ward')
          clusters=fcluster(result,10,criterion='distance')
          print(clusters)

          ## Ploting dendrogram
          plt.figure(figsize=(25, 10))
          plt.title('Hierarchical Clustering Dendrogram')
          plt.xlabel('sample index')
          plt.ylabel('distance')
          dendrogram(
            result,
            leaf_rotation=90.,  # rotates the x axis labels
            leaf_font_size=8.,  # font size for the x axis labels
          )
          plt.show()

          plt.title('Hierarchical Clustering Dendrogram (truncated)')
          plt.xlabel('sample index or (cluster size)')
          plt.ylabel('distance')
          dendrogram(
            result,
            truncate_mode='lastp',  # show only the last p merged clusters
            p=12,  # show only the last p merged clusters
            leaf_rotation=90.,
            leaf_font_size=12.,
            show_contracted=True,  # to get a distribution impression in truncated branches
          )
          plt.show()

          return clusters

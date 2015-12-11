# Author: Vamsidhar Reddy , Nirav Sharda
# Team Rome
# This script is the driver program. It create objects for all classes
# and strings all the code together. It calls the methods step by step
# and generates the final output in the desired format.
## Import all files
import getopt,sys,argparse
from ReadInput import ReadInput
from ClusterSentences import ClusterSentences
from WriteInputOutputKey import WriteInputOutputKey
from DefinitionExample import DefinitionExample
from GenerateDefinition import GenerateDefinition


def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description='process some xml file')
    parser.add_argument("-i","--file", dest="filename",help="read data from FIlENAME")
    args=parser.parse_args()
    if not(args.filename):
        parser.error("incorrect number of arguments")

    if args.filename:
        # create objects for all classes
        readinput=ReadInput()
        clustersentences=ClusterSentences()
        writeinputoutputkey=WriteInputOutputKey()
        definitionexample=DefinitionExample()
        generatedefinition= GenerateDefinition()

        # get the number of sentences
        count=readinput.GetNumberOfSentences(str(args.filename))
        # get list of words of each sentence
        list1=readinput.GetWordsFromSentences(str(args.filename))
        # get the indexes of target word for each sentence
        indexes=readinput.GetIndexOfTargetWord(list1)
        # get the targetword
        targetword=list1[0][indexes[0]]
        # get the dimension words
        dimensionwords=readinput.GetFeatureWords(list1,targetword,200)
        # dimension words after removing target word
        listwithouttargetword=clustersentences.RemoveTargetWord(list1,indexes)
        # get the context vectors
        contextvec=clustersentences.GetLocalContextVector(listwithouttargetword,dimensionwords,count)
        # get the cluster list
        clusters=clustersentences.GetClusters(contextvec,count)
        # Creating input and output key files used by sense cluster scorer
        writeinputoutputkey.WriteOutput(clusters,targetword)
        writeinputoutputkey.WriteInput(str(args.filename),targetword)
        # Create the definition and example
        clusterinfo=definitionexample.ClusterInstances(clusters,contextvec)
        exampleids=definitionexample.PickExample(clusterinfo,contextvec)
        wordsforeachcluster=definitionexample.GetWordsDefinition(clusterinfo,contextvec,dimensionwords)
        noun,verb=generatedefinition.PosTagWords(wordsforeachcluster)
        sentence=generatedefinition.WriteDefinition(noun,verb)
        definitionexample.WriteDefinitionExample(exampleids,str(args.filename),targetword,sentence)
#The main function is called 
if __name__ == "__main__":
        main()

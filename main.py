## Import all files
import getopt,sys,argparse
from ReadInput import ReadInput
from ClusterSentences import ClusterSentences
from WriteInputOutputKey import WriteInputOutputKey
from DefinitionExample import DefinitionExample
from GenerateDefinition import GenerateDefinition


def main():

    # create objects
    parser = argparse.ArgumentParser(description='process some xml file')
    parser.add_argument("-i","--file", dest="filename",help="read data from FIlENAME")
    args=parser.parse_args()
    if not(args.filename):
        parser.error("incorrect number of arguments")

    if args.filename:
        readinput=ReadInput()
        clustersentences=ClusterSentences()
        writeinputoutputkey=WriteInputOutputKey()
        definitionexample=DefinitionExample()
        generatedefinition= GenerateDefinition()
        count=readinput.GetNumberOfSentences(str(args.filename))
        list1=readinput.GetWordsFromSentences(str(args.filename))
        indexes=readinput.GetIndexOfTargetWord(list1)
        targetword=list1[0][indexes[0]]
        dimensionwords=readinput.GetFeatureWords(list1,targetword,200)
        listwithouttargetword=clustersentences.RemoveTargetWord(list1,indexes)
        contextvec=clustersentences.GetLocalContextVector(listwithouttargetword,dimensionwords,count)
        clusters=clustersentences.GetClusters(contextvec,count)
        writeinputoutputkey.WriteOutput(clusters,targetword)
        writeinputoutputkey.WriteInput(str(args.filename),targetword)
        clusterinfo=definitionexample.ClusterInstances(clusters,contextvec)
        exampleids=definitionexample.PickExample(clusterinfo,contextvec)
        wordsforeachcluster=definitionexample.GetWordsDefinition(clusterinfo,contextvec,dimensionwords)
        noun,verb=generatedefinition.PosTagWords(wordsforeachcluster)
        sentence=generatedefinition.WriteDefinition(noun,verb)
        definitionexample.WriteDefinitionExample(exampleids,str(args.filename),targetword,sentence)
#The main function is called 
if __name__ == "__main__":
        main()

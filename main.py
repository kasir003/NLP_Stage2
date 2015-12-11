## Import all files
from ReadInput import ReadInput
from ClusterSentences import ClusterSentences
from WriteInputOutputKey import WriteInputOutputKey
from DefinitionExample import DefinitionExample


def main():

    # create objects
    readinput=ReadInput()
    clustersentences=ClusterSentences()
    writeinputoutputkey=WriteInputOutputKey()
    definitionexample=DefinitionExample()
    filename='inputfiles/live-verb-shard014.xml'
    count=readinput.GetNumberOfSentences(filename)
    list1=readinput.GetWordsFromSentences(filename)
    indexes=readinput.GetIndexOfTargetWord(list1)
    targetword=list1[0][indexes[0]]
    dimensionwords=readinput.GetFeatureWords(list1,targetword,200)
    listwithouttargetword=clustersentences.RemoveTargetWord(list1,indexes)
    contextvec=clustersentences.GetLocalContextVector(listwithouttargetword,dimensionwords,count)
    clusters=clustersentences.GetClusters(contextvec,count)
    writeinputoutputkey.WriteOutput(clusters,targetword)
    writeinputoutputkey.WriteInput(filename,targetword)
    clusterinfo=definitionexample.ClusterInstances(clusters,contextvec)
    print(clusterinfo)
    exampleids=definitionexample.PickExample(clusterinfo,contextvec)
    print(exampleids)
    wordsforeachcluster=definitionexample.GetWordsDefinition(clusterinfo,contextvec,dimensionwords)
    noun,verb=definitionexample.PosTagWords(wordsforeachcluster)
    sentence=definitionexample.WriteDefinition(noun,verb)
    definitionexample.WriteDefinitionExample(exampleids,filename,targetword,sentence)
#The main function is called 
if __name__ == "__main__":
        main()

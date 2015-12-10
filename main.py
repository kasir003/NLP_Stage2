from ReadInput import ReadInput
from ClusterSentences import ClusterSentences
from WriteInputOutputKey import WriteInputOutputKey
def main():
    readinput=ReadInput()
    clustersentences=ClusterSentences()
    writeinputoutputkey=WriteInputOutputKey()
    filename='inputfiles/God-Noun-chime006-1.xml'
    count=readinput.GetNumberOfSentences(filename)
    print(count)
    list1=readinput.GetWordsFromSentences(filename)
    print(list1[0])
    indexes=readinput.GetIndexOfTargetWord(list1)
    targetword=list1[0][indexes[0]]
    print(targetword)
    featurewords=readinput.GetFeatureWords(list1,targetword,200)
    listwithouttargetword=clustersentences.RemoveTargetWord(list1,indexes)
    print(listwithouttargetword[0])
    contextvec=clustersentences.GetLocalContextVector(listwithouttargetword,featurewords,count)
    print(contextvec[0])
    clusters=clustersentences.GetClusters(contextvec)
    writeinputoutputkey.WriteOutput(clusters,targetword)
    writeinputoutputkey.WriteInput(filename,targetword)
#The main function is called 
if __name__ == "__main__":
        main()

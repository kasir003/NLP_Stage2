from ReadInput import ReadInput
from ClusterSentences import ClusterSentences
def main():
    readinput=ReadInput()
    clustersentences=ClusterSentences()
    count=readinput.GetNumberOfSentences('manner-noun-shard014.xml')
    print(count)
    list1=readinput.GetWordsFromSentences('manner-noun-shard014.xml')
    print(list1[0])
    indexes=readinput.GetIndexOfTargetWord(list1)
    featurewords=readinput.GetFeatureWords(list1,list1[0][indexes[0]],100)
    listwithouttargetword=clustersentences.RemoveTargetWord(list1,indexes)
    print(listwithouttargetword[0])
    contextvec=clustersentences.GetLocalContextVector(listwithouttargetword,featurewords,count)
    print(contextvec[0])
    clusters=clustersentences.GetClusters(contextvec)
    print(clusters[0:500])
#The main function is called 
if __name__ == "__main__":
        main()

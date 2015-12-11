import sys

class DefinitionExample(object):

    # Constructor

    def __init__(self):
        self.data = []


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

    def WriteExample(self,exampleinstances,filename,targetword):
        f=open(filename,'r')
        examplefilename=targetword+'examplefile'
        f1=open(examplefilename,'w')
        count=-1
        for line in f:
            if '<head>' in line:
                count=count+1
                if count in exampleinstances:
                    f1.write(str(exampleinstances.index(count)+1))
                    f1.write('\n')
                    f1.write(line)
                    f1.write('\n')


                    
            

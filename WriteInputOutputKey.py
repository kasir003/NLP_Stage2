import sys

class WriteInputOutputKey(object):
    def __init__(self):
        self.data = []

    def WriteInput(self,filename,targetword):
        outputfilename=targetword+'inputkeyfile.key'
        f=open(filename,'r')
        f1=open(outputfilename,'w')
        for line in f:
            a=[];
            if '<answer' in line:
                a=line.split('"')
                f1.write('%s   %s\n' % (a[1],a[3]))


    def WriteOutput(self,clusters,targetword):
    	filename=targetword+'outputkeyfile.key'
    	f=open(filename,'w')
    	for x in range(len(clusters)):
    		f.write('%d   %d \n' % (x+1, clusters[x]))



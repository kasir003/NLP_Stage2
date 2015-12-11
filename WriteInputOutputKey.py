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
                b=targetword+'.'+a[1]
                c=targetword+'.'+a[3]
                f1.write('%s   %s   %s\n' % (targetword,b,c))


    def WriteOutput(self,clusters,targetword):
    	filename=targetword+'outputkeyfile.key'
    	f=open(filename,'w')
    	for x in range(len(clusters)):
                b=targetword+'.'+str(x+1)
                c=targetword+'.'+str(clusters[x])
                f.write('%s   %s   %s \n' % (targetword,b,c))



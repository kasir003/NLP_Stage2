import sys
import collections
import nltk
import random
from nltk import pos_tag
from collections import defaultdict

class DefinitionExample(object):

    # Constructor

    def __init__(self):
        self.data = []
        self.rule = defaultdict(list)


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

    def GetWordsDefinition(self,clusterinformation,contextvec,dimensionwords):
        wordsforeachcluster=[]
        for x in range(len(clusterinformation)):
            words=[]
            for y in range(len(clusterinformation[x])):
                for z in range(len(contextvec[clusterinformation[x][y]])):
                    if(contextvec[clusterinformation[x][y]][z]==1):
                        words.append(dimensionwords[z])
    
            wordsforeachcluster.append(collections.Counter(words).most_common(25))
        
        return wordsforeachcluster
    def PosTagWords(self,wordsforeachcluster):
        wordstobetagged=[]
        poswords=[]
        noun=[]
        verb=[]
        for x in range(len(wordsforeachcluster)):
            c=[]
            for index in range(len(wordsforeachcluster[x])):
                c.append(wordsforeachcluster[x][index][0])
            wordstobetagged.append(c)
        
        for x in range(len(wordstobetagged)):
            b=[]
            for y in range(len(wordstobetagged[x])):
                b.append((wordstobetagged[x][y]))
            poswords.append(pos_tag(b))
        

        for index in range(len(poswords)):
            d=[]
            e=[]
            for x in range(len(poswords[index])):
                           if(poswords[index][x][1]=='NN'):
                               d.append(poswords[index][x][0])
                           if((poswords[index][x][1]=='VBP')or(poswords[index][x][1]=='VBD')or(poswords[index][x][1]=='VB')):
                               e.append(poswords[index][x][0])
            noun.append(d)
            verb.append(e)
        return noun,verb

    def prod_rule(self,left,right):
        rules = right.split('|')
        for rule in rules:
            self.rule[left].append(tuple(rule.split()))

    def random_sent(self,sym):

        sentence = ''

        rand_rule = random.choice(self.rule[sym])

        for symbol in rand_rule:
            if symbol in self.rule:
                sentence+=self.random_sent(symbol)
            else:
                sentence+=symbol+' '

        return sentence
    def WriteDefinition(self,noun,verb):
        nounlist=[]
        verblist=[]
        sentence=[]
        for x in range(len(noun)):
            nounlist.append(noun[x][0])
        for x in range(len(verb)):
            verblist.append(verb[x][0])

        for x in range(len(nounlist)):
            self.prod_rule('S', 'NP VP')
            self.prod_rule('NP', 'Det N | Det N')
            self.prod_rule('VP', 'CC V')
            self.prod_rule('CC','or')
            self.prod_rule('Det', 'a | the | this | either  ')
            self.prod_rule('N', nounlist[x])
            self.prod_rule('V', verblist[x])
            sentence.append(self.random_sent('S'))

        return sentence

    def WriteDefinitionExample(self,exampleinstances,filename,targetword,sentence):
        f=open(filename,'r')
        examplefilename=targetword+'defintion_and_examplefile'
        f1=open(examplefilename,'w')
        count=-1
        for line in f:
            if '<head>' in line:
                count=count+1
                if count in exampleinstances:
                    f1.write('Defintion is :\n')
                    f1.write(sentence[exampleinstances.index(count)])
                    f1.write('\n')
                    f1.write('Example is: \n')
                    f1.write(line)
                    f1.write('\n')






            

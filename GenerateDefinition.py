import collections
import nltk
import random
from nltk import pos_tag
from collections import defaultdict
class GenerateDefinition(object):
    def __init__(self):
        self.rule = defaultdict(list)

    
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

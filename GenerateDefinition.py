# Author : Vamsidhar Kasireddy 
# Team : Rome
#  
# This class generates the definition for different senses of the word and return the definitions in a list to the DefinitionExample Class. 
# It generates definition based on Context free grammar rules added in this program.
# 
# Input : The input of this program is list of dimension words of each cluster 
# Sample : [[cluster 1 dimension words][cluster2 dimension words ].....]
# Example : [['came', 'began'], ['said', 'think', 'know', 'make'], ['said', 'man', 'come', 'gave'], ['said', 'father']]
#
# Output : output of program will be a list of sentences representing each cluster 
# Sample : [ [cluster1 sentence 1] [cluster 2 sentence 2 ]]
# Example : ['a come or came ', 'the nothing or said ', 'either ever or said ', 'a come or came ']
# 

import collections
import nltk
import random
from nltk import pos_tag
from collections import defaultdict
class GenerateDefinition(object):
    def __init__(self):
        self.rule = defaultdict(list)

    # This function tags the words in the list with there parts of speech
    # Input is the list of dimension words
    def PosTagWords(self,wordsforeachcluster):
        # defining the lists
        wordstobetagged=[]
        poswords=[]
        noun=[]
        verb=[]
        # extracting the individual words for each cluster
        for x in range(len(wordsforeachcluster)):
            c=[]
            for index in range(len(wordsforeachcluster[x])):
                c.append(wordsforeachcluster[x][index][0])
            wordstobetagged.append(c)
        #tagging all the words in the list
        for x in range(len(wordstobetagged)):
            b=[]
            for y in range(len(wordstobetagged[x])):
                b.append((wordstobetagged[x][y]))
            poswords.append(pos_tag(b))
        # looking for nouns and verbs in the list

        for index in range(len(poswords)):
            d=[]
            e=[]
            for x in range(len(poswords[index])):
                           if(poswords[index][x][1]=='NN'):
                               d.append(poswords[index][x][0])
                           if((poswords[index][x][1]=='VBP')or(poswords[index][x][1]=='VBD')or(poswords[index][x][1]=='VB')or(poswords[index][x][1]=='RB')or(poswords[index][x][1]=='VBG')or(poswords[index][x][1]=='RBR')):
                               e.append(poswords[index][x][0])
            noun.append(d)
            verb.append(e)

            if(len(verb)==0):
                verb.append(noun)
        return noun,verb
    # function sets the CFG RULES based on which sentences are generated
    def prod_rule(self,left,right):
        rules = right.split('|')
        for rule in rules:
            self.rule[left].append(tuple(rule.split()))
    # function generates random sentence based on the words which are arranged according to CFG Rules
    def random_sent(self,sym):

        sentence = ''

        rand_rule = random.choice(self.rule[sym])

        for symbol in rand_rule:
            if symbol in self.rule:
                sentence+=self.random_sent(symbol)
            else:
                sentence+=symbol+' '

        return sentence
    # function assigns the context free grammar rules , appends the sentences to the list according to the cluster and returns the sentence list
    def WriteDefinition(self,noun,verb):
        nounlist=[]
        verblist=[]
        sentence=[]
        for x in range(len(noun)):
            nounlist.append(noun[x][0])
        for x in range(len(verb)):
            verblist.append(verb[x][0])
        # appends the sentences representing the clusters
        for x in range(len(nounlist)):
            self.prod_rule('S', 'NP VP')
            self.prod_rule('NP', 'Det N | Det N')
            self.prod_rule('VP', 'CC V')
            self.prod_rule('CC','or')
            self.prod_rule('Det', 'a | the | either  ')
            self.prod_rule('N', random.choice(nounlist))
            self.prod_rule('V', random.choice(verblist))
            sentence.append(self.random_sent('S'))

        return sentence    

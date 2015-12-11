******************************************************************************************
		UMDuluth-Team-ROME-Cluster words based on context
******************************************************************************************

Author : Vamsidhar Kasireddy - CONTENTS, HOW TO RUN THE PROGRAM,ATTRIBUTIONS
	 Preethi Chimerla - INPUT FILE FORMAT, OUTPUT FILE FORMAT
	 Nirav Sharda - PROBLEM,SOLUTION
	


--------------
CONTRIBUTIONS
--------------

Vamsidhar Kasireddy:

Primary author of GenerateDefinition.py, runit.sh. Contributed 
to Get Clusters function and Main.py. 
Author of the HOW TO RUN section of this README.

Preethi Chimerla:

Primary author of DefinitionExample.py, WriteInputOutputKey.py. 
Also contributed in coming up with a solution of the definition generation. Author of the INPUT FILE and OUTPUT FILE FORMAT sections of this README.

Nirav Sharda:

Primary author of ClusterSentences.py ,ReadInput.py, Install.sh. contributed
to main.py. 
Author of the PROBLEM and SOLUTION sections of this README.

---------
CONTENTS
---------

Contents of the Directory:

1.runit.sh
2.install.sh
3.main.py
4.ReadInput.py
5.ClusterSentences.py
6.DefinitionExample.py
7.GenerateDefinition.py
8.WriteInputOutputKey.py
9.README
10.RESULTS
11.Input
   believe-verb-kasir003.xml
   idea-noun-kasir003.xml
   women-friend-kasir003-1.xml	
   God-Noun-chime006-1.xml
   tell-verb-chime006-2.xml
   priest-heaven-chime006(1).xml
   manner-noun-shard014.xml
   live-verb-shard014.xml
   whale-night-shard014-1.xml

   It basically has all the senseval-2 files of our team.
12.Output
    DefinitionandExamples : Contains all the definition and example text files.
    Keyfiles: Has the original manual key files and system generated output
              key files which can be used for senseclusters_scorer
    It also has all the output senseval-2 files.


13.SenseClusterScorer

--------
PROBLEM 
--------

This section gives details about the problem at hand:

The problem for this project is to create a dictionary from input raw text. 
The input for the system will be some instances (sentences), containing the 
target word, whose meaning has to be determined. The system created as a 
solution must cluster the input instances into N clusters, where N is 
automatically selected by the system. Also the system should give a meaning 
to each of these automatically created clusters and pick an example from the
input instances for each of these clusters. The system should only use the 
input instances containing the target word, along with some random text from
any corpus if needed.

The input file to the system is an xml in senseval 2 format. There are 2 
kinds of input xml files: one of the file contains only one target word which is
either a noun or a verb and the other is a nameconflate xml input file which has 
two target words conflated into one word. The system should automatically cluster 
them into different cluster and give a meaning and also pick an example for 
each cluster.

Then we pick up the first sentence from each cluster as an example, as a part
of the baseline approach. Also we then use the most occuring feature word as
the meaning of each cluster, as a part of the baseline approach.

---------------------------
SOLUTION - BASELINE SYSTEM
---------------------------

This section gives details about the solution used in the system:

The main idea behind the baseline system is that words with same 
sense in different instances (sentences), have similar context i.e 
similar words around the target word. The program initially has all 
the sentences unclustered. It picks up the first sentence which is 
not a part of any cluster and then identifies four words around the target
word i.e both to the left and right of the target word which we call feature 
words. Then it goes through all the other sentences looking for these feature 
words in those sentences. If it finds those feature words it adds those sentences
to the same cluster. Program then finds four words to the left and right of the  target word in all the clustered sentences and adds them to the list storing feature words. We then use this larger set of feature words to go through all the unclustered sentences again finding more sentences that can go to this cluster. 

Once the program loops twice for the feature words and clusters sentences based on the feature words list, it starts working on the remaining unclustered sentences. The program picks up the first instance of the unclustered sentences, identifies feature words around the target word and then searches for those words in all the remaining to be clustered sentences. It keeps on doing that until all the sentences are clustered. 

-----------------------
HOW TO RUN THE PROGRAM
-----------------------

This section gives details about how to run the program:

1) Open Terminal
2) Navigate to the location of the UMDuluth-CS8761-Rome folder.
3) To run the project, runit.sh script should be used. 
4) The runit.sh script has few variables to setup before 
   executing the script on terminal
5) INPUTFILE variable takes in the location of the input senseval-2
   format xml file.
6) The next variable is to setup the location of senseclusters_scorer 
    program and the name of the variable is SENSE_CLUSTERS_SCORER_LOCATION,
    by default it is set to something and the tar file has the 
    sense_cluster_scorer program, so there is no need to change it.
7) To run the main.py python script , need to pass input file name along with "-i" option 
 

------------------
INPUT FILE FORMAT 
------------------

The Primary input for the program is Senseval-2 file format file. 
Three different xml files created by each individual of the team are :
1. A two words, name-conflate pair xml file.
2. Noun xml file.
3. Verb xml file.

Example format for name-conflate pair xml file :
-----------------------------------------------
 <?xml version="1.0" encoding="iso-8859-1" ?>
 <corpus lang='english'>

 <lexelt item="p_h">

 <instance id="1">
 <answer instance="1" senseid="priest"/>
 <context>
  at the valley of Shaveh, which is the king's dale. 14:18 And 
  Melchizedek king of Salem brought forth bread and wine: and 
  he was the  <head>p_h</head> of the most high God.  14:19 
  And he blessed him, and said, Blessed be Abram of the most high 
  God, possessor of     heaven and earth: 
 </context>
 </instance>
 </lexelt>
 </corpus>

Example format for Noun or Verb file :
---------------------------------------
 <?xml version="1.0" encoding="iso-8859-1" ?>
 <corpus lang='english'>

 <lexelt item="G">

 <instance id="1">
 <answer instance="1" senseid="Supreme_Power"/>
 <context>
 In the beginning <head>God</head> created the heaven and the earth.
 And the earth was without form, and void; and darkness was upon 
 the face of the deep. And the 
 </context>
 </instance>
 </lexelt>
 </corpus>


-------------------
OUTPUT FILE FORMAT
-------------------

Three different types of Output files will be generated by this system
1.Output text file
2.Output key file
3.Input key file


1.Output text file: It contains a definition and an example for 
each sense of the target word. The name of this file will be in 
the format as word-definition.text

Example: 
--------
Definition and Examples for God

Defintion is :
either earth or made 
Example is: 
the name of the LORD. This is the book of the generations of Adam. In the day that God created man, in the likeness of <head>God</head> made he him; Male and female created he them; and blessed them, and called their name Adam, in the day when they were created. And 

2.Output Key file: It is generated from the output xml file. 
It acts as input to the Sensecluster Scorer program.
Example:
--------
God   God.1   God.4 
God   God.2   God.1 
God   God.3   God.1 
God   God.4   God.1 
God   God.5   God.1 

3.Input Key file: It is generated from the input xml file. 
It acts as input to the Sensecluster Scorer Program.

Example:
--------
God   God.1   God.Supreme_Power
God   God.2   God.Supreme_Power
God   God.3   God.Supreme_Power
God   God.4   God.Supreme_Power
God   God.5   God.Supreme_Power
God   God.6   God.Supreme_Power

———————————-
ATTRIBUTIONS
————————————
1) David Yarowsky 1995. Unsupervised word sense disambiguation rivaling supervised methods.
Link : http://www.aclweb.org/anthology/P95-1026

Our baseline idea is mostly inspired by the idea given in this paper.

2) Natural Language ToolKit - for Stop words 

http://www.nltk.org/

3) lxml XML toolkit for parsing the input xml.

http://lxml.de/


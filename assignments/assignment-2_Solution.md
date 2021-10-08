# ANLY-580 Assignment 2

#This assignment covers concepts from ANLY-580 Module 2 dealing with distributional semantics.

#To submit this assignment, either enter your answers directly in the `assignments/assignment-2.md` using markdown syntax, or upload a separate file containing your solutions, for example `assignments/assignment-2-solutions.pdf`.

#
#**Format**: take home, open note/wiki

#**Due dates**:
 
 #- Section I: Oct 10
 #- Section II: Oct 06

#**Grade**: 10% (100 pts)

#**Your name**:Haoyu Wang

#**Your NET ID**:hw468

#
## Problems


#1. (10 pts) Describe why the BOW feature representation limits our ability to model human language. What aspect of language, and specifically word meaning, does BOW ignore?

#(1) By using BOW model, it will result to highly sparse structure
#(2) When tackling human language, using BOW will likely produce a very long length of vector since every word will increase dimension, which will be hard for further analysis.
#(3) When BOW meeting unknow unknown language, the information and meaning will be lost.
#(4) The BOW model will lose the inherent and intricate structure of sentence, the meaning of which will be lost.



#2. (20 pts) The word2vec language modeling approach was perhaps the first successful method to learn meaningful word representations. Answer these questions:

#   (a) How does word2vec assign/measure similarity between two words?
    
#Word2Vec can give a distributional representation for every phrase in the corpus. Due to distributional results, a specific measurement in the vector can’t give any precious records. But it can give many duties to locate similarity among phrase by searching vectors as a whole. Then, similarity measures like cosine- similarity can be used between vectors and get the vector.

#  (b) When $N$ is large, what computational bottle neck arises in word2vec that requires us to change the algorithm?
    
#When N is large, the overall complexity is rising because of nonlinear hidden layer. Thus, the recurrent weights in the time dimension and hidden to output layer weights leads to the complexity of the model. So when N is large ,the model will be more complex.
    
#    *Note: we did not tweak the algorithm in the in-class demo, but did mention it during the lecture/demo?*


#3. (20 pts) Why are the inner product and cosine similarity used to measure similarity and not euclidean distance?

#The inner product and cosine similarity can reduce the dimentionality and gives a result between 0 and 1. When analyzing a great amount of text, vectors tend to be very long with lots of dimentions. By use the inner product and cosine similarity can reduce the dimension then euclidean distance and make it easier for futher analyzing.

#4. (50 pts) Write a Python program to compute the trigram ($n=3$) probabilities of the following Dr. Suess corpus:

#    *Hint: See Jurafsky & Martin Chp. 3 for bigram estimation from a similar corpus*
import numpy as np
import pandas as pd
#input the corpus
T1 = "<s> I am Sam </s>"
T2 = "<s> Sam I am </s>"
T3 = "<s> I am Sam </s>"
T4 = "<s> I do not like green eggs and Sam </s>"
T = []
T.append(T1)
T.append(T2)
T.append(T3)
T.append(T4)
T

#Make split
set_all=[]
set1=[]
set2=[]
set3=[]
set4=[]
for i in T1.split(' '):
    set1.append(i)
for i in T2.split(' '):
    set2.append(i)
for i in T3.split(' '):
    set3.append(i)
for i in T4.split(' '):
    set4.append(i)

set_all.append(set1)
set_all.append(set2)
set_all.append(set3)
set_all.append(set4)
set_all

x=0
listY=[]

def rows (listY,text):
    x=0
    while x < len(text)-2:
        listZ=[]
        listZ.append(text[x])
        listZ.append(text[x+1])
        listZ.append(text[x+2])
        x=x+1
        listY.append(listZ)
    return(listY)

listY=rows(listY,set_all[0])
listY=rows(listY,set_all[1])
listY=rows(listY,set_all[2])
listY=rows(listY,set_all[3])
listY

#Define function to find specific wordsblock
def prob (bottom, up, trigram):
    listB=[]
    bottom=bottom.split(' ')
    for i in trigram:
        if (i[0] == bottom[0]) & (i[1] == bottom[1]):
            listB.append(i)
    x=0
    for i in listB:
        if i[2] == up:
            x=x+1
    prob = x/len(listB)
    return(prob)
prob("<s> I", "am", listY)

#Find specific trigram
listbottom = []
listup = []
listprob = []
for i in listY:
    list1=[]
    list2=[]
    list1.append(i[0])
    list1.append(i[1])
    list2.append(i[2])
    b=i[0]+' '+i[1]
    prob1=prob(b,list2[0],listY)
    listbottom.append(list1)
    listup.append(list2)
    listprob.append(prob1)
listprob

#Show each trigram in dataframe.
df=pd.DataFrame()
df["bottom"]=listbottom
df["up"]=listup
df["tragram"]=listprob

    ```
    <s> I am Sam </s>
    <s> Sam I am </s>
    <s> I am Sam </s>
    <s> I do not like green eggs and Sam </s>
    ```

#4. (10 pts Extra Credit) Recall from Lecture 03 that the principle of maximum likelihood makes two qualifying assumptions for any dataset/model combination:

 #   - all examples are drawn from the same distribution

  #  - all examples are drawn independently

   # Which of these qualifying assumptions does word2vec break (many other LMs do too, as it turns)?
   #Answer: all examples are drawn independently

    #*Hint: We make the Markov assumption in language modeling out of necessity; this doesn't mean that it reflects reality!*
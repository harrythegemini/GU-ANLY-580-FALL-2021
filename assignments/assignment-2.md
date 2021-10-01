# ANLY-580 Assignment 2

This assignment covers concepts from ANLY-580 Module 2 dealing with distributional semantics.

To submit this assignment, either enter your answers directly in the `assignments/assignment-2.md` using markdown syntax, or upload a separate file containing your solutions, for example `assignments/assignment-2-solutions.pdf`.

#
**Format**: take home, open note/wiki

**Due dates**:
 
 - Section I: Oct 10
 - Section II: Oct 06

**Grade**: 10% (100 pts)

**Your name**:

**Your NET ID**:

#
## Problems


1. (10 pts) Describe why the BOW feature representation limits our ability to model human language. What aspect of language, and specifically word meaning, does BOW ignore?


2. (20 pts) The word2vec language modeling approach was perhaps the first successful method to learn meaningful word representations. Answer these questions:

    (a) How does word2vec assign/measure similarity between two words?

    (b) When $N$ is large, what computational bottle neck arises in word2vec that requires us to change the algorithm?
    
    *Note: we did not tweak the algorithm in the in-class demo, but did mention it during the lecture/demo?*


3. (20 pts) Why are the inner product and cosine similarity used to measure similarity and not euclidean distance?


4. (50 pts) Write a Python program to compute the trigram ($n=3$) probabilities of the following Dr. Suess corpus:

    *Hint: See Jurafsky & Martin Chp. 3 for bigram estimation from a similar corpus*

    ```
    <s> I am Sam </s>
    <s> Sam I am </s>
    <s> I am Sam </s>
    <s> I do not like green eggs and Sam </s>
    ```

4. (10 pts Extra Credit) Recall from Lecture 03 that the principle of maximum likelihood makes two qualifying assumptions for any dataset/model combination:

    - all examples are drawn from the same distribution

    - all examples are drawn independently

    Which of these qualifying assumptions does word2vec break (many other LMs do too, as it turns)?

    *Hint: We make the Markov assumption in language modeling out of necessity; this doesn't mean that it reflects reality!*
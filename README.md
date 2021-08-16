# ANLY-580 Natural Language Processing

#### Instructor: Chris Larson

#### Term: Fall 2021

#### Section 1: Mondays 6:30-9pm EST (Remote)

#### Section 2: Thursdays 3:30-6pm EST (Intercultural Center Rm.115)

#### Prerequisites: ANLY-501 Machine Learning

#
## Course Description
Natural language processing (NLP) is a critical component of modern information systems. The confluence of deep learning, massive datasets, and hardware accelerators has resulted in systems that approach and in some cases exceed human level performance on benchmark language tasks. In this course we will explore three principal questions: 1) how do we frame language understanding as a tractable statistical inference problem, 2) what are the current state-of-the-art modeling approaches, and 3) how are NLP systems designed and evaluated. In exploring these questions the course exposes students to the foundational math, implementation methods, practical applications, and current research directions in the field. The course will focus less on task-specific feature engineering in order to provide a more complete exposition of the methods that have proven to be most successful in real world applications such as web search, recommender systems, voice and text based chatbots, and machine translation. This course assumes a basic understanding of linear algebra, probability theory, first order optimization methods, and neural networks.


## Reference Texts
1. <a href="https://github.com/jacobeisenstein/gt-nlp-class/blob/master/notes/eisenstein-nlp-notes.pdf">Jacob Eisenstein. Natural Language Processing</a>
2. <a href="https://web.stanford.edu/~jurafsky/slp3/ed3book_dec302020.pdf">Dan Jurafsky, James H. Martin. Speech and Language Processing (3rd ed. draft)</a>


## Course Policies
Students are expected to adhere to all policies in the [Georgetown Honor System Handbook](https://honorcouncil.georgetown.edu/system/policies/), and be aware of [Title IX/Sexual Misconduct](https://sexualassault.georgetown.edu/resourcecenter). We take both of these matters seriously. All work submitted in this class is expected to be your own. In the case of code it is very common to use subroutines written by other people to perform specific tasks; this is OK but you must comment your code when doing so. Each student is required to acknowledge that they are aware of all course policies by completing the [course policy quiz](https://github.com/chrislarson1/GU-ANLY-580-FALL-2021/blob/main/quizzes/quiz-1.md). In person attendance is highly recommended for students in section II.


## Course Grade
The course grade is broken down in the table below. With the exception of labs, all other work (assignments, quizzes, and the project) turned in more than 24 hours late will be assessed a one-time 15% penalty. Code submissions for labs are due at the end of the semester, however, this flexibility is not license to fall behind. The goal is for you to spend the time that is necessary to familiarize yourself with the models, algorithms, and design patterns covered in this course, not test how quickly you can learn the material on a cursory level. Each lab will be graded on a complete/incomplete basis. Incomplete lab tasks will not necessarily be penalized provided that effort was made to complete them (which we can glean from your git commit history and the questions you ask). The rubrik for the final project will be included in the project description released during Lab-07. 

|   Component   | Weight |    Format    |   Section I Due Date   |  Section II Due Date   | 
| :-----------: | :----: | :----------: | :--------------------: | :--------------------: |
| [Quiz 1](https://github.com/chrislarson1/GU-ANLY-580-FALL-2021/blob/main/quizzes/quiz-1.md) | 3% |   individual  | Aug 29 | Sep 01 |
| [Quiz 2]() | 4% | individual | Sep 19 | Sep 15 |
| [Quiz 3]() | 4% | individual | Nov 21 | Nov 10 |
| [Quiz 4]() | 4% | individual | Dec 05 | Dec 01 |
| [Assignment 1](https://github.com/chrislarson1/GU-ANLY-580-FALL-2021/blob/main/assignments/assignment-1.pdf) |   10%  | groups <= 3 | Sep 26 | Sep 22 |
| [Assignment 2]() | 10% | individual | Oct 17 | Oct 06 |
| [Assignment 3]() | 10% | individual | Oct 30 | Oct 19 |
| [Assignment 4]() | 10% | individual | Nov 14 | Nov 03 |
| [Labs](https://github.com/chrislarson1/GU-ANLY-580-FALL-2021/blob/main/labs) |   20%  |   individual | Dec 08 | Dec 08 |
| [Final Project]() | 25% | groups of <= 3 | Dec 08 | Dec 08 |

***Note**: All submissions are due 11:59pm EST on the dates listed. Each of these due dates are listed on the course schedule.*

***Important**: Lab-01 only covers onboarding related material, and is due Aug 29 for Section 1, and Sep 02 for Section 2.*


## Github Onboarding
Students will submit assignments, labs, and the project to private forks of this repository which the instructor and TAs will have access to. Setup instructions are [here](https://github.com/chrislarson1/GU-ANLY-580-FALL-2021/blob/main/github-setup.md).


## Course Schedule

|   Section I  |   Section II   | Lecture |           Description       |    Course Materials     |
| :----------: | :------------: | :-:     | :------------------------- | :---------------------- |
|    Aug 25      |     Aug 26   | 1  | **Introduction to NLP and deep learning** <br> - Course overview <br> - Math refresher <br> **Lab** <br> - Github onboarding <br> - Python environment setup <br> [<a href="https://github.com/chrislarson1/GU-ANLY-580-FALL-2021/tree/main/lectures/lecture-01">Slides</a>] [<a href="https://github.com/chrislarson1/GU-ANLY-580-FALL-2021/tree/main/labs/lab-01">Code</a>] 		| Suggested Reading: <br> [<a href="http://cs229.stanford.edu/section/cs229-linalg.pdf">Eisenstein, Appendix A, B.1, B.2</a>] <br> [<a href="http://cs229.stanford.edu/section/cs229-linalg.pdf">Linear algebra review</a>] <br> [<a href="http://www.columbia.edu/~ks20/4404-Sigman/Notes-Review-Prob.pdf">Probability theory review</a>] <br> [<a href="https://web.stanford.edu/~jurafsky/slp3/ed3book_dec302020.pdf">Jurafsky & Martin, Chp 7</a>] <br> [<a href="https://arxiv.org/pdf/2004.03705.pdf">Review of neural network architectures</a>] <br> [<a href="https://arxiv.org/pdf/1609.04747.pdf">Overview of SGD algorithms</a>] <br> [[Git+GitHub tutorial](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners)] |
|    Aug 29      |     Sep 01   |  | Quiz 1 due **11:59pm EST** | [[Quiz link](https://github.com/chrislarson1/GU-ANLY-580-FALL-2021/blob/main/quizzes/quiz-1.md) ] |
|    Aug 30      |     Sep 02   | 2  | **Text Classification: Part I** <br> - Bag-of-words (BOW) <br> - Decision boundaries <br> - The curse of dimensionality <br> - The perceptron classifier <br> - The linear SVM classifier <br> **Lab** <br> - Text Normalization <br> - Introduction to <a href="https://spacy.io/">Spacy</a> <br> [<a href="https://github.com/chrislarson1/GU-ANLY-580-FALL-2021/tree/main/lectures/lecture-02">Slides</a>] [[Code]()] | Suggested Reading: <br> [<a href="https://github.com/jacobeisenstein/gt-nlp-class/blob/master/notes/eisenstein-nlp-notes.pdf">Eisenstein, Chps 2.1, 2.2, 2.5</a>] <br> [<a href="https://web.stanford.edu/~jurafsky/slp3/ed3book_dec302020.pdf">Jurafsky & Martin, Chp 2.4,4</a>] <br> [<a href="https://www.aaai.org/Papers/ICML/2003/ICML03-081.pdf">Rennie et al., ICML 2003</a>] <br>  [[Joachims, 1998](https://link.springer.com/content/pdf/10.1007/BFb0026683.pdf)] |
|    Sep 13      |     Sep 09   | 3 | **Text Classification: Part II** <br> - Maximum likelihood estimation <br> - Naive Bayes' classifier <br> - Softmax regression <br> **Lab** <br> - Linear text classification on DBpedia dataset <br> [<a href="https://github.com/chrislarson1/GU-ANLY-580-FALL-2021/tree/main/lectures/lecture-03">Slides</a>] [[Code]()] 	| Suggested Reading: <br> [<a href="https://github.com/jacobeisenstein/gt-nlp-class/blob/master/notes/eisenstein-nlp-notes.pdf">Eisenstein, Chps 2.3, 2.4</a>]   |
|    Sep 19      |     Sep 15   |  | Quiz 2 due **11:59pm EST** | [[Quiz link]()] |
|    Sep 20      |     Sep 16   | 4  | **Distributional Semantics: Part 1** <br> - TF-IDF <br> - Low-rank factorization methods <br> - LSA, topic modeling <br> **Lab** <br> - Extracting topics from news feeds <br>  [[Slides]()] [[Code]()]  	| Suggested Reading: <br> [[Ramos, 2003](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.121.1424&rep=rep1&type=pdf)] <br> [<a href="http://cse.msu.edu/~cse960/Papers/LSI/LSI.pdf">LSI overview</a>] <br> [<a href="https://davetang.org/file/Singular_Value_Decomposition_Tutorial.pdf">SVD tutorial</a>] <br> [<a href="https://www.jmlr.org/papers/volume3/blei03a/blei03a.pdf">Bei, et al., JMLR 2003</a>] <br> [<a href="https://radimrehurek.com/gensim/">Gensim website</a>] |
|    Sep 26      |     Sep 22   |  | Assignment 1 due **11:59pm EST** | [[Assignment link](https://github.com/chrislarson1/GU-ANLY-580-FALL-2021/blob/main/assignments/assignment-1.pdf)] |
|    Sep 27      |     Sep 23   | 5  | **Distributional Semantics: Part 2** <br> - Distributional hypothesis <br> - Skip-gram & CBOW models <br> - Word2Vec <br> **Lab** <br> - Visualizing Tweets with Word2Vec <br> [[Slides]()] [[Code]()]  	| Suggested Reading: <br> [<a href="https://github.com/jacobeisenstein/gt-nlp-class/blob/master/notes/eisenstein-nlp-notes.pdf">Eisenstein, Chp 14</a>] <br> [<a href="https://arxiv.org/pdf/1301.3781.pdf">Mikolov et al., 2013</a>] <br> [<a href="https://pair-code.github.io/understanding-umap/">Blogpost on tSNE, UMAP</a>]    |
|    Oct 04      |     Sep 30   | 6  | **Language Modeling: Part 1** <br> - N-grams, sparse data & smoothing <br> - Markov models <br> - Viterbi algorithm <br> **Lab** <br> - Build a semantic matching service with <a href="https://github.com/facebookresearch/StarSpace">StarSpace</a> and <a href="https://github.com/chrislarson1/virtex">Virtex</a> <br> [[Slides]()] [[Code]()]  | Suggested Reading: <br> [<a href="https://github.com/jacobeisenstein/gt-nlp-class/blob/master/notes/eisenstein-nlp-notes.pdf">Eisenstein, Chp 6.1-6.2</a>] <br> [<a href="https://web.stanford.edu/~jurafsky/slp3/ed3book_dec302020.pdf">Jurafsky & Martin, Chps 3, 8</a>] <br> [<a href="https://arxiv.org/pdf/1607.04606.pdf">Bojanowski et al., 2017</a>] <br> [<a href="https://arxiv.org/pdf/1709.03856.pdf">Wu et al., 2017</a>] <br> [<a href="https://fasttext.cc/">FastText</a>] |
|    Oct 17      |     Oct 06   |  | Assignment 2 due **11:59pm EST** | [[Assignment link]()] |
|    Oct 18      |     Oct 07   | 7  | **Language Modeling: Part 2** <br> - Introduction to neural language models <br> - Next word prediction <br> - Downstream tasks <br> - Evaluation metrics <br> **Lab** <br> - Course project kick-off <br> [[Slides]()] [[Code]()]  | Suggested Reading: <br> [<a href="https://github.com/jacobeisenstein/gt-nlp-class/blob/master/notes/eisenstein-nlp-notes-10-15-2018.pdf">Eisenstein, Chp 3</a>] <br> [<a href="http://nlpprogress.com/">NLP Progress website</a>] <br> [<a href="https://huggingface.co/datasets">Huggingface Datasets</a>] <br> [<a href="https://aclanthology.org/W18-5446.pdf">Wang et al., 2018</a>] <br> [<a href="">Project description</a>] |
|    Oct 25      |     Oct 14   | 8  | **Neural Network Architectures for Sequences: Part I** <br> - Convolutional filtering <br> - RNNs, Seq2Seq models <br> - Bidirectionality & ELMO <br> - Siamese nets <br> **Lab** <br> - Introduction to <a href="https://huggingface.co/datasets">Huggingface</a> <br> - Train OpenNMT on en-de dataset <br> [[Slides]()] [[Code]()]  | Suggested Reading: <br> [<a href="https://web.stanford.edu/~jurafsky/slp3/ed3book_dec302020.pdf">Jurafsky & Martin, Chp 9</a>] <br> [<a href="https://github.com/jacobeisenstein/gt-nlp-class/blob/master/notes/eisenstein-nlp-notes-10-15-2018.pdf">Eisenstein, Chp 6.3</a>] <br> [<a href="https://arxiv.org/pdf/1508.06615.pdf">Kim et al., 2016</a>] <br> [[Minaee et al., 2020 (Sec. 2.8)](https://arxiv.org/pdf/2004.03705.pdf)] |
|    Oct 30      |     Oct 19   |  | Assignment 3 due **11:59pm EST** | [[Assignment link]()] |
|    Nov 01      |     Oct 21   | 9  | **Neural Network Architectures for Sequences: Part II** <br> - Masked language model training <br> - Attention <br> - Transformers (BERT, GPT) <br> **Lab** <br> - Finetune BERT on DBpedia, CoNLL-2003, SQuADv2 <br> [[Slides]()] [[Code]()]   | Suggested Reading: <br> [<a href="https://arxiv.org/pdf/1609.08144v2.pdf">Wu et al., 2016</a>] <br> [<a href="https://arxiv.org/pdf/1706.03762.pdf">Vaswani et al., 2017</a>] <br> [<a href="https://arxiv.org/pdf/1810.04805.pdf">Devlin et al., 2019</a>] <br>  [<a href="https://arxiv.org/pdf/2005.14165.pdf">Brown et al., 2020</a>] <br> [<a href="https://cdn.openai.com/palms.pdf">Solaiman et al., 2021</a>] |
|    Nov 08      |     Oct 28   | 10 | **Speech Processing Part I: Speech to Text (STT)** <br> - RNN Transducers, CTC <br> - Transformer based models  <br> **Lab** <br> - Finetune E2E RNNT on your own voice <br> [[Slides]()] [[Code]()]   | Suggested Reading: <br> [<a href="https://arxiv.org/pdf/1211.3711.pdf">Graves, 2012</a>] <br> [<a href="https://arxiv.org/pdf/1811.06621.pdf">He et al., 2018</a>]     |
|    Nov 14      |     Nov 03   |  | Assignment 4 due **11:59pm EST** | [[Assignment link]()] |
|    Nov 15      |     Nov 04   | 11 | **Speech Processing Part II: Text to Speech (TTS)** <br> *Voice Synthesis using Tacotron2 & Waveglow* <br> Guest: Tarek Lahlou <br> Distinguished Data Scientist, Walmart Labs <br> **Lab** <br> - Project work <br> [[Slides]()] [[Code]()]  | Suggested Reading: <br> [<a href="https://deepmind.com/blog/article/wavenet-generative-model-raw-audio">Deepmind blog post</a>] <br> [<a href="https://arxiv.org/pdf/2006.03575.pdf">Donahue et al., ICLR 2021</a>] <br> [<a href="https://arxiv.org/pdf/2102.04040.pdf">Luo et al., 2021</a>]    |
|    Nov 10      |     Nov 10   |  | Project proposals due **11:59pm EST** | [[Project description link]()]  |
|    Nov 21      |     Nov 10   |  | Quiz 3 Due **11:59pm EST** | [[Quiz Link]()] |
|    Nov 22      |     Nov 11   | 12 | **Dialogue Systems: Part I** <br> - Dialogue management <br> - Entity extraction, slot filling <br> - Policy based dialogue <br> **Lab** <br> - Introduction to Rasa <br> [[Slides]()] [[Code]()]    | Suggested Reading: <br> [<a href="https://web.stanford.edu/~jurafsky/slp3/ed3book_dec302020.pdf">Jurafsky & Martin, Chp 24</a>] <br> [<a href="https://arxiv.org/pdf/1712.05181.pdf">Bocklisch et al., 2017</a>]             |
|    Nov 29      |     Nov 18   | 13  | **Dialogue Systems: Part II** <br> *Introduction to Jarvis* <br> Guest: Oluwatobi Olabiyi <br> Senior Research Manager, NVIDIA <br> **Lab** <br> - Project work <br> [[Slides]()] | |
|    Dec 05      |     Dec 01   |  | Quiz 4 due **11:59pm EST** | [[Quiz link]()] |
|    Dec 06      |     Dec 02   | 14 | **NLP System Design** <br> - REST, HTTP, RPCs <br> - Containerization & cloud deployment <br> - Production model serving  <br> **Lab** <br> - Deploy an embedding service on a VM<br> [[Slides]()] [[Code]()]  |   |
| Dec 08 | Dec 08 |  | All lab code/notebooks due **11:59pm EST** <br> Final projects due **11:59pm EST** | |
| TBD    | TBD    |  | Final project poster session & demos | |

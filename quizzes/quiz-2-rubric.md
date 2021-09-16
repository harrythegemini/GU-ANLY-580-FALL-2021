# Quiz 2 rubric

**Format**: Take home. The quiz will be made available via Canvas at 8pm EST the night before the due date, and must be checked in to github by the due date/time. Feel free to use your notes, DO NOT use the internet.

- Section I: 09/26
- Section II: 09/22

**Material covered**: Lecture 01-03

#
## Topics

1. Bag of words feature representation in text classification
    - What is it, how do you construct it, what are some of it's properties (e.g., size, sparsity)

2. Label represention $\bold{y}$ in text classification

3. Decision boundary learning
    - How is a hyperplane represented in $\mathbb{R}^{N}$ 
    - Decision rule using a hyperplane for binary classification
    - Support vector machine (SVM)
        - What are support vectors
        - What is the margin
        - What does maximum margin classifcation mean

4. Probability theory
    - Joint, conditional, and marginal distribution
    - The chain/product rule
    - Independence and conditional independence
    - Bayes Rule

5. Information theory
    - Be able to write down equations for entropy, cross entropy, and KL-divergence

6. Statistical ML
    - Maximum likelihood estimation
        - Be able to write down the likelihood (L), log-likelihood (LL), and negative log-likelihood (NLL) functions for a generic distribution $P(D)$
        - Two principle assumptions of maximum likelihood
    - Generative vs. discriminative learning
        - Be able to give example(s) of each
    - Naive Bayes
        - Naive bayes assumption
        - Data generating process for multinomial NB
    - Softmax regression
        - Relationship between the one-hot encoded vector and the empirical distribution
        - Why NLL gets reduced to cross entropy/KL-divergence when $\bold{y}$ is a one-hot vector

# Quiz 2: Text Classification

**Grade**: 40 pts (4%) + 5 pts (0.5%) extra credit

**Due dates**:
 
 - Section I: Sep 26
 - Section II: Sep 22

**Your name**:

**Your NET ID**: 

#
##  Questions (5 pts each)

1. A bag-of-words feature representation $\bold{x}$ is which of the following:

    (a) A histogram over the words in a document \
    (b) A probability distribution over the words in a document \
    (c) All of the above

2. Which of the following models assume *hard* linear separability of our BOW documents $\bold{X}$ with respect to their class labels $\bold{y}$ (select all that apply)

    (a) Multinomial Naive Bayes \
    (b) Linear SVM \
    (c) The perceptron \
    (d) Softmax regression \
    (e) Linear SVM with soft margin

3. In the SVM, *support vectors* refer to which of the following (select one):

    (a) The margin vectors $\bold{s}$ that connect the closest points $\bold{x}$ to the hyperplane $H$ \
    (b) The vectors $\bold{x}$ that are closest the hyperplane $H$

4. In the SVM, the *margin* refers to which of the following (select one):

    (a) The L2 norm of the margin vectors $\bold{s}$ that connect the closest points $\bold{x}$ to the hyperplane $H$ \
    (b) The L2 norm of the closest points $\bold{x}$ to the hyperplane $H$ \
    (c) The L2 norm of the normal vectors $\bold{w}$ defining $H$

5. There is a uniqe $\bold{w}, b$ that defines every $N$ dimensional hyperplane $H: \{\bold{x} : \bold{x}\bold{w}^{T} + b = 0 \}$ (true/false)?

6. The priciple of maximum likelihood estimation makes which assumptions about a set of observed data $D = \{ \bold{x}^{(1)},y^{(1)}, \dots, \bold{x}^{(M)}, y^{(M)} \}$ (select all that apply):

    (a) All $D^{(i)}$ are drawn from the same distribution (i.e., identically distributed) \
    (b) All $D^{(i)}$ are drawn independently \
    (c) The word counts $\bold{x}^{(i)}_{j}$ are all independent conditioned on their class label $y^{(i)}$

7. Discriminative learning amounts to estimating $\boldsymbol{\theta}$ for (select all that apply):

    (a) $P(\bold{x}, y; \boldsymbol{\theta})$ \
    (b) $P(y; \boldsymbol{\theta})$ \
    (c) $P(\bold{y} | \bold{x}; \boldsymbol{\theta})$ \
    (d) $P(\bold{x} | y; \boldsymbol{\theta})$

8. The data generating process for the multinomial Naive Bayes is (select one):

    (a) $\forall_{i} \; \text{do}:$ (i) $\bold{x}^{(i)} \sim Multinomial(\bold{x} | \text{y}, \boldsymbol{\phi})$, (ii) $y^{(i)} \sim Categorical(\boldsymbol{\mu})$ \
    (b) $\forall_{i} \; \text{do}:$ (i) $y^{(i)} \sim Categorical(\boldsymbol{\mu})$, (ii) $\bold{x}^{(i)} \sim Multinomial(\bold{x} | \text{y}=y^{(i)}, \boldsymbol{\phi})$

##  Extra credit (5 pts)

9. In softmax regression we describe our label as a one-hot vector: $\bold{y} \in \{ 0,1\}^{K}, \sum_{k}\bold{y}_{k} = 1$. What are the following implications of this selection (select all that apply):

    (a) $\bold{y}$ represents an empirical distribution over $K$ classes \
    (b) The entropy $H(\bold{y})$ of our labels is zero \
    (c) Minimizing $NLL(\boldsymbol{\theta} | D)$ equates to minimizing $H(\bold{y}, \; P(\bold{y} | \bold{x} ; \boldsymbol{\theta}))$, the cross entropy between our model distribution and the empirical distribution $\bold{y}$ \
    (d) Minimizing $NLL(\boldsymbol{\theta} | D)$ equates to minimizing $D_{KL}(\bold{y} \; || \; P(\bold{y} | \bold{x} ; \boldsymbol{\theta}))$, the KL divergence between our model distribution and the empirical distribution $\bold{y}$
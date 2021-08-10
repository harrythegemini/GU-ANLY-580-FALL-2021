# ANLY-580 Assignment 1

The purpose of this assignment is to familiarize you with some of the underlying concepts used in machine learning and NLP. Feel free to use definitions from Wikipedia to aid in this self study, but refrain from searching for answers directly. If you get stuck, team up with no more than three classmates and work together. If you work in teams, please list your teammates on your submission.

To submit this assignment, either enter your answers directly in the `assignments/assignment-1.md` using markdown syntax, or upload a separate file containing your solutions, for example `assignments/assignment-1-solutions.pdf`.

*Note: You will need to complete the [Github onboarding instructions](https://github.com/chrislarson1/GU-ANLY-580-FALL-2021/blob/main/github-setup.md) in order to submit this assignment.*

#
**Format**: take home, open Wikipedia, groups of $\leq$ 3

**Due dates**:
 
 - Section I: Sep 19
 - Section II: Sep 15

**Grade**: 10%

**Your name**:

#
## Problems

1. (3 pts) Establish the [convexity](https://en.wikipedia.org/wiki/Convex_function) of the following functions, showing any necessary derivation steps.

    a. $f(x) = x^{2}$

    b. $f(x) = \ln(x)$

    c. $f(x) = \frac{1}{1 + e^{-x}}$

    *Hint: convexity is non binary, some functions are neither convex nor concave, some are convex/concave over finite intervals etc..* 



2. (3 pts) Consider a continuous random variable $X$ that is drawn from a [uniform distribution](https://en.wikipedia.org/wiki/Continuous_uniform_distribution) between the values $0$ and $\theta$. Please compute the following, showing each derivation step:

    a. $\mathbb{E}_{X}[X]$

    b. $\text{var}(X)$ 

    c. $H(X)$

    *Note:* $H(X)$ *denotes the [entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory)) of* $X$. 


3. (5 pts) Given $N$ independently drawn samples of $X$ from (2), $x_{1}, ..., x_{N}$, compute the [maximum likelihood estimate](https://en.wikipedia.org/wiki/Maximum_likelihood_estimation) of $\theta$, $\hat{\theta}$. Please show the steps to arrive at this answer.


3. (5 pts) Imagine you are given the choice of three sound proof doors: Behind one door is \$1M cash; behind the others, crickets. After making your choice (but not observing the outcome), an omnicient host reveals crickets behind one of the other doors. The host then asks you the following: *Would you like to switch doors?* Using [Bayes' Rule](https://en.wikipedia.org/wiki/Bayes%27_theorem), determine whether or not you should switch doors to maximize your chances of winning $1M.


4. (4 pts) Consider the covariance matrix, $\Sigma \in \mathbb{R}^{N \times N}$ of a random vector $X \in \mathbb{R}^{N}$. Show that $\Sigma$ is a [positive semidefnite matrix](https://en.wikipedia.org/wiki/Definite_matrix). What are some of the implications of $\Sigma$ being PSD?

    *Note: The covariance of $X$ is defined as $\Sigma = \mathbb{E}_{X}\big[ \big( X - \mathbb{E}_{X}[X] \big)\big( X - \mathbb{E}_{X}[X] \big)^{T} \big]$*
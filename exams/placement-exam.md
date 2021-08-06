# ANLY-580 Placement Exam

The purpose of this exam is for self study and getting you up to speed with some of the underlying concepts used in machine learning and NLP. You may be familiar with them already, and if so great. If not, put in the effort to learn them; being familiar with these concepts will improve your ability to solve real problems. Feel free to use definitions from Wikipedia to aid in this self study, but refrain from searching for answers directly. If you get stuck, feel free to form groups of no more than three.

Github's markdown renderer does not support native Latex style math. When you pull this down you can view it locally using most IDEs (e.g., [VSCode](https://code.visualstudio.com/)). To submit this test, either enter your answers directly in this document, or upload a separate file called `placement-exam-solutions` in this folder. 

*Note: You will need to complete the [Github onboarding instructions](https://github.com/chrislarson1/GU-ANLY-580-FALL-2021/blob/main/github-setup.md) in order to submit this exam.*

#
### Format: take home, open Wikipedia, groups of $\leq$ 3

### Due dates: 
 - Section I: Sep 08
 - Section II: Sep 12

### Grade: 5%

### Name:

#
## Problems

1. (3 pts) Establish the [convexity](https://en.wikipedia.org/wiki/Convex_function) of the following functions, showing any necessary derivation steps.

    a. $f(x) = x^{2}$ 

    b. $f(x) = \ln(x)$

    c. $f(x) = \frac{1}{1 + e^{-x}}$

    *Hint: convexity is non binary, some functions are neither convex or concave, some are convex/concave over finite intervals etc..* 

<br>

2. (3 pts) Consider a continuous random variable $X$ that is drawn from a [uniform distribution](https://en.wikipedia.org/wiki/Continuous_uniform_distribution) between the values $0$ and $\theta$. Please compute the following, showing each derivation step:

    a. $\mathbb{E}_{X}[X]$

    b. $\text{var}(X)$ 

    c. $H(X)$

    *Note:* $H(X)$ *denotes the [entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory)) of* $X$. 

<br>

3. (5 pts) Given $N$ independently drawn samples of $X$ from (2), $x_{1}, ..., x_{N}$, compute the [maximum likelihood estimate](https://en.wikipedia.org/wiki/Maximum_likelihood_estimation) of $\theta$, $\hat{\theta}$. Please show the steps to arrive at this answer.

<br>

3. (5 pts) Imagine you are given the choice of three sound proof doors: Behind one door is $1M cash; behind the others, crickets. After making your choice (but not observing the outcome), an omnicient host reveals crickets behind one of the other doors. The host then proposes the following: *Would you like to switch doors?* Using [Bayes' Rule](https://en.wikipedia.org/wiki/Bayes%27_theorem), determine whether or not you should switch doors to maximize your chances of winning $1M.

<br>

4. (4 pts) Consider the covariance matrix, $\Sigma \in \mathbb{R}^{N \times N}$ of a random vector $X \in \mathbb{R}^{M \times N}$. Show that $\Sigma$ is a [positive semidefnite matrix](https://en.wikipedia.org/wiki/Definite_matrix), and then explain what this means. Keep in mind that covariance is defined here as $\Sigma = \mathbb{E}\big[ \big( X - \mathbb{E}_{X}[X] \big)\big( X - \mathbb{E}_{X}[X] \big)^{T} \big]$.
# Lab 01: Python Environment Setup


## Github setup
Navigate to the [github onboarding page](https://github.com/chrislarson1/GU-ANLY-580-FALL-2021/blob/main/github-setup.md) and complete the instructions to create your own fork of this repository. All code that you write for assignments, projects, and labs (including this one) will be submitted by pushing the code to your fork.

Once you're setup with Github, it's important that you keep your fork up-to-date with the upstream branch. This means running the following command before starting each assignment or lab:

    $ git pull upstream

## Python environment setup
Navigate to the [Python environment setup page](https://github.com/chrislarson1/GU-ANLY-580-FALL-2021/blob/main/computing-setup.md) and complete the instructions to get your Python environment setup on your local machine. Once you've successfully completed all of the steps, you can run the following command (from the root of this repository) to install the packages that we'll need to start the semester. Note that depending on what python virtual environment you're using (we strongly suggest using Conda as per the instructions), you may already have some of these installed.

    $ pip install -r requirements.txt

## Task I: `jupyterlab-starter.ipynb`
To complete this task you'll need to complete two subtasks: 1) run the first sublock in the jupyter notebook to ensure that your packages were installed successfully and that IPython is pointed at the correct Python binary, and 2) complete the function `linear_transformation()` by implementing matrix multiplication between the tensor `W` and data `X`. When you're finished completing the notebook, save the file and then push it up to github using the following commands:

    $ git add lab-01/jupyterlab-starter.ipynb
    $ git commit -m 'completed lab-01, task 1'
    $ git push origin
# Computing Environment

## Python
This course will make extensive use of the machine learning toolset within the Python ecosystem. If you already have Python3.6.5+ and Docker installed on your local machine and feel comfortable managing your own environment that's perfectly fine. If not, it is highly recommeneded that you follow this guide and get setup with Anaconda, which makes it effortless to configure Python and manage packages. If you are running on Windows, it is highly recommended that you install Virtualbox and run in either a MacOS or Linux operating system.

1. First, complete these [instructions](https://github.com/chrislarson1/GU-ANLY-580-FALL-2021/blob/main/github-setup.md).

2. Check to see if you have conda installed on your machine. If the following command returns a filepath, then you already have conda installed at that location. If not then you will need to install it (step 3).

        $ which conda

3. Go to the [Anaconda website](https://docs.anaconda.com/products/individual) and download the appropriate GUI installer for your machine. This file is ~500MB and may take a while to download. Launch the installer by clicking on it and follow the prompts. Note, you can overwrite your current Anaconda installation by simply rerunning this step.

4. If you don't already have an IDE, a few good choices are [PyCharm](https://www.jetbrains.com/pycharm/download/) and [VSCode](https://code.visualstudio.com/download). Both of these IDEs have a convenient feature that allows you to open a shell directly in the GUI, making it easy to switch between running shell commands and writing code.

6. Create a dedicated conda environment for the ANLY-580 course:

        $ conda activate
        $ conda create --name anly-580
        $ conda activate anly-580

    You should notice that your command line now looks like this, indicating that your conda environment is active:

        (anly-580) $

    If you ever need to deactivate this conda environment (perhaps you're using Python in another course), just run:

        $ conda deactivate

# Installing packages

We will only need a single environment for this course. Prior to begining assignment/lab/project work, always make sure that you've activated your conda environment. After you've done that, any packages that you install will be installed in this environment. To install packages, you can run either of the following commands. Conda is a full fledged dependency manager that will resolve any dependency conflicts that arise, while `pip` will just do what you tell it. In this class `pip` should be sufficient, but feel free to use either.

    (anly-580) $ pip install <package-name>

or 

    (anly-580) $ conda install <package-name>



<br>


## Docker

Some of the labs in this course will make use of docker, which is a piece of software that runs applications in containers on host machines. MacOS users can download Docker desktop application by navigating here [https://docs.docker.com/docker-for-mac/install/](https://docs.docker.com/docker-for-mac/install/). When running on Mac, you can start the docker daemon by simply launching the Docker Desktop application. 

For Linux users, navigate here [https://docs.docker.com/engine/install/](https://docs.docker.com/engine/install/) and follow the instructions for your specific distro. On Linux machines, the docker daemon may not start automatically on boot depending on how your system is configured. You can start it manually using this command:

	$ sudo systemctl start docker


## AWS

We are currently trying to arrange student access to virtual machines on AWS. Specific instructions and assistance will be provided when those arrangements get made to get you running on cloud instances for certain computationally intensive tasks.
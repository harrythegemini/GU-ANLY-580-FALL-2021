# Github Setup

This course will be conducted primarily through Github. Materials will be posted to Canvas, but please treat *this* repository as your single source of truth, with the syllabus (README.md) as your starting point. It will contain up-to-date links to all lectures, labs, assignments, exams, and reading material. To submit assignments, exams, and projects, each student will create a private fork of this repository and then add the instructor as a *collaborator*. Please follow the instructions below to get setup. If you are a Windows user, it is highly recommended that you install VirtualBox and interact with this course on a unix based OS; all examples involving shell commands are unix specific. Also note that these instructions are specific to those running MacOS; it is assumed that if you're running Linux you can translate these instructions to your specific distribution (contact the instructor if you need assistance).

1. Determine if you have brew installed

    	$ brew --version

    If this results in an error you will need to install it (step 2). If the above command returns a version, skip to step 3.

2. Install Homebrew (MacOS package manager):

    	$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

3. Install git via Homebrew

    	$ brew update && brew install git
    	
4. Create a Github account (if you don't already have one) <a href="https://github.com/login">here</a>

5. Email the <a href="chris.larson@georgetown.edu">instructor</a> with your Github user handle to request access to the course repository. You will recieve a confirmation email when you've been granted access.

6. Log in to Github and create a new repository called `GU-ANLY-580-FALL-2021`. Github will ask if you want to create a README, add a license etc.., leave the repo empty by not checking any of those boxes. The repository should be tagged as private by default, but make sure that it is private (you can change this in the settings tab after it has been created). Strict policy: only you, the instructor, and the TAs can have access to your fork. 

7. Clone the course repository onto your local machine, modifying the directory path as necessary:

    	$ cd ~/Documents && git clone https://github.com/chrislarson1/GU-ANLY-580-FALL-2021.git && cd GU-ANLY-580-FALL-2021

8. Next we are going to rename the remote branch `origin` to `upstream`:

		$ git remote rename upstream origin && git remote set-url --push upstream anly-580

9. Now recreate the origin remote and point it to your private github repo, replacing `<YOUR-GITHUB-HANDLE>` with your Github username:

		$ git remote add origin https://github.com/<YOUR-GITHUB-HANDLE>/GU-ANLY-580-FALL-2021.git

10. Before proceeding, check that your remote branches are correct. You should have a `origin` remote pointed at `https://github.com/<YOUR-GITHUB-HANDLE>/GU-ANLY-580-FALL-2021.git`, and an `upstream` remote pointed at `https://github.com/chrislarson1/GU-ANLY-580-FALL-2021.git`.

		$ git remote --v

11. Say outloud to yourself 100 times repeatedly, I will never, ever run `git push upstream`. This is critically important. We've disabled this, but someone knowledgeable in git could easily get around this. Don't do this please!

12. Next, push the cloned repository up to your remote:

		$ git push -u origin

13. Give the instructor access to your repository by going to your repo in the github UI and clicking `Settings -> Manage Access -> Invite a Collaborator` and adding `chrislarson1`.

# 
##  Syncing your fork

New material will be added to the main repository every week. To sync your fork (this is technically not a fork, but we are treating it as one), run the following command:

	$ git pull upstream main && git push origin

#
## Submitting your work

After you've pulled the new content and pushed it to your fork, you can begin completing your coding assignments. To submit files, push the files to your fork using the following flow:

	$ git add <file-to-be-submitted>
	$ git commit -m  "some commit message"
	$ git push origin

#
## Notes

1. The `upstream` remote is read-only, meaning that you should **never** try to push upstream, only pull.

2. Git is a code versioning system. If you have large data files (100MB+) that accompany assignment or project work submissions, please stick them in a storage bucket (e.g., Box, Google Drive) and provide a link to it's location in the code/notebook that you are submitting.
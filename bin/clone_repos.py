import argparse
import logging
import os
import shutil
from csv import reader

PARSER = argparse.ArgumentParser(description='Clones git repos')

# Required parameters
PARSER.add_argument('--baseDir', help='Where the directories will be cloned to')
PARSER.add_argument('--inputFile', help='input csv file that contains the git repos')

parameter = PARSER.parse_args()

baseDirWithSlash = parameter.baseDir

if (parameter.baseDir[len(parameter.baseDir) - 1] != "/"):
    baseDirWithSlash += "/"

directories = os.listdir(baseDirWithSlash)

inputFile = open(parameter.inputFile, newline='')
csv = reader(inputFile, delimiter=',')

# Remove directories that aren't in inputFile anymore
for dir in directories:
    for line2 in csv:
        print(line2)
        if (dir not in line2):
            print("I am here")
            print("rm -rf " + baseDirWithSlash + str(dir))
            # os.system("rm -rf " + baseDirWithSlash + str(dir))
            shutil.rmtree(baseDirWithSlash + str(dir))

# Clone and pull directories
for line in csv:
    if (len(line) == 2):
        repoName = line[1]
        repoSSH = line[0]
        repoDirectory = baseDirWithSlash + str(repoName)
        # Clone
        if (repoName not in directories):
            logging.info("Cloning repository")
            gitcommand = "git clone " + str(repoSSH) + " " + repoDirectory
            print(gitcommand)
        # Pull
        else:
            logging.info("Pulling repository")
            gitcommand = "cd " + repoDirectory + " && git pull"
        os.system(gitcommand)
    else:
        logging.warning(
            "CSV doesn't have all fields, check documentation to see how to properly format the input file.")
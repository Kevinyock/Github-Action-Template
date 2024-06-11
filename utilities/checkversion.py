
from git import Repo
import os
import glob
import argparse

class CheckVersion:

    # Comparing Two Branches
    repo = None
    main_branch = None
    development_branch = None

    main_branch_name = "origin/main"

    def __init__(self):
        print("Initialize Check Version Class")
        self.get_main_and_developing_branch()

    def get_main_and_developing_branch(self):
        self.repo = Repo(self.get_repo_directory)
        self.main_branch = self.repo.commit(self.main_branch_name)
        self.development_branch = self.repo.active_branch.name
        print(self.main_branch)
        print(self.development_branch)

    def checking_version(self):
        print("Getting a list of version_nuimber.txt")
        file_list = self.get_filelist_of_version_number_txt()
        print(file_list)
        for version_file in file_list:
            file = open(version_file)
            version_sematics = file.readline()
            versioning = version_sematics.split(".") # Major.Minor.Patch
            print(version_sematics)
        #print("Checking Version")

    def get_filelist_of_version_number_txt(self):
        return glob.glob('**/version_number.txt',recursive=True)
    
    def split_version_semantic(self):
        print("Getting Major Version")
        print("Getting Minor Version")
        print("Getting Patch Version")
        return
    
    def get_repo_directory(self):
        return os.chdir("..")

parser = argparse.ArgumentParser()
parser.add_argument('--test', help='test')
args = parser.parse_args()

if __name__ == "__main__":
    checkVersion = CheckVersion()
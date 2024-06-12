
import git
import os
import glob
import pathlib
import argparse
import logging

class CheckVersion:

    # Comparing Two Branches
    repo = None
    main_branch = None
    development_branch = None

    main_branch_name = "origin/main"
    development_branch_name = None

    logger = None

    def __init__(self):
        self.logger = logging.getLogger(__file__)
        self.logger.setLevel(logging.INFO)
        self.logger.info("Initialize Check Version Class")
        self.get_main_and_developing_branch()

    def get_main_and_developing_branch(self):
        self.repo = git.Repo(self.get_repo_directory())
        self.main_branch = self.repo.commit(self.main_branch_name)
        self.development_branch = self.repo.commit(self.repo.active_branch)

        self.logger.info(self.main_branch)
        self.logger.info(self.development_branch)

    def checking_version(self):
        self.logger.info("Getting a list of version_nuimber.txt")
        file_list = self.get_filelist_of_version_number_txt()
        self.logger.info(file_list)
        for version_file in file_list:
            file = open(version_file)
            version_sematics = file.readline()
            versioning = version_sematics.split(".") # Major.Minor.Patch
            self.logger.info(version_sematics)
        #self.logger.info("Checking Version")

    def get_filelist_of_version_number_txt(self):
        return glob.glob('**/version_number.txt',recursive=True)
    
    def split_version_semantic(self):
        self.logger.info("Getting Major Version")
        self.logger.info("Getting Minor Version")
        self.logger.info("Getting Patch Version")
        return
    
    def get_repo_directory(self) -> pathlib.Path:
        path = pathlib.Path(__file__).parent.parent
        self.logger.info(path)
        return path

parser = argparse.ArgumentParser()
parser.add_argument('--test', help='test')
args = parser.parse_args()

if __name__ == "__main__":
    checkVersion = CheckVersion()
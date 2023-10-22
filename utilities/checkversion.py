import os
import glob
import argparse
import GitPython

class CheckVersion:
    def __init__(self):
        pass

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



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', help='test')
    args = parser.parse_args()
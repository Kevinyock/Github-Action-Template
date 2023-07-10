import os
import glob

class CheckVersion:
    def __init__(self):
        pass

    def checking_version(self):
        print("Getting a list of version_nuimber.txt")
        file_list = glob.glob("**/version_number.txt",recursive=True)
        print(file_list)
        for version_file in file_list:
            file = open(version_file)
            version_sematics = file.readline()
            versioning = version_sematics.split(".") # Major.Minor.Patch
            print(version_sematics)
        #print("Checking Version")



    
CV = CheckVersion()
CV.checking_version()
###############################################################################
# PyMerge                                                                     #
# Author: Dyon                                                                #
# Description: Script that merges text files into one single file.            #
###############################################################################

import os
import fnmatch

#########################
# CONFIGURATION SECTION #
#########################

config = {
        'sameDirForMergedFiles': True,  # Set this to True to save all merged files to the same directory
        'mergedFilesPath': 'merged_files',  # The path where merged files are going to be saved if 'saveDirForMergedFiles' is set to True
        'pattern': '*.sql',  # Pattern to follow when searching for files
        'paths': [
            # Copy and paste a section to merge files from more directories
            # Path 1
            {
                'source': 'source1',
                'destination': 'destination1',
                'filename': 'filename1.sql'
            },
            # Path 2
            {
                'source': 'source2',
                'destination': 'destination2',
                'filename': 'filename2.sql'
            }
        ]
    }

##########################################
# DONT TOUCH ANYTHING BEYOND THIS LINE!! #
##########################################


class PyMerge:

    sameDirForMergedFiles = False
    mergedFilesPath = ''
    pattern = '*'

    def __init__(self):
        self.sameDirForMergedFiles = config['sameDirForMergedFiles']
        self.mergedFilesPath = config['mergedFilesPath']
        self.pattern = config['pattern']

    def get_files(self, directory, pattern):
        files = []

        for root, dirnames, filenames in os.walk(directory):
            for filename in fnmatch.filter(filenames, pattern):
                files.append(os.path.join(root, filename))

        return files

    def merge_files(self):
        for path in config['paths']:
            source = path['source']
            destination = self.mergedFilesPath if self.sameDirForMergedFiles else path['destination']
            filename = path['filename']
            files = self.get_files(source, self.pattern)

            if len(files) == 0:
                print 'There are no files to merge.'

                return

            if not os.path.exists(destination):
                os.makedirs(destination)

            result = open(os.path.join(destination, filename), 'w+')

            for file in files:
                for line in open(file):
                    result.write(line)

            print 'Merged file saved to "' + result.name + '".'

            result.close()


pm = PyMerge()

pm.merge_files()

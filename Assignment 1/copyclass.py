"""CS 234 Assignment 1 Question 4 - a simple web client
"""
import os
import platform

class PlatformError(Exception):
        def __init__(self, message):
                self.param = message
        def __str__(self):
                return(self.param)

class PathError(Exception):
        def __init__(self, message):
                self.param = message
        def __str__(self):
                return(self.param)

def copy(srcFile, destFile):
        """
        Precondition: Source file is a text file, user is running on linux, they have input an absolute path name.
        Postcondition: A replica of the specified input file will be generated at the specified output path.
        """

        assumptionCheck(srcFile, destFile)
        src = open(srcFile)
        srcLines = src.readlines()
        src.close()
        dst = open(destFile, 'w')

        for line in srcLines:
                dst.write(line)
        dst.close()

def assumptionCheck(srcFile, destFile):
        if (type(srcFile) != type("s")):
                raise TypeError, "Source file path must be a string"
        elif (type(destFile) != type("s")):
                raise TypeError, "Destination file path must be a string"
        elif (platform.system() != 'Linux'):
                raise PlatformError, "Must be running on Linux"
        elif (os.path.isabs(srcFile) == False):
                raise PathError, "Source file path must be absolute"
        elif (os.path.isabs(destFile) == False):
                raise PathError, "Destination file path must be absolute"

"""
	Assumptions: 
	- Source File is a text file
	- User is running on Linux
	- Input and output file path are absolute
	- Input file must exist (this is already built in when you run open(...) )

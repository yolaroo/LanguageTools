__author__ = 'piXIII'

from DataMap import *



def buildAction ():

    bookArray = ["Torah","Prophets","Writings"]
    THE_LANGUAGE = "English"
    FILE_NAME = "merged"
    ROOT_DIR = "Tanach"
    LANGUAGE_DESIGNATOR = "title"

    filesFromDirectoryBuilder(bookArray,THE_LANGUAGE,ROOT_DIR,FILE_NAME,LANGUAGE_DESIGNATOR)

    THE_LANGUAGE = "Hebrew"
    LANGUAGE_DESIGNATOR = "heTitle"

    filesFromDirectoryBuilder(bookArray,THE_LANGUAGE,ROOT_DIR,FILE_NAME,LANGUAGE_DESIGNATOR)

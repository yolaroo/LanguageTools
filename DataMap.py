__author__ = 'piXIII'

import os
import codecs
from ClassBuilder import *
import json

def filesFromDirectoryBuilder(theBookArray,theLanguage,theRootDirectory,theFileName,theLanguageJSONDictionaryTitleProperty) :
    book_count = 0
    myWrapper = wrapperClass()
    myDocument = documentClass()
    myWrapper.document = myDocument
    for the_book in theBookArray:
        rootdir = theRootDirectory+'/'+ the_book
        for subdir, dirs, files in os.walk(rootdir):
            for file in files:
                if theLanguage in subdir:
                     if theFileName in file:
                        book_count += 1
                        my_path = subdir+"/"+file
                        with codecs.open(my_path, 'r', encoding='utf-8-sig') as json_file:
                            json_data = json.load(json_file)
                            text_title = json_data[theLanguageJSONDictionaryTitleProperty]
                            chapter_data = json_data["text"]
                            chapter_count = len(chapter_data)
                            myBook = bookClass(text_title,the_book)
                            myDocument.add_book(myBook)
                            for x in range(0,chapter_count):
                                single_chapter = chapter_data[x]
                                chapter_number_string = str(x+1)
                                myChapter = chapterClass(chapter_number_string)
                                myChapter.chapterlineText = single_chapter
                                myBook.add_chapter(myChapter)

    my_file = myWrapper.to_JSON()
    NEW_FILE_NAME = theRootDirectory+theLanguage+".json"
    with open(NEW_FILE_NAME, 'w', encoding='utf-8-sig') as f:
        f.write(my_file)
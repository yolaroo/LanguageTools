__author__ = 'piXIII'
import json

class chapterClass:
    def __init__(self,chapterNumber):
        self=self
        self.chapterNumber=chapterNumber
        self.chapterlineText = []
    def add_chapterlineText(self, chapterlineText):
        self.chapterlineText.append(chapterlineText)

class bookClass:
    def __init__(self,title,bookGroup):
        self=self
        self.title = title
        self.bookGroup = bookGroup
        self.chapter = []
    def add_chapter(self, chapter):
        self.chapter.append(chapter)

class documentClass:
    def __init__(self):
        self=self
        self.book = []
    def add_book(self, book):
        self.book.append(book)

class wrapperClass:
    def __init__(self):
        self=self
        self.document = documentClass()
    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


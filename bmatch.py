import os

import sys

df iterFiles(path):
    if(os.path.isfile(path)):
        yield path
    elif (os.path.isdir(path)):
        for dirpath, _, filenames in os.walk(path):
            for filename in filenames:
                yield os.path.join(dirpath, filename)


class Match:
    def getFiletype(self, filename):
        raise NotImplementedError

    def getHeadFiles(self, fileContent):
        raise NotImplementedError

    def removeComments(self, fileContent):
        raise NotImplementedError

    def initHeadQueue(self, headPath):
        raise NotImplementedError

    def intHeadQueueFromFile(self, headFile):
        raise NotImplementedError

    def getHeadFile(self):
        raise NotImplementedError

    def putHeadFile(self, headFile):
        raise NotImplementedError

    def putPath(self, key, value):
        raise NotImplementedError

    def getIncludeFiles(self, key):
        raise NotImplementedError

    def getIncludePath(self, file):
        raise NotImplementedError



    def recordPath(self, file_):
        raise NotImplementedError

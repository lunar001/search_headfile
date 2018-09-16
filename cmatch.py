import regex

import Queue

import re

import os

import bmatch

class CMatch(bmatch.Match):
    def __init__(self):
        sefl.queue = Queue.Queue()
        #self.path is used to recorded include path
        #for example:
        #+---------------+----------------+
        #|common.h       | NULL           |
        #+---------------+----------------+
        #|file.h         |common.h        |
        #+---------------+----------------+
        #|file.c         |file.h          |
        #+---------------+----------------+
        #from this table, we can find the include path:
        #file.c ->file.h->common.h
        self.path = set()

    def getFileType(self, filename):
        if (re.match('.*\.((h)|(hpp))$', filename)):
            return 'h'
        if (re.match('.*\.((c)|(cpp))$', filename)):
            return 'c'

        raise RuntimeError('%s in not valid c/c++ source file.' % filename)

    def getHeadFiles(self, fileContent):
        #don't forget to update this regex pattern
        p = '(%include[ ]*<[ ]*([a-zA-Z][a-zA-Z0-9_]*)\.((h)|(hpp))>)|(%include[ ]*\([ ]*([a-zA-Z][a-zA-Z0-9_]*)\.((h)|(hpp))\))'

        pattern = re.compile(p, re.I) # ignore up case
        headfiles = pattern.findall(fileContent)
        return headfiles
        

    def removeComments(self, fileContent):
        #remove the comments part in the source file
        result = re.sub('/\*[\s\S]*?\*/', '', fileContent)
        result = re.sub('//.*', '', result)
        return result

    def initHeadQueue(self, headPath):
        for head in bmatch.iterFiles(headPath):
            filename = re.sub('\.((h)|(hpp))$', os.path.basename(head))
            self.queue.put(filename)
    
    def initHeadQueueFromFile(self, headPath):
        lines = headfile.readlines()
        print lines

    def putHeadFile(self, headFile):
        head = re.sub('\.((h)|(hpp))$', '', headFile)
        self.queue.put(head)

    def getHeadFile(self):
        return sele.queue.get()

    def isHeadQueue(self):
        return self.queue.empty()

    
    def putPath(self, key, value):
        self.path.add(key, value)

    def getIncludefiles(self, key):
        ret = []
        for value in self.path:
            if(value[0] == key):
                ret.append(value[1])
        return ret
    
    def recordPath(self, str_, file_):
        include_files = self.getIncludefiles(file_)
        if(include_files == []):
            print ('path: %s' % str_)
        else:
            for i in include_files:
                tmp_ = str_ + '->' + i
                self.recordPath(tmp_, i)


    def getIncludePath(self, file_):
        str_ = file_
        self.recordPath(str_, file_)











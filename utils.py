from __future__ import print_function

import os
import re
import sys
import Queue

from multiprocessing import Pool as ProcessPool
from functools import partial

import cmatch

def iterFiles(path):
    if(os.path.isfile(path)):
        yield path
    elif (os.path.isdir(path)):
        for dirpaht, _, filenames in os.walk(path):
            for filename in filenames:
                yield os.path.join(dirpath, filename)

def get_src_file(check_head_file, match, src_file):
    '''if src_file including check_head_file, return src_file
        else return None'''
    try:
        ftype = match.getFiletype(src_file)
        if(ftype == 'c' or ftype == 'h'):
            fp = open(src_file)
            fileContent = fp.read()
            fileContent = match.removeComments(fileContent)
            headfiles = match.getHeadFiles(fileContent)
            headfiles = [headfile.lower() for headfile in headfiles]
            fp.close()
            if(check_head_file in headfiles):
                return os.path.basename(src_file)
            else:
                return None
        else:

            return None
    except RuntimeError:
        return None

def 
def search_head_files(head_path, src_path):
    match = cmatch.CMatch()
    match.initHeadQueue(head_path)
    src_files = [ src_file for src_file in iterFiles(src_path) ]
    buildlist = []
    num_workers = 4 
    workers = ProcessPool(num_workers);
    while (match.isHeadQueue() == False):
        check_head_file = match.getHeadFile()
        print ('check for head ', check_head_file)
        _get_src_file = partial(get_src_file, check_head_file, match)
        for src_file in src_files:
            ret = _get_src_file(src_file)
            if(ret):
                try:
                    if(match.getFileType(ret) == 'h'):
                        match.putHeadFile(ret)
                        # record path
                    else:
                        buildlist.append(ret)
                        match.putPath(ret, check_head_file+'.copy')
                except RuntimeError:
                    pass


 # print (src_files)
       # for src_file in workers.imap_unordered(_get_src_file, src_files):
       #     pass;
            #if (src_file):
            #    try:
            #        if(getFileType(src_file) == 'h'):
            #           match.putHeadFile(src_file) 
            #        else:
            #            buildlist.append(src_file)
            #    except RuntimeError:
            #        print('invalid file %s' % src_file)
            #        buildlist.append(src_file)
    workers.close()                                                                                                             
    workers.join()                                                                                                              
    print (len(set(buildlist)))                                                                                                 
                                                                                                                                
    for bl in buildlist:                                                                                                        
        match.getIncludePath(bl)                                                                                                
    for bl in set(buildlist):                                                                                                   
        print(bl)      




f __name__ == '__main__':
    #search_head_files(sys.argv[1], sys.argv[2])
    search_head_files('dirpath1', 'dirpaht2')
   # search_head_files('./h', './src/') 

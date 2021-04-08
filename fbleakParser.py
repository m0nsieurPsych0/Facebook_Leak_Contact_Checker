#!/usr/bin/env python
__author__ = 'M0nsieurPsych0'

from re import compile, search
import json

class FbleakParser():
    def __init__(self, leakdb, dictdb):
        self._dictdb = dictdb
        self._filePath = leakdb
        self._rgxPhoneNumber = compile(r'^[1][\d]{10}')
        self._dictData = {}

    def _createDict(self):
        with open(self._filePath, 'r', encoding='UTF8') as f:
            for line in f:
                phoneNumber = search(self._rgxPhoneNumber, line)
                if phoneNumber != None:
                    self._dictData[phoneNumber.group(0)] = line
        self._dictToFile()
    
    def _dictToFile(self):
        # To keep dict as is we dump the data as json
        with open(self._dictdb, 'w', encoding='UTF8') as f:
            f.write(json.dumps(self._dictData))

    def _fileToDict(self):
        # Reading the file as json and outputing in a dict variable
        with open(self._dictdb, 'r', encoding='UTF8') as f:
            return json.loads(f.read())

    def process(self):
        try:
            return self._fileToDict()
        except FileNotFoundError:
            print("'dictdb.txt' not found... Creating!")
            self._createDict()
            return self._fileToDict()


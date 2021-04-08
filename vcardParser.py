#!/usr/bin/env python

__author__ = 'M0nsieurPsych0'

from vobject import readOne
from re import match, split, compile, MULTILINE

class VcardParser():
    def __init__(self, vcard):
        self._vCard = vcard
        self._rgxVcard = compile(r'(BEGIN:VCARD[\s\S]+?END:VCARD)', MULTILINE)
        self._rgxPhoneStart = compile(r'^[1]')
        self._vObjList = []
        self.phoneList = []

        self._importVcard()
        self._createPhoneList()
          

    def _importVcard(self):
        content = None

        with open(self._vCard, 'r', encoding='UTF8') as vc:
            content = vc.read()

        # regex split
        vregx = split(self._rgxVcard, content)
        
        # Remove empty items and Remove '\n'
        for i in vregx:
            if i == '' or i == '\n':
                vregx.pop(vregx.index(i))
                
        # Create a list of Vobject
        for i in vregx:
            self._vObjList.append(readOne(i))
        
    def _createPhoneList(self):
        # Take each Vobject and extract the phone number
        for obj in self._vObjList:
            if obj.contents.get('tel') != None:
                tel = obj.contents['tel']
                for val in tel:
                    # Remove the '+' et '-'
                    tmp = val.value.strip('+').replace('-', '')
                    # Check if the first digit is a '1'
                    if not match(self._rgxPhoneStart, tmp):
                        tmp = '1' + tmp
                    if len(tmp) == 11:    
                        self.phoneList.append(tmp)



#!/usr/bin/env python

__author__ = 'M0nsieurPsych0'

from argparse import ArgumentParser
from sys import exit

from vcardParser import VcardParser
from fbleakParser import FbleakParser


def argParse():
    p = ArgumentParser()
    p.add_argument('-i', '--vcard',  action="store", type=str, dest='vcard',   required=True,         help="Vcard file (Ex: 'contact.vcf')")
    p.add_argument('-l', '--fbleak', action="store", type=str, dest='fbleak',  required=True,         help="Facebook leaked data (Ex: 'country.txt')")
    p.add_argument('-d', '--dictdb', action="store", type=str, dest='dictdb',  default='dictdb.txt',  help="generated dictionnary data (default: 'dictdb.txt')")
    p.add_argument('-o', '--output', action="store", type=str, dest='outpath', default='victims.txt', help="output file with matched contacts (default: 'victims.txt')")    
    
    return p

def findMatch(vcard, fbleak, dictdb, outpath):
    matching = list()
    print(" Parsing Vcard...")
    phoneList = VcardParser(vcard).phoneList
    print("Done!\n", "Parsing FB data...")
    bigDict = FbleakParser(fbleak, dictdb).process()
    print("Done!\n", "Checking if contacts have been leaked...")
    for number in phoneList:
        if number in bigDict:
            matching.append(bigDict[number])
    print("{} have been compromised! :(\n".format(len(matching)), " Creating '{}'...".format(outpath))
    with open(outpath, 'a', encoding='UTF8') as w:
        for m in matching:
            w.write(m)
    print("Done!")

def main():
    args = argParse().parse_args()
    findMatch(args.vcard, args.fbleak, args.dictdb, args.outpath)


if __name__ == "__main__":
    exit(main())
    

    
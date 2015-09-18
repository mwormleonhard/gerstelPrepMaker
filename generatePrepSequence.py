# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 22:18:53 2015
@author: Martin Worm-Leonhard

----------------------------------------------------------------------------
"THE BEER-WARE LICENSE" (Revision 42):
<mwormleonhard@gmail.com> wrote this file. As long as you retain this notice you
can do whatever you want with this stuff. If we meet some day, and you think
this stuff is worth it, you can buy me a beer in return.   Martin Worm-Leonhard
----------------------------------------------------------------------------
"""
import PrepControlStrings
import csv, re


def getVolumeLists(infilename='volumelist.csv'):
    """Reads a csv file with headers 'Vial' and 'Volume' and returns a list of
    tuples (Vial, Volume). Volume is in uL"""

    vialvolumelist = []
    with open(infilename, 'rb') as f:
        reader = csv.DictReader(f)
        for row in reader:
            vialvolumelist.append((row['Vial'], row['Volume']))
    return vialvolumelist


def writePrepSequence(vialvolumelist, outfilename='output.prp', startvial=1, endvial=10):
    linesInSeq = 3*len(vialvolumelist)

    with open(outfilename, 'wb') as f:
        f.write(PrepControlStrings.preamble.format(numLines=linesInSeq))
        for vial, volume in vialvolumelist:
            if float(volume) <= 10:
                f.write(PrepControlStrings.methodblock10ulSyringe.format(volume=volume))
            elif float(volume) < 100:
                f.write(PrepControlStrings.methodblock100ulSyringe.format(volume=volume))
            else:
                raise Exception('Volume error')
        f.write(PrepControlStrings.prepstepHeader)
        linecount = 1        
        for vial, volume in vialvolumelist:
            if float(volume) <= 10:
                f.write(PrepControlStrings.prepstep.format(line1=linecount, line2=linecount+1, line3=linecount+2, destvialstart=startvial, destvialend=endvial, sourcevial=vial, volume=volume, head="LEFT"))
                linecount += 3
            elif float(volume) < 100:
                f.write(PrepControlStrings.prepstep.format(line1=linecount, line2=linecount+1, line3=linecount+2, destvialstart=startvial, destvialend=endvial, sourcevial=vial, volume=volume, head="RIGHT"))
                linecount += 3
            else:
                raise Exception('Volume error')
        f.write(PrepControlStrings.endmatter)

if __name__ == '__main__':
    writePrepSequence(vialvolumelist=getVolumeLists())
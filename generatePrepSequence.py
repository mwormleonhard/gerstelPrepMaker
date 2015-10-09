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
import csv
import datetime
from more_itertools import unique_everseen  # Pip install more_itertools
import tkFileDialog
import tkSimpleDialog
import tkMessageBox


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

    linesInSeq = 4*len(vialvolumelist)+2
    uniqueVolumes = list(unique_everseen([vol for (vial, vol) in vialvolumelist]))

    with open(outfilename, 'wb') as f:
        f.write(PrepControlStrings.preamble.format(numLines=linesInSeq,
                                                   datetime=datetime.datetime.now().isoformat()))
        for volume in uniqueVolumes:
            if 0 < float(volume) <= 10:
                f.write(PrepControlStrings.methodblock10ulSyringe.format(volume=volume))
            elif float(volume) < 100:
                f.write(PrepControlStrings.methodblock100ulSyringe.format(volume=volume))
            else:
                raise Exception('Volume error')

        f.write(PrepControlStrings.wash100ul)
        f.write(PrepControlStrings.wash10ul)
        f.write(PrepControlStrings.prepstepHeader)

        linecount = 3
        f.write(PrepControlStrings.washstep.format(line4=1,
                                                   head="RIGHT",
                                                   vol=10))
        f.write(PrepControlStrings.washstep.format(line4=2,
                                                   head="LEFT",
                                                   vol=100))
        for vial, volume in vialvolumelist:
            if 0 < float(volume) <= 10:
                f.write(PrepControlStrings.prepstep.format(line1=linecount,
                                                           line2=linecount+1,
                                                           line3=linecount+2,
                                                           destvialstart=startvial,
                                                           destvialend=endvial,
                                                           sourcevial=vial,
                                                           volume=volume,
                                                           head="RIGHT"))
                
                f.write(PrepControlStrings.washstep.format(line4=linecount+3,
                                                           head="RIGHT",
                                                           vol=10))
                linecount += 4
            elif float(volume) < 100:
                f.write(PrepControlStrings.prepstep.format(line1=linecount,
                                                           line2=linecount+1,
                                                           line3=linecount+2,
                                                           destvialstart=startvial,
                                                           destvialend=endvial,
                                                           sourcevial=vial,
                                                           volume=volume,
                                                           head="LEFT"))
                
                f.write(PrepControlStrings.washstep.format(line4=linecount+3,
                                                           head="LEFT",
                                                           vol=100))
                linecount += 4
            else:
                raise Exception('Volume error')
        f.write(PrepControlStrings.endmatter)

if __name__ == '__main__':
    infile = tkFileDialog.askopenfilename(defaultextension='.csv',
                                          filetypes=[('CSV file', '.csv')],
                                          title='CSV file containing vials and volumes')

    outfile = tkFileDialog.asksaveasfilename(defaultextension='.prp',
                                             filetypes=[('PREP sequence', '.prp')],
                                             title='Output file for prep sequence')

    destvialstart = tkSimpleDialog.askinteger(title='First destination vial',
                                              prompt='Enter first vial number for destination',
                                              initialvalue=1,
                                              minvalue=1,
                                              maxvalue=90)

    destvialend = tkSimpleDialog.askinteger(title='Last destination vial',
                                            prompt='Enter last vial number for destination',
                                            initialvalue=10,
                                            minvalue=1,
                                            maxvalue=90)

    writePrepSequence(vialvolumelist=getVolumeLists(infilename=infile),
                      outfilename=outfile,
                      startvial=destvialstart,
                      endvial=destvialend)

    statusmessage = 'File ' + infile + ' read and processed\n\n File ' + outfile + \
    ' created\n\nInstall 100uLALX syringe in left head before loading .prp file\n\n\
    Install 10uLALX syringe in right head before loading .prp file \n\n Have a nice day! :-)'

    tkMessageBox.showinfo(title='All done!',
                          message=statusmessage)

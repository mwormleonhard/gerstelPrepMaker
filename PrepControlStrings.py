# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 22:11:12 2015

@author: Martin Worm-Leonhard

----------------------------------------------------------------------------
"THE BEER-WARE LICENSE" (Revision 42):
<mwormleonhard@gmail.com> wrote this file. As long as you retain this notice you
can do whatever you want with this stuff. If we meet some day, and you think
this stuff is worth it, you can buy me a beer in return.   Martin Worm-Leonhard
----------------------------------------------------------------------------
"""

preamble = r"""[Comment]
Short=
Full=

[INFO]
VERSION=2.2
VALUESEPARATOR=:
LINES={numLines}
METHODPATH=C:\ProgramData\Gerstel\Maestro\1\Methods\
PREPPATH=
Syr=100ulALX
LeftSyr=100ulALX
RightSyr=10ulALX
MaestroVersion=1.4.29.15

[CSPREP]
FORMAT=Vial|InjPerVial|Method|Samplename|SampleInfo|Filename|Source|Type|Level|UpdRF|UpdRT|Amount|Multiplier|Barcode|MHMethod|MHDatafile
LINES=0
"""

methodblock100ulSyringe = """
[flyt{volume}ul]
Description={volume} uL Transfer by 100uL syringe
Type=ADD
Syr=100ulALX
Fill Volume=100.0
Fill Strokes=0
Fill Speed=100.00
Accurate Add Waste=10.0
Inj. Volume={volume}
Inj. Speed=100.00
Visc./Pullup Delay=0
Eject Speed=100.00
Air Volume below=0.0
Vial Penetration=32.00
Dest. Vial Penetration=32.00
Preclean Solv.1=0
Postclean Solv.1=0
Preclean Solv.2=0
Postclean Solv.2=0
Preclean Sample=0
Fill Speed Solv.1=100.00
Viscosity Delay Solv.1=0
Eject Speed Solv.1=100.00
Fill Speed Solv.2=100.00
Viscosity Delay Solv.2=0
Eject Speed Solv.2=100.00
Post Inj. Delay=0
Pressurize Penetration=0.00
Pressurize Speed=100.00
AccurateAdd=1
Wash Station 1=Wash1
Wash Station 2=Wash2
Dilute Volume=
Dilutor Fill Speed=
Dilutor Viscosity Delay=0
Dilutor Eject Speed=
Pressurize=0
Syringe Video Check Min Level=97
Syringe Video Check Retry Count=3
Use Syringe Video Check=0
Syringe Video Check Action=0
Syringe Video Check Dispose To=0
"""
methodblock10ulSyringe = """
[flyt{volume}ul]
Description={volume} uL Transfer by 10uL syringe
Type=ADD
Syr=10ulALX
Fill Volume=10.0
Fill Strokes=0
Fill Speed=50.00
Accurate Add Waste=1.0
Inj. Volume={volume}
Inj. Speed=50.00
Visc./Pullup Delay=0
Eject Speed=50.00
Air Volume below=0.0
Vial Penetration=32.00
Dest. Vial Penetration=32.00
Preclean Solv.1=0
Postclean Solv.1=0
Preclean Solv.2=0
Postclean Solv.2=0
Preclean Sample=0
Fill Speed Solv.1=50.00
Viscosity Delay Solv.1=0
Eject Speed Solv.1=50.00
Fill Speed Solv.2=50.00
Viscosity Delay Solv.2=0
Eject Speed Solv.2=50.00
Post Inj. Delay=0
Pressurize Penetration=0.00
Pressurize Speed=50.00
AccurateAdd=1
Wash Station 1=Wash1
Wash Station 2=Wash2
Dilute Volume=
Dilutor Fill Speed=
Dilutor Viscosity Delay=0
Dilutor Eject Speed=
Pressurize=0
Syringe Video Check Min Level=97
Syringe Video Check Retry Count=3
Use Syringe Video Check=0
Syringe Video Check Action=0
Syringe Video Check Dispose To=0
"""

prepstepHeader = "\n[PREPSTEPS]"

prepstep = """
{line1}=ACTION:PREP|VIALRANGE:{destvialstart}-{destvialend}|METHOD:NoPrepAhead|
{line2}=ACTION:ADD|SAMPLER:{head}|METHOD:flyt{volume}ul|SOURCE:Tray1,VT98|DEST:Tray2,VT98|SOURCEVIAL:{sourcevial}|DESTVIAL:0|
{line3}=ACTION:END|"""

endmatter = """

[PrepPreview]

[Active Methods]
"""

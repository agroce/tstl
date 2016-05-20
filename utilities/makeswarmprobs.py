import sut
import sys

fout = open(sys.argv[1],'w')
P = sys.argv[2]

sut = sut.sut()

for ac in sut.actionClasses():
    fout.write(ac + " %%%% " + P + "\n")

fout.close()

import sut
import sys

# Appending current working directory to sys.path
# So that user can run randomtester from the directory where sut.py is located
current_working_dir = os.getcwd()
sys.path.append(current_working_dir)

fout = open(sys.argv[1],'w')
P = sys.argv[2]

sut = sut.sut()

for ac in sut.actionClasses():
    fout.write(ac + " %%%% " + P + "\n")

fout.close()

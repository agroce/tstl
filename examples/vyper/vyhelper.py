from __future__ import print_function
import subprocess

def run(c, loud=False):
    if loud:
        print("RUNNING:")
        print(c)
    with open("vfile.vy", 'w') as vf:
        vf.write(c)
    with open("vrun.out", 'w') as vout:
        subprocess.call(["vyper", "vfile.vy"], stdout=vout, stderr=vout)
    with open("vrun.out", 'r') as vout:
        for line in vout:
            if loud:
                print(line)
            assert("Fatal" not in line)
            assert("CompilerPanic" not in line)

def indent4(code):
    c = code.split("\n")
    newc = ""
    for line in c:
        newc += "    " + line + "\n"
    return newc

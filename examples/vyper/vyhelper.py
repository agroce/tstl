from __future__ import print_function
import subprocess

seen={}

def run(c, loud=False):
    if c in seen:
        return seen[c]
    if loud:
        print("RUNNING:")
        print(c)
    with open("vfile.vy", 'w') as vf:
        vf.write(c)
    with open("vrun.out", 'w') as vout:
        subprocess.call(["vyper", "vfile.vy"], stdout=vout, stderr=vout)
    with open("vrun.out", 'r') as vout:
        r = vout.read()
        if ("Fatal" in r) or ("CompilerPanic" in r):
            # ignore known bug
            if "Number of times repeated must be a constant nonzero positive integer" not in r:
                print(c)
                print(r)
                seen[c] = False
                return False
            else:
                print("IGNORING KNOWN LOOP RANGE BUG")
        elif "Error" not in r:
            print(c)
            print(r)
        if loud:
            print(r)
    seen[c] = True
    return True

def indent4(code):
    c = code.split("\n")
    newc = ""
    for line in c:
        newc += "    " + line + "\n"
    return newc

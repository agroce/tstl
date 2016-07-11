import subprocess

n = 0
while True:
    n += 1
    nstr = str(n)
    subprocess.call(["ulimit -t 120; python ~/tstl/generators/randomtester.py --nocover --timeout 120 --full --output bug" + nstr], shell=True)

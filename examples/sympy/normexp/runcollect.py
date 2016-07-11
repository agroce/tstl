import subprocess

while True:
    subprocess.call(["ulimit -t7200; python collect1.py"],shell=True)

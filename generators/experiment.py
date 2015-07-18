import subprocess
import sys

print "USAGE: python experiment.py <prefix> <# runs> <config file> [options...]"
print
print "  will generate files of form <prefix>.<configname>.<number>.out"
print "  where number is 0-<#runs>-1"
print "  config file has format <name> <python script> <params> on each line"
print "  and options are common options for each run (e.g., timeout, coverage reporting"

prefix = sys.argv[1]
repeats = int(sys.argv[2])
configs = sys.argv[3]
options = sys.argv[4:]

runs = {}

for l in open(configs):
    ls = l.split()
    runs[ls[0]] = (ls[1], ls[2:])

for i in xrange(0,repeats):
    for name in runs:
        out = prefix + "." + name + "." + str(i) + ".out"
        outf = open(out,'w')
        print "GENERATING",out
        (command, params) = runs[name]
        cmd = "python "
        cmd += command
        for p in params:
            cmd += " " + p
        for p in options:
            cmd += " " + p
        subprocess.call([cmd],shell=True,stdout = outf,stderr = outf)
        outf.close()
        

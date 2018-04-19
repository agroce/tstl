import csv
import scipy
import scipy.stats

classic = []
reduce10 = []
combo = []

with open("allbugs.csv") as amindataf:
    reader = csv.reader(amindataf)
    for row in reader:
        if 'classic' in row:
            continue
        [test, classicT, reduce10T, _, comboT] = row
        classic.append(int(classicT))
        reduce10.append(int(reduce10T))
        combo.append(int(comboT))

print scipy.mean(reduce10)
print scipy.mean(combo)

print scipy.stats.wilcoxon(reduce10,combo)

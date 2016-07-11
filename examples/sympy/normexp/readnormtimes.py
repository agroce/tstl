n = 0

for l in open("normalizers.times"):
    f = l.split("bug")[1][:-1]
    f = "bug" + f
    for l in open(f):
        print n,l,
    n += 1


    
        

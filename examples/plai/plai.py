import subprocess
import time
import os
import signal

testCount = 0
testCache = {}

def func(fd):
    s = fd.split(" ")
    return s[0] + " " + s[1]

def is_recursive(fds):
    f_pos = 0
    found = fds.find("fdC ", f_pos)
    while(found != -1):
        fcall = "appC '" + fds[found + 5: found + 6]
        fcall_pos = fds.find(fcall, found)
        fdC_pos = fds.find("fdC ", found + 1)
        if (fcall_pos != -1) and ((fcall_pos < fdC_pos) or (fdC_pos == -1)):
            return True
        f_pos = found + 1
        found = fds.find("fdC ", f_pos)
    return False

def get_names(fds):
    f_names = []
    id_names = []
    f_pos = 0
    found = fds.find("fdC ", f_pos)
    while(found != -1):
        f_names.append(fds[found + 5: found + 6])
        id_names.append(fds[found + 8: found + 9])
        f_pos = found + 1
        found = fds.find("fdC ", f_pos)
    return (f_names, id_names)

def obviously_dumb(expr, fds):
    if "appC" not in expr:
        return True
    if "idC" in expr:
        return True
    if "fdC" not in fds:
        return True
    if is_recursive(fds):
        return True
    (f_names, id_names) = get_names(fds)
    #print("f_names:", f_names)
    #print("id_names:", id_names)
    e_pos = 0
    found = expr.find("idC ", e_pos)
    while (found != -1):
        id = expr[found + 5:found + 6]
        if id not in id_names:
            #print(id, "NOT IN ID_NAMES")
            return True
        e_pos = found + 1
        found = expr.find("idC ", e_pos)
    e_pos = 0
    found = expr.find("appC ", e_pos)
    while (found != -1):
        f = expr[found + 6:found + 7]
        if f not in f_names:
            #print(f, "NOT IN F_NAMES")
            return True
        e_pos = found + 1
        found = expr.find("appC ", e_pos)
    return False
    
def test(expr, fds):
    global testCount, testCache
    if ((expr, fds)) in testCache:
       return True
    if obviously_dumb(expr, fds):
       #print("DUMB:\n  EXPR:", expr,"\n  FDS:", fds)
       return True
    print("="*80)   
    print("TEST#", testCount)
    print("  " + expr)
    print("  " + fds)

    with open("test.rkt", 'w') as outf:
        for line in open("top.rkt", "r"):
            outf.write(line)
        outf.write("(define expr " + expr + ")\n")
        outf.write("(define fds (list " + fds + "))\n")
        outf.write("(define i_result (try (interp expr mt-env fds) (lambda () -987654321)))\n(define s_result (try (sub_interp expr fds) (lambda () -987654321)))\n(test i_result s_result)\n")
    testCount += 1
    with open("test.out", 'w') as outf:
        P = subprocess.Popen(
            "/Applications/Racket\ v7.7/bin/raco test test.rkt",
            shell=True, stdout=outf, stderr=outf, preexec_fn=os.setsid)
    start = time.time()
    while (P.poll() is None) and ((time.time() - start) < 7): # 7 second timeout
        time.sleep(1)
    if P.poll() is None:
        print("TEST TIMED OUT, TERMINATING")
        os.killpg(os.getpgid(P.pid), signal.SIGTERM)
        return True
            
    test_failed = False
    with open("test.out", 'r') as outf:
        for line in outf:
            print(line)
            if "bad " in line:
                test_failed = True

    if (not test_failed):
        testCache[(expr, fds)] = True

    return (not test_failed)

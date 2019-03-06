import math
import multiprocessing
import random
import sys
import time

def is_sorted(data):
    for i in range(0, len(data)-1):
        if data[i][0] > data[i+1][0]:
            return False
    return True

def trySort(data, lock):
    for i in range(0, len(data)-1):
        if data[i][0] > data[i+1][0]:
            lock.acquire()
            #print "Swapping", i, data[i], "with", i+1, data[i+1]
            temp = data[i]
            data[i] = data[i+1]
            data[i+1] = temp
            lock.release()

def swap_sort_parallel(data):
    # Creates a pool of worker processes, one per CPU core.
    manager = multiprocessing.Manager()
    d = manager.list(data)
    lock = multiprocessing.Lock()
    processes = multiprocessing.cpu_count()
    while not is_sorted(d):
        ps = []
        for i in range(0, processes):
            p = multiprocessing.Process(target=trySort, args=(d, lock))
            p.start()
            ps.append(p)
        for p in ps:
            p.join()
    return d

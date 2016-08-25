import argparse
import math
import random
import sut as SUT
import sys
import time
from collections import namedtuple

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('-c', '--coverages', type = int, default = 1,
                            help = 'Which coverages used for measuring uniquness of pool. If 1, branch coverages. If 0, statement coverages. (default = 1).')
	parser.add_argument('-i', '--inp', type = int, default = 10,
                            help = 'Initial number of pools (10 default).')
	parser.add_argument('-m', '--mnp', type = int, default = 100,
                            help = 'Maximum number of pools (100 default).')
	parser.add_argument('-n', '--nseconds', type = int, default = 1,
                            help = 'Each n seconds new pool is added (default each 1 second).')
	parser.add_argument('-q', '--quickTests', action = 'store_true',
                            help = 'Produce quick tests for coverage.')
	parser.add_argument('-r', '--running', action = 'store_true',
                            help = 'Produce running branch coverage report.')
	parser.add_argument('-s', '--seed', type = int, default = None,
                            help = 'Random seed (default = None).')
	parser.add_argument('-t', '--timeout', type = int, default = 3600,
                            help = 'Timeout in seconds (300 default).')
	parser.add_argument('-C', '--count', type = bool, default = True,
                            help = 'Whether count number of coverages or not for measuring uniquness of pool (default = True).')
        parser.add_argument('-I', '--internal', action = 'store_true',
                            help = 'Produce internal coverage report at the end.')
	parser.add_argument('-S', '--single', action = 'store_true',
                            help = 'Using only single pool instead of multi pools.')
	parsed_args = parser.parse_args(sys.argv[1:])
	return (parsed_args, parser)

def make_config(pargs, parser):
	pdict = pargs.__dict__
	key_list = pdict.keys()
	arg_list = [pdict[k] for k in key_list]
	Config = namedtuple('Config', key_list)
	nt_config = Config(*arg_list)
	return nt_config

def check_redundancy(seq, a, keys, sut):
	if not len(seq):
		return False
	index = 0
	for i in seq:
		if not check_redundancy_helper(sut.actOrder(i), keys, index, len(seq) + 1):
			return False
		index += 1
	return check_redundancy_helper(sut.actOrder(a), keys, index, len(seq) + 1)

def check_redundancy_helper(aorder, keys, index, length):
	return aorder in keys.keys() and (index, length) in keys[aorder]

def covered(pool):
	global config
	coverages = pool[0].currBranches() if config.coverages == 1 else pool[0].currStatements()
	for c in coverages:
		if config.count:
			if c in pool[4]:
				pool[4][c] += 1
			else:
				pool[4][c] = 1
		else:
			if not c in pool[4]:
				pool[4][c] = 1

def create_new_pool():
	return [SUT.sut(), [[]], [], 0.0, dict(), 0.0]

def delete_pools(pools, num):
	newpools = []
	for pool in pools:
		pool[5] = uniquness(pool, pools)
	sortedpools = sorted(pools, key = lambda x: x[5], reverse = True)
	for pool in sortedpools:
		newpools.append(pool)
		if len(newpools) == num:
			break
	return newpools

def feedback(pool, keys, branches, statements):
	global config, fid, R, start, ntests, nskips
	elapsed = time.time()
	sut = pool[0]
	seq = R.choice(pool[1])[:]
	sut.replay(seq)
	if time.time() - start > config.timeout:
		return False
	n = R.randint(2, 100) if R.randint(0, 9) == 0 else 1
	skip = 0
	for i in xrange(n):
		a = sut.randomEnabled(R)
		if check_redundancy(seq, a, keys, sut):
			skip += 1
			if n == skip:
				nskips += 1
				return True
			continue
		seq.append(a)
		ok = sut.safely(a)
		update_coverages(a, branches, statements, sut)
		if not ok:
			print "FIND BUG in ", time.time() - start, "SECONDS"
			update_keys(seq, keys, sut)
			pool[2].append(seq)
			pool[3] += (time.time() - elapsed)
			fid = handle_failure(sut, fid, start)
			return True
		if time.time() - start > config.timeout:
			return False
	ntests += 1
	update_keys(seq, keys, sut)
	if not config.single:
		covered(pool)
	pool[1].append(seq)
	pool[3] += (time.time() - elapsed)
	return True

def handle_failure(sut, fid, start):
	filename = 'failure' + `fid` + '.test'
	sut.saveTest(sut.test(), filename)
	return fid + 1

def internal(pools):
	i = 0
	for pool in pools:
		print "Producing internal coverage report for pool", i, "..."
		pool[0].internalReport()
		print ""
		i += 1

def score(pool):
	global config
	if pool[3] == 0.0 or len(pool[0].allBranches()) == 0 or len(pool[0].allStatements()) == 0:
		return float('inf')
	if config.coverages:
		return len(pool[0].allBranches()) / pool[3]
	else:
		return len(pool[0].allStatements()) / pool[3]

def select_pool(pools):
	global config
	if config.single:
		return pools[0]
	maxscore = -1.0
	for pool in pools:
		s = score(pool)
		if s == float('inf'):
			return pool
		if s > maxscore:
			maxscore = s
			selected = pool
	return selected

def uniquness(pool, pools):
	if len(pool[4]) == 0:
		return float('inf')
	uniquness = 0.0
	for c in pool[4]:
		uniquness += uniquness_helper(pool, c, pools)
	return uniquness / len(pool[4])

def uniquness_helper(pool, c, pools):
	totalcovered = 0.0
	for p in pools:
		if c in p[4]:
			totalcovered += p[4][c]
	return pool[4][c] / totalcovered

def update_coverages(a, branches, statements, sut):
	global config, start
	if sut.newBranches() != set([]):
		if config.running:
			print "ACTION:", a[0]
		for b in sut.newBranches():
			branches.add(b)
			if config.running:
				print time.time() - start, len(branches), "New branch", b
	if sut.newStatements() != set([]):
		for s in sut.newStatements():
			statements.add(s)

def update_keys(seq, keys, sut):
	index = 0
	for i in seq:
		if sut.actOrder(i) in keys.keys():
			if (index, len(seq)) in keys[sut.actOrder(i)]:
				continue
			else:
				keys[sut.actOrder(i)].add((index, len(seq)))
		else:
			keys[sut.actOrder(i)] = set((index, len(seq)))
		index += 1

def main():
	global config, fid, R, start, ntests, nskips
	parsed_args, parser = parse_args()
	config = make_config(parsed_args, parser)
	print('Feedback-controlled random testing using config={}'.format(config))
	R = random.Random(config.seed)
	fid = 0
	ntests = 0
	nskips = 0
	start = time.time()
	pools = []
	keys = dict()
	branches = set()
	statements = set()
	n = 1 if config.single else config.inp
	for i in xrange(n):
		pools.append(create_new_pool())
	lastadded = time.time()
	while time.time() - start < config.timeout:
		if not config.single and time.time() - lastadded > config.nseconds:
			pools.append(create_new_pool())
			lastadded = time.time()
		if not feedback(select_pool(pools), keys, branches, statements):
			break
		if not config.single and len(pools) > config.mnp:
			pools = delete_pools(pools, config.mnp / 2)
	if config.internal:
		internal(pools)
	print time.time() - start, "TOTAL RUNTIME"
	print ntests, "EXECUTED"
	print nskips, "SKIPPED"
	print len(branches), "BRANCHES COVERED"
	print len(statements), "STATEMENTS COVERED"

if __name__ == '__main__':
	main()

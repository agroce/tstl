To try this out, install

1) tstl
2) eth-testrpc

Then compile the .tstl file.

To get tests running, I would do something like:

```
pip install tstl
pip install eth-testrpc
tstl solc.tstl
tstl_rt --noCover --depth 1000 --swarm
```

Look at tstl docs for how to use any generated tests.

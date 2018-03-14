from __future__ import print_function
from solc import *
from solc.exceptions import SolcError
from testrpc.client import EthTesterClient
from testrpc.client.utils import encode_data
from testrpc.client.utils import decode_hex
from ethereum.utils import sha3
from ethereum.tester import TransactionFailed
from rlp.utils import big_endian_to_int

def fid(functionDef):
    end = functionDef.find("(")
    return functionDef[:end]

def runTest(contract, optimize, verbose=False):
    client = EthTesterClient()
    a = client.get_accounts()[0]
    try:
        bin = compile_source(contract,optimize=optimize).values()[0]['bin']
    except SolcError as e:
        if "Internal compiler error during compilation" in str(e):
            print ("INTERNAL COMPILER ERROR WITH optimize =",optimize)
            print (e)
            return "INTERNAL COMPILER ERROR"
        if verbose:
            print (e)
        return ("COMPILATION FAILED", None)
    try:
        txnHash = client.send_transaction(_from = a, data = bytes(bin), value = 0)
    except TransactionFailed as e:
        if verbose:
            print (e)
        return ("SEND CONTRACT TRANSACTION FAILED", bytes(bin))
    txnReceipt = client.get_transaction_receipt(txnHash)
    contractAddress = txnReceipt['contractAddress']
    fsig = encode_data(sha3("f()")[:4])
    try:
        val = client.call(_from = a, to = contractAddress, data = fsig)
    except TransactionFailed as e:
        if verbose:
            print ("CALL FAILURE:")
            print (e)
        return ("CALL FAILED", bytes(bin))
    return (big_endian_to_int(decode_hex(val)), bytes(bin))

def test(functions, verbose=False, verboseNoOpt=False):
    if verbose:
        print ("="*50)
    # Expects to receive a set of function definitions with a top-level, no-parameter, function called f()
    contract = "contract c {\n" + functions + "\n}"
    (resultNoOpt,binNoOpt) = runTest(contract, False, verbose=verboseNoOpt)
    if len(binNoOpt) > (24 * 1024):
        print ("NON-OPTIMIZED CONTRACT TOO LARGE")
        return
    (resultOpt,binOpt) = runTest(contract, True, verbose=verbose)
    if binOpt != binNoOpt:
        print ("BINARIES DIFFER",len(binOpt),"BYTES VS.",len(binNoOpt),"BYTES NON-OPTIMIZED")
    if resultOpt != resultNoOpt:
        print ("*"*80)
        print ("MISMATCH:")
        print ("CONTRACT:")
        print (contract)
        print ("="*50)
        print ("OPTIMIZED VALUE:", resultOpt)
        print ("="*50)        
        print ("NON-OPTIMIZED VALUE:",resultNoOpt)
        print ("*"*80)        
        assert False
    if resultOpt not in ["COMPILATION FAILED", "SEND CONTRACT TRANSACTION FAILED", "CALL FAILED"]:
        print ("SUCCESSFULLY TESTED:")
        print (contract)
        print ("RETURNED:",resultOpt)
    else:
        print (resultOpt,"FOR FUNCTIONS OF LENGTH",len(functions))
        if verbose:
            print ("*"*40)
            print ("CONTRACT:")
            print (contract)
            print ("*"*40)
    if (resultOpt == "INTERNAL COMPILER ERROR") or (resultNoOpt == "INTERNAL COMPILER ERROR"):
        print ("*"*40)        
        print (contract)
        print ("*"*40)        
        assert False
        
        


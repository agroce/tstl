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

def runTest(contract, optimize):
    client = EthTesterClient()
    a = client.get_accounts()[0]
    try:
        bin = compile_source(contract,optimize=optimize).values()[0]['bin']
    except SolcError as e:
        return ("COMPILATION FAILED", None)
    try:
        txnHash = client.send_transaction(_from = a, data = bytes(bin), value = 0)
    except TransactionFailed as e:
        return ("SEND CONTRACT TRANSACTION FAILED", bytes(bin))
    txnReceipt = client.get_transaction_receipt(txnHash)
    contractAddress = txnReceipt['contractAddress']
    fsig = encode_data(sha3("f()")[:4])
    try:
        val = client.call(_from = a, to = contractAddress, data = fsig)
    except TransactionFailed as e:
        return ("CALL FAILED", bytes(bin))
    return (big_endian_to_int(decode_hex(val)), bytes(bin))

def test(functions):
    # Expects to receive a set of function definitions with a top-level, no-parameter, function called f()
    contract = "contract c {" + functions + "}"
    (resultOpt,binOpt) = runTest(contract, True)
    (resultNoOpt,binNoOpt) = runTest(contract, False)
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
        print (functions)
        print ("RETURNED:",resultOpt)
    else:
        print (resultOpt,"FOR FUNCTIONS OF LENGTH",len(functions))
        


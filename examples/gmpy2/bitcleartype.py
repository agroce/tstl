import gmpy2
from gmpy2 import mpz,mpq,mpfr,mpc
def mpz_set_bit(value, bit):
    return value.bit_set(bit)

def mpz_clear_bit(value, bit):
    print type(value),type(bit)
    return value.bit_clear(bit)

def int_set_bit(value, bit):
    return value | (1<<bit)

def int_clear_bit(value, bit):
    return value & ~(1<<bit)


def check():
            global val0
            if ("val0" in globals()): 
                assert str(val0) == str(val_REF0)

            global val1
            if ("val1" in globals()): 
                assert str(val1) == str(val_REF1)

            global val2
            if ("val2" in globals()): 
                assert str(val2) == str(val_REF2)

            global val3
            if ("val3" in globals()): 
                assert str(val3) == str(val_REF3)

            global val4
            if ("val4" in globals()): 
                assert str(val4) == str(val_REF4)

            global val5
            if ("val5" in globals()): 
                assert str(val5) == str(val_REF5)

            global val6
            if ("val6" in globals()): 
                assert str(val6) == str(val_REF6)

            global val7
            if ("val7" in globals()): 
                assert str(val7) == str(val_REF7)

            global val8
            if ("val8" in globals()): 
                assert str(val8) == str(val_REF8)

            global val9
            if ("val9" in globals()): 
                assert str(val9) == str(val_REF9)

            if ("val0" in globals()): 
                assert val0.bit_length() == val_REF0.bit_length()

            if ("val1" in globals()): 
                assert val1.bit_length() == val_REF1.bit_length()

            if ("val2" in globals()): 
                assert val2.bit_length() == val_REF2.bit_length()

            if ("val3" in globals()): 
                assert val3.bit_length() == val_REF3.bit_length()

            if ("val4" in globals()): 
                assert val4.bit_length() == val_REF4.bit_length()

            if ("val5" in globals()): 
                assert val5.bit_length() == val_REF5.bit_length()

            if ("val6" in globals()): 
                assert val6.bit_length() == val_REF6.bit_length()

            if ("val7" in globals()): 
                assert val7.bit_length() == val_REF7.bit_length()

            if ("val8" in globals()): 
                assert val8.bit_length() == val_REF8.bit_length()

            if ("val9" in globals()): 
                assert val9.bit_length() == val_REF9.bit_length()





val0 = mpz(1) 
val_REF0 = int(1)
check()
pval1 = 8 
check()
val1 = mpz(3) 
val_REF1 = int(3)
check()
val5 = mpz(6) 
val_REF5 = int(6)
check()
val3 = mpz(5) 
val_REF3 = int(5)
check()
try:
  val0 = val5 << pval1 
except (OverflowError, ValueError):
  pass
try:
  val_REF0 = val_REF5 << pval1
except (OverflowError, ValueError):
  pass
check()
try:
  val5 = val1 << val0 
except (OverflowError, ValueError):
  pass
try:
  val_REF5 = val_REF1 << val_REF0
except (OverflowError, ValueError):
  pass
check()
print "val3:",val3,type(val3)
print "val5:",val5,type(val5)
val0 = mpz_clear_bit(val3,val5) 
val_REF0 = int_clear_bit(val_REF3,val_REF5)
check()


print "TEST COMPLETED SUCCESSFULLY"

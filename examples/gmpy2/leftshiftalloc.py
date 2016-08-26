import gmpy2
from gmpy2 import mpz,mpq,mpfr,mpc


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





print '''val6 = mpz(4) '''
val6 = mpz(4) 
val_REF6 = int(4)
check()
print '''val6 = val6 | val6 '''
val6 = val6 | val6 
val_REF6 = val_REF6 | val_REF6
check()
print '''val0 = mpz(3) '''
val0 = mpz(3) 
val_REF0 = int(3)
check()
print '''val6 = val6 * val0 '''
val6 = val6 * val0 
val_REF6 = val_REF6 * val_REF0
check()
print '''val0 = val0 ^ val0 '''
val0 = val0 ^ val0 
val_REF0 = val_REF0 ^ val_REF0
check()
print '''val0 = val0 | val0 '''
val0 = val0 | val0 
val_REF0 = val_REF0 | val_REF0
check()
print '''val0 = val6 ^ val6 '''
val0 = val6 ^ val6 
val_REF0 = val_REF6 ^ val_REF6
check()
print '''val3 = mpz(4) '''
val3 = mpz(4) 
val_REF3 = int(4)
check()
print '''val6 = val3 - val0 '''
val6 = val3 - val0 
val_REF6 = val_REF3 - val_REF0
check()
print '''val3 = val6 >> val6 '''
try:
  val3 = val6 >> val6 
except (OverflowError):
  pass
try:
  val_REF3 = val_REF6 >> val_REF6
except (OverflowError):
  pass
check()
print '''val3 = val3 + val3 '''
val3 = val3 + val3 
val_REF3 = val_REF3 + val_REF3
check()
print '''val5 = mpz(9) '''
val5 = mpz(9) 
val_REF5 = int(9)
check()
print '''val5 = val3 / val5 '''
val5 = val3 / val5 
val_REF5 = val_REF3 / val_REF5
check()
print '''val6 = val6 + val5 '''
val6 = val6 + val5 
val_REF6 = val_REF6 + val_REF5
check()
print '''val5 = val5 - val6 '''
val5 = val5 - val6 
val_REF5 = val_REF5 - val_REF6
check()
print '''val3 = val5 * val6 '''
val3 = val5 * val6 
val_REF3 = val_REF5 * val_REF6
check()
print '''val6 = val3 & val0 '''
val6 = val3 & val0 
val_REF6 = val_REF3 & val_REF0
check()
print '''val6 = val0 * val5 '''
val6 = val0 * val5 
val_REF6 = val_REF0 * val_REF5
check()
print '''val3 = val0 | val5 '''
val3 = val0 | val5 
val_REF3 = val_REF0 | val_REF5
check()
print '''val0 = val6 >> val6 '''
try:
  val0 = val6 >> val6 
except (OverflowError):
  pass
try:
  val_REF0 = val_REF6 >> val_REF6
except (OverflowError):
  pass
check()
print '''val0 = val5 ^ val0 '''
val0 = val5 ^ val0 
val_REF0 = val_REF5 ^ val_REF0
check()
print '''val0 = val0 * val6 '''
val0 = val0 * val6 
val_REF0 = val_REF0 * val_REF6
check()
print '''val6 = val6 * val3 '''
val6 = val6 * val3 
val_REF6 = val_REF6 * val_REF3
check()
print '''val3 = mpz(3) '''
val3 = mpz(3) 
val_REF3 = int(3)
check()
print '''val0 = val3 << val0 '''
try:
  val0 = val3 << val0 
except (OverflowError):
  pass
try:
  val_REF0 = val_REF3 << val_REF0
except (OverflowError):
  pass
check()
print '''val6 = mpz(1) '''
val6 = mpz(1) 
val_REF6 = int(1)
check()
print '''val5 = val5 + val3 '''
val5 = val5 + val3 
val_REF5 = val_REF5 + val_REF3
check()
print '''val0 = val0 - val6 '''
val0 = val0 - val6 
val_REF0 = val_REF0 - val_REF6
check()
print '''val6 = val6 * val6 '''
val6 = val6 * val6 
val_REF6 = val_REF6 * val_REF6
check()
print '''val3 = val3 | val6 '''
val3 = val3 | val6 
val_REF3 = val_REF3 | val_REF6
check()
print '''val2 = mpz(9) '''
val2 = mpz(9) 
val_REF2 = int(9)
check()
print '''val5 = val0 - val6 '''
val5 = val0 - val6 
val_REF5 = val_REF0 - val_REF6
check()
print '''val2 = val5 * val6 '''
val2 = val5 * val6 
val_REF2 = val_REF5 * val_REF6
check()
print '''val0 = val0 & val5 '''
val0 = val0 & val5 
val_REF0 = val_REF0 & val_REF5
check()
print '''val0 = val6 * val6 '''
val0 = val6 * val6 
val_REF0 = val_REF6 * val_REF6
check()
print '''val2 = val3 / val0 '''
val2 = val3 / val0 
val_REF2 = val_REF3 / val_REF0
check()
print '''val2 = val5 + val3 '''
val2 = val5 + val3 
val_REF2 = val_REF5 + val_REF3
check()
print '''val6 = val2 | val2 '''
val6 = val2 | val2 
val_REF6 = val_REF2 | val_REF2
check()
print '''val6 = val5 << val3 '''
try:
  val6 = val5 << val3 
except (OverflowError):
  pass
try:
  val_REF6 = val_REF5 << val_REF3
except (OverflowError):
  pass
check()
print '''val3 = val2 * val5 '''
val3 = val2 * val5 
val_REF3 = val_REF2 * val_REF5
check()
print '''val0 = val5 & val2 '''
val0 = val5 & val2 
val_REF0 = val_REF5 & val_REF2
check()
print '''val3 = val2 - val6 '''
val3 = val2 - val6 
val_REF3 = val_REF2 - val_REF6
check()
print '''val0 = val6 - val3 '''
val0 = val6 - val3 
val_REF0 = val_REF6 - val_REF3
check()
print '''val6 = val0 / val3 '''
val6 = val0 / val3 
val_REF6 = val_REF0 / val_REF3
check()
print '''val6 = val3 + val5 '''
val6 = val3 + val5 
val_REF6 = val_REF3 + val_REF5
check()
print '''val2 = val2 + val5 '''
val2 = val2 + val5 
val_REF2 = val_REF2 + val_REF5
check()
print '''val2 = val0 * val5 '''
val2 = val0 * val5 
val_REF2 = val_REF0 * val_REF5
check()
print '''val2 = mpz(2) '''
val2 = mpz(2) 
val_REF2 = int(2)
check()
print '''val0 = val3 / val2 '''
val0 = val3 / val2 
val_REF0 = val_REF3 / val_REF2
check()
print '''val2 = val6 * val0 '''
val2 = val6 * val0 
val_REF2 = val_REF6 * val_REF0
check()
print '''val3 = val6 | val2 '''
val3 = val6 | val2 
val_REF3 = val_REF6 | val_REF2
check()
print '''val2 = val3 + val2 '''
val2 = val3 + val2 
val_REF2 = val_REF3 + val_REF2
check()
print '''val5 = val0 + val5 '''
val5 = val0 + val5 
val_REF5 = val_REF0 + val_REF5
check()
print '''val2 = val6 ^ val2 '''
val2 = val6 ^ val2 
val_REF2 = val_REF6 ^ val_REF2
check()
print '''val5 = mpz(6) '''
val5 = mpz(6) 
val_REF5 = int(6)
check()
print '''val2 = val2 & val6 '''
val2 = val2 & val6 
val_REF2 = val_REF2 & val_REF6
check()
print '''val6 = -(val2) '''
val6 = -(val2) 
val_REF6 = -(val_REF2)
check()
print '''val0 = val2 & val2 '''
val0 = val2 & val2 
val_REF0 = val_REF2 & val_REF2
check()
print '''val0 = val3 & val2 '''
val0 = val3 & val2 
val_REF0 = val_REF3 & val_REF2
check()
print '''val5 = val2 ^ val6 '''
val5 = val2 ^ val6 
val_REF5 = val_REF2 ^ val_REF6
check()
print '''val3 = val0 | val3 '''
val3 = val0 | val3 
val_REF3 = val_REF0 | val_REF3
check()
print '''val5 = val2 | val2 '''
val5 = val2 | val2 
val_REF5 = val_REF2 | val_REF2
check()
print '''val6 = abs(val5) '''
val6 = abs(val5) 
val_REF6 = abs(val_REF5)
check()
print '''val2 = val3 * val6 '''
val2 = val3 * val6 
val_REF2 = val_REF3 * val_REF6
check()
print '''val3 = val5 * val0 '''
val3 = val5 * val0 
val_REF3 = val_REF5 * val_REF0
check()
print '''val5 = val3 / val0 '''
val5 = val3 / val0 
val_REF5 = val_REF3 / val_REF0
check()
print '''val8 = mpz(9) '''
val8 = mpz(9) 
val_REF8 = int(9)
check()
print '''val3 = val3 * val6 '''
val3 = val3 * val6 
val_REF3 = val_REF3 * val_REF6
check()
print '''val0 = mpz(5) '''
val0 = mpz(5) 
val_REF0 = int(5)
check()
print '''val6 = val0 | val3 '''
val6 = val0 | val3 
val_REF6 = val_REF0 | val_REF3
check()
print '''val0 = val6 - val5 '''
val0 = val6 - val5 
val_REF0 = val_REF6 - val_REF5
check()
print '''val5 = val3 + val3 '''
val5 = val3 + val3 
val_REF5 = val_REF3 + val_REF3
check()
print '''val3 = val5 & val8 '''
val3 = val5 & val8 
val_REF3 = val_REF5 & val_REF8
check()
print '''val3 = val5 % val6 '''
val3 = val5 % val6 
val_REF3 = val_REF5 % val_REF6
check()
print '''val2 = val0 << val6 '''
try:
  val2 = val0 << val6 
except (OverflowError):
  pass
try:
  val_REF2 = val_REF0 << val_REF6
except (OverflowError):
  pass
check()
print '''val5 = val0 % val6 '''
val5 = val0 % val6 
val_REF5 = val_REF0 % val_REF6
check()
print '''val5 = val2 - val0 '''
val5 = val2 - val0 
val_REF5 = val_REF2 - val_REF0
check()
print '''val2 = val0 ^ val8 '''
val2 = val0 ^ val8 
val_REF2 = val_REF0 ^ val_REF8
check()
print '''val6 = mpz(7) '''
val6 = mpz(7) 
val_REF6 = int(7)
check()
print '''val0 = val8 % val5 '''
val0 = val8 % val5 
val_REF0 = val_REF8 % val_REF5
check()
print '''val2 = val8 + val5 '''
val2 = val8 + val5 
val_REF2 = val_REF8 + val_REF5
check()
print '''val0 = val6 << val8 '''
try:
  val0 = val6 << val8 
except (OverflowError):
  pass
try:
  val_REF0 = val_REF6 << val_REF8
except (OverflowError):
  pass
check()
print '''val5 = val0 % val5 '''
val5 = val0 % val5 
val_REF5 = val_REF0 % val_REF5
check()
print '''val5 = val2 / val3 '''
val5 = val2 / val3 
val_REF5 = val_REF2 / val_REF3
check()
print '''val5 = val0 % val0 '''
val5 = val0 % val0 
val_REF5 = val_REF0 % val_REF0
check()
print '''val8 = val8 >> val0 '''
try:
  val8 = val8 >> val0 
except (OverflowError):
  pass
try:
  val_REF8 = val_REF8 >> val_REF0
except (OverflowError):
  pass
check()
print '''val3 = val3 << val6 '''
try:
  val3 = val3 << val6 
except (OverflowError):
  pass
try:
  val_REF3 = val_REF3 << val_REF6
except (OverflowError):
  pass
check()
print '''val0 = val6 & val6 '''
val0 = val6 & val6 
val_REF0 = val_REF6 & val_REF6
check()
print '''val2 = abs(val2) '''
val2 = abs(val2) 
val_REF2 = abs(val_REF2)
check()
print '''val5 = val3 & val8 '''
val5 = val3 & val8 
val_REF5 = val_REF3 & val_REF8
check()
print '''val6 = val6 & val8 '''
val6 = val6 & val8 
val_REF6 = val_REF6 & val_REF8
check()
print '''val5 = val5 << val8 '''
try:
  val5 = val5 << val8 
except (OverflowError):
  pass
try:
  val_REF5 = val_REF5 << val_REF8
except (OverflowError):
  pass
check()
print '''val8 = mpz(9) '''
val8 = mpz(9) 
val_REF8 = int(9)
check()
print '''val6 = val0 % val0 '''
val6 = val0 % val0 
val_REF6 = val_REF0 % val_REF0
check()
print '''val3 = val3 % val3 '''
val3 = val3 % val3 
val_REF3 = val_REF3 % val_REF3
check()
print '''val6 = val3 | val8 '''
val6 = val3 | val8 
val_REF6 = val_REF3 | val_REF8
check()
print '''val1 = mpz(3) '''
val1 = mpz(3) 
val_REF1 = int(3)
check()
print '''val5 = val1 * val6 '''
val5 = val1 * val6 
val_REF5 = val_REF1 * val_REF6
check()
print '''val5 = abs(val3) '''
val5 = abs(val3) 
val_REF5 = abs(val_REF3)
check()
print '''val2 = val8 << val5 '''
try:
  val2 = val8 << val5 
except (OverflowError):
  pass
try:
  val_REF2 = val_REF8 << val_REF5
except (OverflowError):
  pass
check()
print '''val3 = val2 ^ val3 '''
val3 = val2 ^ val3 
val_REF3 = val_REF2 ^ val_REF3
check()
print '''val8 = val8 * val2 '''
val8 = val8 * val2 
val_REF8 = val_REF8 * val_REF2
check()
print '''val8 = val1 % val0 '''
val8 = val1 % val0 
val_REF8 = val_REF1 % val_REF0
check()
print '''val8 = val0 % val8 '''
val8 = val0 % val8 
val_REF8 = val_REF0 % val_REF8
check()
print '''val8 = val1 ^ val1 '''
val8 = val1 ^ val1 
val_REF8 = val_REF1 ^ val_REF1
check()
print '''val1 = val2 % val1 '''
val1 = val2 % val1 
val_REF1 = val_REF2 % val_REF1
check()
print '''val1 = val2 << val2 '''
try:
  val1 = val2 << val2 
except (OverflowError):
  pass
try:
  val_REF1 = val_REF2 << val_REF2
except (OverflowError):
  pass
check()
print '''val8 = val8 << val5 '''
try:
  val8 = val8 << val5 
except (OverflowError):
  pass
try:
  val_REF8 = val_REF8 << val_REF5
except (OverflowError):
  pass
check()
print '''val5 = val1 - val1 '''
val5 = val1 - val1 
val_REF5 = val_REF1 - val_REF1
check()
print '''val1 = val5 - val0 '''
val1 = val5 - val0 
val_REF1 = val_REF5 - val_REF0
check()
print '''val1 = val3 & val1 '''
val1 = val3 & val1 
val_REF1 = val_REF3 & val_REF1
check()
print '''val5 = val0 | val1 '''
val5 = val0 | val1 
val_REF5 = val_REF0 | val_REF1
check()
print '''val2 = val1 - val5 '''
val2 = val1 - val5 
val_REF2 = val_REF1 - val_REF5
check()
print '''val5 = val2 ^ val0 '''
val5 = val2 ^ val0 
val_REF5 = val_REF2 ^ val_REF0
check()
print '''val0 = val6 * val6 '''
val0 = val6 * val6 
val_REF0 = val_REF6 * val_REF6
check()
print '''val8 = val6 / val1 '''
val8 = val6 / val1 
val_REF8 = val_REF6 / val_REF1
check()
print '''val2 = val5 * val0 '''
val2 = val5 * val0 
val_REF2 = val_REF5 * val_REF0
check()
print '''val0 = val5 << val3 '''
try:
  val0 = val5 << val3 
except (OverflowError):
  pass
try:
  val_REF0 = val_REF5 << val_REF3
except (OverflowError):
  pass
check()
print '''val8 = val2 * val1 '''
val8 = val2 * val1 
val_REF8 = val_REF2 * val_REF1
check()
print '''val2 = val5 & val3 '''
val2 = val5 & val3 
val_REF2 = val_REF5 & val_REF3
check()
print '''val1 = val2 / val2 '''
val1 = val2 / val2 
val_REF1 = val_REF2 / val_REF2
check()
print '''val1 = val1 % val3 '''
val1 = val1 % val3 
val_REF1 = val_REF1 % val_REF3
check()
print '''val3 = val8 | val5 '''
val3 = val8 | val5 
val_REF3 = val_REF8 | val_REF5
check()
print '''val0 = val8 ^ val5 '''
val0 = val8 ^ val5 
val_REF0 = val_REF8 ^ val_REF5
check()
print '''val2 = val5 & val5 '''
val2 = val5 & val5 
val_REF2 = val_REF5 & val_REF5
check()
print '''val8 = val2 % val1 '''
val8 = val2 % val1 
val_REF8 = val_REF2 % val_REF1
check()
print '''val2 = mpz(2) '''
val2 = mpz(2) 
val_REF2 = int(2)
check()
print '''val8 = val3 ^ val1 '''
val8 = val3 ^ val1 
val_REF8 = val_REF3 ^ val_REF1
check()
print '''val0 = val3 % val5 '''
val0 = val3 % val5 
val_REF0 = val_REF3 % val_REF5
check()
print '''val0 = val2 - val8 '''
val0 = val2 - val8 
val_REF0 = val_REF2 - val_REF8
check()
print '''val2 = val5 / val1 '''
val2 = val5 / val1 
val_REF2 = val_REF5 / val_REF1
check()
print '''val0 = val6 | val0 '''
val0 = val6 | val0 
val_REF0 = val_REF6 | val_REF0
check()
print '''val1 = val0 & val6 '''
val1 = val0 & val6 
val_REF1 = val_REF0 & val_REF6
check()
print '''val5 = val0 - val1 '''
val5 = val0 - val1 
val_REF5 = val_REF0 - val_REF1
check()
print '''val3 = val5 - val3 '''
val3 = val5 - val3 
val_REF3 = val_REF5 - val_REF3
check()
print '''val8 = val3 ^ val3 '''
val8 = val3 ^ val3 
val_REF8 = val_REF3 ^ val_REF3
check()
print '''val6 = val8 / val0 '''
val6 = val8 / val0 
val_REF6 = val_REF8 / val_REF0
check()
print '''val3 = val5 / val2 '''
val3 = val5 / val2 
val_REF3 = val_REF5 / val_REF2
check()
print '''val8 = val8 & val5 '''
val8 = val8 & val5 
val_REF8 = val_REF8 & val_REF5
check()
print '''val8 = val1 % val2 '''
val8 = val1 % val2 
val_REF8 = val_REF1 % val_REF2
check()
print '''val6 = val2 * val0 '''
val6 = val2 * val0 
val_REF6 = val_REF2 * val_REF0
check()
print '''val2 = val0 * val5 '''
val2 = val0 * val5 
val_REF2 = val_REF0 * val_REF5
check()
print '''val6 = val5 - val8 '''
val6 = val5 - val8 
val_REF6 = val_REF5 - val_REF8
check()
print '''val3 = val5 + val0 '''
val3 = val5 + val0 
val_REF3 = val_REF5 + val_REF0
check()
print '''val2 = val6 - val8 '''
val2 = val6 - val8 
val_REF2 = val_REF6 - val_REF8
check()
print '''val5 = val3 - val1 '''
val5 = val3 - val1 
val_REF5 = val_REF3 - val_REF1
check()
print '''val5 = val1 % val3 '''
val5 = val1 % val3 
val_REF5 = val_REF1 % val_REF3
check()
print '''val2 = val6 << val2 '''
try:
  val2 = val6 << val2 
except (OverflowError):
  pass
try:
  val_REF2 = val_REF6 << val_REF2
except (OverflowError):
  pass
check()
print '''val4 = mpz(7) '''
val4 = mpz(7) 
val_REF4 = int(7)
check()
print '''val4 = val3 - val3 '''
val4 = val3 - val3 
val_REF4 = val_REF3 - val_REF3
check()
print '''val8 = val6 | val5 '''
val8 = val6 | val5 
val_REF8 = val_REF6 | val_REF5
check()
print '''val2 = val0 * val6 '''
val2 = val0 * val6 
val_REF2 = val_REF0 * val_REF6
check()
print '''val4 = val6 / val5 '''
val4 = val6 / val5 
val_REF4 = val_REF6 / val_REF5
check()
print '''val4 = val3 | val2 '''
val4 = val3 | val2 
val_REF4 = val_REF3 | val_REF2
check()
print '''val8 = val6 - val0 '''
val8 = val6 - val0 
val_REF8 = val_REF6 - val_REF0
check()
print '''val4 = val5 << val2 '''
try:
  val4 = val5 << val2 
except (OverflowError):
  pass
try:
  val_REF4 = val_REF5 << val_REF2
except (OverflowError):
  pass
check()
print '''val5 = val8 * val8 '''
val5 = val8 * val8 
val_REF5 = val_REF8 * val_REF8
check()
print '''val3 = val4 & val1 '''
val3 = val4 & val1 
val_REF3 = val_REF4 & val_REF1
check()
print '''val0 = val6 ^ val8 '''
val0 = val6 ^ val8 
val_REF0 = val_REF6 ^ val_REF8
check()
print '''val3 = val4 >> val6 '''
try:
  val3 = val4 >> val6 
except (OverflowError):
  pass
try:
  val_REF3 = val_REF4 >> val_REF6
except (OverflowError):
  pass
check()
print '''val8 = val2 % val2 '''
val8 = val2 % val2 
val_REF8 = val_REF2 % val_REF2
check()
print '''val6 = val5 + val0 '''
val6 = val5 + val0 
val_REF6 = val_REF5 + val_REF0
check()
print '''val3 = val1 ^ val1 '''
val3 = val1 ^ val1 
val_REF3 = val_REF1 ^ val_REF1
check()
print '''val1 = val5 - val1 '''
val1 = val5 - val1 
val_REF1 = val_REF5 - val_REF1
check()
print '''val1 = val2 % val4 '''
val1 = val2 % val4 
val_REF1 = val_REF2 % val_REF4
check()
print '''val6 = val3 / val5 '''
val6 = val3 / val5 
val_REF6 = val_REF3 / val_REF5
check()
print '''val5 = val8 << val3 '''
try:
  val5 = val8 << val3 
except (OverflowError):
  pass
try:
  val_REF5 = val_REF8 << val_REF3
except (OverflowError):
  pass
check()
print '''val6 = val4 | val4 '''
val6 = val4 | val4 
val_REF6 = val_REF4 | val_REF4
check()
print '''val3 = val0 + val3 '''
val3 = val0 + val3 
val_REF3 = val_REF0 + val_REF3
check()
print '''val4 = val6 >> val2 '''
try:
  val4 = val6 >> val2 
except (OverflowError):
  pass
try:
  val_REF4 = val_REF6 >> val_REF2
except (OverflowError):
  pass
check()
print '''val1 = val4 + val1 '''
val1 = val4 + val1 
val_REF1 = val_REF4 + val_REF1
check()
print '''val3 = val2 | val8 '''
val3 = val2 | val8 
val_REF3 = val_REF2 | val_REF8
check()
print '''val2 = val3 - val5 '''
val2 = val3 - val5 
val_REF2 = val_REF3 - val_REF5
check()
print '''val0 = abs(val6) '''
val0 = abs(val6) 
val_REF0 = abs(val_REF6)
check()
print '''val1 = val5 + val3 '''
val1 = val5 + val3 
val_REF1 = val_REF5 + val_REF3
check()
print '''val2 = val6 & val5 '''
val2 = val6 & val5 
val_REF2 = val_REF6 & val_REF5
check()
print '''val1 = val2 << val6 '''
try:
  val1 = val2 << val6 
except (OverflowError):
  pass
try:
  val_REF1 = val_REF2 << val_REF6
except (OverflowError):
  pass
check()
print '''val0 = val0 * val3 '''
val0 = val0 * val3 
val_REF0 = val_REF0 * val_REF3
check()
print '''val2 = val6 | val6 '''
val2 = val6 | val6 
val_REF2 = val_REF6 | val_REF6
check()
print '''val8 = mpz(3) '''
val8 = mpz(3) 
val_REF8 = int(3)
check()
print '''val2 = val2 + val1 '''
val2 = val2 + val1 
val_REF2 = val_REF2 + val_REF1
check()
print '''val2 = val4 & val0 '''
val2 = val4 & val0 
val_REF2 = val_REF4 & val_REF0
check()
print '''val1 = val6 * val4 '''
val1 = val6 * val4 
val_REF1 = val_REF6 * val_REF4
check()
print '''val0 = val8 >> val2 '''
try:
  val0 = val8 >> val2 
except (OverflowError):
  pass
try:
  val_REF0 = val_REF8 >> val_REF2
except (OverflowError):
  pass
check()
print '''val5 = val5 ^ val2 '''
val5 = val5 ^ val2 
val_REF5 = val_REF5 ^ val_REF2
check()
print '''val2 = val6 ^ val6 '''
val2 = val6 ^ val6 
val_REF2 = val_REF6 ^ val_REF6
check()
print '''val5 = val5 + val0 '''
val5 = val5 + val0 
val_REF5 = val_REF5 + val_REF0
check()
print '''val5 = val2 & val3 '''
val5 = val2 & val3 
val_REF5 = val_REF2 & val_REF3
check()
print '''val8 = val0 ^ val0 '''
val8 = val0 ^ val0 
val_REF8 = val_REF0 ^ val_REF0
check()
print '''val4 = val5 >> val4 '''
try:
  val4 = val5 >> val4 
except (OverflowError):
  pass
try:
  val_REF4 = val_REF5 >> val_REF4
except (OverflowError):
  pass
check()
print '''val5 = val6 + val5 '''
val5 = val6 + val5 
val_REF5 = val_REF6 + val_REF5
check()
print '''val8 = val6 + val6 '''
val8 = val6 + val6 
val_REF8 = val_REF6 + val_REF6
check()
print '''val0 = val6 - val5 '''
val0 = val6 - val5 
val_REF0 = val_REF6 - val_REF5
check()
print '''val2 = val3 << val2 '''
try:
  val2 = val3 << val2 
except (OverflowError):
  pass
try:
  val_REF2 = val_REF3 << val_REF2
except (OverflowError):
  pass
check()
print '''val6 = val8 >> val8 '''
try:
  val6 = val8 >> val8 
except (OverflowError):
  pass
try:
  val_REF6 = val_REF8 >> val_REF8
except (OverflowError):
  pass
check()
print '''val0 = val2 & val4 '''
val0 = val2 & val4 
val_REF0 = val_REF2 & val_REF4
check()
print '''val2 = val2 << val4 '''
try:
  val2 = val2 << val4 
except (OverflowError):
  pass
try:
  val_REF2 = val_REF2 << val_REF4
except (OverflowError):
  pass
check()
print '''val5 = val1 | val0 '''
val5 = val1 | val0 
val_REF5 = val_REF1 | val_REF0
check()
print '''val1 = val6 % val3 '''
val1 = val6 % val3 
val_REF1 = val_REF6 % val_REF3
check()
print '''val8 = val4 << val6 '''
try:
  val8 = val4 << val6 
except (OverflowError):
  pass
try:
  val_REF8 = val_REF4 << val_REF6
except (OverflowError):
  pass
check()
print '''val3 = val1 | val3 '''
val3 = val1 | val3 
val_REF3 = val_REF1 | val_REF3
check()
print '''val6 = val5 >> val1 '''
try:
  val6 = val5 >> val1 
except (OverflowError):
  pass
try:
  val_REF6 = val_REF5 >> val_REF1
except (OverflowError):
  pass
check()
print '''val4 = val3 ^ val6 '''
val4 = val3 ^ val6 
val_REF4 = val_REF3 ^ val_REF6
check()
print '''val1 = val1 ^ val6 '''
val1 = val1 ^ val6 
val_REF1 = val_REF1 ^ val_REF6
check()
print '''val1 = val3 * val8 '''
val1 = val3 * val8 
val_REF1 = val_REF3 * val_REF8
check()
print '''val3 = val5 & val8 '''
val3 = val5 & val8 
val_REF3 = val_REF5 & val_REF8
check()
print '''val2 = val3 + val1 '''
val2 = val3 + val1 
val_REF2 = val_REF3 + val_REF1
check()
print '''val8 = val0 & val8 '''
val8 = val0 & val8 
val_REF8 = val_REF0 & val_REF8
check()
print '''val2 = val1 & val5 '''
val2 = val1 & val5 
val_REF2 = val_REF1 & val_REF5
check()
print '''val5 = val2 * val3 '''
val5 = val2 * val3 
val_REF5 = val_REF2 * val_REF3
check()
print '''val2 = val6 - val4 '''
val2 = val6 - val4 
val_REF2 = val_REF6 - val_REF4
check()
print '''val2 = val5 << val5 '''
try:
  val2 = val5 << val5 
except (OverflowError):
  pass
try:
  val_REF2 = val_REF5 << val_REF5
except (OverflowError):
  pass
check()
print '''val6 = val8 >> val0 '''
try:
  val6 = val8 >> val0 
except (OverflowError):
  pass
try:
  val_REF6 = val_REF8 >> val_REF0
except (OverflowError):
  pass
check()
print '''val0 = val6 + val4 '''
val0 = val6 + val4 
val_REF0 = val_REF6 + val_REF4
check()
print '''val6 = val0 & val0 '''
val6 = val0 & val0 
val_REF6 = val_REF0 & val_REF0
check()
print '''val1 = val8 | val3 '''
val1 = val8 | val3 
val_REF1 = val_REF8 | val_REF3
check()
print '''val6 = val0 / val6 '''
val6 = val0 / val6 
val_REF6 = val_REF0 / val_REF6
check()
print '''val3 = val0 & val2 '''
val3 = val0 & val2 
val_REF3 = val_REF0 & val_REF2
check()
print '''val1 = val6 - val5 '''
val1 = val6 - val5 
val_REF1 = val_REF6 - val_REF5
check()
print '''val3 = val6 % val6 '''
val3 = val6 % val6 
val_REF3 = val_REF6 % val_REF6
check()
print '''val4 = val3 << val4 '''
print "val3:",val3, val_REF3
print "val4:",val4, val_REF4
try:
  val4 = val3 << val4 
except (OverflowError):
  pass
try:
  val_REF4 = val_REF3 << val_REF4
except (OverflowError,MemoryError):
  print "Raised exception"
  pass
print val4, val_REF4
check()


print "TEST COMPLETED SUCCESSFULLY"

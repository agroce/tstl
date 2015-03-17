import copy
import traceback
import re
import sys
import coverage
import dominion
import dominion2
class t(object):
   def act0(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[0]=0

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[0]=False
   def guard0(self):
      return (((self.p_INT_used[0]) or (self.p_INT[0] == None)))
   def act1(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[0]=1

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[0]=False
   def guard1(self):
      return (((self.p_INT_used[0]) or (self.p_INT[0] == None)))
   def act2(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[0]=2

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[0]=False
   def guard2(self):
      return (((self.p_INT_used[0]) or (self.p_INT[0] == None)))
   def act3(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[0]=3

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[0]=False
   def guard3(self):
      return (((self.p_INT_used[0]) or (self.p_INT[0] == None)))
   def act4(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[0]=4

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[0]=False
   def guard4(self):
      return (((self.p_INT_used[0]) or (self.p_INT[0] == None)))
   def act5(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[0]=5

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[0]=False
   def guard5(self):
      return (((self.p_INT_used[0]) or (self.p_INT[0] == None)))
   def act6(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[0]=6

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[0]=False
   def guard6(self):
      return (((self.p_INT_used[0]) or (self.p_INT[0] == None)))
   def act7(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[0]=7

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[0]=False
   def guard7(self):
      return (((self.p_INT_used[0]) or (self.p_INT[0] == None)))
   def act8(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[0]=8

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[0]=False
   def guard8(self):
      return (((self.p_INT_used[0]) or (self.p_INT[0] == None)))
   def act9(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[0]=9

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[0]=False
   def guard9(self):
      return (((self.p_INT_used[0]) or (self.p_INT[0] == None)))
   def act10(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[0]=10

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[0]=False
   def guard10(self):
      return (((self.p_INT_used[0]) or (self.p_INT[0] == None)))
   def act11(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[0]=11

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[0]=False
   def guard11(self):
      return (((self.p_INT_used[0]) or (self.p_INT[0] == None)))
   def act12(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[0]=12

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[0]=False
   def guard12(self):
      return (((self.p_INT_used[0]) or (self.p_INT[0] == None)))
   def act13(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[0]=13

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[0]=False
   def guard13(self):
      return (((self.p_INT_used[0]) or (self.p_INT[0] == None)))
   def act14(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[0]=14

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[0]=False
   def guard14(self):
      return (((self.p_INT_used[0]) or (self.p_INT[0] == None)))
   def act15(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[0]=15

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[0]=False
   def guard15(self):
      return (((self.p_INT_used[0]) or (self.p_INT[0] == None)))
   def act16(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[0]=16

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[0]=False
   def guard16(self):
      return (((self.p_INT_used[0]) or (self.p_INT[0] == None)))
   def act17(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[0]=17

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[0]=False
   def guard17(self):
      return (((self.p_INT_used[0]) or (self.p_INT[0] == None)))
   def act18(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[0]=18

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[0]=False
   def guard18(self):
      return (((self.p_INT_used[0]) or (self.p_INT[0] == None)))
   def act19(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[0]=19

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[0]=False
   def guard19(self):
      return (((self.p_INT_used[0]) or (self.p_INT[0] == None)))
   def act20(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[0]=20

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[0]=False
   def guard20(self):
      return (((self.p_INT_used[0]) or (self.p_INT[0] == None)))
   def act21(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[1]=0

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[1]=False
   def guard21(self):
      return (((self.p_INT_used[1]) or (self.p_INT[1] == None)))
   def act22(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[1]=1

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[1]=False
   def guard22(self):
      return (((self.p_INT_used[1]) or (self.p_INT[1] == None)))
   def act23(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[1]=2

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[1]=False
   def guard23(self):
      return (((self.p_INT_used[1]) or (self.p_INT[1] == None)))
   def act24(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[1]=3

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[1]=False
   def guard24(self):
      return (((self.p_INT_used[1]) or (self.p_INT[1] == None)))
   def act25(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[1]=4

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[1]=False
   def guard25(self):
      return (((self.p_INT_used[1]) or (self.p_INT[1] == None)))
   def act26(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[1]=5

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[1]=False
   def guard26(self):
      return (((self.p_INT_used[1]) or (self.p_INT[1] == None)))
   def act27(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[1]=6

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[1]=False
   def guard27(self):
      return (((self.p_INT_used[1]) or (self.p_INT[1] == None)))
   def act28(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[1]=7

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[1]=False
   def guard28(self):
      return (((self.p_INT_used[1]) or (self.p_INT[1] == None)))
   def act29(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[1]=8

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[1]=False
   def guard29(self):
      return (((self.p_INT_used[1]) or (self.p_INT[1] == None)))
   def act30(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[1]=9

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[1]=False
   def guard30(self):
      return (((self.p_INT_used[1]) or (self.p_INT[1] == None)))
   def act31(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[1]=10

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[1]=False
   def guard31(self):
      return (((self.p_INT_used[1]) or (self.p_INT[1] == None)))
   def act32(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[1]=11

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[1]=False
   def guard32(self):
      return (((self.p_INT_used[1]) or (self.p_INT[1] == None)))
   def act33(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[1]=12

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[1]=False
   def guard33(self):
      return (((self.p_INT_used[1]) or (self.p_INT[1] == None)))
   def act34(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[1]=13

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[1]=False
   def guard34(self):
      return (((self.p_INT_used[1]) or (self.p_INT[1] == None)))
   def act35(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[1]=14

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[1]=False
   def guard35(self):
      return (((self.p_INT_used[1]) or (self.p_INT[1] == None)))
   def act36(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[1]=15

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[1]=False
   def guard36(self):
      return (((self.p_INT_used[1]) or (self.p_INT[1] == None)))
   def act37(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[1]=16

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[1]=False
   def guard37(self):
      return (((self.p_INT_used[1]) or (self.p_INT[1] == None)))
   def act38(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[1]=17

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[1]=False
   def guard38(self):
      return (((self.p_INT_used[1]) or (self.p_INT[1] == None)))
   def act39(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[1]=18

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[1]=False
   def guard39(self):
      return (((self.p_INT_used[1]) or (self.p_INT[1] == None)))
   def act40(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[1]=19

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[1]=False
   def guard40(self):
      return (((self.p_INT_used[1]) or (self.p_INT[1] == None)))
   def act41(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[1]=20

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[1]=False
   def guard41(self):
      return (((self.p_INT_used[1]) or (self.p_INT[1] == None)))
   def act42(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[2]=0

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[2]=False
   def guard42(self):
      return (((self.p_INT_used[2]) or (self.p_INT[2] == None)))
   def act43(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[2]=1

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[2]=False
   def guard43(self):
      return (((self.p_INT_used[2]) or (self.p_INT[2] == None)))
   def act44(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[2]=2

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[2]=False
   def guard44(self):
      return (((self.p_INT_used[2]) or (self.p_INT[2] == None)))
   def act45(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[2]=3

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[2]=False
   def guard45(self):
      return (((self.p_INT_used[2]) or (self.p_INT[2] == None)))
   def act46(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[2]=4

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[2]=False
   def guard46(self):
      return (((self.p_INT_used[2]) or (self.p_INT[2] == None)))
   def act47(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[2]=5

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[2]=False
   def guard47(self):
      return (((self.p_INT_used[2]) or (self.p_INT[2] == None)))
   def act48(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[2]=6

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[2]=False
   def guard48(self):
      return (((self.p_INT_used[2]) or (self.p_INT[2] == None)))
   def act49(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[2]=7

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[2]=False
   def guard49(self):
      return (((self.p_INT_used[2]) or (self.p_INT[2] == None)))
   def act50(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[2]=8

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[2]=False
   def guard50(self):
      return (((self.p_INT_used[2]) or (self.p_INT[2] == None)))
   def act51(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[2]=9

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[2]=False
   def guard51(self):
      return (((self.p_INT_used[2]) or (self.p_INT[2] == None)))
   def act52(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[2]=10

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[2]=False
   def guard52(self):
      return (((self.p_INT_used[2]) or (self.p_INT[2] == None)))
   def act53(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[2]=11

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[2]=False
   def guard53(self):
      return (((self.p_INT_used[2]) or (self.p_INT[2] == None)))
   def act54(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[2]=12

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[2]=False
   def guard54(self):
      return (((self.p_INT_used[2]) or (self.p_INT[2] == None)))
   def act55(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[2]=13

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[2]=False
   def guard55(self):
      return (((self.p_INT_used[2]) or (self.p_INT[2] == None)))
   def act56(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[2]=14

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[2]=False
   def guard56(self):
      return (((self.p_INT_used[2]) or (self.p_INT[2] == None)))
   def act57(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[2]=15

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[2]=False
   def guard57(self):
      return (((self.p_INT_used[2]) or (self.p_INT[2] == None)))
   def act58(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[2]=16

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[2]=False
   def guard58(self):
      return (((self.p_INT_used[2]) or (self.p_INT[2] == None)))
   def act59(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[2]=17

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[2]=False
   def guard59(self):
      return (((self.p_INT_used[2]) or (self.p_INT[2] == None)))
   def act60(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[2]=18

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[2]=False
   def guard60(self):
      return (((self.p_INT_used[2]) or (self.p_INT[2] == None)))
   def act61(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[2]=19

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[2]=False
   def guard61(self):
      return (((self.p_INT_used[2]) or (self.p_INT[2] == None)))
   def act62(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[2]=20

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[2]=False
   def guard62(self):
      return (((self.p_INT_used[2]) or (self.p_INT[2] == None)))
   def act63(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[3]=0

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[3]=False
   def guard63(self):
      return (((self.p_INT_used[3]) or (self.p_INT[3] == None)))
   def act64(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[3]=1

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[3]=False
   def guard64(self):
      return (((self.p_INT_used[3]) or (self.p_INT[3] == None)))
   def act65(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[3]=2

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[3]=False
   def guard65(self):
      return (((self.p_INT_used[3]) or (self.p_INT[3] == None)))
   def act66(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[3]=3

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[3]=False
   def guard66(self):
      return (((self.p_INT_used[3]) or (self.p_INT[3] == None)))
   def act67(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[3]=4

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[3]=False
   def guard67(self):
      return (((self.p_INT_used[3]) or (self.p_INT[3] == None)))
   def act68(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[3]=5

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[3]=False
   def guard68(self):
      return (((self.p_INT_used[3]) or (self.p_INT[3] == None)))
   def act69(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[3]=6

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[3]=False
   def guard69(self):
      return (((self.p_INT_used[3]) or (self.p_INT[3] == None)))
   def act70(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[3]=7

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[3]=False
   def guard70(self):
      return (((self.p_INT_used[3]) or (self.p_INT[3] == None)))
   def act71(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[3]=8

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[3]=False
   def guard71(self):
      return (((self.p_INT_used[3]) or (self.p_INT[3] == None)))
   def act72(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[3]=9

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[3]=False
   def guard72(self):
      return (((self.p_INT_used[3]) or (self.p_INT[3] == None)))
   def act73(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[3]=10

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[3]=False
   def guard73(self):
      return (((self.p_INT_used[3]) or (self.p_INT[3] == None)))
   def act74(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[3]=11

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[3]=False
   def guard74(self):
      return (((self.p_INT_used[3]) or (self.p_INT[3] == None)))
   def act75(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[3]=12

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[3]=False
   def guard75(self):
      return (((self.p_INT_used[3]) or (self.p_INT[3] == None)))
   def act76(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[3]=13

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[3]=False
   def guard76(self):
      return (((self.p_INT_used[3]) or (self.p_INT[3] == None)))
   def act77(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[3]=14

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[3]=False
   def guard77(self):
      return (((self.p_INT_used[3]) or (self.p_INT[3] == None)))
   def act78(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[3]=15

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[3]=False
   def guard78(self):
      return (((self.p_INT_used[3]) or (self.p_INT[3] == None)))
   def act79(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[3]=16

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[3]=False
   def guard79(self):
      return (((self.p_INT_used[3]) or (self.p_INT[3] == None)))
   def act80(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[3]=17

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[3]=False
   def guard80(self):
      return (((self.p_INT_used[3]) or (self.p_INT[3] == None)))
   def act81(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[3]=18

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[3]=False
   def guard81(self):
      return (((self.p_INT_used[3]) or (self.p_INT[3] == None)))
   def act82(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[3]=19

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[3]=False
   def guard82(self):
      return (((self.p_INT_used[3]) or (self.p_INT[3] == None)))
   def act83(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_INT[3]=20

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_INT_used[3]=False
   def guard83(self):
      return (((self.p_INT_used[3]) or (self.p_INT[3] == None)))
   def act84(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[0]=0

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[0]=False
   def guard84(self):
      return (((self.p_SINT_used[0]) or (self.p_SINT[0] == None)))
   def act85(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[0]=1

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[0]=False
   def guard85(self):
      return (((self.p_SINT_used[0]) or (self.p_SINT[0] == None)))
   def act86(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[0]=2

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[0]=False
   def guard86(self):
      return (((self.p_SINT_used[0]) or (self.p_SINT[0] == None)))
   def act87(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[0]=3

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[0]=False
   def guard87(self):
      return (((self.p_SINT_used[0]) or (self.p_SINT[0] == None)))
   def act88(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[0]=4

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[0]=False
   def guard88(self):
      return (((self.p_SINT_used[0]) or (self.p_SINT[0] == None)))
   def act89(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[0]=5

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[0]=False
   def guard89(self):
      return (((self.p_SINT_used[0]) or (self.p_SINT[0] == None)))
   def act90(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[0]=6

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[0]=False
   def guard90(self):
      return (((self.p_SINT_used[0]) or (self.p_SINT[0] == None)))
   def act91(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[0]=7

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[0]=False
   def guard91(self):
      return (((self.p_SINT_used[0]) or (self.p_SINT[0] == None)))
   def act92(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[0]=8

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[0]=False
   def guard92(self):
      return (((self.p_SINT_used[0]) or (self.p_SINT[0] == None)))
   def act93(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[0]=9

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[0]=False
   def guard93(self):
      return (((self.p_SINT_used[0]) or (self.p_SINT[0] == None)))
   def act94(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[0]=10

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[0]=False
   def guard94(self):
      return (((self.p_SINT_used[0]) or (self.p_SINT[0] == None)))
   def act95(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[1]=0

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[1]=False
   def guard95(self):
      return (((self.p_SINT_used[1]) or (self.p_SINT[1] == None)))
   def act96(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[1]=1

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[1]=False
   def guard96(self):
      return (((self.p_SINT_used[1]) or (self.p_SINT[1] == None)))
   def act97(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[1]=2

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[1]=False
   def guard97(self):
      return (((self.p_SINT_used[1]) or (self.p_SINT[1] == None)))
   def act98(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[1]=3

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[1]=False
   def guard98(self):
      return (((self.p_SINT_used[1]) or (self.p_SINT[1] == None)))
   def act99(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[1]=4

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[1]=False
   def guard99(self):
      return (((self.p_SINT_used[1]) or (self.p_SINT[1] == None)))
   def act100(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[1]=5

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[1]=False
   def guard100(self):
      return (((self.p_SINT_used[1]) or (self.p_SINT[1] == None)))
   def act101(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[1]=6

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[1]=False
   def guard101(self):
      return (((self.p_SINT_used[1]) or (self.p_SINT[1] == None)))
   def act102(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[1]=7

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[1]=False
   def guard102(self):
      return (((self.p_SINT_used[1]) or (self.p_SINT[1] == None)))
   def act103(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[1]=8

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[1]=False
   def guard103(self):
      return (((self.p_SINT_used[1]) or (self.p_SINT[1] == None)))
   def act104(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[1]=9

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[1]=False
   def guard104(self):
      return (((self.p_SINT_used[1]) or (self.p_SINT[1] == None)))
   def act105(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[1]=10

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[1]=False
   def guard105(self):
      return (((self.p_SINT_used[1]) or (self.p_SINT[1] == None)))
   def act106(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[2]=0

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[2]=False
   def guard106(self):
      return (((self.p_SINT_used[2]) or (self.p_SINT[2] == None)))
   def act107(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[2]=1

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[2]=False
   def guard107(self):
      return (((self.p_SINT_used[2]) or (self.p_SINT[2] == None)))
   def act108(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[2]=2

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[2]=False
   def guard108(self):
      return (((self.p_SINT_used[2]) or (self.p_SINT[2] == None)))
   def act109(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[2]=3

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[2]=False
   def guard109(self):
      return (((self.p_SINT_used[2]) or (self.p_SINT[2] == None)))
   def act110(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[2]=4

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[2]=False
   def guard110(self):
      return (((self.p_SINT_used[2]) or (self.p_SINT[2] == None)))
   def act111(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[2]=5

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[2]=False
   def guard111(self):
      return (((self.p_SINT_used[2]) or (self.p_SINT[2] == None)))
   def act112(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[2]=6

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[2]=False
   def guard112(self):
      return (((self.p_SINT_used[2]) or (self.p_SINT[2] == None)))
   def act113(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[2]=7

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[2]=False
   def guard113(self):
      return (((self.p_SINT_used[2]) or (self.p_SINT[2] == None)))
   def act114(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[2]=8

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[2]=False
   def guard114(self):
      return (((self.p_SINT_used[2]) or (self.p_SINT[2] == None)))
   def act115(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[2]=9

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[2]=False
   def guard115(self):
      return (((self.p_SINT_used[2]) or (self.p_SINT[2] == None)))
   def act116(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[2]=10

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[2]=False
   def guard116(self):
      return (((self.p_SINT_used[2]) or (self.p_SINT[2] == None)))
   def act117(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[3]=0

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[3]=False
   def guard117(self):
      return (((self.p_SINT_used[3]) or (self.p_SINT[3] == None)))
   def act118(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[3]=1

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[3]=False
   def guard118(self):
      return (((self.p_SINT_used[3]) or (self.p_SINT[3] == None)))
   def act119(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[3]=2

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[3]=False
   def guard119(self):
      return (((self.p_SINT_used[3]) or (self.p_SINT[3] == None)))
   def act120(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[3]=3

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[3]=False
   def guard120(self):
      return (((self.p_SINT_used[3]) or (self.p_SINT[3] == None)))
   def act121(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[3]=4

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[3]=False
   def guard121(self):
      return (((self.p_SINT_used[3]) or (self.p_SINT[3] == None)))
   def act122(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[3]=5

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[3]=False
   def guard122(self):
      return (((self.p_SINT_used[3]) or (self.p_SINT[3] == None)))
   def act123(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[3]=6

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[3]=False
   def guard123(self):
      return (((self.p_SINT_used[3]) or (self.p_SINT[3] == None)))
   def act124(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[3]=7

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[3]=False
   def guard124(self):
      return (((self.p_SINT_used[3]) or (self.p_SINT[3] == None)))
   def act125(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[3]=8

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[3]=False
   def guard125(self):
      return (((self.p_SINT_used[3]) or (self.p_SINT[3] == None)))
   def act126(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[3]=9

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[3]=False
   def guard126(self):
      return (((self.p_SINT_used[3]) or (self.p_SINT[3] == None)))
   def act127(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_SINT[3]=10

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_SINT_used[3]=False
   def guard127(self):
      return (((self.p_SINT_used[3]) or (self.p_SINT[3] == None)))
   def act128(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[0]=0

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[0]=False
   def guard128(self):
      return (((self.p_CARDS_used[0]) or (self.p_CARDS[0] == None)))
   def act129(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[0]=1

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[0]=False
   def guard129(self):
      return (((self.p_CARDS_used[0]) or (self.p_CARDS[0] == None)))
   def act130(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[0]=2

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[0]=False
   def guard130(self):
      return (((self.p_CARDS_used[0]) or (self.p_CARDS[0] == None)))
   def act131(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[0]=3

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[0]=False
   def guard131(self):
      return (((self.p_CARDS_used[0]) or (self.p_CARDS[0] == None)))
   def act132(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[0]=4

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[0]=False
   def guard132(self):
      return (((self.p_CARDS_used[0]) or (self.p_CARDS[0] == None)))
   def act133(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[0]=5

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[0]=False
   def guard133(self):
      return (((self.p_CARDS_used[0]) or (self.p_CARDS[0] == None)))
   def act134(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[0]=6

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[0]=False
   def guard134(self):
      return (((self.p_CARDS_used[0]) or (self.p_CARDS[0] == None)))
   def act135(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[0]=7

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[0]=False
   def guard135(self):
      return (((self.p_CARDS_used[0]) or (self.p_CARDS[0] == None)))
   def act136(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[0]=8

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[0]=False
   def guard136(self):
      return (((self.p_CARDS_used[0]) or (self.p_CARDS[0] == None)))
   def act137(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[0]=9

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[0]=False
   def guard137(self):
      return (((self.p_CARDS_used[0]) or (self.p_CARDS[0] == None)))
   def act138(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[0]=10

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[0]=False
   def guard138(self):
      return (((self.p_CARDS_used[0]) or (self.p_CARDS[0] == None)))
   def act139(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[0]=11

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[0]=False
   def guard139(self):
      return (((self.p_CARDS_used[0]) or (self.p_CARDS[0] == None)))
   def act140(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[0]=12

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[0]=False
   def guard140(self):
      return (((self.p_CARDS_used[0]) or (self.p_CARDS[0] == None)))
   def act141(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[0]=13

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[0]=False
   def guard141(self):
      return (((self.p_CARDS_used[0]) or (self.p_CARDS[0] == None)))
   def act142(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[0]=14

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[0]=False
   def guard142(self):
      return (((self.p_CARDS_used[0]) or (self.p_CARDS[0] == None)))
   def act143(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[0]=15

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[0]=False
   def guard143(self):
      return (((self.p_CARDS_used[0]) or (self.p_CARDS[0] == None)))
   def act144(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[0]=16

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[0]=False
   def guard144(self):
      return (((self.p_CARDS_used[0]) or (self.p_CARDS[0] == None)))
   def act145(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[1]=0

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[1]=False
   def guard145(self):
      return (((self.p_CARDS_used[1]) or (self.p_CARDS[1] == None)))
   def act146(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[1]=1

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[1]=False
   def guard146(self):
      return (((self.p_CARDS_used[1]) or (self.p_CARDS[1] == None)))
   def act147(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[1]=2

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[1]=False
   def guard147(self):
      return (((self.p_CARDS_used[1]) or (self.p_CARDS[1] == None)))
   def act148(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[1]=3

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[1]=False
   def guard148(self):
      return (((self.p_CARDS_used[1]) or (self.p_CARDS[1] == None)))
   def act149(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[1]=4

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[1]=False
   def guard149(self):
      return (((self.p_CARDS_used[1]) or (self.p_CARDS[1] == None)))
   def act150(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[1]=5

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[1]=False
   def guard150(self):
      return (((self.p_CARDS_used[1]) or (self.p_CARDS[1] == None)))
   def act151(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[1]=6

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[1]=False
   def guard151(self):
      return (((self.p_CARDS_used[1]) or (self.p_CARDS[1] == None)))
   def act152(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[1]=7

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[1]=False
   def guard152(self):
      return (((self.p_CARDS_used[1]) or (self.p_CARDS[1] == None)))
   def act153(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[1]=8

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[1]=False
   def guard153(self):
      return (((self.p_CARDS_used[1]) or (self.p_CARDS[1] == None)))
   def act154(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[1]=9

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[1]=False
   def guard154(self):
      return (((self.p_CARDS_used[1]) or (self.p_CARDS[1] == None)))
   def act155(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[1]=10

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[1]=False
   def guard155(self):
      return (((self.p_CARDS_used[1]) or (self.p_CARDS[1] == None)))
   def act156(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[1]=11

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[1]=False
   def guard156(self):
      return (((self.p_CARDS_used[1]) or (self.p_CARDS[1] == None)))
   def act157(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[1]=12

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[1]=False
   def guard157(self):
      return (((self.p_CARDS_used[1]) or (self.p_CARDS[1] == None)))
   def act158(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[1]=13

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[1]=False
   def guard158(self):
      return (((self.p_CARDS_used[1]) or (self.p_CARDS[1] == None)))
   def act159(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[1]=14

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[1]=False
   def guard159(self):
      return (((self.p_CARDS_used[1]) or (self.p_CARDS[1] == None)))
   def act160(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[1]=15

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[1]=False
   def guard160(self):
      return (((self.p_CARDS_used[1]) or (self.p_CARDS[1] == None)))
   def act161(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[1]=16

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[1]=False
   def guard161(self):
      return (((self.p_CARDS_used[1]) or (self.p_CARDS[1] == None)))
   def act162(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[2]=0

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[2]=False
   def guard162(self):
      return (((self.p_CARDS_used[2]) or (self.p_CARDS[2] == None)))
   def act163(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[2]=1

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[2]=False
   def guard163(self):
      return (((self.p_CARDS_used[2]) or (self.p_CARDS[2] == None)))
   def act164(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[2]=2

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[2]=False
   def guard164(self):
      return (((self.p_CARDS_used[2]) or (self.p_CARDS[2] == None)))
   def act165(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[2]=3

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[2]=False
   def guard165(self):
      return (((self.p_CARDS_used[2]) or (self.p_CARDS[2] == None)))
   def act166(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[2]=4

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[2]=False
   def guard166(self):
      return (((self.p_CARDS_used[2]) or (self.p_CARDS[2] == None)))
   def act167(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[2]=5

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[2]=False
   def guard167(self):
      return (((self.p_CARDS_used[2]) or (self.p_CARDS[2] == None)))
   def act168(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[2]=6

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[2]=False
   def guard168(self):
      return (((self.p_CARDS_used[2]) or (self.p_CARDS[2] == None)))
   def act169(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[2]=7

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[2]=False
   def guard169(self):
      return (((self.p_CARDS_used[2]) or (self.p_CARDS[2] == None)))
   def act170(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[2]=8

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[2]=False
   def guard170(self):
      return (((self.p_CARDS_used[2]) or (self.p_CARDS[2] == None)))
   def act171(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[2]=9

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[2]=False
   def guard171(self):
      return (((self.p_CARDS_used[2]) or (self.p_CARDS[2] == None)))
   def act172(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[2]=10

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[2]=False
   def guard172(self):
      return (((self.p_CARDS_used[2]) or (self.p_CARDS[2] == None)))
   def act173(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[2]=11

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[2]=False
   def guard173(self):
      return (((self.p_CARDS_used[2]) or (self.p_CARDS[2] == None)))
   def act174(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[2]=12

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[2]=False
   def guard174(self):
      return (((self.p_CARDS_used[2]) or (self.p_CARDS[2] == None)))
   def act175(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[2]=13

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[2]=False
   def guard175(self):
      return (((self.p_CARDS_used[2]) or (self.p_CARDS[2] == None)))
   def act176(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[2]=14

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[2]=False
   def guard176(self):
      return (((self.p_CARDS_used[2]) or (self.p_CARDS[2] == None)))
   def act177(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[2]=15

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[2]=False
   def guard177(self):
      return (((self.p_CARDS_used[2]) or (self.p_CARDS[2] == None)))
   def act178(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[2]=16

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[2]=False
   def guard178(self):
      return (((self.p_CARDS_used[2]) or (self.p_CARDS[2] == None)))
   def act179(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[3]=0

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[3]=False
   def guard179(self):
      return (((self.p_CARDS_used[3]) or (self.p_CARDS[3] == None)))
   def act180(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[3]=1

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[3]=False
   def guard180(self):
      return (((self.p_CARDS_used[3]) or (self.p_CARDS[3] == None)))
   def act181(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[3]=2

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[3]=False
   def guard181(self):
      return (((self.p_CARDS_used[3]) or (self.p_CARDS[3] == None)))
   def act182(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[3]=3

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[3]=False
   def guard182(self):
      return (((self.p_CARDS_used[3]) or (self.p_CARDS[3] == None)))
   def act183(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[3]=4

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[3]=False
   def guard183(self):
      return (((self.p_CARDS_used[3]) or (self.p_CARDS[3] == None)))
   def act184(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[3]=5

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[3]=False
   def guard184(self):
      return (((self.p_CARDS_used[3]) or (self.p_CARDS[3] == None)))
   def act185(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[3]=6

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[3]=False
   def guard185(self):
      return (((self.p_CARDS_used[3]) or (self.p_CARDS[3] == None)))
   def act186(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[3]=7

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[3]=False
   def guard186(self):
      return (((self.p_CARDS_used[3]) or (self.p_CARDS[3] == None)))
   def act187(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[3]=8

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[3]=False
   def guard187(self):
      return (((self.p_CARDS_used[3]) or (self.p_CARDS[3] == None)))
   def act188(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[3]=9

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[3]=False
   def guard188(self):
      return (((self.p_CARDS_used[3]) or (self.p_CARDS[3] == None)))
   def act189(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[3]=10

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[3]=False
   def guard189(self):
      return (((self.p_CARDS_used[3]) or (self.p_CARDS[3] == None)))
   def act190(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[3]=11

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[3]=False
   def guard190(self):
      return (((self.p_CARDS_used[3]) or (self.p_CARDS[3] == None)))
   def act191(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[3]=12

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[3]=False
   def guard191(self):
      return (((self.p_CARDS_used[3]) or (self.p_CARDS[3] == None)))
   def act192(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[3]=13

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[3]=False
   def guard192(self):
      return (((self.p_CARDS_used[3]) or (self.p_CARDS[3] == None)))
   def act193(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[3]=14

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[3]=False
   def guard193(self):
      return (((self.p_CARDS_used[3]) or (self.p_CARDS[3] == None)))
   def act194(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[3]=15

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[3]=False
   def guard194(self):
      return (((self.p_CARDS_used[3]) or (self.p_CARDS[3] == None)))
   def act195(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_CARDS[3]=16

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_CARDS_used[3]=False
   def guard195(self):
      return (((self.p_CARDS_used[3]) or (self.p_CARDS[3] == None)))
   def act196(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_PNUM[0]=2

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_PNUM_used[0]=False
   def guard196(self):
      return (((self.p_PNUM_used[0]) or (self.p_PNUM[0] == None)))
   def act197(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_PNUM[0]=3

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_PNUM_used[0]=False
   def guard197(self):
      return (((self.p_PNUM_used[0]) or (self.p_PNUM[0] == None)))
   def act198(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_PNUM[0]=4

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_PNUM_used[0]=False
   def guard198(self):
      return (((self.p_PNUM_used[0]) or (self.p_PNUM[0] == None)))
   def act199(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_PNUM[1]=2

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_PNUM_used[1]=False
   def guard199(self):
      return (((self.p_PNUM_used[1]) or (self.p_PNUM[1] == None)))
   def act200(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_PNUM[1]=3

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_PNUM_used[1]=False
   def guard200(self):
      return (((self.p_PNUM_used[1]) or (self.p_PNUM[1] == None)))
   def act201(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_PNUM[1]=4

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_PNUM_used[1]=False
   def guard201(self):
      return (((self.p_PNUM_used[1]) or (self.p_PNUM[1] == None)))
   def act202(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_PNUM[2]=2

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_PNUM_used[2]=False
   def guard202(self):
      return (((self.p_PNUM_used[2]) or (self.p_PNUM[2] == None)))
   def act203(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_PNUM[2]=3

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_PNUM_used[2]=False
   def guard203(self):
      return (((self.p_PNUM_used[2]) or (self.p_PNUM[2] == None)))
   def act204(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_PNUM[2]=4

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_PNUM_used[2]=False
   def guard204(self):
      return (((self.p_PNUM_used[2]) or (self.p_PNUM[2] == None)))
   def act205(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_PNUM[3]=2

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_PNUM_used[3]=False
   def guard205(self):
      return (((self.p_PNUM_used[3]) or (self.p_PNUM[3] == None)))
   def act206(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_PNUM[3]=3

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_PNUM_used[3]=False
   def guard206(self):
      return (((self.p_PNUM_used[3]) or (self.p_PNUM[3] == None)))
   def act207(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_PNUM[3]=4

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_PNUM_used[3]=False
   def guard207(self):
      return (((self.p_PNUM_used[3]) or (self.p_PNUM[3] == None)))
   def act208(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[0], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_DOM_REF[0]=dominion2.initializeGame(self.p_PNUM[0], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[0])

      self.p_INT_used[0]=True
      self.p_DOM_used[0]=False
      self.p_PNUM_used[0]=True
   def guard208(self):
      return (self.p_INT[0] != None) and (((self.p_DOM_used[0]) or (self.p_DOM[0] == None))) and (self.p_PNUM[0] != None)
   def act209(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[0], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_DOM_REF[0]=dominion2.initializeGame(self.p_PNUM[0], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[1])

      self.p_INT_used[1]=True
      self.p_DOM_used[0]=False
      self.p_PNUM_used[0]=True
   def guard209(self):
      return (self.p_INT[1] != None) and (((self.p_DOM_used[0]) or (self.p_DOM[0] == None))) and (self.p_PNUM[0] != None)
   def act210(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[0], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[2])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_DOM_REF[0]=dominion2.initializeGame(self.p_PNUM[0], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[2])

      self.p_INT_used[2]=True
      self.p_DOM_used[0]=False
      self.p_PNUM_used[0]=True
   def guard210(self):
      return (self.p_INT[2] != None) and (((self.p_DOM_used[0]) or (self.p_DOM[0] == None))) and (self.p_PNUM[0] != None)
   def act211(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[0], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[3])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_DOM_REF[0]=dominion2.initializeGame(self.p_PNUM[0], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[3])

      self.p_INT_used[3]=True
      self.p_DOM_used[0]=False
      self.p_PNUM_used[0]=True
   def guard211(self):
      return (self.p_INT[3] != None) and (((self.p_DOM_used[0]) or (self.p_DOM[0] == None))) and (self.p_PNUM[0] != None)
   def act212(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[1], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_DOM_REF[0]=dominion2.initializeGame(self.p_PNUM[1], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[0])

      self.p_INT_used[0]=True
      self.p_DOM_used[0]=False
      self.p_PNUM_used[1]=True
   def guard212(self):
      return (self.p_INT[0] != None) and (((self.p_DOM_used[0]) or (self.p_DOM[0] == None))) and (self.p_PNUM[1] != None)
   def act213(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[1], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_DOM_REF[0]=dominion2.initializeGame(self.p_PNUM[1], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[1])

      self.p_INT_used[1]=True
      self.p_DOM_used[0]=False
      self.p_PNUM_used[1]=True
   def guard213(self):
      return (self.p_INT[1] != None) and (((self.p_DOM_used[0]) or (self.p_DOM[0] == None))) and (self.p_PNUM[1] != None)
   def act214(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[1], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[2])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_DOM_REF[0]=dominion2.initializeGame(self.p_PNUM[1], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[2])

      self.p_INT_used[2]=True
      self.p_DOM_used[0]=False
      self.p_PNUM_used[1]=True
   def guard214(self):
      return (self.p_INT[2] != None) and (((self.p_DOM_used[0]) or (self.p_DOM[0] == None))) and (self.p_PNUM[1] != None)
   def act215(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[1], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[3])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_DOM_REF[0]=dominion2.initializeGame(self.p_PNUM[1], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[3])

      self.p_INT_used[3]=True
      self.p_DOM_used[0]=False
      self.p_PNUM_used[1]=True
   def guard215(self):
      return (self.p_INT[3] != None) and (((self.p_DOM_used[0]) or (self.p_DOM[0] == None))) and (self.p_PNUM[1] != None)
   def act216(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[2], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_DOM_REF[0]=dominion2.initializeGame(self.p_PNUM[2], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[0])

      self.p_INT_used[0]=True
      self.p_DOM_used[0]=False
      self.p_PNUM_used[2]=True
   def guard216(self):
      return (self.p_INT[0] != None) and (((self.p_DOM_used[0]) or (self.p_DOM[0] == None))) and (self.p_PNUM[2] != None)
   def act217(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[2], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_DOM_REF[0]=dominion2.initializeGame(self.p_PNUM[2], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[1])

      self.p_INT_used[1]=True
      self.p_DOM_used[0]=False
      self.p_PNUM_used[2]=True
   def guard217(self):
      return (self.p_INT[1] != None) and (((self.p_DOM_used[0]) or (self.p_DOM[0] == None))) and (self.p_PNUM[2] != None)
   def act218(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[2], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[2])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_DOM_REF[0]=dominion2.initializeGame(self.p_PNUM[2], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[2])

      self.p_INT_used[2]=True
      self.p_DOM_used[0]=False
      self.p_PNUM_used[2]=True
   def guard218(self):
      return (self.p_INT[2] != None) and (((self.p_DOM_used[0]) or (self.p_DOM[0] == None))) and (self.p_PNUM[2] != None)
   def act219(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[2], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[3])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_DOM_REF[0]=dominion2.initializeGame(self.p_PNUM[2], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[3])

      self.p_INT_used[3]=True
      self.p_DOM_used[0]=False
      self.p_PNUM_used[2]=True
   def guard219(self):
      return (self.p_INT[3] != None) and (((self.p_DOM_used[0]) or (self.p_DOM[0] == None))) and (self.p_PNUM[2] != None)
   def act220(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[3], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_DOM_REF[0]=dominion2.initializeGame(self.p_PNUM[3], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[0])

      self.p_INT_used[0]=True
      self.p_DOM_used[0]=False
      self.p_PNUM_used[3]=True
   def guard220(self):
      return (self.p_INT[0] != None) and (((self.p_DOM_used[0]) or (self.p_DOM[0] == None))) and (self.p_PNUM[3] != None)
   def act221(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[3], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_DOM_REF[0]=dominion2.initializeGame(self.p_PNUM[3], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[1])

      self.p_INT_used[1]=True
      self.p_DOM_used[0]=False
      self.p_PNUM_used[3]=True
   def guard221(self):
      return (self.p_INT[1] != None) and (((self.p_DOM_used[0]) or (self.p_DOM[0] == None))) and (self.p_PNUM[3] != None)
   def act222(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[3], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[2])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_DOM_REF[0]=dominion2.initializeGame(self.p_PNUM[3], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[2])

      self.p_INT_used[2]=True
      self.p_DOM_used[0]=False
      self.p_PNUM_used[3]=True
   def guard222(self):
      return (self.p_INT[2] != None) and (((self.p_DOM_used[0]) or (self.p_DOM[0] == None))) and (self.p_PNUM[3] != None)
   def act223(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[3], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[3])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_DOM_REF[0]=dominion2.initializeGame(self.p_PNUM[3], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[3])

      self.p_INT_used[3]=True
      self.p_DOM_used[0]=False
      self.p_PNUM_used[3]=True
   def guard223(self):
      return (self.p_INT[3] != None) and (((self.p_DOM_used[0]) or (self.p_DOM[0] == None))) and (self.p_PNUM[3] != None)
   def act224(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[0], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_DOM_REF[1]=dominion2.initializeGame(self.p_PNUM[0], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[0])

      self.p_INT_used[0]=True
      self.p_DOM_used[1]=False
      self.p_PNUM_used[0]=True
   def guard224(self):
      return (self.p_INT[0] != None) and (((self.p_DOM_used[1]) or (self.p_DOM[1] == None))) and (self.p_PNUM[0] != None)
   def act225(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[0], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_DOM_REF[1]=dominion2.initializeGame(self.p_PNUM[0], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[1])

      self.p_INT_used[1]=True
      self.p_DOM_used[1]=False
      self.p_PNUM_used[0]=True
   def guard225(self):
      return (self.p_INT[1] != None) and (((self.p_DOM_used[1]) or (self.p_DOM[1] == None))) and (self.p_PNUM[0] != None)
   def act226(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[0], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[2])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_DOM_REF[1]=dominion2.initializeGame(self.p_PNUM[0], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[2])

      self.p_INT_used[2]=True
      self.p_DOM_used[1]=False
      self.p_PNUM_used[0]=True
   def guard226(self):
      return (self.p_INT[2] != None) and (((self.p_DOM_used[1]) or (self.p_DOM[1] == None))) and (self.p_PNUM[0] != None)
   def act227(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[0], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[3])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_DOM_REF[1]=dominion2.initializeGame(self.p_PNUM[0], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[3])

      self.p_INT_used[3]=True
      self.p_DOM_used[1]=False
      self.p_PNUM_used[0]=True
   def guard227(self):
      return (self.p_INT[3] != None) and (((self.p_DOM_used[1]) or (self.p_DOM[1] == None))) and (self.p_PNUM[0] != None)
   def act228(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[1], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_DOM_REF[1]=dominion2.initializeGame(self.p_PNUM[1], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[0])

      self.p_INT_used[0]=True
      self.p_DOM_used[1]=False
      self.p_PNUM_used[1]=True
   def guard228(self):
      return (self.p_INT[0] != None) and (((self.p_DOM_used[1]) or (self.p_DOM[1] == None))) and (self.p_PNUM[1] != None)
   def act229(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[1], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_DOM_REF[1]=dominion2.initializeGame(self.p_PNUM[1], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[1])

      self.p_INT_used[1]=True
      self.p_DOM_used[1]=False
      self.p_PNUM_used[1]=True
   def guard229(self):
      return (self.p_INT[1] != None) and (((self.p_DOM_used[1]) or (self.p_DOM[1] == None))) and (self.p_PNUM[1] != None)
   def act230(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[1], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[2])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_DOM_REF[1]=dominion2.initializeGame(self.p_PNUM[1], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[2])

      self.p_INT_used[2]=True
      self.p_DOM_used[1]=False
      self.p_PNUM_used[1]=True
   def guard230(self):
      return (self.p_INT[2] != None) and (((self.p_DOM_used[1]) or (self.p_DOM[1] == None))) and (self.p_PNUM[1] != None)
   def act231(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[1], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[3])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_DOM_REF[1]=dominion2.initializeGame(self.p_PNUM[1], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[3])

      self.p_INT_used[3]=True
      self.p_DOM_used[1]=False
      self.p_PNUM_used[1]=True
   def guard231(self):
      return (self.p_INT[3] != None) and (((self.p_DOM_used[1]) or (self.p_DOM[1] == None))) and (self.p_PNUM[1] != None)
   def act232(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[2], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_DOM_REF[1]=dominion2.initializeGame(self.p_PNUM[2], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[0])

      self.p_INT_used[0]=True
      self.p_DOM_used[1]=False
      self.p_PNUM_used[2]=True
   def guard232(self):
      return (self.p_INT[0] != None) and (((self.p_DOM_used[1]) or (self.p_DOM[1] == None))) and (self.p_PNUM[2] != None)
   def act233(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[2], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_DOM_REF[1]=dominion2.initializeGame(self.p_PNUM[2], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[1])

      self.p_INT_used[1]=True
      self.p_DOM_used[1]=False
      self.p_PNUM_used[2]=True
   def guard233(self):
      return (self.p_INT[1] != None) and (((self.p_DOM_used[1]) or (self.p_DOM[1] == None))) and (self.p_PNUM[2] != None)
   def act234(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[2], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[2])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_DOM_REF[1]=dominion2.initializeGame(self.p_PNUM[2], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[2])

      self.p_INT_used[2]=True
      self.p_DOM_used[1]=False
      self.p_PNUM_used[2]=True
   def guard234(self):
      return (self.p_INT[2] != None) and (((self.p_DOM_used[1]) or (self.p_DOM[1] == None))) and (self.p_PNUM[2] != None)
   def act235(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[2], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[3])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_DOM_REF[1]=dominion2.initializeGame(self.p_PNUM[2], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[3])

      self.p_INT_used[3]=True
      self.p_DOM_used[1]=False
      self.p_PNUM_used[2]=True
   def guard235(self):
      return (self.p_INT[3] != None) and (((self.p_DOM_used[1]) or (self.p_DOM[1] == None))) and (self.p_PNUM[2] != None)
   def act236(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[3], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_DOM_REF[1]=dominion2.initializeGame(self.p_PNUM[3], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[0])

      self.p_INT_used[0]=True
      self.p_DOM_used[1]=False
      self.p_PNUM_used[3]=True
   def guard236(self):
      return (self.p_INT[0] != None) and (((self.p_DOM_used[1]) or (self.p_DOM[1] == None))) and (self.p_PNUM[3] != None)
   def act237(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[3], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_DOM_REF[1]=dominion2.initializeGame(self.p_PNUM[3], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[1])

      self.p_INT_used[1]=True
      self.p_DOM_used[1]=False
      self.p_PNUM_used[3]=True
   def guard237(self):
      return (self.p_INT[1] != None) and (((self.p_DOM_used[1]) or (self.p_DOM[1] == None))) and (self.p_PNUM[3] != None)
   def act238(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[3], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[2])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_DOM_REF[1]=dominion2.initializeGame(self.p_PNUM[3], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[2])

      self.p_INT_used[2]=True
      self.p_DOM_used[1]=False
      self.p_PNUM_used[3]=True
   def guard238(self):
      return (self.p_INT[2] != None) and (((self.p_DOM_used[1]) or (self.p_DOM[1] == None))) and (self.p_PNUM[3] != None)
   def act239(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[3], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[3])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      self.p_DOM_REF[1]=dominion2.initializeGame(self.p_PNUM[3], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[3])

      self.p_INT_used[3]=True
      self.p_DOM_used[1]=False
      self.p_PNUM_used[3]=True
   def guard239(self):
      return (self.p_INT[3] != None) and (((self.p_DOM_used[1]) or (self.p_DOM[1] == None))) and (self.p_PNUM[3] != None)
   def act240(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.buyCard(self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.buyCard(self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
   def guard240(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None)
   def act241(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.buyCard(self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.buyCard(self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
   def guard241(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None)
   def act242(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.buyCard(self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.buyCard(self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
   def guard242(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None)
   def act243(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.buyCard(self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.buyCard(self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
   def guard243(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None)
   def act244(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.buyCard(self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.buyCard(self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
   def guard244(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None)
   def act245(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.buyCard(self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.buyCard(self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
   def guard245(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None)
   def act246(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.buyCard(self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.buyCard(self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
   def guard246(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None)
   def act247(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.buyCard(self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.buyCard(self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
   def guard247(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None)
   def act248(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.endTurn(self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.endTurn(self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
   def guard248(self):
      return (self.p_DOM[0] != None)
   def act249(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.endTurn(self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.endTurn(self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
   def guard249(self):
      return (self.p_DOM[1] != None)
   def act250(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.isGameOver(self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.isGameOver(self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
   def guard250(self):
      return (self.p_DOM[0] != None)
   def act251(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.isGameOver(self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.isGameOver(self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
   def guard251(self):
      return (self.p_DOM[1] != None)
   def act252(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.whoseTurn(self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.whoseTurn(self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
   def guard252(self):
      return (self.p_DOM[0] != None)
   def act253(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.whoseTurn(self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.whoseTurn(self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
   def guard253(self):
      return (self.p_DOM[1] != None)
   def act254(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.scoreFor(self.p_PNUM[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.scoreFor(self.p_PNUM[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_PNUM_used[0]=True
   def guard254(self):
      return (self.p_DOM[0] != None) and (self.p_PNUM[0] != None)
   def act255(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.scoreFor(self.p_PNUM[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.scoreFor(self.p_PNUM[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_PNUM_used[0]=True
   def guard255(self):
      return (self.p_DOM[1] != None) and (self.p_PNUM[0] != None)
   def act256(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.scoreFor(self.p_PNUM[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.scoreFor(self.p_PNUM[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_PNUM_used[1]=True
   def guard256(self):
      return (self.p_DOM[0] != None) and (self.p_PNUM[1] != None)
   def act257(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.scoreFor(self.p_PNUM[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.scoreFor(self.p_PNUM[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_PNUM_used[1]=True
   def guard257(self):
      return (self.p_DOM[1] != None) and (self.p_PNUM[1] != None)
   def act258(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.scoreFor(self.p_PNUM[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.scoreFor(self.p_PNUM[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_PNUM_used[2]=True
   def guard258(self):
      return (self.p_DOM[0] != None) and (self.p_PNUM[2] != None)
   def act259(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.scoreFor(self.p_PNUM[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.scoreFor(self.p_PNUM[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_PNUM_used[2]=True
   def guard259(self):
      return (self.p_DOM[1] != None) and (self.p_PNUM[2] != None)
   def act260(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.scoreFor(self.p_PNUM[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.scoreFor(self.p_PNUM[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_PNUM_used[3]=True
   def guard260(self):
      return (self.p_DOM[0] != None) and (self.p_PNUM[3] != None)
   def act261(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.scoreFor(self.p_PNUM[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.scoreFor(self.p_PNUM[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_PNUM_used[3]=True
   def guard261(self):
      return (self.p_DOM[1] != None) and (self.p_PNUM[3] != None)
   def act262(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[0]=True
   def guard262(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[0] != None)
   def act263(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[0]=True
   def guard263(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[0] != None)
   def act264(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[0]=True
   def guard264(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[0] != None)
   def act265(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[0]=True
   def guard265(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[0] != None)
   def act266(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[0]=True
   def guard266(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[0] != None)
   def act267(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[0]=True
   def guard267(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[0] != None)
   def act268(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[0]=True
   def guard268(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[0] != None)
   def act269(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[0]=True
   def guard269(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[0] != None)
   def act270(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[0]=True
   def guard270(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[0] != None)
   def act271(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[0]=True
   def guard271(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[0] != None)
   def act272(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[0]=True
   def guard272(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[0] != None)
   def act273(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[0]=True
   def guard273(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[0] != None)
   def act274(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[0]=True
   def guard274(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[0] != None)
   def act275(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[0]=True
   def guard275(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[0] != None)
   def act276(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[0]=True
   def guard276(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[0] != None)
   def act277(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[0]=True
   def guard277(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[0] != None)
   def act278(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[0]=True
   def guard278(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[0] != None)
   def act279(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[0]=True
   def guard279(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[0] != None)
   def act280(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[0]=True
   def guard280(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[0] != None)
   def act281(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[0]=True
   def guard281(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[0] != None)
   def act282(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[0]=True
   def guard282(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[0] != None)
   def act283(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[0]=True
   def guard283(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[0] != None)
   def act284(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[0]=True
   def guard284(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[0] != None)
   def act285(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[0]=True
   def guard285(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[0] != None)
   def act286(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[0]=True
   def guard286(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[0] != None)
   def act287(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[0]=True
   def guard287(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[0] != None)
   def act288(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[0]=True
   def guard288(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[0] != None)
   def act289(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[0]=True
   def guard289(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[0] != None)
   def act290(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[0]=True
   def guard290(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[0] != None)
   def act291(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[0]=True
   def guard291(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[0] != None)
   def act292(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[0]=True
   def guard292(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[0] != None)
   def act293(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[0]=True
   def guard293(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[0] != None)
   def act294(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[0]=True
   def guard294(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[0] != None)
   def act295(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[0]=True
   def guard295(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[0] != None)
   def act296(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[0]=True
   def guard296(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[0] != None)
   def act297(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[0]=True
   def guard297(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[0] != None)
   def act298(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[0]=True
   def guard298(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[0] != None)
   def act299(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[0]=True
   def guard299(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[0] != None)
   def act300(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[0]=True
   def guard300(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[0] != None)
   def act301(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[0]=True
   def guard301(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[0] != None)
   def act302(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[0]=True
   def guard302(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[0] != None)
   def act303(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[0]=True
   def guard303(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[0] != None)
   def act304(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[0]=True
   def guard304(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[0] != None)
   def act305(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[0]=True
   def guard305(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[0] != None)
   def act306(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[0]=True
   def guard306(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[0] != None)
   def act307(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[0]=True
   def guard307(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[0] != None)
   def act308(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[0]=True
   def guard308(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[0] != None)
   def act309(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[0]=True
   def guard309(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[0] != None)
   def act310(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[0]=True
   def guard310(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[0] != None)
   def act311(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[0]=True
   def guard311(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[0] != None)
   def act312(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[0]=True
   def guard312(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[0] != None)
   def act313(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[0]=True
   def guard313(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[0] != None)
   def act314(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[0]=True
   def guard314(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[0] != None)
   def act315(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[0]=True
   def guard315(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[0] != None)
   def act316(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[0]=True
   def guard316(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[0] != None)
   def act317(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[0]=True
   def guard317(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[0] != None)
   def act318(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[0]=True
   def guard318(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[0] != None)
   def act319(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[0]=True
   def guard319(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[0] != None)
   def act320(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[0]=True
   def guard320(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[0] != None)
   def act321(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[0]=True
   def guard321(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[0] != None)
   def act322(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[0]=True
   def guard322(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[0] != None)
   def act323(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[0]=True
   def guard323(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[0] != None)
   def act324(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[0]=True
   def guard324(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[0] != None)
   def act325(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[0]=True
   def guard325(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[0] != None)
   def act326(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[0]=True
   def guard326(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[0] != None)
   def act327(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[0]=True
   def guard327(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[0] != None)
   def act328(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[0]=True
   def guard328(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[0] != None)
   def act329(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[0]=True
   def guard329(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[0] != None)
   def act330(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[0]=True
   def guard330(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[0] != None)
   def act331(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[0]=True
   def guard331(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[0] != None)
   def act332(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[0]=True
   def guard332(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[0] != None)
   def act333(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[0]=True
   def guard333(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[0] != None)
   def act334(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[0]=True
   def guard334(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[0] != None)
   def act335(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[0]=True
   def guard335(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[0] != None)
   def act336(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[0]=True
   def guard336(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[0] != None)
   def act337(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[0]=True
   def guard337(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[0] != None)
   def act338(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[0]=True
   def guard338(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[0] != None)
   def act339(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[0]=True
   def guard339(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[0] != None)
   def act340(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[0]=True
   def guard340(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[0] != None)
   def act341(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[0]=True
   def guard341(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[0] != None)
   def act342(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[0]=True
   def guard342(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[0] != None)
   def act343(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[0]=True
   def guard343(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[0] != None)
   def act344(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[0]=True
   def guard344(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[0] != None)
   def act345(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[0]=True
   def guard345(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[0] != None)
   def act346(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[0]=True
   def guard346(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[0] != None)
   def act347(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[0]=True
   def guard347(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[0] != None)
   def act348(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[0]=True
   def guard348(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[0] != None)
   def act349(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[0]=True
   def guard349(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[0] != None)
   def act350(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[0]=True
   def guard350(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[0] != None)
   def act351(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[0]=True
   def guard351(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[0] != None)
   def act352(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[0]=True
   def guard352(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[0] != None)
   def act353(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[0]=True
   def guard353(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[0] != None)
   def act354(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[0]=True
   def guard354(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[0] != None)
   def act355(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[0]=True
   def guard355(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[0] != None)
   def act356(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[0]=True
   def guard356(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[0] != None)
   def act357(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[0]=True
   def guard357(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[0] != None)
   def act358(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[0]=True
   def guard358(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[0] != None)
   def act359(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[0]=True
   def guard359(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[0] != None)
   def act360(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[0]=True
   def guard360(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[0] != None)
   def act361(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[0]=True
   def guard361(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[0] != None)
   def act362(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[0]=True
   def guard362(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[0] != None)
   def act363(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[0]=True
   def guard363(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[0] != None)
   def act364(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[0]=True
   def guard364(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[0] != None)
   def act365(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[0]=True
   def guard365(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[0] != None)
   def act366(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[0]=True
   def guard366(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[0] != None)
   def act367(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[0]=True
   def guard367(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[0] != None)
   def act368(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[0]=True
   def guard368(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[0] != None)
   def act369(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[0]=True
   def guard369(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[0] != None)
   def act370(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[0]=True
   def guard370(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[0] != None)
   def act371(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[0]=True
   def guard371(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[0] != None)
   def act372(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[0]=True
   def guard372(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[0] != None)
   def act373(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[0]=True
   def guard373(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[0] != None)
   def act374(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[0]=True
   def guard374(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[0] != None)
   def act375(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[0]=True
   def guard375(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[0] != None)
   def act376(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[0]=True
   def guard376(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[0] != None)
   def act377(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[0]=True
   def guard377(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[0] != None)
   def act378(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[0]=True
   def guard378(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[0] != None)
   def act379(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[0]=True
   def guard379(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[0] != None)
   def act380(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[0]=True
   def guard380(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[0] != None)
   def act381(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[0]=True
   def guard381(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[0] != None)
   def act382(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[0]=True
   def guard382(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[0] != None)
   def act383(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[0]=True
   def guard383(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[0] != None)
   def act384(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[0]=True
   def guard384(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[0] != None)
   def act385(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[0]=True
   def guard385(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[0] != None)
   def act386(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[0]=True
   def guard386(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[0] != None)
   def act387(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[0]=True
   def guard387(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[0] != None)
   def act388(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[0]=True
   def guard388(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[0] != None)
   def act389(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[0]=True
   def guard389(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[0] != None)
   def act390(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[1]=True
   def guard390(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[1] != None)
   def act391(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[1]=True
   def guard391(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[1] != None)
   def act392(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[1]=True
   def guard392(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[1] != None)
   def act393(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[1]=True
   def guard393(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[1] != None)
   def act394(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[1]=True
   def guard394(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[1] != None)
   def act395(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[1]=True
   def guard395(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[1] != None)
   def act396(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[1]=True
   def guard396(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[1] != None)
   def act397(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[1]=True
   def guard397(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[1] != None)
   def act398(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[1]=True
   def guard398(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[1] != None)
   def act399(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[1]=True
   def guard399(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[1] != None)
   def act400(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[1]=True
   def guard400(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[1] != None)
   def act401(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[1]=True
   def guard401(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[1] != None)
   def act402(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[1]=True
   def guard402(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[1] != None)
   def act403(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[1]=True
   def guard403(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[1] != None)
   def act404(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[1]=True
   def guard404(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[1] != None)
   def act405(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[1]=True
   def guard405(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[1] != None)
   def act406(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[1]=True
   def guard406(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[1] != None)
   def act407(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[1]=True
   def guard407(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[1] != None)
   def act408(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[1]=True
   def guard408(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[1] != None)
   def act409(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[1]=True
   def guard409(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[1] != None)
   def act410(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[1]=True
   def guard410(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[1] != None)
   def act411(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[1]=True
   def guard411(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[1] != None)
   def act412(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[1]=True
   def guard412(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[1] != None)
   def act413(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[1]=True
   def guard413(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[1] != None)
   def act414(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[1]=True
   def guard414(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[1] != None)
   def act415(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[1]=True
   def guard415(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[1] != None)
   def act416(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[1]=True
   def guard416(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[1] != None)
   def act417(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[1]=True
   def guard417(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[1] != None)
   def act418(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[1]=True
   def guard418(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[1] != None)
   def act419(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[1]=True
   def guard419(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[1] != None)
   def act420(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[1]=True
   def guard420(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[1] != None)
   def act421(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[1]=True
   def guard421(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[1] != None)
   def act422(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[1]=True
   def guard422(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[1] != None)
   def act423(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[1]=True
   def guard423(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[1] != None)
   def act424(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[1]=True
   def guard424(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[1] != None)
   def act425(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[1]=True
   def guard425(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[1] != None)
   def act426(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[1]=True
   def guard426(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[1] != None)
   def act427(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[1]=True
   def guard427(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[1] != None)
   def act428(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[1]=True
   def guard428(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[1] != None)
   def act429(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[1]=True
   def guard429(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[1] != None)
   def act430(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[1]=True
   def guard430(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[1] != None)
   def act431(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[1]=True
   def guard431(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[1] != None)
   def act432(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[1]=True
   def guard432(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[1] != None)
   def act433(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[1]=True
   def guard433(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[1] != None)
   def act434(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[1]=True
   def guard434(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[1] != None)
   def act435(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[1]=True
   def guard435(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[1] != None)
   def act436(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[1]=True
   def guard436(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[1] != None)
   def act437(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[1]=True
   def guard437(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[1] != None)
   def act438(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[1]=True
   def guard438(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[1] != None)
   def act439(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[1]=True
   def guard439(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[1] != None)
   def act440(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[1]=True
   def guard440(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[1] != None)
   def act441(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[1]=True
   def guard441(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[1] != None)
   def act442(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[1]=True
   def guard442(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[1] != None)
   def act443(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[1]=True
   def guard443(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[1] != None)
   def act444(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[1]=True
   def guard444(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[1] != None)
   def act445(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[1]=True
   def guard445(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[1] != None)
   def act446(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[1]=True
   def guard446(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[1] != None)
   def act447(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[1]=True
   def guard447(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[1] != None)
   def act448(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[1]=True
   def guard448(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[1] != None)
   def act449(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[1]=True
   def guard449(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[1] != None)
   def act450(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[1]=True
   def guard450(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[1] != None)
   def act451(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[1]=True
   def guard451(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[1] != None)
   def act452(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[1]=True
   def guard452(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[1] != None)
   def act453(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[1]=True
   def guard453(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[1] != None)
   def act454(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[1]=True
   def guard454(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[1] != None)
   def act455(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[1]=True
   def guard455(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[1] != None)
   def act456(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[1]=True
   def guard456(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[1] != None)
   def act457(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[1]=True
   def guard457(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[1] != None)
   def act458(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[1]=True
   def guard458(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[1] != None)
   def act459(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[1]=True
   def guard459(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[1] != None)
   def act460(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[1]=True
   def guard460(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[1] != None)
   def act461(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[1]=True
   def guard461(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[1] != None)
   def act462(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[1]=True
   def guard462(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[1] != None)
   def act463(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[1]=True
   def guard463(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[1] != None)
   def act464(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[1]=True
   def guard464(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[1] != None)
   def act465(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[1]=True
   def guard465(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[1] != None)
   def act466(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[1]=True
   def guard466(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[1] != None)
   def act467(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[1]=True
   def guard467(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[1] != None)
   def act468(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[1]=True
   def guard468(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[1] != None)
   def act469(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[1]=True
   def guard469(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[1] != None)
   def act470(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[1]=True
   def guard470(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[1] != None)
   def act471(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[1]=True
   def guard471(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[1] != None)
   def act472(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[1]=True
   def guard472(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[1] != None)
   def act473(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[1]=True
   def guard473(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[1] != None)
   def act474(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[1]=True
   def guard474(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[1] != None)
   def act475(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[1]=True
   def guard475(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[1] != None)
   def act476(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[1]=True
   def guard476(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[1] != None)
   def act477(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[1]=True
   def guard477(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[1] != None)
   def act478(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[1]=True
   def guard478(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[1] != None)
   def act479(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[1]=True
   def guard479(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[1] != None)
   def act480(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[1]=True
   def guard480(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[1] != None)
   def act481(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[1]=True
   def guard481(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[1] != None)
   def act482(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[1]=True
   def guard482(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[1] != None)
   def act483(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[1]=True
   def guard483(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[1] != None)
   def act484(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[1]=True
   def guard484(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[1] != None)
   def act485(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[1]=True
   def guard485(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[1] != None)
   def act486(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[1]=True
   def guard486(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[1] != None)
   def act487(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[1]=True
   def guard487(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[1] != None)
   def act488(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[1]=True
   def guard488(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[1] != None)
   def act489(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[1]=True
   def guard489(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[1] != None)
   def act490(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[1]=True
   def guard490(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[1] != None)
   def act491(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[1]=True
   def guard491(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[1] != None)
   def act492(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[1]=True
   def guard492(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[1] != None)
   def act493(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[1]=True
   def guard493(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[1] != None)
   def act494(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[1]=True
   def guard494(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[1] != None)
   def act495(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[1]=True
   def guard495(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[1] != None)
   def act496(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[1]=True
   def guard496(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[1] != None)
   def act497(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[1]=True
   def guard497(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[1] != None)
   def act498(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[1]=True
   def guard498(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[1] != None)
   def act499(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[1]=True
   def guard499(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[1] != None)
   def act500(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[1]=True
   def guard500(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[1] != None)
   def act501(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[1]=True
   def guard501(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[1] != None)
   def act502(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[1]=True
   def guard502(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[1] != None)
   def act503(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[1]=True
   def guard503(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[1] != None)
   def act504(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[1]=True
   def guard504(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[1] != None)
   def act505(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[1]=True
   def guard505(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[1] != None)
   def act506(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[1]=True
   def guard506(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[1] != None)
   def act507(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[1]=True
   def guard507(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[1] != None)
   def act508(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[1]=True
   def guard508(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[1] != None)
   def act509(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[1]=True
   def guard509(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[1] != None)
   def act510(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[1]=True
   def guard510(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[1] != None)
   def act511(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[1]=True
   def guard511(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[1] != None)
   def act512(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[1]=True
   def guard512(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[1] != None)
   def act513(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[1]=True
   def guard513(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[1] != None)
   def act514(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[1]=True
   def guard514(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[1] != None)
   def act515(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[1]=True
   def guard515(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[1] != None)
   def act516(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[1]=True
   def guard516(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[1] != None)
   def act517(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[1]=True
   def guard517(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[1] != None)
   def act518(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[2]=True
   def guard518(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[2] != None)
   def act519(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[2]=True
   def guard519(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[2] != None)
   def act520(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[2]=True
   def guard520(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[2] != None)
   def act521(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[2]=True
   def guard521(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[2] != None)
   def act522(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[2]=True
   def guard522(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[2] != None)
   def act523(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[2]=True
   def guard523(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[2] != None)
   def act524(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[2]=True
   def guard524(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[2] != None)
   def act525(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[2]=True
   def guard525(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[2] != None)
   def act526(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[2]=True
   def guard526(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[2] != None)
   def act527(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[2]=True
   def guard527(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[2] != None)
   def act528(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[2]=True
   def guard528(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[2] != None)
   def act529(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[2]=True
   def guard529(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[2] != None)
   def act530(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[2]=True
   def guard530(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[2] != None)
   def act531(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[2]=True
   def guard531(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[2] != None)
   def act532(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[2]=True
   def guard532(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[2] != None)
   def act533(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[2]=True
   def guard533(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[2] != None)
   def act534(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[2]=True
   def guard534(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[2] != None)
   def act535(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[2]=True
   def guard535(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[2] != None)
   def act536(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[2]=True
   def guard536(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[2] != None)
   def act537(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[2]=True
   def guard537(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[2] != None)
   def act538(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[2]=True
   def guard538(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[2] != None)
   def act539(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[2]=True
   def guard539(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[2] != None)
   def act540(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[2]=True
   def guard540(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[2] != None)
   def act541(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[2]=True
   def guard541(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[2] != None)
   def act542(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[2]=True
   def guard542(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[2] != None)
   def act543(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[2]=True
   def guard543(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[2] != None)
   def act544(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[2]=True
   def guard544(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[2] != None)
   def act545(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[2]=True
   def guard545(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[2] != None)
   def act546(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[2]=True
   def guard546(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[2] != None)
   def act547(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[2]=True
   def guard547(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[2] != None)
   def act548(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[2]=True
   def guard548(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[2] != None)
   def act549(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[2]=True
   def guard549(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[2] != None)
   def act550(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[2]=True
   def guard550(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[2] != None)
   def act551(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[2]=True
   def guard551(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[2] != None)
   def act552(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[2]=True
   def guard552(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[2] != None)
   def act553(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[2]=True
   def guard553(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[2] != None)
   def act554(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[2]=True
   def guard554(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[2] != None)
   def act555(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[2]=True
   def guard555(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[2] != None)
   def act556(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[2]=True
   def guard556(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[2] != None)
   def act557(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[2]=True
   def guard557(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[2] != None)
   def act558(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[2]=True
   def guard558(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[2] != None)
   def act559(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[2]=True
   def guard559(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[2] != None)
   def act560(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[2]=True
   def guard560(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[2] != None)
   def act561(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[2]=True
   def guard561(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[2] != None)
   def act562(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[2]=True
   def guard562(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[2] != None)
   def act563(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[2]=True
   def guard563(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[2] != None)
   def act564(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[2]=True
   def guard564(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[2] != None)
   def act565(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[2]=True
   def guard565(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[2] != None)
   def act566(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[2]=True
   def guard566(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[2] != None)
   def act567(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[2]=True
   def guard567(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[2] != None)
   def act568(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[2]=True
   def guard568(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[2] != None)
   def act569(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[2]=True
   def guard569(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[2] != None)
   def act570(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[2]=True
   def guard570(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[2] != None)
   def act571(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[2]=True
   def guard571(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[2] != None)
   def act572(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[2]=True
   def guard572(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[2] != None)
   def act573(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[2]=True
   def guard573(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[2] != None)
   def act574(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[2]=True
   def guard574(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[2] != None)
   def act575(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[2]=True
   def guard575(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[2] != None)
   def act576(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[2]=True
   def guard576(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[2] != None)
   def act577(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[2]=True
   def guard577(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[2] != None)
   def act578(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[2]=True
   def guard578(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[2] != None)
   def act579(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[2]=True
   def guard579(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[2] != None)
   def act580(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[2]=True
   def guard580(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[2] != None)
   def act581(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[2]=True
   def guard581(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[2] != None)
   def act582(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[2]=True
   def guard582(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[2] != None)
   def act583(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[2]=True
   def guard583(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[2] != None)
   def act584(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[2]=True
   def guard584(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[2] != None)
   def act585(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[2]=True
   def guard585(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[2] != None)
   def act586(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[2]=True
   def guard586(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[2] != None)
   def act587(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[2]=True
   def guard587(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[2] != None)
   def act588(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[2]=True
   def guard588(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[2] != None)
   def act589(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[2]=True
   def guard589(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[2] != None)
   def act590(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[2]=True
   def guard590(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[2] != None)
   def act591(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[2]=True
   def guard591(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[2] != None)
   def act592(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[2]=True
   def guard592(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[2] != None)
   def act593(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[2]=True
   def guard593(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[2] != None)
   def act594(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[2]=True
   def guard594(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[2] != None)
   def act595(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[2]=True
   def guard595(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[2] != None)
   def act596(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[2]=True
   def guard596(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[2] != None)
   def act597(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[2]=True
   def guard597(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[2] != None)
   def act598(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[2]=True
   def guard598(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[2] != None)
   def act599(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[2]=True
   def guard599(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[2] != None)
   def act600(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[2]=True
   def guard600(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[2] != None)
   def act601(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[2]=True
   def guard601(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[2] != None)
   def act602(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[2]=True
   def guard602(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[2] != None)
   def act603(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[2]=True
   def guard603(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[2] != None)
   def act604(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[2]=True
   def guard604(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[2] != None)
   def act605(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[2]=True
   def guard605(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[2] != None)
   def act606(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[2]=True
   def guard606(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[2] != None)
   def act607(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[2]=True
   def guard607(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[2] != None)
   def act608(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[2]=True
   def guard608(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[2] != None)
   def act609(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[2]=True
   def guard609(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[2] != None)
   def act610(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[2]=True
   def guard610(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[2] != None)
   def act611(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[2]=True
   def guard611(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[2] != None)
   def act612(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[2]=True
   def guard612(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[2] != None)
   def act613(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[2]=True
   def guard613(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[2] != None)
   def act614(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[2]=True
   def guard614(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[2] != None)
   def act615(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[2]=True
   def guard615(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[2] != None)
   def act616(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[2]=True
   def guard616(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[2] != None)
   def act617(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[2]=True
   def guard617(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[2] != None)
   def act618(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[2]=True
   def guard618(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[2] != None)
   def act619(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[2]=True
   def guard619(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[2] != None)
   def act620(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[2]=True
   def guard620(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[2] != None)
   def act621(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[2]=True
   def guard621(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[2] != None)
   def act622(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[2]=True
   def guard622(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[2] != None)
   def act623(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[2]=True
   def guard623(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[2] != None)
   def act624(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[2]=True
   def guard624(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[2] != None)
   def act625(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[2]=True
   def guard625(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[2] != None)
   def act626(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[2]=True
   def guard626(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[2] != None)
   def act627(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[2]=True
   def guard627(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[2] != None)
   def act628(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[2]=True
   def guard628(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[2] != None)
   def act629(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[2]=True
   def guard629(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[2] != None)
   def act630(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[2]=True
   def guard630(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[2] != None)
   def act631(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[2]=True
   def guard631(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[2] != None)
   def act632(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[2]=True
   def guard632(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[2] != None)
   def act633(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[2]=True
   def guard633(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[2] != None)
   def act634(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[2]=True
   def guard634(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[2] != None)
   def act635(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[2]=True
   def guard635(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[2] != None)
   def act636(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[2]=True
   def guard636(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[2] != None)
   def act637(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[2]=True
   def guard637(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[2] != None)
   def act638(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[2]=True
   def guard638(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[2] != None)
   def act639(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[2]=True
   def guard639(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[2] != None)
   def act640(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[2]=True
   def guard640(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[2] != None)
   def act641(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[2]=True
   def guard641(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[2] != None)
   def act642(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[2]=True
   def guard642(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[2] != None)
   def act643(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[2]=True
   def guard643(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[2] != None)
   def act644(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[2]=True
   def guard644(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[2] != None)
   def act645(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[2]=True
   def guard645(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[2] != None)
   def act646(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[3]=True
   def guard646(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[3] != None)
   def act647(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[3]=True
   def guard647(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[3] != None)
   def act648(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[3]=True
   def guard648(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[3] != None)
   def act649(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[3]=True
   def guard649(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[3] != None)
   def act650(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[3]=True
   def guard650(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[3] != None)
   def act651(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[3]=True
   def guard651(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[3] != None)
   def act652(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[3]=True
   def guard652(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[3] != None)
   def act653(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[3]=True
   def guard653(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[3] != None)
   def act654(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[3]=True
   def guard654(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[3] != None)
   def act655(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[3]=True
   def guard655(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[3] != None)
   def act656(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[3]=True
   def guard656(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[3] != None)
   def act657(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[3]=True
   def guard657(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[3] != None)
   def act658(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[3]=True
   def guard658(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[3] != None)
   def act659(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[3]=True
   def guard659(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[3] != None)
   def act660(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[3]=True
   def guard660(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[3] != None)
   def act661(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[3]=True
   def guard661(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[3] != None)
   def act662(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[3]=True
   def guard662(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[3] != None)
   def act663(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[3]=True
   def guard663(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[3] != None)
   def act664(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[3]=True
   def guard664(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[3] != None)
   def act665(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[3]=True
   def guard665(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[3] != None)
   def act666(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[3]=True
   def guard666(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[3] != None)
   def act667(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[3]=True
   def guard667(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[3] != None)
   def act668(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[3]=True
   def guard668(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[3] != None)
   def act669(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[3]=True
   def guard669(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[3] != None)
   def act670(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[3]=True
   def guard670(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[3] != None)
   def act671(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[3]=True
   def guard671(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[3] != None)
   def act672(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[3]=True
   def guard672(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[3] != None)
   def act673(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[3]=True
   def guard673(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[3] != None)
   def act674(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[3]=True
   def guard674(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[3] != None)
   def act675(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[3]=True
   def guard675(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[3] != None)
   def act676(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[3]=True
   def guard676(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[3] != None)
   def act677(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[3]=True
   def guard677(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[3] != None)
   def act678(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[3]=True
   def guard678(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[3] != None)
   def act679(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[3]=True
   def guard679(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[3] != None)
   def act680(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[3]=True
   def guard680(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[3] != None)
   def act681(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[3]=True
   def guard681(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[3] != None)
   def act682(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[3]=True
   def guard682(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[3] != None)
   def act683(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[3]=True
   def guard683(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[3] != None)
   def act684(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[3]=True
   def guard684(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[3] != None)
   def act685(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[3]=True
   def guard685(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[3] != None)
   def act686(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[3]=True
   def guard686(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[3] != None)
   def act687(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[3]=True
   def guard687(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[3] != None)
   def act688(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[3]=True
   def guard688(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[3] != None)
   def act689(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[3]=True
   def guard689(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[3] != None)
   def act690(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[3]=True
   def guard690(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[3] != None)
   def act691(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[3]=True
   def guard691(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[3] != None)
   def act692(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[3]=True
   def guard692(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[3] != None)
   def act693(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[3]=True
   def guard693(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[3] != None)
   def act694(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[3]=True
   def guard694(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[3] != None)
   def act695(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[3]=True
   def guard695(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[3] != None)
   def act696(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[3]=True
   def guard696(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[3] != None)
   def act697(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[3]=True
   def guard697(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[3] != None)
   def act698(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[3]=True
   def guard698(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[3] != None)
   def act699(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[3]=True
   def guard699(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[3] != None)
   def act700(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[3]=True
   def guard700(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[3] != None)
   def act701(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[3]=True
   def guard701(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[3] != None)
   def act702(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[3]=True
   def guard702(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[3] != None)
   def act703(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[3]=True
   def guard703(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[3] != None)
   def act704(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[3]=True
   def guard704(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[3] != None)
   def act705(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[3]=True
   def guard705(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[3] != None)
   def act706(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[3]=True
   def guard706(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[3] != None)
   def act707(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[3]=True
   def guard707(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[3] != None)
   def act708(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[3]=True
   def guard708(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[3] != None)
   def act709(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[3]=True
   def guard709(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[3] != None)
   def act710(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[3]=True
   def guard710(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[3] != None)
   def act711(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[3]=True
   def guard711(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[3] != None)
   def act712(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[3]=True
   def guard712(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[3] != None)
   def act713(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[3]=True
   def guard713(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[3] != None)
   def act714(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[3]=True
   def guard714(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[3] != None)
   def act715(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[3]=True
   def guard715(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[3] != None)
   def act716(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[3]=True
   def guard716(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[3] != None)
   def act717(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[3]=True
   def guard717(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[3] != None)
   def act718(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[3]=True
   def guard718(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[3] != None)
   def act719(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[3]=True
   def guard719(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[3] != None)
   def act720(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[3]=True
   def guard720(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[3] != None)
   def act721(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[3]=True
   def guard721(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[3] != None)
   def act722(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[3]=True
   def guard722(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[3] != None)
   def act723(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[3]=True
   def guard723(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[3] != None)
   def act724(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[3]=True
   def guard724(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[3] != None)
   def act725(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[3]=True
   def guard725(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[3] != None)
   def act726(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[3]=True
   def guard726(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[3] != None)
   def act727(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[3]=True
   def guard727(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[3] != None)
   def act728(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[3]=True
   def guard728(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[3] != None)
   def act729(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[3]=True
   def guard729(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[3] != None)
   def act730(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[3]=True
   def guard730(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[3] != None)
   def act731(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[3]=True
   def guard731(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[3] != None)
   def act732(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[3]=True
   def guard732(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[3] != None)
   def act733(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[3]=True
   def guard733(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[3] != None)
   def act734(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[3]=True
   def guard734(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[3] != None)
   def act735(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[3]=True
   def guard735(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[3] != None)
   def act736(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[3]=True
   def guard736(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[3] != None)
   def act737(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[3]=True
   def guard737(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[3] != None)
   def act738(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[3]=True
   def guard738(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[3] != None)
   def act739(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[3]=True
   def guard739(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[3] != None)
   def act740(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[3]=True
   def guard740(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[3] != None)
   def act741(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[3]=True
   def guard741(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[3] != None)
   def act742(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[3]=True
   def guard742(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[3] != None)
   def act743(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[3]=True
   def guard743(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[3] != None)
   def act744(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[3]=True
   def guard744(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[3] != None)
   def act745(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[3]=True
   def guard745(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[3] != None)
   def act746(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[3]=True
   def guard746(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[3] != None)
   def act747(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[3]=True
   def guard747(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[3] != None)
   def act748(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[3]=True
   def guard748(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[3] != None)
   def act749(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[3]=True
   def guard749(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[3] != None)
   def act750(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[3]=True
   def guard750(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[3] != None)
   def act751(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[3]=True
   def guard751(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[3] != None)
   def act752(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[3]=True
   def guard752(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[3] != None)
   def act753(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[3]=True
   def guard753(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[3] != None)
   def act754(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[3]=True
   def guard754(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[3] != None)
   def act755(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[3]=True
   def guard755(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[3] != None)
   def act756(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[3]=True
   def guard756(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[3] != None)
   def act757(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[3]=True
   def guard757(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[3] != None)
   def act758(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[3]=True
   def guard758(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[3] != None)
   def act759(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[3]=True
   def guard759(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[3] != None)
   def act760(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[3]=True
   def guard760(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[3] != None)
   def act761(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[3]=True
   def guard761(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[3] != None)
   def act762(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[3]=True
   def guard762(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[3] != None)
   def act763(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[3]=True
   def guard763(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[3] != None)
   def act764(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[3]=True
   def guard764(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[3] != None)
   def act765(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[3]=True
   def guard765(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[3] != None)
   def act766(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[3]=True
   def guard766(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[3] != None)
   def act767(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[0]=True
      self.p_SINT_used[3]=True
   def guard767(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[0] != None) and (self.p_SINT[3] != None)
   def act768(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[3]=True
   def guard768(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[3] != None)
   def act769(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[1]=True
      self.p_SINT_used[3]=True
   def guard769(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[1] != None) and (self.p_SINT[3] != None)
   def act770(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[3]=True
   def guard770(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[3] != None)
   def act771(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[2]=True
      self.p_SINT_used[3]=True
   def guard771(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[2] != None) and (self.p_SINT[3] != None)
   def act772(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM_REF[0])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[3]=True
   def guard772(self):
      return (self.p_DOM[0] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[3] != None)
   def act773(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1])

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = dominion2.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM_REF[1])

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_CARDS_used[3]=True
      self.p_SINT_used[3]=True
   def guard773(self):
      return (self.p_DOM[1] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_CARDS[3] != None) and (self.p_SINT[3] != None)
   def act774(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = sorted(dominion.thehand(self.p_DOM[0]))

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = sorted(dominion2.thehand(self.p_DOM_REF[0]))

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
   def guard774(self):
      return (self.p_DOM[0] != None)
   def act775(self):
      self.log()
      if self.__collectCov:
         self.__cov.start()
      try:
         __result = sorted(dominion.thehand(self.p_DOM[1]))

      finally:
         if self.__collectCov:
            self.__cov.stop()
            self.__updateCov()
      __result_REF = sorted(dominion2.thehand(self.p_DOM_REF[1]))

      assert __result == __result_REF, " (%s) == (%s) " % (__result, __result_REF)
   def guard775(self):
      return (self.p_DOM[1] != None)
   def __init__(self):
      self.__features = []
      self.__cov = coverage.coverage(branch=True, source=["dominion.py","dominion2.py","playdom.py"])
      self.__collectCov = True
      self.__allBranches = set()
      self.__allStatements = set()
      self.__newBranches = set()
      self.__newStatements = set()
      self.__currBranches = set()
      self.__currStatements = set()
      self.__newCurrBranches = set()
      self.__newCurrStatements = set()
      self.p_INT = {}
      self.p_INT_used = {}
      self.p_INT[0] = None
      self.p_INT_used[0] = True
      self.p_INT[1] = None
      self.p_INT_used[1] = True
      self.p_INT[2] = None
      self.p_INT_used[2] = True
      self.p_INT[3] = None
      self.p_INT_used[3] = True
      self.p_INT[4] = None
      self.p_INT_used[4] = True
      self.p_DOM_REF = {}
      self.p_DOM_REF_used = {}
      self.p_DOM_REF[0] = None
      self.p_DOM_REF_used[0] = True
      self.p_DOM_REF[1] = None
      self.p_DOM_REF_used[1] = True
      self.p_DOM_REF[2] = None
      self.p_DOM_REF_used[2] = True
      self.p_DOM = {}
      self.p_DOM_used = {}
      self.p_DOM[0] = None
      self.p_DOM_used[0] = True
      self.p_DOM[1] = None
      self.p_DOM_used[1] = True
      self.p_DOM[2] = None
      self.p_DOM_used[2] = True
      self.p_PNUM = {}
      self.p_PNUM_used = {}
      self.p_PNUM[0] = None
      self.p_PNUM_used[0] = True
      self.p_PNUM[1] = None
      self.p_PNUM_used[1] = True
      self.p_PNUM[2] = None
      self.p_PNUM_used[2] = True
      self.p_PNUM[3] = None
      self.p_PNUM_used[3] = True
      self.p_PNUM[4] = None
      self.p_PNUM_used[4] = True
      self.p_CARDS = {}
      self.p_CARDS_used = {}
      self.p_CARDS[0] = None
      self.p_CARDS_used[0] = True
      self.p_CARDS[1] = None
      self.p_CARDS_used[1] = True
      self.p_CARDS[2] = None
      self.p_CARDS_used[2] = True
      self.p_CARDS[3] = None
      self.p_CARDS_used[3] = True
      self.p_CARDS[4] = None
      self.p_CARDS_used[4] = True
      self.p_SINT = {}
      self.p_SINT_used = {}
      self.p_SINT[0] = None
      self.p_SINT_used[0] = True
      self.p_SINT[1] = None
      self.p_SINT_used[1] = True
      self.p_SINT[2] = None
      self.p_SINT_used[2] = True
      self.p_SINT[3] = None
      self.p_SINT_used[3] = True
      self.p_SINT[4] = None
      self.p_SINT_used[4] = True
      self.__actions = []
      self.__names = {}
      self.__failure = None
      self.__log = None
      self.__logAction = self.logPrint
      self.__actions.append(('''self.p_INT[0]=0 ''',self.guard0,self.act0))

      self.__names['''self.p_INT[0]=0 '''] = ('''self.p_INT[0]=0 ''',self.guard0,self.act0)

      self.__actions.append(('''self.p_INT[0]=1 ''',self.guard1,self.act1))

      self.__names['''self.p_INT[0]=1 '''] = ('''self.p_INT[0]=1 ''',self.guard1,self.act1)

      self.__actions.append(('''self.p_INT[0]=2 ''',self.guard2,self.act2))

      self.__names['''self.p_INT[0]=2 '''] = ('''self.p_INT[0]=2 ''',self.guard2,self.act2)

      self.__actions.append(('''self.p_INT[0]=3 ''',self.guard3,self.act3))

      self.__names['''self.p_INT[0]=3 '''] = ('''self.p_INT[0]=3 ''',self.guard3,self.act3)

      self.__actions.append(('''self.p_INT[0]=4 ''',self.guard4,self.act4))

      self.__names['''self.p_INT[0]=4 '''] = ('''self.p_INT[0]=4 ''',self.guard4,self.act4)

      self.__actions.append(('''self.p_INT[0]=5 ''',self.guard5,self.act5))

      self.__names['''self.p_INT[0]=5 '''] = ('''self.p_INT[0]=5 ''',self.guard5,self.act5)

      self.__actions.append(('''self.p_INT[0]=6 ''',self.guard6,self.act6))

      self.__names['''self.p_INT[0]=6 '''] = ('''self.p_INT[0]=6 ''',self.guard6,self.act6)

      self.__actions.append(('''self.p_INT[0]=7 ''',self.guard7,self.act7))

      self.__names['''self.p_INT[0]=7 '''] = ('''self.p_INT[0]=7 ''',self.guard7,self.act7)

      self.__actions.append(('''self.p_INT[0]=8 ''',self.guard8,self.act8))

      self.__names['''self.p_INT[0]=8 '''] = ('''self.p_INT[0]=8 ''',self.guard8,self.act8)

      self.__actions.append(('''self.p_INT[0]=9 ''',self.guard9,self.act9))

      self.__names['''self.p_INT[0]=9 '''] = ('''self.p_INT[0]=9 ''',self.guard9,self.act9)

      self.__actions.append(('''self.p_INT[0]=10 ''',self.guard10,self.act10))

      self.__names['''self.p_INT[0]=10 '''] = ('''self.p_INT[0]=10 ''',self.guard10,self.act10)

      self.__actions.append(('''self.p_INT[0]=11 ''',self.guard11,self.act11))

      self.__names['''self.p_INT[0]=11 '''] = ('''self.p_INT[0]=11 ''',self.guard11,self.act11)

      self.__actions.append(('''self.p_INT[0]=12 ''',self.guard12,self.act12))

      self.__names['''self.p_INT[0]=12 '''] = ('''self.p_INT[0]=12 ''',self.guard12,self.act12)

      self.__actions.append(('''self.p_INT[0]=13 ''',self.guard13,self.act13))

      self.__names['''self.p_INT[0]=13 '''] = ('''self.p_INT[0]=13 ''',self.guard13,self.act13)

      self.__actions.append(('''self.p_INT[0]=14 ''',self.guard14,self.act14))

      self.__names['''self.p_INT[0]=14 '''] = ('''self.p_INT[0]=14 ''',self.guard14,self.act14)

      self.__actions.append(('''self.p_INT[0]=15 ''',self.guard15,self.act15))

      self.__names['''self.p_INT[0]=15 '''] = ('''self.p_INT[0]=15 ''',self.guard15,self.act15)

      self.__actions.append(('''self.p_INT[0]=16 ''',self.guard16,self.act16))

      self.__names['''self.p_INT[0]=16 '''] = ('''self.p_INT[0]=16 ''',self.guard16,self.act16)

      self.__actions.append(('''self.p_INT[0]=17 ''',self.guard17,self.act17))

      self.__names['''self.p_INT[0]=17 '''] = ('''self.p_INT[0]=17 ''',self.guard17,self.act17)

      self.__actions.append(('''self.p_INT[0]=18 ''',self.guard18,self.act18))

      self.__names['''self.p_INT[0]=18 '''] = ('''self.p_INT[0]=18 ''',self.guard18,self.act18)

      self.__actions.append(('''self.p_INT[0]=19 ''',self.guard19,self.act19))

      self.__names['''self.p_INT[0]=19 '''] = ('''self.p_INT[0]=19 ''',self.guard19,self.act19)

      self.__actions.append(('''self.p_INT[0]=20 ''',self.guard20,self.act20))

      self.__names['''self.p_INT[0]=20 '''] = ('''self.p_INT[0]=20 ''',self.guard20,self.act20)

      self.__actions.append(('''self.p_INT[1]=0 ''',self.guard21,self.act21))

      self.__names['''self.p_INT[1]=0 '''] = ('''self.p_INT[1]=0 ''',self.guard21,self.act21)

      self.__actions.append(('''self.p_INT[1]=1 ''',self.guard22,self.act22))

      self.__names['''self.p_INT[1]=1 '''] = ('''self.p_INT[1]=1 ''',self.guard22,self.act22)

      self.__actions.append(('''self.p_INT[1]=2 ''',self.guard23,self.act23))

      self.__names['''self.p_INT[1]=2 '''] = ('''self.p_INT[1]=2 ''',self.guard23,self.act23)

      self.__actions.append(('''self.p_INT[1]=3 ''',self.guard24,self.act24))

      self.__names['''self.p_INT[1]=3 '''] = ('''self.p_INT[1]=3 ''',self.guard24,self.act24)

      self.__actions.append(('''self.p_INT[1]=4 ''',self.guard25,self.act25))

      self.__names['''self.p_INT[1]=4 '''] = ('''self.p_INT[1]=4 ''',self.guard25,self.act25)

      self.__actions.append(('''self.p_INT[1]=5 ''',self.guard26,self.act26))

      self.__names['''self.p_INT[1]=5 '''] = ('''self.p_INT[1]=5 ''',self.guard26,self.act26)

      self.__actions.append(('''self.p_INT[1]=6 ''',self.guard27,self.act27))

      self.__names['''self.p_INT[1]=6 '''] = ('''self.p_INT[1]=6 ''',self.guard27,self.act27)

      self.__actions.append(('''self.p_INT[1]=7 ''',self.guard28,self.act28))

      self.__names['''self.p_INT[1]=7 '''] = ('''self.p_INT[1]=7 ''',self.guard28,self.act28)

      self.__actions.append(('''self.p_INT[1]=8 ''',self.guard29,self.act29))

      self.__names['''self.p_INT[1]=8 '''] = ('''self.p_INT[1]=8 ''',self.guard29,self.act29)

      self.__actions.append(('''self.p_INT[1]=9 ''',self.guard30,self.act30))

      self.__names['''self.p_INT[1]=9 '''] = ('''self.p_INT[1]=9 ''',self.guard30,self.act30)

      self.__actions.append(('''self.p_INT[1]=10 ''',self.guard31,self.act31))

      self.__names['''self.p_INT[1]=10 '''] = ('''self.p_INT[1]=10 ''',self.guard31,self.act31)

      self.__actions.append(('''self.p_INT[1]=11 ''',self.guard32,self.act32))

      self.__names['''self.p_INT[1]=11 '''] = ('''self.p_INT[1]=11 ''',self.guard32,self.act32)

      self.__actions.append(('''self.p_INT[1]=12 ''',self.guard33,self.act33))

      self.__names['''self.p_INT[1]=12 '''] = ('''self.p_INT[1]=12 ''',self.guard33,self.act33)

      self.__actions.append(('''self.p_INT[1]=13 ''',self.guard34,self.act34))

      self.__names['''self.p_INT[1]=13 '''] = ('''self.p_INT[1]=13 ''',self.guard34,self.act34)

      self.__actions.append(('''self.p_INT[1]=14 ''',self.guard35,self.act35))

      self.__names['''self.p_INT[1]=14 '''] = ('''self.p_INT[1]=14 ''',self.guard35,self.act35)

      self.__actions.append(('''self.p_INT[1]=15 ''',self.guard36,self.act36))

      self.__names['''self.p_INT[1]=15 '''] = ('''self.p_INT[1]=15 ''',self.guard36,self.act36)

      self.__actions.append(('''self.p_INT[1]=16 ''',self.guard37,self.act37))

      self.__names['''self.p_INT[1]=16 '''] = ('''self.p_INT[1]=16 ''',self.guard37,self.act37)

      self.__actions.append(('''self.p_INT[1]=17 ''',self.guard38,self.act38))

      self.__names['''self.p_INT[1]=17 '''] = ('''self.p_INT[1]=17 ''',self.guard38,self.act38)

      self.__actions.append(('''self.p_INT[1]=18 ''',self.guard39,self.act39))

      self.__names['''self.p_INT[1]=18 '''] = ('''self.p_INT[1]=18 ''',self.guard39,self.act39)

      self.__actions.append(('''self.p_INT[1]=19 ''',self.guard40,self.act40))

      self.__names['''self.p_INT[1]=19 '''] = ('''self.p_INT[1]=19 ''',self.guard40,self.act40)

      self.__actions.append(('''self.p_INT[1]=20 ''',self.guard41,self.act41))

      self.__names['''self.p_INT[1]=20 '''] = ('''self.p_INT[1]=20 ''',self.guard41,self.act41)

      self.__actions.append(('''self.p_INT[2]=0 ''',self.guard42,self.act42))

      self.__names['''self.p_INT[2]=0 '''] = ('''self.p_INT[2]=0 ''',self.guard42,self.act42)

      self.__actions.append(('''self.p_INT[2]=1 ''',self.guard43,self.act43))

      self.__names['''self.p_INT[2]=1 '''] = ('''self.p_INT[2]=1 ''',self.guard43,self.act43)

      self.__actions.append(('''self.p_INT[2]=2 ''',self.guard44,self.act44))

      self.__names['''self.p_INT[2]=2 '''] = ('''self.p_INT[2]=2 ''',self.guard44,self.act44)

      self.__actions.append(('''self.p_INT[2]=3 ''',self.guard45,self.act45))

      self.__names['''self.p_INT[2]=3 '''] = ('''self.p_INT[2]=3 ''',self.guard45,self.act45)

      self.__actions.append(('''self.p_INT[2]=4 ''',self.guard46,self.act46))

      self.__names['''self.p_INT[2]=4 '''] = ('''self.p_INT[2]=4 ''',self.guard46,self.act46)

      self.__actions.append(('''self.p_INT[2]=5 ''',self.guard47,self.act47))

      self.__names['''self.p_INT[2]=5 '''] = ('''self.p_INT[2]=5 ''',self.guard47,self.act47)

      self.__actions.append(('''self.p_INT[2]=6 ''',self.guard48,self.act48))

      self.__names['''self.p_INT[2]=6 '''] = ('''self.p_INT[2]=6 ''',self.guard48,self.act48)

      self.__actions.append(('''self.p_INT[2]=7 ''',self.guard49,self.act49))

      self.__names['''self.p_INT[2]=7 '''] = ('''self.p_INT[2]=7 ''',self.guard49,self.act49)

      self.__actions.append(('''self.p_INT[2]=8 ''',self.guard50,self.act50))

      self.__names['''self.p_INT[2]=8 '''] = ('''self.p_INT[2]=8 ''',self.guard50,self.act50)

      self.__actions.append(('''self.p_INT[2]=9 ''',self.guard51,self.act51))

      self.__names['''self.p_INT[2]=9 '''] = ('''self.p_INT[2]=9 ''',self.guard51,self.act51)

      self.__actions.append(('''self.p_INT[2]=10 ''',self.guard52,self.act52))

      self.__names['''self.p_INT[2]=10 '''] = ('''self.p_INT[2]=10 ''',self.guard52,self.act52)

      self.__actions.append(('''self.p_INT[2]=11 ''',self.guard53,self.act53))

      self.__names['''self.p_INT[2]=11 '''] = ('''self.p_INT[2]=11 ''',self.guard53,self.act53)

      self.__actions.append(('''self.p_INT[2]=12 ''',self.guard54,self.act54))

      self.__names['''self.p_INT[2]=12 '''] = ('''self.p_INT[2]=12 ''',self.guard54,self.act54)

      self.__actions.append(('''self.p_INT[2]=13 ''',self.guard55,self.act55))

      self.__names['''self.p_INT[2]=13 '''] = ('''self.p_INT[2]=13 ''',self.guard55,self.act55)

      self.__actions.append(('''self.p_INT[2]=14 ''',self.guard56,self.act56))

      self.__names['''self.p_INT[2]=14 '''] = ('''self.p_INT[2]=14 ''',self.guard56,self.act56)

      self.__actions.append(('''self.p_INT[2]=15 ''',self.guard57,self.act57))

      self.__names['''self.p_INT[2]=15 '''] = ('''self.p_INT[2]=15 ''',self.guard57,self.act57)

      self.__actions.append(('''self.p_INT[2]=16 ''',self.guard58,self.act58))

      self.__names['''self.p_INT[2]=16 '''] = ('''self.p_INT[2]=16 ''',self.guard58,self.act58)

      self.__actions.append(('''self.p_INT[2]=17 ''',self.guard59,self.act59))

      self.__names['''self.p_INT[2]=17 '''] = ('''self.p_INT[2]=17 ''',self.guard59,self.act59)

      self.__actions.append(('''self.p_INT[2]=18 ''',self.guard60,self.act60))

      self.__names['''self.p_INT[2]=18 '''] = ('''self.p_INT[2]=18 ''',self.guard60,self.act60)

      self.__actions.append(('''self.p_INT[2]=19 ''',self.guard61,self.act61))

      self.__names['''self.p_INT[2]=19 '''] = ('''self.p_INT[2]=19 ''',self.guard61,self.act61)

      self.__actions.append(('''self.p_INT[2]=20 ''',self.guard62,self.act62))

      self.__names['''self.p_INT[2]=20 '''] = ('''self.p_INT[2]=20 ''',self.guard62,self.act62)

      self.__actions.append(('''self.p_INT[3]=0 ''',self.guard63,self.act63))

      self.__names['''self.p_INT[3]=0 '''] = ('''self.p_INT[3]=0 ''',self.guard63,self.act63)

      self.__actions.append(('''self.p_INT[3]=1 ''',self.guard64,self.act64))

      self.__names['''self.p_INT[3]=1 '''] = ('''self.p_INT[3]=1 ''',self.guard64,self.act64)

      self.__actions.append(('''self.p_INT[3]=2 ''',self.guard65,self.act65))

      self.__names['''self.p_INT[3]=2 '''] = ('''self.p_INT[3]=2 ''',self.guard65,self.act65)

      self.__actions.append(('''self.p_INT[3]=3 ''',self.guard66,self.act66))

      self.__names['''self.p_INT[3]=3 '''] = ('''self.p_INT[3]=3 ''',self.guard66,self.act66)

      self.__actions.append(('''self.p_INT[3]=4 ''',self.guard67,self.act67))

      self.__names['''self.p_INT[3]=4 '''] = ('''self.p_INT[3]=4 ''',self.guard67,self.act67)

      self.__actions.append(('''self.p_INT[3]=5 ''',self.guard68,self.act68))

      self.__names['''self.p_INT[3]=5 '''] = ('''self.p_INT[3]=5 ''',self.guard68,self.act68)

      self.__actions.append(('''self.p_INT[3]=6 ''',self.guard69,self.act69))

      self.__names['''self.p_INT[3]=6 '''] = ('''self.p_INT[3]=6 ''',self.guard69,self.act69)

      self.__actions.append(('''self.p_INT[3]=7 ''',self.guard70,self.act70))

      self.__names['''self.p_INT[3]=7 '''] = ('''self.p_INT[3]=7 ''',self.guard70,self.act70)

      self.__actions.append(('''self.p_INT[3]=8 ''',self.guard71,self.act71))

      self.__names['''self.p_INT[3]=8 '''] = ('''self.p_INT[3]=8 ''',self.guard71,self.act71)

      self.__actions.append(('''self.p_INT[3]=9 ''',self.guard72,self.act72))

      self.__names['''self.p_INT[3]=9 '''] = ('''self.p_INT[3]=9 ''',self.guard72,self.act72)

      self.__actions.append(('''self.p_INT[3]=10 ''',self.guard73,self.act73))

      self.__names['''self.p_INT[3]=10 '''] = ('''self.p_INT[3]=10 ''',self.guard73,self.act73)

      self.__actions.append(('''self.p_INT[3]=11 ''',self.guard74,self.act74))

      self.__names['''self.p_INT[3]=11 '''] = ('''self.p_INT[3]=11 ''',self.guard74,self.act74)

      self.__actions.append(('''self.p_INT[3]=12 ''',self.guard75,self.act75))

      self.__names['''self.p_INT[3]=12 '''] = ('''self.p_INT[3]=12 ''',self.guard75,self.act75)

      self.__actions.append(('''self.p_INT[3]=13 ''',self.guard76,self.act76))

      self.__names['''self.p_INT[3]=13 '''] = ('''self.p_INT[3]=13 ''',self.guard76,self.act76)

      self.__actions.append(('''self.p_INT[3]=14 ''',self.guard77,self.act77))

      self.__names['''self.p_INT[3]=14 '''] = ('''self.p_INT[3]=14 ''',self.guard77,self.act77)

      self.__actions.append(('''self.p_INT[3]=15 ''',self.guard78,self.act78))

      self.__names['''self.p_INT[3]=15 '''] = ('''self.p_INT[3]=15 ''',self.guard78,self.act78)

      self.__actions.append(('''self.p_INT[3]=16 ''',self.guard79,self.act79))

      self.__names['''self.p_INT[3]=16 '''] = ('''self.p_INT[3]=16 ''',self.guard79,self.act79)

      self.__actions.append(('''self.p_INT[3]=17 ''',self.guard80,self.act80))

      self.__names['''self.p_INT[3]=17 '''] = ('''self.p_INT[3]=17 ''',self.guard80,self.act80)

      self.__actions.append(('''self.p_INT[3]=18 ''',self.guard81,self.act81))

      self.__names['''self.p_INT[3]=18 '''] = ('''self.p_INT[3]=18 ''',self.guard81,self.act81)

      self.__actions.append(('''self.p_INT[3]=19 ''',self.guard82,self.act82))

      self.__names['''self.p_INT[3]=19 '''] = ('''self.p_INT[3]=19 ''',self.guard82,self.act82)

      self.__actions.append(('''self.p_INT[3]=20 ''',self.guard83,self.act83))

      self.__names['''self.p_INT[3]=20 '''] = ('''self.p_INT[3]=20 ''',self.guard83,self.act83)

      self.__actions.append(('''self.p_SINT[0]=0 ''',self.guard84,self.act84))

      self.__names['''self.p_SINT[0]=0 '''] = ('''self.p_SINT[0]=0 ''',self.guard84,self.act84)

      self.__actions.append(('''self.p_SINT[0]=1 ''',self.guard85,self.act85))

      self.__names['''self.p_SINT[0]=1 '''] = ('''self.p_SINT[0]=1 ''',self.guard85,self.act85)

      self.__actions.append(('''self.p_SINT[0]=2 ''',self.guard86,self.act86))

      self.__names['''self.p_SINT[0]=2 '''] = ('''self.p_SINT[0]=2 ''',self.guard86,self.act86)

      self.__actions.append(('''self.p_SINT[0]=3 ''',self.guard87,self.act87))

      self.__names['''self.p_SINT[0]=3 '''] = ('''self.p_SINT[0]=3 ''',self.guard87,self.act87)

      self.__actions.append(('''self.p_SINT[0]=4 ''',self.guard88,self.act88))

      self.__names['''self.p_SINT[0]=4 '''] = ('''self.p_SINT[0]=4 ''',self.guard88,self.act88)

      self.__actions.append(('''self.p_SINT[0]=5 ''',self.guard89,self.act89))

      self.__names['''self.p_SINT[0]=5 '''] = ('''self.p_SINT[0]=5 ''',self.guard89,self.act89)

      self.__actions.append(('''self.p_SINT[0]=6 ''',self.guard90,self.act90))

      self.__names['''self.p_SINT[0]=6 '''] = ('''self.p_SINT[0]=6 ''',self.guard90,self.act90)

      self.__actions.append(('''self.p_SINT[0]=7 ''',self.guard91,self.act91))

      self.__names['''self.p_SINT[0]=7 '''] = ('''self.p_SINT[0]=7 ''',self.guard91,self.act91)

      self.__actions.append(('''self.p_SINT[0]=8 ''',self.guard92,self.act92))

      self.__names['''self.p_SINT[0]=8 '''] = ('''self.p_SINT[0]=8 ''',self.guard92,self.act92)

      self.__actions.append(('''self.p_SINT[0]=9 ''',self.guard93,self.act93))

      self.__names['''self.p_SINT[0]=9 '''] = ('''self.p_SINT[0]=9 ''',self.guard93,self.act93)

      self.__actions.append(('''self.p_SINT[0]=10 ''',self.guard94,self.act94))

      self.__names['''self.p_SINT[0]=10 '''] = ('''self.p_SINT[0]=10 ''',self.guard94,self.act94)

      self.__actions.append(('''self.p_SINT[1]=0 ''',self.guard95,self.act95))

      self.__names['''self.p_SINT[1]=0 '''] = ('''self.p_SINT[1]=0 ''',self.guard95,self.act95)

      self.__actions.append(('''self.p_SINT[1]=1 ''',self.guard96,self.act96))

      self.__names['''self.p_SINT[1]=1 '''] = ('''self.p_SINT[1]=1 ''',self.guard96,self.act96)

      self.__actions.append(('''self.p_SINT[1]=2 ''',self.guard97,self.act97))

      self.__names['''self.p_SINT[1]=2 '''] = ('''self.p_SINT[1]=2 ''',self.guard97,self.act97)

      self.__actions.append(('''self.p_SINT[1]=3 ''',self.guard98,self.act98))

      self.__names['''self.p_SINT[1]=3 '''] = ('''self.p_SINT[1]=3 ''',self.guard98,self.act98)

      self.__actions.append(('''self.p_SINT[1]=4 ''',self.guard99,self.act99))

      self.__names['''self.p_SINT[1]=4 '''] = ('''self.p_SINT[1]=4 ''',self.guard99,self.act99)

      self.__actions.append(('''self.p_SINT[1]=5 ''',self.guard100,self.act100))

      self.__names['''self.p_SINT[1]=5 '''] = ('''self.p_SINT[1]=5 ''',self.guard100,self.act100)

      self.__actions.append(('''self.p_SINT[1]=6 ''',self.guard101,self.act101))

      self.__names['''self.p_SINT[1]=6 '''] = ('''self.p_SINT[1]=6 ''',self.guard101,self.act101)

      self.__actions.append(('''self.p_SINT[1]=7 ''',self.guard102,self.act102))

      self.__names['''self.p_SINT[1]=7 '''] = ('''self.p_SINT[1]=7 ''',self.guard102,self.act102)

      self.__actions.append(('''self.p_SINT[1]=8 ''',self.guard103,self.act103))

      self.__names['''self.p_SINT[1]=8 '''] = ('''self.p_SINT[1]=8 ''',self.guard103,self.act103)

      self.__actions.append(('''self.p_SINT[1]=9 ''',self.guard104,self.act104))

      self.__names['''self.p_SINT[1]=9 '''] = ('''self.p_SINT[1]=9 ''',self.guard104,self.act104)

      self.__actions.append(('''self.p_SINT[1]=10 ''',self.guard105,self.act105))

      self.__names['''self.p_SINT[1]=10 '''] = ('''self.p_SINT[1]=10 ''',self.guard105,self.act105)

      self.__actions.append(('''self.p_SINT[2]=0 ''',self.guard106,self.act106))

      self.__names['''self.p_SINT[2]=0 '''] = ('''self.p_SINT[2]=0 ''',self.guard106,self.act106)

      self.__actions.append(('''self.p_SINT[2]=1 ''',self.guard107,self.act107))

      self.__names['''self.p_SINT[2]=1 '''] = ('''self.p_SINT[2]=1 ''',self.guard107,self.act107)

      self.__actions.append(('''self.p_SINT[2]=2 ''',self.guard108,self.act108))

      self.__names['''self.p_SINT[2]=2 '''] = ('''self.p_SINT[2]=2 ''',self.guard108,self.act108)

      self.__actions.append(('''self.p_SINT[2]=3 ''',self.guard109,self.act109))

      self.__names['''self.p_SINT[2]=3 '''] = ('''self.p_SINT[2]=3 ''',self.guard109,self.act109)

      self.__actions.append(('''self.p_SINT[2]=4 ''',self.guard110,self.act110))

      self.__names['''self.p_SINT[2]=4 '''] = ('''self.p_SINT[2]=4 ''',self.guard110,self.act110)

      self.__actions.append(('''self.p_SINT[2]=5 ''',self.guard111,self.act111))

      self.__names['''self.p_SINT[2]=5 '''] = ('''self.p_SINT[2]=5 ''',self.guard111,self.act111)

      self.__actions.append(('''self.p_SINT[2]=6 ''',self.guard112,self.act112))

      self.__names['''self.p_SINT[2]=6 '''] = ('''self.p_SINT[2]=6 ''',self.guard112,self.act112)

      self.__actions.append(('''self.p_SINT[2]=7 ''',self.guard113,self.act113))

      self.__names['''self.p_SINT[2]=7 '''] = ('''self.p_SINT[2]=7 ''',self.guard113,self.act113)

      self.__actions.append(('''self.p_SINT[2]=8 ''',self.guard114,self.act114))

      self.__names['''self.p_SINT[2]=8 '''] = ('''self.p_SINT[2]=8 ''',self.guard114,self.act114)

      self.__actions.append(('''self.p_SINT[2]=9 ''',self.guard115,self.act115))

      self.__names['''self.p_SINT[2]=9 '''] = ('''self.p_SINT[2]=9 ''',self.guard115,self.act115)

      self.__actions.append(('''self.p_SINT[2]=10 ''',self.guard116,self.act116))

      self.__names['''self.p_SINT[2]=10 '''] = ('''self.p_SINT[2]=10 ''',self.guard116,self.act116)

      self.__actions.append(('''self.p_SINT[3]=0 ''',self.guard117,self.act117))

      self.__names['''self.p_SINT[3]=0 '''] = ('''self.p_SINT[3]=0 ''',self.guard117,self.act117)

      self.__actions.append(('''self.p_SINT[3]=1 ''',self.guard118,self.act118))

      self.__names['''self.p_SINT[3]=1 '''] = ('''self.p_SINT[3]=1 ''',self.guard118,self.act118)

      self.__actions.append(('''self.p_SINT[3]=2 ''',self.guard119,self.act119))

      self.__names['''self.p_SINT[3]=2 '''] = ('''self.p_SINT[3]=2 ''',self.guard119,self.act119)

      self.__actions.append(('''self.p_SINT[3]=3 ''',self.guard120,self.act120))

      self.__names['''self.p_SINT[3]=3 '''] = ('''self.p_SINT[3]=3 ''',self.guard120,self.act120)

      self.__actions.append(('''self.p_SINT[3]=4 ''',self.guard121,self.act121))

      self.__names['''self.p_SINT[3]=4 '''] = ('''self.p_SINT[3]=4 ''',self.guard121,self.act121)

      self.__actions.append(('''self.p_SINT[3]=5 ''',self.guard122,self.act122))

      self.__names['''self.p_SINT[3]=5 '''] = ('''self.p_SINT[3]=5 ''',self.guard122,self.act122)

      self.__actions.append(('''self.p_SINT[3]=6 ''',self.guard123,self.act123))

      self.__names['''self.p_SINT[3]=6 '''] = ('''self.p_SINT[3]=6 ''',self.guard123,self.act123)

      self.__actions.append(('''self.p_SINT[3]=7 ''',self.guard124,self.act124))

      self.__names['''self.p_SINT[3]=7 '''] = ('''self.p_SINT[3]=7 ''',self.guard124,self.act124)

      self.__actions.append(('''self.p_SINT[3]=8 ''',self.guard125,self.act125))

      self.__names['''self.p_SINT[3]=8 '''] = ('''self.p_SINT[3]=8 ''',self.guard125,self.act125)

      self.__actions.append(('''self.p_SINT[3]=9 ''',self.guard126,self.act126))

      self.__names['''self.p_SINT[3]=9 '''] = ('''self.p_SINT[3]=9 ''',self.guard126,self.act126)

      self.__actions.append(('''self.p_SINT[3]=10 ''',self.guard127,self.act127))

      self.__names['''self.p_SINT[3]=10 '''] = ('''self.p_SINT[3]=10 ''',self.guard127,self.act127)

      self.__actions.append(('''self.p_CARDS[0]=0 ''',self.guard128,self.act128))

      self.__names['''self.p_CARDS[0]=0 '''] = ('''self.p_CARDS[0]=0 ''',self.guard128,self.act128)

      self.__actions.append(('''self.p_CARDS[0]=1 ''',self.guard129,self.act129))

      self.__names['''self.p_CARDS[0]=1 '''] = ('''self.p_CARDS[0]=1 ''',self.guard129,self.act129)

      self.__actions.append(('''self.p_CARDS[0]=2 ''',self.guard130,self.act130))

      self.__names['''self.p_CARDS[0]=2 '''] = ('''self.p_CARDS[0]=2 ''',self.guard130,self.act130)

      self.__actions.append(('''self.p_CARDS[0]=3 ''',self.guard131,self.act131))

      self.__names['''self.p_CARDS[0]=3 '''] = ('''self.p_CARDS[0]=3 ''',self.guard131,self.act131)

      self.__actions.append(('''self.p_CARDS[0]=4 ''',self.guard132,self.act132))

      self.__names['''self.p_CARDS[0]=4 '''] = ('''self.p_CARDS[0]=4 ''',self.guard132,self.act132)

      self.__actions.append(('''self.p_CARDS[0]=5 ''',self.guard133,self.act133))

      self.__names['''self.p_CARDS[0]=5 '''] = ('''self.p_CARDS[0]=5 ''',self.guard133,self.act133)

      self.__actions.append(('''self.p_CARDS[0]=6 ''',self.guard134,self.act134))

      self.__names['''self.p_CARDS[0]=6 '''] = ('''self.p_CARDS[0]=6 ''',self.guard134,self.act134)

      self.__actions.append(('''self.p_CARDS[0]=7 ''',self.guard135,self.act135))

      self.__names['''self.p_CARDS[0]=7 '''] = ('''self.p_CARDS[0]=7 ''',self.guard135,self.act135)

      self.__actions.append(('''self.p_CARDS[0]=8 ''',self.guard136,self.act136))

      self.__names['''self.p_CARDS[0]=8 '''] = ('''self.p_CARDS[0]=8 ''',self.guard136,self.act136)

      self.__actions.append(('''self.p_CARDS[0]=9 ''',self.guard137,self.act137))

      self.__names['''self.p_CARDS[0]=9 '''] = ('''self.p_CARDS[0]=9 ''',self.guard137,self.act137)

      self.__actions.append(('''self.p_CARDS[0]=10 ''',self.guard138,self.act138))

      self.__names['''self.p_CARDS[0]=10 '''] = ('''self.p_CARDS[0]=10 ''',self.guard138,self.act138)

      self.__actions.append(('''self.p_CARDS[0]=11 ''',self.guard139,self.act139))

      self.__names['''self.p_CARDS[0]=11 '''] = ('''self.p_CARDS[0]=11 ''',self.guard139,self.act139)

      self.__actions.append(('''self.p_CARDS[0]=12 ''',self.guard140,self.act140))

      self.__names['''self.p_CARDS[0]=12 '''] = ('''self.p_CARDS[0]=12 ''',self.guard140,self.act140)

      self.__actions.append(('''self.p_CARDS[0]=13 ''',self.guard141,self.act141))

      self.__names['''self.p_CARDS[0]=13 '''] = ('''self.p_CARDS[0]=13 ''',self.guard141,self.act141)

      self.__actions.append(('''self.p_CARDS[0]=14 ''',self.guard142,self.act142))

      self.__names['''self.p_CARDS[0]=14 '''] = ('''self.p_CARDS[0]=14 ''',self.guard142,self.act142)

      self.__actions.append(('''self.p_CARDS[0]=15 ''',self.guard143,self.act143))

      self.__names['''self.p_CARDS[0]=15 '''] = ('''self.p_CARDS[0]=15 ''',self.guard143,self.act143)

      self.__actions.append(('''self.p_CARDS[0]=16 ''',self.guard144,self.act144))

      self.__names['''self.p_CARDS[0]=16 '''] = ('''self.p_CARDS[0]=16 ''',self.guard144,self.act144)

      self.__actions.append(('''self.p_CARDS[1]=0 ''',self.guard145,self.act145))

      self.__names['''self.p_CARDS[1]=0 '''] = ('''self.p_CARDS[1]=0 ''',self.guard145,self.act145)

      self.__actions.append(('''self.p_CARDS[1]=1 ''',self.guard146,self.act146))

      self.__names['''self.p_CARDS[1]=1 '''] = ('''self.p_CARDS[1]=1 ''',self.guard146,self.act146)

      self.__actions.append(('''self.p_CARDS[1]=2 ''',self.guard147,self.act147))

      self.__names['''self.p_CARDS[1]=2 '''] = ('''self.p_CARDS[1]=2 ''',self.guard147,self.act147)

      self.__actions.append(('''self.p_CARDS[1]=3 ''',self.guard148,self.act148))

      self.__names['''self.p_CARDS[1]=3 '''] = ('''self.p_CARDS[1]=3 ''',self.guard148,self.act148)

      self.__actions.append(('''self.p_CARDS[1]=4 ''',self.guard149,self.act149))

      self.__names['''self.p_CARDS[1]=4 '''] = ('''self.p_CARDS[1]=4 ''',self.guard149,self.act149)

      self.__actions.append(('''self.p_CARDS[1]=5 ''',self.guard150,self.act150))

      self.__names['''self.p_CARDS[1]=5 '''] = ('''self.p_CARDS[1]=5 ''',self.guard150,self.act150)

      self.__actions.append(('''self.p_CARDS[1]=6 ''',self.guard151,self.act151))

      self.__names['''self.p_CARDS[1]=6 '''] = ('''self.p_CARDS[1]=6 ''',self.guard151,self.act151)

      self.__actions.append(('''self.p_CARDS[1]=7 ''',self.guard152,self.act152))

      self.__names['''self.p_CARDS[1]=7 '''] = ('''self.p_CARDS[1]=7 ''',self.guard152,self.act152)

      self.__actions.append(('''self.p_CARDS[1]=8 ''',self.guard153,self.act153))

      self.__names['''self.p_CARDS[1]=8 '''] = ('''self.p_CARDS[1]=8 ''',self.guard153,self.act153)

      self.__actions.append(('''self.p_CARDS[1]=9 ''',self.guard154,self.act154))

      self.__names['''self.p_CARDS[1]=9 '''] = ('''self.p_CARDS[1]=9 ''',self.guard154,self.act154)

      self.__actions.append(('''self.p_CARDS[1]=10 ''',self.guard155,self.act155))

      self.__names['''self.p_CARDS[1]=10 '''] = ('''self.p_CARDS[1]=10 ''',self.guard155,self.act155)

      self.__actions.append(('''self.p_CARDS[1]=11 ''',self.guard156,self.act156))

      self.__names['''self.p_CARDS[1]=11 '''] = ('''self.p_CARDS[1]=11 ''',self.guard156,self.act156)

      self.__actions.append(('''self.p_CARDS[1]=12 ''',self.guard157,self.act157))

      self.__names['''self.p_CARDS[1]=12 '''] = ('''self.p_CARDS[1]=12 ''',self.guard157,self.act157)

      self.__actions.append(('''self.p_CARDS[1]=13 ''',self.guard158,self.act158))

      self.__names['''self.p_CARDS[1]=13 '''] = ('''self.p_CARDS[1]=13 ''',self.guard158,self.act158)

      self.__actions.append(('''self.p_CARDS[1]=14 ''',self.guard159,self.act159))

      self.__names['''self.p_CARDS[1]=14 '''] = ('''self.p_CARDS[1]=14 ''',self.guard159,self.act159)

      self.__actions.append(('''self.p_CARDS[1]=15 ''',self.guard160,self.act160))

      self.__names['''self.p_CARDS[1]=15 '''] = ('''self.p_CARDS[1]=15 ''',self.guard160,self.act160)

      self.__actions.append(('''self.p_CARDS[1]=16 ''',self.guard161,self.act161))

      self.__names['''self.p_CARDS[1]=16 '''] = ('''self.p_CARDS[1]=16 ''',self.guard161,self.act161)

      self.__actions.append(('''self.p_CARDS[2]=0 ''',self.guard162,self.act162))

      self.__names['''self.p_CARDS[2]=0 '''] = ('''self.p_CARDS[2]=0 ''',self.guard162,self.act162)

      self.__actions.append(('''self.p_CARDS[2]=1 ''',self.guard163,self.act163))

      self.__names['''self.p_CARDS[2]=1 '''] = ('''self.p_CARDS[2]=1 ''',self.guard163,self.act163)

      self.__actions.append(('''self.p_CARDS[2]=2 ''',self.guard164,self.act164))

      self.__names['''self.p_CARDS[2]=2 '''] = ('''self.p_CARDS[2]=2 ''',self.guard164,self.act164)

      self.__actions.append(('''self.p_CARDS[2]=3 ''',self.guard165,self.act165))

      self.__names['''self.p_CARDS[2]=3 '''] = ('''self.p_CARDS[2]=3 ''',self.guard165,self.act165)

      self.__actions.append(('''self.p_CARDS[2]=4 ''',self.guard166,self.act166))

      self.__names['''self.p_CARDS[2]=4 '''] = ('''self.p_CARDS[2]=4 ''',self.guard166,self.act166)

      self.__actions.append(('''self.p_CARDS[2]=5 ''',self.guard167,self.act167))

      self.__names['''self.p_CARDS[2]=5 '''] = ('''self.p_CARDS[2]=5 ''',self.guard167,self.act167)

      self.__actions.append(('''self.p_CARDS[2]=6 ''',self.guard168,self.act168))

      self.__names['''self.p_CARDS[2]=6 '''] = ('''self.p_CARDS[2]=6 ''',self.guard168,self.act168)

      self.__actions.append(('''self.p_CARDS[2]=7 ''',self.guard169,self.act169))

      self.__names['''self.p_CARDS[2]=7 '''] = ('''self.p_CARDS[2]=7 ''',self.guard169,self.act169)

      self.__actions.append(('''self.p_CARDS[2]=8 ''',self.guard170,self.act170))

      self.__names['''self.p_CARDS[2]=8 '''] = ('''self.p_CARDS[2]=8 ''',self.guard170,self.act170)

      self.__actions.append(('''self.p_CARDS[2]=9 ''',self.guard171,self.act171))

      self.__names['''self.p_CARDS[2]=9 '''] = ('''self.p_CARDS[2]=9 ''',self.guard171,self.act171)

      self.__actions.append(('''self.p_CARDS[2]=10 ''',self.guard172,self.act172))

      self.__names['''self.p_CARDS[2]=10 '''] = ('''self.p_CARDS[2]=10 ''',self.guard172,self.act172)

      self.__actions.append(('''self.p_CARDS[2]=11 ''',self.guard173,self.act173))

      self.__names['''self.p_CARDS[2]=11 '''] = ('''self.p_CARDS[2]=11 ''',self.guard173,self.act173)

      self.__actions.append(('''self.p_CARDS[2]=12 ''',self.guard174,self.act174))

      self.__names['''self.p_CARDS[2]=12 '''] = ('''self.p_CARDS[2]=12 ''',self.guard174,self.act174)

      self.__actions.append(('''self.p_CARDS[2]=13 ''',self.guard175,self.act175))

      self.__names['''self.p_CARDS[2]=13 '''] = ('''self.p_CARDS[2]=13 ''',self.guard175,self.act175)

      self.__actions.append(('''self.p_CARDS[2]=14 ''',self.guard176,self.act176))

      self.__names['''self.p_CARDS[2]=14 '''] = ('''self.p_CARDS[2]=14 ''',self.guard176,self.act176)

      self.__actions.append(('''self.p_CARDS[2]=15 ''',self.guard177,self.act177))

      self.__names['''self.p_CARDS[2]=15 '''] = ('''self.p_CARDS[2]=15 ''',self.guard177,self.act177)

      self.__actions.append(('''self.p_CARDS[2]=16 ''',self.guard178,self.act178))

      self.__names['''self.p_CARDS[2]=16 '''] = ('''self.p_CARDS[2]=16 ''',self.guard178,self.act178)

      self.__actions.append(('''self.p_CARDS[3]=0 ''',self.guard179,self.act179))

      self.__names['''self.p_CARDS[3]=0 '''] = ('''self.p_CARDS[3]=0 ''',self.guard179,self.act179)

      self.__actions.append(('''self.p_CARDS[3]=1 ''',self.guard180,self.act180))

      self.__names['''self.p_CARDS[3]=1 '''] = ('''self.p_CARDS[3]=1 ''',self.guard180,self.act180)

      self.__actions.append(('''self.p_CARDS[3]=2 ''',self.guard181,self.act181))

      self.__names['''self.p_CARDS[3]=2 '''] = ('''self.p_CARDS[3]=2 ''',self.guard181,self.act181)

      self.__actions.append(('''self.p_CARDS[3]=3 ''',self.guard182,self.act182))

      self.__names['''self.p_CARDS[3]=3 '''] = ('''self.p_CARDS[3]=3 ''',self.guard182,self.act182)

      self.__actions.append(('''self.p_CARDS[3]=4 ''',self.guard183,self.act183))

      self.__names['''self.p_CARDS[3]=4 '''] = ('''self.p_CARDS[3]=4 ''',self.guard183,self.act183)

      self.__actions.append(('''self.p_CARDS[3]=5 ''',self.guard184,self.act184))

      self.__names['''self.p_CARDS[3]=5 '''] = ('''self.p_CARDS[3]=5 ''',self.guard184,self.act184)

      self.__actions.append(('''self.p_CARDS[3]=6 ''',self.guard185,self.act185))

      self.__names['''self.p_CARDS[3]=6 '''] = ('''self.p_CARDS[3]=6 ''',self.guard185,self.act185)

      self.__actions.append(('''self.p_CARDS[3]=7 ''',self.guard186,self.act186))

      self.__names['''self.p_CARDS[3]=7 '''] = ('''self.p_CARDS[3]=7 ''',self.guard186,self.act186)

      self.__actions.append(('''self.p_CARDS[3]=8 ''',self.guard187,self.act187))

      self.__names['''self.p_CARDS[3]=8 '''] = ('''self.p_CARDS[3]=8 ''',self.guard187,self.act187)

      self.__actions.append(('''self.p_CARDS[3]=9 ''',self.guard188,self.act188))

      self.__names['''self.p_CARDS[3]=9 '''] = ('''self.p_CARDS[3]=9 ''',self.guard188,self.act188)

      self.__actions.append(('''self.p_CARDS[3]=10 ''',self.guard189,self.act189))

      self.__names['''self.p_CARDS[3]=10 '''] = ('''self.p_CARDS[3]=10 ''',self.guard189,self.act189)

      self.__actions.append(('''self.p_CARDS[3]=11 ''',self.guard190,self.act190))

      self.__names['''self.p_CARDS[3]=11 '''] = ('''self.p_CARDS[3]=11 ''',self.guard190,self.act190)

      self.__actions.append(('''self.p_CARDS[3]=12 ''',self.guard191,self.act191))

      self.__names['''self.p_CARDS[3]=12 '''] = ('''self.p_CARDS[3]=12 ''',self.guard191,self.act191)

      self.__actions.append(('''self.p_CARDS[3]=13 ''',self.guard192,self.act192))

      self.__names['''self.p_CARDS[3]=13 '''] = ('''self.p_CARDS[3]=13 ''',self.guard192,self.act192)

      self.__actions.append(('''self.p_CARDS[3]=14 ''',self.guard193,self.act193))

      self.__names['''self.p_CARDS[3]=14 '''] = ('''self.p_CARDS[3]=14 ''',self.guard193,self.act193)

      self.__actions.append(('''self.p_CARDS[3]=15 ''',self.guard194,self.act194))

      self.__names['''self.p_CARDS[3]=15 '''] = ('''self.p_CARDS[3]=15 ''',self.guard194,self.act194)

      self.__actions.append(('''self.p_CARDS[3]=16 ''',self.guard195,self.act195))

      self.__names['''self.p_CARDS[3]=16 '''] = ('''self.p_CARDS[3]=16 ''',self.guard195,self.act195)

      self.__actions.append(('''self.p_PNUM[0]=2 ''',self.guard196,self.act196))

      self.__names['''self.p_PNUM[0]=2 '''] = ('''self.p_PNUM[0]=2 ''',self.guard196,self.act196)

      self.__actions.append(('''self.p_PNUM[0]=3 ''',self.guard197,self.act197))

      self.__names['''self.p_PNUM[0]=3 '''] = ('''self.p_PNUM[0]=3 ''',self.guard197,self.act197)

      self.__actions.append(('''self.p_PNUM[0]=4 ''',self.guard198,self.act198))

      self.__names['''self.p_PNUM[0]=4 '''] = ('''self.p_PNUM[0]=4 ''',self.guard198,self.act198)

      self.__actions.append(('''self.p_PNUM[1]=2 ''',self.guard199,self.act199))

      self.__names['''self.p_PNUM[1]=2 '''] = ('''self.p_PNUM[1]=2 ''',self.guard199,self.act199)

      self.__actions.append(('''self.p_PNUM[1]=3 ''',self.guard200,self.act200))

      self.__names['''self.p_PNUM[1]=3 '''] = ('''self.p_PNUM[1]=3 ''',self.guard200,self.act200)

      self.__actions.append(('''self.p_PNUM[1]=4 ''',self.guard201,self.act201))

      self.__names['''self.p_PNUM[1]=4 '''] = ('''self.p_PNUM[1]=4 ''',self.guard201,self.act201)

      self.__actions.append(('''self.p_PNUM[2]=2 ''',self.guard202,self.act202))

      self.__names['''self.p_PNUM[2]=2 '''] = ('''self.p_PNUM[2]=2 ''',self.guard202,self.act202)

      self.__actions.append(('''self.p_PNUM[2]=3 ''',self.guard203,self.act203))

      self.__names['''self.p_PNUM[2]=3 '''] = ('''self.p_PNUM[2]=3 ''',self.guard203,self.act203)

      self.__actions.append(('''self.p_PNUM[2]=4 ''',self.guard204,self.act204))

      self.__names['''self.p_PNUM[2]=4 '''] = ('''self.p_PNUM[2]=4 ''',self.guard204,self.act204)

      self.__actions.append(('''self.p_PNUM[3]=2 ''',self.guard205,self.act205))

      self.__names['''self.p_PNUM[3]=2 '''] = ('''self.p_PNUM[3]=2 ''',self.guard205,self.act205)

      self.__actions.append(('''self.p_PNUM[3]=3 ''',self.guard206,self.act206))

      self.__names['''self.p_PNUM[3]=3 '''] = ('''self.p_PNUM[3]=3 ''',self.guard206,self.act206)

      self.__actions.append(('''self.p_PNUM[3]=4 ''',self.guard207,self.act207))

      self.__names['''self.p_PNUM[3]=4 '''] = ('''self.p_PNUM[3]=4 ''',self.guard207,self.act207)

      self.__actions.append(('''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[0], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[0]) ''',self.guard208,self.act208))

      self.__names['''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[0], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[0]) '''] = ('''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[0], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[0]) ''',self.guard208,self.act208)

      self.__actions.append(('''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[0], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[1]) ''',self.guard209,self.act209))

      self.__names['''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[0], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[1]) '''] = ('''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[0], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[1]) ''',self.guard209,self.act209)

      self.__actions.append(('''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[0], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[2]) ''',self.guard210,self.act210))

      self.__names['''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[0], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[2]) '''] = ('''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[0], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[2]) ''',self.guard210,self.act210)

      self.__actions.append(('''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[0], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[3]) ''',self.guard211,self.act211))

      self.__names['''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[0], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[3]) '''] = ('''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[0], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[3]) ''',self.guard211,self.act211)

      self.__actions.append(('''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[1], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[0]) ''',self.guard212,self.act212))

      self.__names['''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[1], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[0]) '''] = ('''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[1], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[0]) ''',self.guard212,self.act212)

      self.__actions.append(('''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[1], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[1]) ''',self.guard213,self.act213))

      self.__names['''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[1], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[1]) '''] = ('''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[1], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[1]) ''',self.guard213,self.act213)

      self.__actions.append(('''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[1], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[2]) ''',self.guard214,self.act214))

      self.__names['''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[1], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[2]) '''] = ('''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[1], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[2]) ''',self.guard214,self.act214)

      self.__actions.append(('''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[1], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[3]) ''',self.guard215,self.act215))

      self.__names['''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[1], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[3]) '''] = ('''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[1], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[3]) ''',self.guard215,self.act215)

      self.__actions.append(('''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[2], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[0]) ''',self.guard216,self.act216))

      self.__names['''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[2], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[0]) '''] = ('''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[2], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[0]) ''',self.guard216,self.act216)

      self.__actions.append(('''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[2], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[1]) ''',self.guard217,self.act217))

      self.__names['''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[2], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[1]) '''] = ('''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[2], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[1]) ''',self.guard217,self.act217)

      self.__actions.append(('''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[2], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[2]) ''',self.guard218,self.act218))

      self.__names['''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[2], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[2]) '''] = ('''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[2], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[2]) ''',self.guard218,self.act218)

      self.__actions.append(('''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[2], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[3]) ''',self.guard219,self.act219))

      self.__names['''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[2], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[3]) '''] = ('''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[2], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[3]) ''',self.guard219,self.act219)

      self.__actions.append(('''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[3], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[0]) ''',self.guard220,self.act220))

      self.__names['''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[3], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[0]) '''] = ('''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[3], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[0]) ''',self.guard220,self.act220)

      self.__actions.append(('''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[3], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[1]) ''',self.guard221,self.act221))

      self.__names['''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[3], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[1]) '''] = ('''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[3], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[1]) ''',self.guard221,self.act221)

      self.__actions.append(('''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[3], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[2]) ''',self.guard222,self.act222))

      self.__names['''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[3], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[2]) '''] = ('''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[3], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[2]) ''',self.guard222,self.act222)

      self.__actions.append(('''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[3], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[3]) ''',self.guard223,self.act223))

      self.__names['''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[3], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[3]) '''] = ('''self.p_DOM[0]=dominion.initializeGame(self.p_PNUM[3], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[3]) ''',self.guard223,self.act223)

      self.__actions.append(('''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[0], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[0]) ''',self.guard224,self.act224))

      self.__names['''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[0], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[0]) '''] = ('''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[0], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[0]) ''',self.guard224,self.act224)

      self.__actions.append(('''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[0], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[1]) ''',self.guard225,self.act225))

      self.__names['''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[0], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[1]) '''] = ('''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[0], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[1]) ''',self.guard225,self.act225)

      self.__actions.append(('''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[0], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[2]) ''',self.guard226,self.act226))

      self.__names['''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[0], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[2]) '''] = ('''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[0], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[2]) ''',self.guard226,self.act226)

      self.__actions.append(('''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[0], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[3]) ''',self.guard227,self.act227))

      self.__names['''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[0], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[3]) '''] = ('''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[0], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[3]) ''',self.guard227,self.act227)

      self.__actions.append(('''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[1], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[0]) ''',self.guard228,self.act228))

      self.__names['''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[1], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[0]) '''] = ('''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[1], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[0]) ''',self.guard228,self.act228)

      self.__actions.append(('''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[1], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[1]) ''',self.guard229,self.act229))

      self.__names['''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[1], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[1]) '''] = ('''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[1], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[1]) ''',self.guard229,self.act229)

      self.__actions.append(('''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[1], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[2]) ''',self.guard230,self.act230))

      self.__names['''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[1], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[2]) '''] = ('''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[1], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[2]) ''',self.guard230,self.act230)

      self.__actions.append(('''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[1], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[3]) ''',self.guard231,self.act231))

      self.__names['''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[1], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[3]) '''] = ('''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[1], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[3]) ''',self.guard231,self.act231)

      self.__actions.append(('''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[2], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[0]) ''',self.guard232,self.act232))

      self.__names['''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[2], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[0]) '''] = ('''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[2], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[0]) ''',self.guard232,self.act232)

      self.__actions.append(('''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[2], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[1]) ''',self.guard233,self.act233))

      self.__names['''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[2], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[1]) '''] = ('''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[2], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[1]) ''',self.guard233,self.act233)

      self.__actions.append(('''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[2], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[2]) ''',self.guard234,self.act234))

      self.__names['''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[2], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[2]) '''] = ('''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[2], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[2]) ''',self.guard234,self.act234)

      self.__actions.append(('''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[2], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[3]) ''',self.guard235,self.act235))

      self.__names['''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[2], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[3]) '''] = ('''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[2], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[3]) ''',self.guard235,self.act235)

      self.__actions.append(('''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[3], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[0]) ''',self.guard236,self.act236))

      self.__names['''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[3], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[0]) '''] = ('''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[3], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[0]) ''',self.guard236,self.act236)

      self.__actions.append(('''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[3], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[1]) ''',self.guard237,self.act237))

      self.__names['''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[3], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[1]) '''] = ('''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[3], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[1]) ''',self.guard237,self.act237)

      self.__actions.append(('''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[3], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[2]) ''',self.guard238,self.act238))

      self.__names['''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[3], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[2]) '''] = ('''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[3], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[2]) ''',self.guard238,self.act238)

      self.__actions.append(('''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[3], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[3]) ''',self.guard239,self.act239))

      self.__names['''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[3], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[3]) '''] = ('''self.p_DOM[1]=dominion.initializeGame(self.p_PNUM[3], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], self.p_INT[3]) ''',self.guard239,self.act239)

      self.__actions.append(('''__result = dominion.buyCard(self.p_CARDS[0],self.p_DOM[0]) ''',self.guard240,self.act240))

      self.__names['''__result = dominion.buyCard(self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.buyCard(self.p_CARDS[0],self.p_DOM[0]) ''',self.guard240,self.act240)

      self.__actions.append(('''__result = dominion.buyCard(self.p_CARDS[0],self.p_DOM[1]) ''',self.guard241,self.act241))

      self.__names['''__result = dominion.buyCard(self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.buyCard(self.p_CARDS[0],self.p_DOM[1]) ''',self.guard241,self.act241)

      self.__actions.append(('''__result = dominion.buyCard(self.p_CARDS[1],self.p_DOM[0]) ''',self.guard242,self.act242))

      self.__names['''__result = dominion.buyCard(self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.buyCard(self.p_CARDS[1],self.p_DOM[0]) ''',self.guard242,self.act242)

      self.__actions.append(('''__result = dominion.buyCard(self.p_CARDS[1],self.p_DOM[1]) ''',self.guard243,self.act243))

      self.__names['''__result = dominion.buyCard(self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.buyCard(self.p_CARDS[1],self.p_DOM[1]) ''',self.guard243,self.act243)

      self.__actions.append(('''__result = dominion.buyCard(self.p_CARDS[2],self.p_DOM[0]) ''',self.guard244,self.act244))

      self.__names['''__result = dominion.buyCard(self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.buyCard(self.p_CARDS[2],self.p_DOM[0]) ''',self.guard244,self.act244)

      self.__actions.append(('''__result = dominion.buyCard(self.p_CARDS[2],self.p_DOM[1]) ''',self.guard245,self.act245))

      self.__names['''__result = dominion.buyCard(self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.buyCard(self.p_CARDS[2],self.p_DOM[1]) ''',self.guard245,self.act245)

      self.__actions.append(('''__result = dominion.buyCard(self.p_CARDS[3],self.p_DOM[0]) ''',self.guard246,self.act246))

      self.__names['''__result = dominion.buyCard(self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.buyCard(self.p_CARDS[3],self.p_DOM[0]) ''',self.guard246,self.act246)

      self.__actions.append(('''__result = dominion.buyCard(self.p_CARDS[3],self.p_DOM[1]) ''',self.guard247,self.act247))

      self.__names['''__result = dominion.buyCard(self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.buyCard(self.p_CARDS[3],self.p_DOM[1]) ''',self.guard247,self.act247)

      self.__actions.append(('''__result = dominion.endTurn(self.p_DOM[0]) ''',self.guard248,self.act248))

      self.__names['''__result = dominion.endTurn(self.p_DOM[0]) '''] = ('''__result = dominion.endTurn(self.p_DOM[0]) ''',self.guard248,self.act248)

      self.__actions.append(('''__result = dominion.endTurn(self.p_DOM[1]) ''',self.guard249,self.act249))

      self.__names['''__result = dominion.endTurn(self.p_DOM[1]) '''] = ('''__result = dominion.endTurn(self.p_DOM[1]) ''',self.guard249,self.act249)

      self.__actions.append(('''__result = dominion.isGameOver(self.p_DOM[0]) ''',self.guard250,self.act250))

      self.__names['''__result = dominion.isGameOver(self.p_DOM[0]) '''] = ('''__result = dominion.isGameOver(self.p_DOM[0]) ''',self.guard250,self.act250)

      self.__actions.append(('''__result = dominion.isGameOver(self.p_DOM[1]) ''',self.guard251,self.act251))

      self.__names['''__result = dominion.isGameOver(self.p_DOM[1]) '''] = ('''__result = dominion.isGameOver(self.p_DOM[1]) ''',self.guard251,self.act251)

      self.__actions.append(('''__result = dominion.whoseTurn(self.p_DOM[0]) ''',self.guard252,self.act252))

      self.__names['''__result = dominion.whoseTurn(self.p_DOM[0]) '''] = ('''__result = dominion.whoseTurn(self.p_DOM[0]) ''',self.guard252,self.act252)

      self.__actions.append(('''__result = dominion.whoseTurn(self.p_DOM[1]) ''',self.guard253,self.act253))

      self.__names['''__result = dominion.whoseTurn(self.p_DOM[1]) '''] = ('''__result = dominion.whoseTurn(self.p_DOM[1]) ''',self.guard253,self.act253)

      self.__actions.append(('''__result = dominion.scoreFor(self.p_PNUM[0],self.p_DOM[0]) ''',self.guard254,self.act254))

      self.__names['''__result = dominion.scoreFor(self.p_PNUM[0],self.p_DOM[0]) '''] = ('''__result = dominion.scoreFor(self.p_PNUM[0],self.p_DOM[0]) ''',self.guard254,self.act254)

      self.__actions.append(('''__result = dominion.scoreFor(self.p_PNUM[0],self.p_DOM[1]) ''',self.guard255,self.act255))

      self.__names['''__result = dominion.scoreFor(self.p_PNUM[0],self.p_DOM[1]) '''] = ('''__result = dominion.scoreFor(self.p_PNUM[0],self.p_DOM[1]) ''',self.guard255,self.act255)

      self.__actions.append(('''__result = dominion.scoreFor(self.p_PNUM[1],self.p_DOM[0]) ''',self.guard256,self.act256))

      self.__names['''__result = dominion.scoreFor(self.p_PNUM[1],self.p_DOM[0]) '''] = ('''__result = dominion.scoreFor(self.p_PNUM[1],self.p_DOM[0]) ''',self.guard256,self.act256)

      self.__actions.append(('''__result = dominion.scoreFor(self.p_PNUM[1],self.p_DOM[1]) ''',self.guard257,self.act257))

      self.__names['''__result = dominion.scoreFor(self.p_PNUM[1],self.p_DOM[1]) '''] = ('''__result = dominion.scoreFor(self.p_PNUM[1],self.p_DOM[1]) ''',self.guard257,self.act257)

      self.__actions.append(('''__result = dominion.scoreFor(self.p_PNUM[2],self.p_DOM[0]) ''',self.guard258,self.act258))

      self.__names['''__result = dominion.scoreFor(self.p_PNUM[2],self.p_DOM[0]) '''] = ('''__result = dominion.scoreFor(self.p_PNUM[2],self.p_DOM[0]) ''',self.guard258,self.act258)

      self.__actions.append(('''__result = dominion.scoreFor(self.p_PNUM[2],self.p_DOM[1]) ''',self.guard259,self.act259))

      self.__names['''__result = dominion.scoreFor(self.p_PNUM[2],self.p_DOM[1]) '''] = ('''__result = dominion.scoreFor(self.p_PNUM[2],self.p_DOM[1]) ''',self.guard259,self.act259)

      self.__actions.append(('''__result = dominion.scoreFor(self.p_PNUM[3],self.p_DOM[0]) ''',self.guard260,self.act260))

      self.__names['''__result = dominion.scoreFor(self.p_PNUM[3],self.p_DOM[0]) '''] = ('''__result = dominion.scoreFor(self.p_PNUM[3],self.p_DOM[0]) ''',self.guard260,self.act260)

      self.__actions.append(('''__result = dominion.scoreFor(self.p_PNUM[3],self.p_DOM[1]) ''',self.guard261,self.act261))

      self.__names['''__result = dominion.scoreFor(self.p_PNUM[3],self.p_DOM[1]) '''] = ('''__result = dominion.scoreFor(self.p_PNUM[3],self.p_DOM[1]) ''',self.guard261,self.act261)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard262,self.act262))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard262,self.act262)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard263,self.act263))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard263,self.act263)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard264,self.act264))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard264,self.act264)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard265,self.act265))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard265,self.act265)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard266,self.act266))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard266,self.act266)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard267,self.act267))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard267,self.act267)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard268,self.act268))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard268,self.act268)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard269,self.act269))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard269,self.act269)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard270,self.act270))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard270,self.act270)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard271,self.act271))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard271,self.act271)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard272,self.act272))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard272,self.act272)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard273,self.act273))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard273,self.act273)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard274,self.act274))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard274,self.act274)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard275,self.act275))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard275,self.act275)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard276,self.act276))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard276,self.act276)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard277,self.act277))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard277,self.act277)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard278,self.act278))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard278,self.act278)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard279,self.act279))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard279,self.act279)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard280,self.act280))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard280,self.act280)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard281,self.act281))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard281,self.act281)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard282,self.act282))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard282,self.act282)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard283,self.act283))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard283,self.act283)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard284,self.act284))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard284,self.act284)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard285,self.act285))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard285,self.act285)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard286,self.act286))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard286,self.act286)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard287,self.act287))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard287,self.act287)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard288,self.act288))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard288,self.act288)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard289,self.act289))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard289,self.act289)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard290,self.act290))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard290,self.act290)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard291,self.act291))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard291,self.act291)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard292,self.act292))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard292,self.act292)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard293,self.act293))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard293,self.act293)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard294,self.act294))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard294,self.act294)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard295,self.act295))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard295,self.act295)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard296,self.act296))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard296,self.act296)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard297,self.act297))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard297,self.act297)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard298,self.act298))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard298,self.act298)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard299,self.act299))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard299,self.act299)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard300,self.act300))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard300,self.act300)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard301,self.act301))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard301,self.act301)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard302,self.act302))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard302,self.act302)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard303,self.act303))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard303,self.act303)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard304,self.act304))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard304,self.act304)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard305,self.act305))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard305,self.act305)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard306,self.act306))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard306,self.act306)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard307,self.act307))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard307,self.act307)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard308,self.act308))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard308,self.act308)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard309,self.act309))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard309,self.act309)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard310,self.act310))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard310,self.act310)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard311,self.act311))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard311,self.act311)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard312,self.act312))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard312,self.act312)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard313,self.act313))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard313,self.act313)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard314,self.act314))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard314,self.act314)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard315,self.act315))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard315,self.act315)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard316,self.act316))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard316,self.act316)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard317,self.act317))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard317,self.act317)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard318,self.act318))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard318,self.act318)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard319,self.act319))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard319,self.act319)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard320,self.act320))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard320,self.act320)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard321,self.act321))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard321,self.act321)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard322,self.act322))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard322,self.act322)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard323,self.act323))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard323,self.act323)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard324,self.act324))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard324,self.act324)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard325,self.act325))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard325,self.act325)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard326,self.act326))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard326,self.act326)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard327,self.act327))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard327,self.act327)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard328,self.act328))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard328,self.act328)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard329,self.act329))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard329,self.act329)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard330,self.act330))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard330,self.act330)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard331,self.act331))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard331,self.act331)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard332,self.act332))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard332,self.act332)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard333,self.act333))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard333,self.act333)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard334,self.act334))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard334,self.act334)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard335,self.act335))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard335,self.act335)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard336,self.act336))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard336,self.act336)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard337,self.act337))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard337,self.act337)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard338,self.act338))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard338,self.act338)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard339,self.act339))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard339,self.act339)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard340,self.act340))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard340,self.act340)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard341,self.act341))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard341,self.act341)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard342,self.act342))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard342,self.act342)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard343,self.act343))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard343,self.act343)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard344,self.act344))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard344,self.act344)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard345,self.act345))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard345,self.act345)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard346,self.act346))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard346,self.act346)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard347,self.act347))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard347,self.act347)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard348,self.act348))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard348,self.act348)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard349,self.act349))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard349,self.act349)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard350,self.act350))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard350,self.act350)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard351,self.act351))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard351,self.act351)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard352,self.act352))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard352,self.act352)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard353,self.act353))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard353,self.act353)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard354,self.act354))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard354,self.act354)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard355,self.act355))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard355,self.act355)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard356,self.act356))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard356,self.act356)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard357,self.act357))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard357,self.act357)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard358,self.act358))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard358,self.act358)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard359,self.act359))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard359,self.act359)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard360,self.act360))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard360,self.act360)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard361,self.act361))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard361,self.act361)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard362,self.act362))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard362,self.act362)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard363,self.act363))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard363,self.act363)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard364,self.act364))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard364,self.act364)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard365,self.act365))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard365,self.act365)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard366,self.act366))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard366,self.act366)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard367,self.act367))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard367,self.act367)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard368,self.act368))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard368,self.act368)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard369,self.act369))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard369,self.act369)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard370,self.act370))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard370,self.act370)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard371,self.act371))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard371,self.act371)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard372,self.act372))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard372,self.act372)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard373,self.act373))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard373,self.act373)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard374,self.act374))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard374,self.act374)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard375,self.act375))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard375,self.act375)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard376,self.act376))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard376,self.act376)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard377,self.act377))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard377,self.act377)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard378,self.act378))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard378,self.act378)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard379,self.act379))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard379,self.act379)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard380,self.act380))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard380,self.act380)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard381,self.act381))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard381,self.act381)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard382,self.act382))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard382,self.act382)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard383,self.act383))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard383,self.act383)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard384,self.act384))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard384,self.act384)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard385,self.act385))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard385,self.act385)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard386,self.act386))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard386,self.act386)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard387,self.act387))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard387,self.act387)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard388,self.act388))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard388,self.act388)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard389,self.act389))

      self.__names['''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[0],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard389,self.act389)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard390,self.act390))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard390,self.act390)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard391,self.act391))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard391,self.act391)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard392,self.act392))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard392,self.act392)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard393,self.act393))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard393,self.act393)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard394,self.act394))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard394,self.act394)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard395,self.act395))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard395,self.act395)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard396,self.act396))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard396,self.act396)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard397,self.act397))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard397,self.act397)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard398,self.act398))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard398,self.act398)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard399,self.act399))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard399,self.act399)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard400,self.act400))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard400,self.act400)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard401,self.act401))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard401,self.act401)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard402,self.act402))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard402,self.act402)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard403,self.act403))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard403,self.act403)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard404,self.act404))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard404,self.act404)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard405,self.act405))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard405,self.act405)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard406,self.act406))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard406,self.act406)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard407,self.act407))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard407,self.act407)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard408,self.act408))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard408,self.act408)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard409,self.act409))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard409,self.act409)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard410,self.act410))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard410,self.act410)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard411,self.act411))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard411,self.act411)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard412,self.act412))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard412,self.act412)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard413,self.act413))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard413,self.act413)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard414,self.act414))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard414,self.act414)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard415,self.act415))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard415,self.act415)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard416,self.act416))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard416,self.act416)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard417,self.act417))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard417,self.act417)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard418,self.act418))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard418,self.act418)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard419,self.act419))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard419,self.act419)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard420,self.act420))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard420,self.act420)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard421,self.act421))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard421,self.act421)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard422,self.act422))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard422,self.act422)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard423,self.act423))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard423,self.act423)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard424,self.act424))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard424,self.act424)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard425,self.act425))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard425,self.act425)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard426,self.act426))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard426,self.act426)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard427,self.act427))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard427,self.act427)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard428,self.act428))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard428,self.act428)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard429,self.act429))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard429,self.act429)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard430,self.act430))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard430,self.act430)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard431,self.act431))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard431,self.act431)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard432,self.act432))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard432,self.act432)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard433,self.act433))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard433,self.act433)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard434,self.act434))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard434,self.act434)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard435,self.act435))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard435,self.act435)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard436,self.act436))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard436,self.act436)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard437,self.act437))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard437,self.act437)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard438,self.act438))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard438,self.act438)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard439,self.act439))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard439,self.act439)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard440,self.act440))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard440,self.act440)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard441,self.act441))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard441,self.act441)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard442,self.act442))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard442,self.act442)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard443,self.act443))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard443,self.act443)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard444,self.act444))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard444,self.act444)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard445,self.act445))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard445,self.act445)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard446,self.act446))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard446,self.act446)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard447,self.act447))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard447,self.act447)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard448,self.act448))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard448,self.act448)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard449,self.act449))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard449,self.act449)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard450,self.act450))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard450,self.act450)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard451,self.act451))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard451,self.act451)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard452,self.act452))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard452,self.act452)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard453,self.act453))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard453,self.act453)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard454,self.act454))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard454,self.act454)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard455,self.act455))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard455,self.act455)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard456,self.act456))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard456,self.act456)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard457,self.act457))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard457,self.act457)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard458,self.act458))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard458,self.act458)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard459,self.act459))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard459,self.act459)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard460,self.act460))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard460,self.act460)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard461,self.act461))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard461,self.act461)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard462,self.act462))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard462,self.act462)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard463,self.act463))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard463,self.act463)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard464,self.act464))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard464,self.act464)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard465,self.act465))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard465,self.act465)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard466,self.act466))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard466,self.act466)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard467,self.act467))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard467,self.act467)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard468,self.act468))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard468,self.act468)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard469,self.act469))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard469,self.act469)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard470,self.act470))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard470,self.act470)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard471,self.act471))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard471,self.act471)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard472,self.act472))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard472,self.act472)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard473,self.act473))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard473,self.act473)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard474,self.act474))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard474,self.act474)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard475,self.act475))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard475,self.act475)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard476,self.act476))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard476,self.act476)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard477,self.act477))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard477,self.act477)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard478,self.act478))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard478,self.act478)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard479,self.act479))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard479,self.act479)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard480,self.act480))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard480,self.act480)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard481,self.act481))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard481,self.act481)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard482,self.act482))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard482,self.act482)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard483,self.act483))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard483,self.act483)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard484,self.act484))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard484,self.act484)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard485,self.act485))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard485,self.act485)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard486,self.act486))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard486,self.act486)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard487,self.act487))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard487,self.act487)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard488,self.act488))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard488,self.act488)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard489,self.act489))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard489,self.act489)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard490,self.act490))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard490,self.act490)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard491,self.act491))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard491,self.act491)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard492,self.act492))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard492,self.act492)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard493,self.act493))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard493,self.act493)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard494,self.act494))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard494,self.act494)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard495,self.act495))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard495,self.act495)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard496,self.act496))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard496,self.act496)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard497,self.act497))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard497,self.act497)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard498,self.act498))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard498,self.act498)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard499,self.act499))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard499,self.act499)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard500,self.act500))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard500,self.act500)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard501,self.act501))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard501,self.act501)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard502,self.act502))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard502,self.act502)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard503,self.act503))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard503,self.act503)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard504,self.act504))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard504,self.act504)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard505,self.act505))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard505,self.act505)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard506,self.act506))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard506,self.act506)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard507,self.act507))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard507,self.act507)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard508,self.act508))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard508,self.act508)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard509,self.act509))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard509,self.act509)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard510,self.act510))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard510,self.act510)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard511,self.act511))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard511,self.act511)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard512,self.act512))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard512,self.act512)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard513,self.act513))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard513,self.act513)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard514,self.act514))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard514,self.act514)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard515,self.act515))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard515,self.act515)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard516,self.act516))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard516,self.act516)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard517,self.act517))

      self.__names['''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[1],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard517,self.act517)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard518,self.act518))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard518,self.act518)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard519,self.act519))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard519,self.act519)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard520,self.act520))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard520,self.act520)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard521,self.act521))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard521,self.act521)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard522,self.act522))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard522,self.act522)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard523,self.act523))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard523,self.act523)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard524,self.act524))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard524,self.act524)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard525,self.act525))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard525,self.act525)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard526,self.act526))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard526,self.act526)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard527,self.act527))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard527,self.act527)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard528,self.act528))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard528,self.act528)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard529,self.act529))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard529,self.act529)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard530,self.act530))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard530,self.act530)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard531,self.act531))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard531,self.act531)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard532,self.act532))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard532,self.act532)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard533,self.act533))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard533,self.act533)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard534,self.act534))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard534,self.act534)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard535,self.act535))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard535,self.act535)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard536,self.act536))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard536,self.act536)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard537,self.act537))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard537,self.act537)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard538,self.act538))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard538,self.act538)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard539,self.act539))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard539,self.act539)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard540,self.act540))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard540,self.act540)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard541,self.act541))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard541,self.act541)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard542,self.act542))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard542,self.act542)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard543,self.act543))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard543,self.act543)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard544,self.act544))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard544,self.act544)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard545,self.act545))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard545,self.act545)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard546,self.act546))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard546,self.act546)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard547,self.act547))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard547,self.act547)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard548,self.act548))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard548,self.act548)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard549,self.act549))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard549,self.act549)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard550,self.act550))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard550,self.act550)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard551,self.act551))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard551,self.act551)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard552,self.act552))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard552,self.act552)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard553,self.act553))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard553,self.act553)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard554,self.act554))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard554,self.act554)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard555,self.act555))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard555,self.act555)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard556,self.act556))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard556,self.act556)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard557,self.act557))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard557,self.act557)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard558,self.act558))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard558,self.act558)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard559,self.act559))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard559,self.act559)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard560,self.act560))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard560,self.act560)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard561,self.act561))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard561,self.act561)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard562,self.act562))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard562,self.act562)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard563,self.act563))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard563,self.act563)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard564,self.act564))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard564,self.act564)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard565,self.act565))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard565,self.act565)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard566,self.act566))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard566,self.act566)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard567,self.act567))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard567,self.act567)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard568,self.act568))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard568,self.act568)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard569,self.act569))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard569,self.act569)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard570,self.act570))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard570,self.act570)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard571,self.act571))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard571,self.act571)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard572,self.act572))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard572,self.act572)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard573,self.act573))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard573,self.act573)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard574,self.act574))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard574,self.act574)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard575,self.act575))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard575,self.act575)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard576,self.act576))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard576,self.act576)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard577,self.act577))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard577,self.act577)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard578,self.act578))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard578,self.act578)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard579,self.act579))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard579,self.act579)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard580,self.act580))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard580,self.act580)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard581,self.act581))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard581,self.act581)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard582,self.act582))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard582,self.act582)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard583,self.act583))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard583,self.act583)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard584,self.act584))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard584,self.act584)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard585,self.act585))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard585,self.act585)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard586,self.act586))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard586,self.act586)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard587,self.act587))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard587,self.act587)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard588,self.act588))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard588,self.act588)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard589,self.act589))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard589,self.act589)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard590,self.act590))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard590,self.act590)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard591,self.act591))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard591,self.act591)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard592,self.act592))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard592,self.act592)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard593,self.act593))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard593,self.act593)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard594,self.act594))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard594,self.act594)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard595,self.act595))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard595,self.act595)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard596,self.act596))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard596,self.act596)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard597,self.act597))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard597,self.act597)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard598,self.act598))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard598,self.act598)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard599,self.act599))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard599,self.act599)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard600,self.act600))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard600,self.act600)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard601,self.act601))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard601,self.act601)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard602,self.act602))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard602,self.act602)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard603,self.act603))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard603,self.act603)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard604,self.act604))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard604,self.act604)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard605,self.act605))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard605,self.act605)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard606,self.act606))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard606,self.act606)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard607,self.act607))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard607,self.act607)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard608,self.act608))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard608,self.act608)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard609,self.act609))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard609,self.act609)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard610,self.act610))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard610,self.act610)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard611,self.act611))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard611,self.act611)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard612,self.act612))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard612,self.act612)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard613,self.act613))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard613,self.act613)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard614,self.act614))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard614,self.act614)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard615,self.act615))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard615,self.act615)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard616,self.act616))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard616,self.act616)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard617,self.act617))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard617,self.act617)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard618,self.act618))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard618,self.act618)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard619,self.act619))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard619,self.act619)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard620,self.act620))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard620,self.act620)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard621,self.act621))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard621,self.act621)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard622,self.act622))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard622,self.act622)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard623,self.act623))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard623,self.act623)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard624,self.act624))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard624,self.act624)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard625,self.act625))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard625,self.act625)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard626,self.act626))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard626,self.act626)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard627,self.act627))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard627,self.act627)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard628,self.act628))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard628,self.act628)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard629,self.act629))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard629,self.act629)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard630,self.act630))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard630,self.act630)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard631,self.act631))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard631,self.act631)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard632,self.act632))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard632,self.act632)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard633,self.act633))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard633,self.act633)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard634,self.act634))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard634,self.act634)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard635,self.act635))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard635,self.act635)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard636,self.act636))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard636,self.act636)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard637,self.act637))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard637,self.act637)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard638,self.act638))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard638,self.act638)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard639,self.act639))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard639,self.act639)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard640,self.act640))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard640,self.act640)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard641,self.act641))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard641,self.act641)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard642,self.act642))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard642,self.act642)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard643,self.act643))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard643,self.act643)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard644,self.act644))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard644,self.act644)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard645,self.act645))

      self.__names['''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[2],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard645,self.act645)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard646,self.act646))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard646,self.act646)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard647,self.act647))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard647,self.act647)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard648,self.act648))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard648,self.act648)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard649,self.act649))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard649,self.act649)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard650,self.act650))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard650,self.act650)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard651,self.act651))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard651,self.act651)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard652,self.act652))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard652,self.act652)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard653,self.act653))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard653,self.act653)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard654,self.act654))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard654,self.act654)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard655,self.act655))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard655,self.act655)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard656,self.act656))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard656,self.act656)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard657,self.act657))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard657,self.act657)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard658,self.act658))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard658,self.act658)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard659,self.act659))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard659,self.act659)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard660,self.act660))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard660,self.act660)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard661,self.act661))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard661,self.act661)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard662,self.act662))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard662,self.act662)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard663,self.act663))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard663,self.act663)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard664,self.act664))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard664,self.act664)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard665,self.act665))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard665,self.act665)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard666,self.act666))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard666,self.act666)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard667,self.act667))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard667,self.act667)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard668,self.act668))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard668,self.act668)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard669,self.act669))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard669,self.act669)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard670,self.act670))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard670,self.act670)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard671,self.act671))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard671,self.act671)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard672,self.act672))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard672,self.act672)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard673,self.act673))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard673,self.act673)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard674,self.act674))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard674,self.act674)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard675,self.act675))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard675,self.act675)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard676,self.act676))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard676,self.act676)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard677,self.act677))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[0],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard677,self.act677)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard678,self.act678))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard678,self.act678)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard679,self.act679))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard679,self.act679)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard680,self.act680))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard680,self.act680)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard681,self.act681))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard681,self.act681)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard682,self.act682))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard682,self.act682)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard683,self.act683))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard683,self.act683)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard684,self.act684))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard684,self.act684)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard685,self.act685))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard685,self.act685)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard686,self.act686))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard686,self.act686)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard687,self.act687))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard687,self.act687)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard688,self.act688))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard688,self.act688)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard689,self.act689))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard689,self.act689)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard690,self.act690))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard690,self.act690)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard691,self.act691))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard691,self.act691)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard692,self.act692))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard692,self.act692)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard693,self.act693))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard693,self.act693)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard694,self.act694))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard694,self.act694)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard695,self.act695))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard695,self.act695)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard696,self.act696))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard696,self.act696)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard697,self.act697))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard697,self.act697)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard698,self.act698))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard698,self.act698)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard699,self.act699))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard699,self.act699)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard700,self.act700))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard700,self.act700)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard701,self.act701))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard701,self.act701)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard702,self.act702))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard702,self.act702)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard703,self.act703))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard703,self.act703)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard704,self.act704))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard704,self.act704)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard705,self.act705))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard705,self.act705)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard706,self.act706))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard706,self.act706)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard707,self.act707))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard707,self.act707)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard708,self.act708))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard708,self.act708)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard709,self.act709))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[1],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard709,self.act709)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard710,self.act710))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard710,self.act710)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard711,self.act711))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard711,self.act711)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard712,self.act712))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard712,self.act712)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard713,self.act713))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard713,self.act713)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard714,self.act714))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard714,self.act714)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard715,self.act715))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard715,self.act715)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard716,self.act716))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard716,self.act716)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard717,self.act717))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard717,self.act717)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard718,self.act718))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard718,self.act718)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard719,self.act719))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard719,self.act719)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard720,self.act720))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard720,self.act720)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard721,self.act721))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard721,self.act721)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard722,self.act722))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard722,self.act722)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard723,self.act723))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard723,self.act723)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard724,self.act724))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard724,self.act724)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard725,self.act725))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard725,self.act725)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard726,self.act726))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard726,self.act726)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard727,self.act727))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard727,self.act727)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard728,self.act728))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard728,self.act728)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard729,self.act729))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard729,self.act729)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard730,self.act730))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard730,self.act730)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard731,self.act731))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard731,self.act731)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard732,self.act732))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard732,self.act732)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard733,self.act733))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard733,self.act733)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard734,self.act734))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard734,self.act734)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard735,self.act735))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard735,self.act735)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard736,self.act736))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard736,self.act736)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard737,self.act737))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard737,self.act737)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard738,self.act738))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard738,self.act738)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard739,self.act739))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard739,self.act739)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard740,self.act740))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard740,self.act740)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard741,self.act741))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[2],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard741,self.act741)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard742,self.act742))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard742,self.act742)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard743,self.act743))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard743,self.act743)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard744,self.act744))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard744,self.act744)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard745,self.act745))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard745,self.act745)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard746,self.act746))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard746,self.act746)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard747,self.act747))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard747,self.act747)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard748,self.act748))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard748,self.act748)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard749,self.act749))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[0],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard749,self.act749)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard750,self.act750))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard750,self.act750)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard751,self.act751))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard751,self.act751)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard752,self.act752))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard752,self.act752)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard753,self.act753))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard753,self.act753)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard754,self.act754))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard754,self.act754)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard755,self.act755))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard755,self.act755)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard756,self.act756))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard756,self.act756)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard757,self.act757))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[1],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard757,self.act757)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard758,self.act758))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard758,self.act758)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard759,self.act759))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard759,self.act759)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard760,self.act760))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard760,self.act760)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard761,self.act761))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard761,self.act761)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard762,self.act762))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard762,self.act762)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard763,self.act763))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard763,self.act763)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard764,self.act764))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard764,self.act764)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard765,self.act765))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[2],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard765,self.act765)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard766,self.act766))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[0]) ''',self.guard766,self.act766)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard767,self.act767))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[0],self.p_DOM[1]) ''',self.guard767,self.act767)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard768,self.act768))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[0]) ''',self.guard768,self.act768)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard769,self.act769))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[1],self.p_DOM[1]) ''',self.guard769,self.act769)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard770,self.act770))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[0]) ''',self.guard770,self.act770)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard771,self.act771))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[2],self.p_DOM[1]) ''',self.guard771,self.act771)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard772,self.act772))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[0]) ''',self.guard772,self.act772)

      self.__actions.append(('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard773,self.act773))

      self.__names['''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) '''] = ('''__result = dominion.playCard(self.p_SINT[3],self.p_CARDS[3],self.p_CARDS[3],self.p_CARDS[3],self.p_DOM[1]) ''',self.guard773,self.act773)

      self.__actions.append(('''__result = sorted(dominion.thehand(self.p_DOM[0])) ''',self.guard774,self.act774))

      self.__names['''__result = sorted(dominion.thehand(self.p_DOM[0])) '''] = ('''__result = sorted(dominion.thehand(self.p_DOM[0])) ''',self.guard774,self.act774)

      self.__actions.append(('''__result = sorted(dominion.thehand(self.p_DOM[1])) ''',self.guard775,self.act775))

      self.__names['''__result = sorted(dominion.thehand(self.p_DOM[1])) '''] = ('''__result = sorted(dominion.thehand(self.p_DOM[1])) ''',self.guard775,self.act775)

      self.__actions_backup = list(self.__actions)
   def restart(self):
      self.__currBranches = set()
      self.__currStatements = set()
      self.__newCurrBranches = set()
      self.__newCurrStatements = set()
      reload(dominion)
      reload(dominion2)
      self.p_INT = {}
      self.p_INT_used = {}
      self.p_INT[0] = None
      self.p_INT_used[0] = True
      self.p_INT[1] = None
      self.p_INT_used[1] = True
      self.p_INT[2] = None
      self.p_INT_used[2] = True
      self.p_INT[3] = None
      self.p_INT_used[3] = True
      self.p_INT[4] = None
      self.p_INT_used[4] = True
      self.p_DOM_REF = {}
      self.p_DOM_REF_used = {}
      self.p_DOM_REF[0] = None
      self.p_DOM_REF_used[0] = True
      self.p_DOM_REF[1] = None
      self.p_DOM_REF_used[1] = True
      self.p_DOM_REF[2] = None
      self.p_DOM_REF_used[2] = True
      self.p_DOM = {}
      self.p_DOM_used = {}
      self.p_DOM[0] = None
      self.p_DOM_used[0] = True
      self.p_DOM[1] = None
      self.p_DOM_used[1] = True
      self.p_DOM[2] = None
      self.p_DOM_used[2] = True
      self.p_PNUM = {}
      self.p_PNUM_used = {}
      self.p_PNUM[0] = None
      self.p_PNUM_used[0] = True
      self.p_PNUM[1] = None
      self.p_PNUM_used[1] = True
      self.p_PNUM[2] = None
      self.p_PNUM_used[2] = True
      self.p_PNUM[3] = None
      self.p_PNUM_used[3] = True
      self.p_PNUM[4] = None
      self.p_PNUM_used[4] = True
      self.p_CARDS = {}
      self.p_CARDS_used = {}
      self.p_CARDS[0] = None
      self.p_CARDS_used[0] = True
      self.p_CARDS[1] = None
      self.p_CARDS_used[1] = True
      self.p_CARDS[2] = None
      self.p_CARDS_used[2] = True
      self.p_CARDS[3] = None
      self.p_CARDS_used[3] = True
      self.p_CARDS[4] = None
      self.p_CARDS_used[4] = True
      self.p_SINT = {}
      self.p_SINT_used = {}
      self.p_SINT[0] = None
      self.p_SINT_used[0] = True
      self.p_SINT[1] = None
      self.p_SINT_used[1] = True
      self.p_SINT[2] = None
      self.p_SINT_used[2] = True
      self.p_SINT[3] = None
      self.p_SINT_used[3] = True
      self.p_SINT[4] = None
      self.p_SINT_used[4] = True
   def log(self):
      if self.__log == None:
         return
      if (self.__log == 'All') or (self.__log >= 0):
         try:
            self.__logAction("""dominion.thehand(self.p_DOM[0]) """,dominion.thehand(self.p_DOM[0]) )
         except:
            pass
      if (self.__log == 'All') or (self.__log >= 0):
         try:
            self.__logAction("""dominion2.thehand(self.p_DOM_REF[0]) """,dominion2.thehand(self.p_DOM_REF[0]) )
         except:
            pass
      if (self.__log == 'All') or (self.__log >= 0):
         try:
            self.__logAction("""dominion.thehand(self.p_DOM[1]) """,dominion.thehand(self.p_DOM[1]) )
         except:
            pass
      if (self.__log == 'All') or (self.__log >= 0):
         try:
            self.__logAction("""dominion2.thehand(self.p_DOM_REF[1]) """,dominion2.thehand(self.p_DOM_REF[1]) )
         except:
            pass
   def state(self):
      return [ copy.deepcopy(self.p_INT),copy.deepcopy(self.p_INT_used),copy.deepcopy(self.p_DOM_REF),copy.deepcopy(self.p_DOM_REF_used),copy.deepcopy(self.p_DOM),copy.deepcopy(self.p_DOM_used),copy.deepcopy(self.p_PNUM),copy.deepcopy(self.p_PNUM_used),copy.deepcopy(self.p_CARDS),copy.deepcopy(self.p_CARDS_used),copy.deepcopy(self.p_SINT),copy.deepcopy(self.p_SINT_used)]
   def backtrack(self,old):
      self.p_INT = copy.deepcopy(old[0])
      self.p_INT_used = copy.deepcopy(old[1])
      self.p_DOM_REF = copy.deepcopy(old[2])
      self.p_DOM_REF_used = copy.deepcopy(old[3])
      self.p_DOM = copy.deepcopy(old[4])
      self.p_DOM_used = copy.deepcopy(old[5])
      self.p_PNUM = copy.deepcopy(old[6])
      self.p_PNUM_used = copy.deepcopy(old[7])
      self.p_CARDS = copy.deepcopy(old[8])
      self.p_CARDS_used = copy.deepcopy(old[9])
      self.p_SINT = copy.deepcopy(old[10])
      self.p_SINT_used = copy.deepcopy(old[11])
   def check(self):
      return True
   def enabled(self):
       return filter(lambda (s, g, a): g(), self.__actions)
   
   def features(self):
       return self.__features
   
   def actions(self):
       return self.__actions
   
   def disable(self,f):
       newActions = []
       for (name,act,guard) in self.__actions:
           if not re.match(f,name):
               newActions.append((name,act,guard))
       self.__actions = newActions
   
   def enableAll(self):
       self.__actions = self.__actions_backup
   
   def serializable(self, step):
       return step[0]
   
   def playable(self, name):
       return self.__names[name]
   
   def safely(self, act):
       try:
           act()
       except:
           self.__failure = sys.exc_info()
           return False
       return True
   
   def failure(self):
       return self.__failure
   
   def replay(self, test, catchUncaught = False):
       self.restart()
       for (name, guard, act) in test:
           if guard():
               if catchUncaught:
                   try:
                       act()
                   except:
                       pass
               else:
                   act()
           if not self.check():
               return False
       return True
   
   def replayUntil(self, test, pred, catchUncaught = False):
       self.restart()
       newt = []
       if pred():
           return newt
   
       for (name, guard, act) in test:
   
           newt.append((name, guard, act))
           if guard():
               if catchUncaught:
                   try:
                       act()
                   except:
                       pass
               else:
                   act()
           if pred():
               return newt
           if not self.check():
               return False
       return None
   
   def failsCheck(self, test):
       try:
           return not self.replay(test, catchUncaught = True)
       except:
           return True
       return False
   
   def fails(self, test):
       try:
           return not self.replay(test)
       except:
           return True
       return False
   
   def logOff(self):
       self.__log = None
   
   def logAll(self):
       self.__log = 'All'
   
   def setLog(self, level):
       self.__log = level
   
   def setLogAction(self, f):
       self.__logAction = f
   
   def logPrint(self, code, text):
       print "[LOG " + str(code) + "] " + str(text)
   
   def __candidates(self, t, n):
       candidates = []
       s = len(t) / n
       for i in xrange(0,n):
           tc = t[0:i*s]
           tc.extend(t[(i+1)*s:])
           candidates.append(tc)
       return candidates
   
   def reduce(self, test, pred, pruneGuards = False, keepLast = True):
       if keepLast:
           tb = test[:-1]
           addLast = [test[-1]]
       else:
           tb = test
           addLast = []
       n = 2
       count = 0
       while True:
           count += 1
           c = self.__candidates(tb, n)
           reduced = False
           for tc in c:
               if pred(tc + addLast):
                   tb = tc
                   n = 2
                   if pruneGuards:
                       self.restart()
                       newtb = []
                       for a in tb:
                           if a[1]():
                               newtb.append(a)
                               try:
                                   a[2]()
                               except:
                                   pass
                       tb = newtb
                   reduced = True
                   break
           if not reduced:
               if n == len(tb):
                   return tb + addLast
               n = min(n*2, len(tb))
           elif len(tb) == 1:
               if pred([] + addLast):
                   return ([] + addLast)
               else:
                   return (tb + addLast)
   def __updateCov(self):
       self.__newBranches = set()
       self.__newStatements = set()
       self.__newCurrBranches = set()
       self.__newCurrStatements = set()
       for src_file, arcs in self.__cov.collector.get_arc_data().iteritems():
           for arc in arcs:
               branch = (src_file, arc)
               if branch not in self.__allBranches:
                   self.__allBranches.add(branch)
                   self.__newBranches.add(branch)
               if branch not in self.__currBranches:
                   self.__currBranches.add(branch)
                   self.__newCurrBranches.add(branch)
       for src_file, lines in self.__cov.collector.get_line_data().iteritems():
           for line in lines:
               statement = (src_file, line)
               if statement not in self.__allStatements:
                   self.__allStatements.add(statement)
                   self.__newStatements.add(statement)
               if statement not in self.__currStatements:
                   self.__currStatements.add(branch)
                   self.__newCurrStatements.add(branch)        
   
   def resetCov(self):
       self.__cov.collector.reset()
   
   def report(self):
       self.__cov.html_report()
   
   def allBranches(self):
       return self.__allBranches
   
   def allStatements(self):
       return self.__allStatements
   
   def currBranches(self):
       return self.__currBranches
   
   def currStatements(self):
       return self.__currStatements
   
   def newBranches(self):
       return self.__newBranches
   
   def newStatements(self):
       return self.__newStatements
   
   def newCurrBranches(self):
       return self.__newCurrBranches
   
   def newCurrStatements(self):
       return self.__newCurrStatements
   
   def startCoverage(self):
       self.__collectCov = True
   
   def stopCoverage(self):
       self.__collectCov = False    
   
   def coversBranches(self, branches, catchUncaught=False):
       def coverPred(test):
           try:
               self.replay(test, catchUncaught)
           except:
               pass
           cb = self.currBranches()
           for b in branches:
               if b not in cb:
                   return False
           return True
       return coverPred
   
   def coversStatements(self, statements, catchUnCaught=False):
       def coverPred(test):
           try:
               self.replay(test, catchUnCaught)
           except:
               pass
           cs = self.currStatements()
           for s in statements:
               if s not in cs:
                   return False
           return True
       return coverPred

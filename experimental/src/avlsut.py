import copy
import traceback
import re
import sys
import avl
import bintree
class t(object):
   def act0(self):
      self.p_INT[0]=1

      self.p_INT_used[0]=False
   def guard0(self):
      return (self.p_INT_used[0])
   def act1(self):
      self.p_INT[0]=2

      self.p_INT_used[0]=False
   def guard1(self):
      return (self.p_INT_used[0])
   def act2(self):
      self.p_INT[0]=3

      self.p_INT_used[0]=False
   def guard2(self):
      return (self.p_INT_used[0])
   def act3(self):
      self.p_INT[0]=4

      self.p_INT_used[0]=False
   def guard3(self):
      return (self.p_INT_used[0])
   def act4(self):
      self.p_INT[0]=5

      self.p_INT_used[0]=False
   def guard4(self):
      return (self.p_INT_used[0])
   def act5(self):
      self.p_INT[0]=6

      self.p_INT_used[0]=False
   def guard5(self):
      return (self.p_INT_used[0])
   def act6(self):
      self.p_INT[0]=7

      self.p_INT_used[0]=False
   def guard6(self):
      return (self.p_INT_used[0])
   def act7(self):
      self.p_INT[0]=8

      self.p_INT_used[0]=False
   def guard7(self):
      return (self.p_INT_used[0])
   def act8(self):
      self.p_INT[0]=9

      self.p_INT_used[0]=False
   def guard8(self):
      return (self.p_INT_used[0])
   def act9(self):
      self.p_INT[0]=10

      self.p_INT_used[0]=False
   def guard9(self):
      return (self.p_INT_used[0])
   def act10(self):
      self.p_INT[0]=11

      self.p_INT_used[0]=False
   def guard10(self):
      return (self.p_INT_used[0])
   def act11(self):
      self.p_INT[0]=12

      self.p_INT_used[0]=False
   def guard11(self):
      return (self.p_INT_used[0])
   def act12(self):
      self.p_INT[0]=13

      self.p_INT_used[0]=False
   def guard12(self):
      return (self.p_INT_used[0])
   def act13(self):
      self.p_INT[0]=14

      self.p_INT_used[0]=False
   def guard13(self):
      return (self.p_INT_used[0])
   def act14(self):
      self.p_INT[0]=15

      self.p_INT_used[0]=False
   def guard14(self):
      return (self.p_INT_used[0])
   def act15(self):
      self.p_INT[0]=16

      self.p_INT_used[0]=False
   def guard15(self):
      return (self.p_INT_used[0])
   def act16(self):
      self.p_INT[0]=17

      self.p_INT_used[0]=False
   def guard16(self):
      return (self.p_INT_used[0])
   def act17(self):
      self.p_INT[0]=18

      self.p_INT_used[0]=False
   def guard17(self):
      return (self.p_INT_used[0])
   def act18(self):
      self.p_INT[0]=19

      self.p_INT_used[0]=False
   def guard18(self):
      return (self.p_INT_used[0])
   def act19(self):
      self.p_INT[0]=20

      self.p_INT_used[0]=False
   def guard19(self):
      return (self.p_INT_used[0])
   def act20(self):
      self.p_INT[1]=1

      self.p_INT_used[1]=False
   def guard20(self):
      return (self.p_INT_used[1])
   def act21(self):
      self.p_INT[1]=2

      self.p_INT_used[1]=False
   def guard21(self):
      return (self.p_INT_used[1])
   def act22(self):
      self.p_INT[1]=3

      self.p_INT_used[1]=False
   def guard22(self):
      return (self.p_INT_used[1])
   def act23(self):
      self.p_INT[1]=4

      self.p_INT_used[1]=False
   def guard23(self):
      return (self.p_INT_used[1])
   def act24(self):
      self.p_INT[1]=5

      self.p_INT_used[1]=False
   def guard24(self):
      return (self.p_INT_used[1])
   def act25(self):
      self.p_INT[1]=6

      self.p_INT_used[1]=False
   def guard25(self):
      return (self.p_INT_used[1])
   def act26(self):
      self.p_INT[1]=7

      self.p_INT_used[1]=False
   def guard26(self):
      return (self.p_INT_used[1])
   def act27(self):
      self.p_INT[1]=8

      self.p_INT_used[1]=False
   def guard27(self):
      return (self.p_INT_used[1])
   def act28(self):
      self.p_INT[1]=9

      self.p_INT_used[1]=False
   def guard28(self):
      return (self.p_INT_used[1])
   def act29(self):
      self.p_INT[1]=10

      self.p_INT_used[1]=False
   def guard29(self):
      return (self.p_INT_used[1])
   def act30(self):
      self.p_INT[1]=11

      self.p_INT_used[1]=False
   def guard30(self):
      return (self.p_INT_used[1])
   def act31(self):
      self.p_INT[1]=12

      self.p_INT_used[1]=False
   def guard31(self):
      return (self.p_INT_used[1])
   def act32(self):
      self.p_INT[1]=13

      self.p_INT_used[1]=False
   def guard32(self):
      return (self.p_INT_used[1])
   def act33(self):
      self.p_INT[1]=14

      self.p_INT_used[1]=False
   def guard33(self):
      return (self.p_INT_used[1])
   def act34(self):
      self.p_INT[1]=15

      self.p_INT_used[1]=False
   def guard34(self):
      return (self.p_INT_used[1])
   def act35(self):
      self.p_INT[1]=16

      self.p_INT_used[1]=False
   def guard35(self):
      return (self.p_INT_used[1])
   def act36(self):
      self.p_INT[1]=17

      self.p_INT_used[1]=False
   def guard36(self):
      return (self.p_INT_used[1])
   def act37(self):
      self.p_INT[1]=18

      self.p_INT_used[1]=False
   def guard37(self):
      return (self.p_INT_used[1])
   def act38(self):
      self.p_INT[1]=19

      self.p_INT_used[1]=False
   def guard38(self):
      return (self.p_INT_used[1])
   def act39(self):
      self.p_INT[1]=20

      self.p_INT_used[1]=False
   def guard39(self):
      return (self.p_INT_used[1])
   def act40(self):
      self.p_INT[2]=1

      self.p_INT_used[2]=False
   def guard40(self):
      return (self.p_INT_used[2])
   def act41(self):
      self.p_INT[2]=2

      self.p_INT_used[2]=False
   def guard41(self):
      return (self.p_INT_used[2])
   def act42(self):
      self.p_INT[2]=3

      self.p_INT_used[2]=False
   def guard42(self):
      return (self.p_INT_used[2])
   def act43(self):
      self.p_INT[2]=4

      self.p_INT_used[2]=False
   def guard43(self):
      return (self.p_INT_used[2])
   def act44(self):
      self.p_INT[2]=5

      self.p_INT_used[2]=False
   def guard44(self):
      return (self.p_INT_used[2])
   def act45(self):
      self.p_INT[2]=6

      self.p_INT_used[2]=False
   def guard45(self):
      return (self.p_INT_used[2])
   def act46(self):
      self.p_INT[2]=7

      self.p_INT_used[2]=False
   def guard46(self):
      return (self.p_INT_used[2])
   def act47(self):
      self.p_INT[2]=8

      self.p_INT_used[2]=False
   def guard47(self):
      return (self.p_INT_used[2])
   def act48(self):
      self.p_INT[2]=9

      self.p_INT_used[2]=False
   def guard48(self):
      return (self.p_INT_used[2])
   def act49(self):
      self.p_INT[2]=10

      self.p_INT_used[2]=False
   def guard49(self):
      return (self.p_INT_used[2])
   def act50(self):
      self.p_INT[2]=11

      self.p_INT_used[2]=False
   def guard50(self):
      return (self.p_INT_used[2])
   def act51(self):
      self.p_INT[2]=12

      self.p_INT_used[2]=False
   def guard51(self):
      return (self.p_INT_used[2])
   def act52(self):
      self.p_INT[2]=13

      self.p_INT_used[2]=False
   def guard52(self):
      return (self.p_INT_used[2])
   def act53(self):
      self.p_INT[2]=14

      self.p_INT_used[2]=False
   def guard53(self):
      return (self.p_INT_used[2])
   def act54(self):
      self.p_INT[2]=15

      self.p_INT_used[2]=False
   def guard54(self):
      return (self.p_INT_used[2])
   def act55(self):
      self.p_INT[2]=16

      self.p_INT_used[2]=False
   def guard55(self):
      return (self.p_INT_used[2])
   def act56(self):
      self.p_INT[2]=17

      self.p_INT_used[2]=False
   def guard56(self):
      return (self.p_INT_used[2])
   def act57(self):
      self.p_INT[2]=18

      self.p_INT_used[2]=False
   def guard57(self):
      return (self.p_INT_used[2])
   def act58(self):
      self.p_INT[2]=19

      self.p_INT_used[2]=False
   def guard58(self):
      return (self.p_INT_used[2])
   def act59(self):
      self.p_INT[2]=20

      self.p_INT_used[2]=False
   def guard59(self):
      return (self.p_INT_used[2])
   def act60(self):
      self.p_INT[3]=1

      self.p_INT_used[3]=False
   def guard60(self):
      return (self.p_INT_used[3])
   def act61(self):
      self.p_INT[3]=2

      self.p_INT_used[3]=False
   def guard61(self):
      return (self.p_INT_used[3])
   def act62(self):
      self.p_INT[3]=3

      self.p_INT_used[3]=False
   def guard62(self):
      return (self.p_INT_used[3])
   def act63(self):
      self.p_INT[3]=4

      self.p_INT_used[3]=False
   def guard63(self):
      return (self.p_INT_used[3])
   def act64(self):
      self.p_INT[3]=5

      self.p_INT_used[3]=False
   def guard64(self):
      return (self.p_INT_used[3])
   def act65(self):
      self.p_INT[3]=6

      self.p_INT_used[3]=False
   def guard65(self):
      return (self.p_INT_used[3])
   def act66(self):
      self.p_INT[3]=7

      self.p_INT_used[3]=False
   def guard66(self):
      return (self.p_INT_used[3])
   def act67(self):
      self.p_INT[3]=8

      self.p_INT_used[3]=False
   def guard67(self):
      return (self.p_INT_used[3])
   def act68(self):
      self.p_INT[3]=9

      self.p_INT_used[3]=False
   def guard68(self):
      return (self.p_INT_used[3])
   def act69(self):
      self.p_INT[3]=10

      self.p_INT_used[3]=False
   def guard69(self):
      return (self.p_INT_used[3])
   def act70(self):
      self.p_INT[3]=11

      self.p_INT_used[3]=False
   def guard70(self):
      return (self.p_INT_used[3])
   def act71(self):
      self.p_INT[3]=12

      self.p_INT_used[3]=False
   def guard71(self):
      return (self.p_INT_used[3])
   def act72(self):
      self.p_INT[3]=13

      self.p_INT_used[3]=False
   def guard72(self):
      return (self.p_INT_used[3])
   def act73(self):
      self.p_INT[3]=14

      self.p_INT_used[3]=False
   def guard73(self):
      return (self.p_INT_used[3])
   def act74(self):
      self.p_INT[3]=15

      self.p_INT_used[3]=False
   def guard74(self):
      return (self.p_INT_used[3])
   def act75(self):
      self.p_INT[3]=16

      self.p_INT_used[3]=False
   def guard75(self):
      return (self.p_INT_used[3])
   def act76(self):
      self.p_INT[3]=17

      self.p_INT_used[3]=False
   def guard76(self):
      return (self.p_INT_used[3])
   def act77(self):
      self.p_INT[3]=18

      self.p_INT_used[3]=False
   def guard77(self):
      return (self.p_INT_used[3])
   def act78(self):
      self.p_INT[3]=19

      self.p_INT_used[3]=False
   def guard78(self):
      return (self.p_INT_used[3])
   def act79(self):
      self.p_INT[3]=20

      self.p_INT_used[3]=False
   def guard79(self):
      return (self.p_INT_used[3])
   def act80(self):
      self.p_AVL[0]=AvlTree()

      self.p_AVL__REF[0]=BinTree()

      self.p_AVL_used[0]=False
   def guard80(self):
      return (self.p_AVL_used[0])
   def act81(self):
      self.p_AVL[0].insert(self.p_INT[0])

      self.p_AVL__REF[0].insert(self.p_INT[0])

      self.p_INT_used[0]=True
      self.p_AVL_used[0]=True
   def guard81(self):
      return (self.p_INT[0] != None) and (self.p_AVL[0] != None)
   def act82(self):
      self.p_AVL[0].insert(self.p_INT[1])

      self.p_AVL__REF[0].insert(self.p_INT[1])

      self.p_INT_used[1]=True
      self.p_AVL_used[0]=True
   def guard82(self):
      return (self.p_INT[1] != None) and (self.p_AVL[0] != None)
   def act83(self):
      self.p_AVL[0].insert(self.p_INT[2])

      self.p_AVL__REF[0].insert(self.p_INT[2])

      self.p_INT_used[2]=True
      self.p_AVL_used[0]=True
   def guard83(self):
      return (self.p_INT[2] != None) and (self.p_AVL[0] != None)
   def act84(self):
      self.p_AVL[0].insert(self.p_INT[3])

      self.p_AVL__REF[0].insert(self.p_INT[3])

      self.p_INT_used[3]=True
      self.p_AVL_used[0]=True
   def guard84(self):
      return (self.p_INT[3] != None) and (self.p_AVL[0] != None)
   def act85(self):
      self.p_AVL[0].delete(self.p_INT[0])

      self.p_AVL__REF[0].delete(self.p_INT[0])

      self.p_INT_used[0]=True
      self.p_AVL_used[0]=True
   def guard85(self):
      return (self.p_INT[0] != None) and (self.p_AVL[0] != None)
   def act86(self):
      self.p_AVL[0].delete(self.p_INT[1])

      self.p_AVL__REF[0].delete(self.p_INT[1])

      self.p_INT_used[1]=True
      self.p_AVL_used[0]=True
   def guard86(self):
      return (self.p_INT[1] != None) and (self.p_AVL[0] != None)
   def act87(self):
      self.p_AVL[0].delete(self.p_INT[2])

      self.p_AVL__REF[0].delete(self.p_INT[2])

      self.p_INT_used[2]=True
      self.p_AVL_used[0]=True
   def guard87(self):
      return (self.p_INT[2] != None) and (self.p_AVL[0] != None)
   def act88(self):
      self.p_AVL[0].delete(self.p_INT[3])

      self.p_AVL__REF[0].delete(self.p_INT[3])

      self.p_INT_used[3]=True
      self.p_AVL_used[0]=True
   def guard88(self):
      return (self.p_INT[3] != None) and (self.p_AVL[0] != None)
   def act89(self):
      __result = self.p_AVL[0].find(self.p_INT[0])

      __result__REF = self.p_AVL__REF[0].find(self.p_INT[0])

      assert __result == __result__REF
      self.p_INT_used[0]=True
      self.p_AVL_used[0]=True
   def guard89(self):
      return (self.p_INT[0] != None) and (self.p_AVL[0] != None)
   def act90(self):
      __result = self.p_AVL[0].find(self.p_INT[1])

      __result__REF = self.p_AVL__REF[0].find(self.p_INT[1])

      assert __result == __result__REF
      self.p_INT_used[1]=True
      self.p_AVL_used[0]=True
   def guard90(self):
      return (self.p_INT[1] != None) and (self.p_AVL[0] != None)
   def act91(self):
      __result = self.p_AVL[0].find(self.p_INT[2])

      __result__REF = self.p_AVL__REF[0].find(self.p_INT[2])

      assert __result == __result__REF
      self.p_INT_used[2]=True
      self.p_AVL_used[0]=True
   def guard91(self):
      return (self.p_INT[2] != None) and (self.p_AVL[0] != None)
   def act92(self):
      __result = self.p_AVL[0].find(self.p_INT[3])

      __result__REF = self.p_AVL__REF[0].find(self.p_INT[3])

      assert __result == __result__REF
      self.p_INT_used[3]=True
      self.p_AVL_used[0]=True
   def guard92(self):
      return (self.p_INT[3] != None) and (self.p_AVL[0] != None)
   def __init__(self):
      self.__features = []
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
      self.p_AVL = {}
      self.p_AVL_used = {}
      self.p_AVL[0] = None
      self.p_AVL_used[0] = True
      self.p_AVL[1] = None
      self.p_AVL_used[1] = True
      self.p_AVL___REF = {}
      self.p_AVL___REF_used = {}
      self.p_AVL___REF[0] = None
      self.p_AVL___REF_used[0] = True
      self.p_AVL___REF[1] = None
      self.p_AVL___REF_used[1] = True
      self.__actions = []
      self.__actions.append((r"self.p_INT[0]=1",self.guard0,self.act0))

      self.__actions.append((r"self.p_INT[0]=2",self.guard1,self.act1))

      self.__actions.append((r"self.p_INT[0]=3",self.guard2,self.act2))

      self.__actions.append((r"self.p_INT[0]=4",self.guard3,self.act3))

      self.__actions.append((r"self.p_INT[0]=5",self.guard4,self.act4))

      self.__actions.append((r"self.p_INT[0]=6",self.guard5,self.act5))

      self.__actions.append((r"self.p_INT[0]=7",self.guard6,self.act6))

      self.__actions.append((r"self.p_INT[0]=8",self.guard7,self.act7))

      self.__actions.append((r"self.p_INT[0]=9",self.guard8,self.act8))

      self.__actions.append((r"self.p_INT[0]=10",self.guard9,self.act9))

      self.__actions.append((r"self.p_INT[0]=11",self.guard10,self.act10))

      self.__actions.append((r"self.p_INT[0]=12",self.guard11,self.act11))

      self.__actions.append((r"self.p_INT[0]=13",self.guard12,self.act12))

      self.__actions.append((r"self.p_INT[0]=14",self.guard13,self.act13))

      self.__actions.append((r"self.p_INT[0]=15",self.guard14,self.act14))

      self.__actions.append((r"self.p_INT[0]=16",self.guard15,self.act15))

      self.__actions.append((r"self.p_INT[0]=17",self.guard16,self.act16))

      self.__actions.append((r"self.p_INT[0]=18",self.guard17,self.act17))

      self.__actions.append((r"self.p_INT[0]=19",self.guard18,self.act18))

      self.__actions.append((r"self.p_INT[0]=20",self.guard19,self.act19))

      self.__actions.append((r"self.p_INT[1]=1",self.guard20,self.act20))

      self.__actions.append((r"self.p_INT[1]=2",self.guard21,self.act21))

      self.__actions.append((r"self.p_INT[1]=3",self.guard22,self.act22))

      self.__actions.append((r"self.p_INT[1]=4",self.guard23,self.act23))

      self.__actions.append((r"self.p_INT[1]=5",self.guard24,self.act24))

      self.__actions.append((r"self.p_INT[1]=6",self.guard25,self.act25))

      self.__actions.append((r"self.p_INT[1]=7",self.guard26,self.act26))

      self.__actions.append((r"self.p_INT[1]=8",self.guard27,self.act27))

      self.__actions.append((r"self.p_INT[1]=9",self.guard28,self.act28))

      self.__actions.append((r"self.p_INT[1]=10",self.guard29,self.act29))

      self.__actions.append((r"self.p_INT[1]=11",self.guard30,self.act30))

      self.__actions.append((r"self.p_INT[1]=12",self.guard31,self.act31))

      self.__actions.append((r"self.p_INT[1]=13",self.guard32,self.act32))

      self.__actions.append((r"self.p_INT[1]=14",self.guard33,self.act33))

      self.__actions.append((r"self.p_INT[1]=15",self.guard34,self.act34))

      self.__actions.append((r"self.p_INT[1]=16",self.guard35,self.act35))

      self.__actions.append((r"self.p_INT[1]=17",self.guard36,self.act36))

      self.__actions.append((r"self.p_INT[1]=18",self.guard37,self.act37))

      self.__actions.append((r"self.p_INT[1]=19",self.guard38,self.act38))

      self.__actions.append((r"self.p_INT[1]=20",self.guard39,self.act39))

      self.__actions.append((r"self.p_INT[2]=1",self.guard40,self.act40))

      self.__actions.append((r"self.p_INT[2]=2",self.guard41,self.act41))

      self.__actions.append((r"self.p_INT[2]=3",self.guard42,self.act42))

      self.__actions.append((r"self.p_INT[2]=4",self.guard43,self.act43))

      self.__actions.append((r"self.p_INT[2]=5",self.guard44,self.act44))

      self.__actions.append((r"self.p_INT[2]=6",self.guard45,self.act45))

      self.__actions.append((r"self.p_INT[2]=7",self.guard46,self.act46))

      self.__actions.append((r"self.p_INT[2]=8",self.guard47,self.act47))

      self.__actions.append((r"self.p_INT[2]=9",self.guard48,self.act48))

      self.__actions.append((r"self.p_INT[2]=10",self.guard49,self.act49))

      self.__actions.append((r"self.p_INT[2]=11",self.guard50,self.act50))

      self.__actions.append((r"self.p_INT[2]=12",self.guard51,self.act51))

      self.__actions.append((r"self.p_INT[2]=13",self.guard52,self.act52))

      self.__actions.append((r"self.p_INT[2]=14",self.guard53,self.act53))

      self.__actions.append((r"self.p_INT[2]=15",self.guard54,self.act54))

      self.__actions.append((r"self.p_INT[2]=16",self.guard55,self.act55))

      self.__actions.append((r"self.p_INT[2]=17",self.guard56,self.act56))

      self.__actions.append((r"self.p_INT[2]=18",self.guard57,self.act57))

      self.__actions.append((r"self.p_INT[2]=19",self.guard58,self.act58))

      self.__actions.append((r"self.p_INT[2]=20",self.guard59,self.act59))

      self.__actions.append((r"self.p_INT[3]=1",self.guard60,self.act60))

      self.__actions.append((r"self.p_INT[3]=2",self.guard61,self.act61))

      self.__actions.append((r"self.p_INT[3]=3",self.guard62,self.act62))

      self.__actions.append((r"self.p_INT[3]=4",self.guard63,self.act63))

      self.__actions.append((r"self.p_INT[3]=5",self.guard64,self.act64))

      self.__actions.append((r"self.p_INT[3]=6",self.guard65,self.act65))

      self.__actions.append((r"self.p_INT[3]=7",self.guard66,self.act66))

      self.__actions.append((r"self.p_INT[3]=8",self.guard67,self.act67))

      self.__actions.append((r"self.p_INT[3]=9",self.guard68,self.act68))

      self.__actions.append((r"self.p_INT[3]=10",self.guard69,self.act69))

      self.__actions.append((r"self.p_INT[3]=11",self.guard70,self.act70))

      self.__actions.append((r"self.p_INT[3]=12",self.guard71,self.act71))

      self.__actions.append((r"self.p_INT[3]=13",self.guard72,self.act72))

      self.__actions.append((r"self.p_INT[3]=14",self.guard73,self.act73))

      self.__actions.append((r"self.p_INT[3]=15",self.guard74,self.act74))

      self.__actions.append((r"self.p_INT[3]=16",self.guard75,self.act75))

      self.__actions.append((r"self.p_INT[3]=17",self.guard76,self.act76))

      self.__actions.append((r"self.p_INT[3]=18",self.guard77,self.act77))

      self.__actions.append((r"self.p_INT[3]=19",self.guard78,self.act78))

      self.__actions.append((r"self.p_INT[3]=20",self.guard79,self.act79))

      self.__actions.append((r"self.p_AVL[0]=AvlTree()",self.guard80,self.act80))

      self.__actions.append((r"self.p_AVL[0].insert(self.p_INT[0])",self.guard81,self.act81))

      self.__actions.append((r"self.p_AVL[0].insert(self.p_INT[1])",self.guard82,self.act82))

      self.__actions.append((r"self.p_AVL[0].insert(self.p_INT[2])",self.guard83,self.act83))

      self.__actions.append((r"self.p_AVL[0].insert(self.p_INT[3])",self.guard84,self.act84))

      self.__actions.append((r"self.p_AVL[0].delete(self.p_INT[0])",self.guard85,self.act85))

      self.__actions.append((r"self.p_AVL[0].delete(self.p_INT[1])",self.guard86,self.act86))

      self.__actions.append((r"self.p_AVL[0].delete(self.p_INT[2])",self.guard87,self.act87))

      self.__actions.append((r"self.p_AVL[0].delete(self.p_INT[3])",self.guard88,self.act88))

      self.__actions.append((r"__result = self.p_AVL[0].find(self.p_INT[0])",self.guard89,self.act89))

      self.__actions.append((r"__result = self.p_AVL[0].find(self.p_INT[1])",self.guard90,self.act90))

      self.__actions.append((r"__result = self.p_AVL[0].find(self.p_INT[2])",self.guard91,self.act91))

      self.__actions.append((r"__result = self.p_AVL[0].find(self.p_INT[3])",self.guard92,self.act92))

      self.__actions_backup = list(self.__actions)
   def restart(self):
      reload(avl)
      reload(bintree)
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
      self.p_AVL = {}
      self.p_AVL_used = {}
      self.p_AVL[0] = None
      self.p_AVL_used[0] = True
      self.p_AVL[1] = None
      self.p_AVL_used[1] = True
      self.p_AVL___REF = {}
      self.p_AVL___REF_used = {}
      self.p_AVL___REF[0] = None
      self.p_AVL___REF_used[0] = True
      self.p_AVL___REF[1] = None
      self.p_AVL___REF_used[1] = True
   def state(self):
      return [copy.deepcopy(self.p_INT),copy.deepcopy(self.p_INT_used),copy.deepcopy(self.p_AVL),copy.deepcopy(self.p_AVL_used),copy.deepcopy(self.p_AVL___REF),copy.deepcopy(self.p_AVL___REF_used)]
   def backtrack(self,old):
      self.p_INT = copy.deepcopy(old[0])
      self.p_INT_used = copy.deepcopy(old[1])
      self.p_AVL = copy.deepcopy(old[2])
      self.p_AVL_used = copy.deepcopy(old[3])
      self.p_AVL___REF = copy.deepcopy(old[4])
      self.p_AVL___REF_used = copy.deepcopy(old[5])
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

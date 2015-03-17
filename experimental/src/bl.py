import copy
import traceback
import sys
def guardedAppend(l,item,limit, SPECULATIVE_CALL = False):
  if len(l) >= limit:
    return False
  if SPECULATIVE_CALL: return True
  l.append(item)
class t(object):
   def act0(self):
      self.p_LIST[0] = []

      self.p_LIST_used[0]=False
   def guard0(self):
      return True and (self.p_LIST_used[0])
   def act1(self):
      guardedAppend(self.p_LIST[0],self.p_VAL[0],10)

      self.p_VAL_used[0]=True
   def guard1(self):
      return True and (self.p_LIST[0] != None) and (self.p_VAL[0] != None) and (guardedAppend(self.p_LIST[0],self.p_VAL[0],10,True))
   def act2(self):
      self.p_VAL[0] = 1

      self.p_VAL_used[0]=False
   def guard2(self):
      return True and (self.p_VAL_used[0])
   def act3(self):
      self.p_VAL[0] = 2

      self.p_VAL_used[0]=False
   def guard3(self):
      return True and (self.p_VAL_used[0])
   def act4(self):
      self.p_VAL[0] = 3

      self.p_VAL_used[0]=False
   def guard4(self):
      return True and (self.p_VAL_used[0])
   def act5(self):
      self.p_VAL[0] = 4

      self.p_VAL_used[0]=False
   def guard5(self):
      return True and (self.p_VAL_used[0])
   def act6(self):
      self.p_VAL[0] = 5

      self.p_VAL_used[0]=False
   def guard6(self):
      return True and (self.p_VAL_used[0])
   def act7(self):
      self.p_VAL[0] = 6

      self.p_VAL_used[0]=False
   def guard7(self):
      return True and (self.p_VAL_used[0])
   def act8(self):
      self.p_VAL[0] = 7

      self.p_VAL_used[0]=False
   def guard8(self):
      return True and (self.p_VAL_used[0])
   def act9(self):
      self.p_VAL[0] = 8

      self.p_VAL_used[0]=False
   def guard9(self):
      return True and (self.p_VAL_used[0])
   def act10(self):
      self.p_VAL[0] = 9

      self.p_VAL_used[0]=False
   def guard10(self):
      return True and (self.p_VAL_used[0])
   def act11(self):
      self.p_VAL[0] = 10

      self.p_VAL_used[0]=False
   def guard11(self):
      return True and (self.p_VAL_used[0])
   def act12(self):
      print self.p_LIST[0]

      self.p_LIST_used[0]=True
   def guard12(self):
      return True and (self.p_LIST[0] != None)
   def __init__(self):
      self.p_LIST = {}
      self.p_LIST_used = {}
      self.p_LIST[0] = None
      self.p_LIST_used[0] = True
      self.p_LIST[1] = None
      self.p_LIST_used[1] = True
      self.p_VAL = {}
      self.p_VAL_used = {}
      self.p_VAL[0] = None
      self.p_VAL_used[0] = True
      self.p_VAL[1] = None
      self.p_VAL_used[1] = True
      self.actions = []
      self.actions.append((r"self.p_LIST[0] = []",self.guard0,self.act0))

      self.actions.append((r"guardedAppend(self.p_LIST[0],self.p_VAL[0],10)",self.guard1,self.act1))

      self.actions.append((r"self.p_VAL[0] = 1",self.guard2,self.act2))

      self.actions.append((r"self.p_VAL[0] = 2",self.guard3,self.act3))

      self.actions.append((r"self.p_VAL[0] = 3",self.guard4,self.act4))

      self.actions.append((r"self.p_VAL[0] = 4",self.guard5,self.act5))

      self.actions.append((r"self.p_VAL[0] = 5",self.guard6,self.act6))

      self.actions.append((r"self.p_VAL[0] = 6",self.guard7,self.act7))

      self.actions.append((r"self.p_VAL[0] = 7",self.guard8,self.act8))

      self.actions.append((r"self.p_VAL[0] = 8",self.guard9,self.act9))

      self.actions.append((r"self.p_VAL[0] = 9",self.guard10,self.act10))

      self.actions.append((r"self.p_VAL[0] = 10",self.guard11,self.act11))

      self.actions.append((r"print self.p_LIST[0]",self.guard12,self.act12))

   def restart(self):
      self.p_LIST = {}
      self.p_LIST_used = {}
      self.p_LIST[0] = None
      self.p_LIST_used[0] = True
      self.p_LIST[1] = None
      self.p_LIST_used[1] = True
      self.p_VAL = {}
      self.p_VAL_used = {}
      self.p_VAL[0] = None
      self.p_VAL_used[0] = True
      self.p_VAL[1] = None
      self.p_VAL_used[1] = True
   def state(self):
      return [copy.deepcopy(self.p_LIST),copy.deepcopy(self.p_LIST_used),copy.deepcopy(self.p_VAL),copy.deepcopy(self.p_VAL_used)]
   def backtrack(self,old):
      self.p_LIST = copy.deepcopy(old[0])
      self.p_LIST_used = copy.deepcopy(old[1])
      self.p_VAL = copy.deepcopy(old[2])
      self.p_VAL_used = copy.deepcopy(old[3])
   def check(self):
      try:
         if True and (self.p_LIST[0] != None) and (self.p_LIST[0] != None):
            assert (len(self.p_LIST[0]) < 10) or (6 not in self.p_LIST[0])

         if True and (self.p_VAL[0] != None):
            assert self.p_VAL[0] != -1

      except:
         _,_,tb = sys.exc_info()
         traceback.print_tb(tb)
         return False
      return True
   def enabled(self):
       return filter(lambda (s, g, a): g(), self.actions)

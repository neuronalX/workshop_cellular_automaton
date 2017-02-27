# Copyright (2017) Nicolas P. Rougier @NPRougier
# From https://twitter.com/NPRougier/status/835234915008512000
_='0'
R,C="{:08b}".format(30),_*9+'1'+_*9
for k in range(9):
  print(C)
  C = _+''.join([R[7-eval('0b'+C[i:i+3])] for i in range(len(C)-2)])+_

from typing import Pattern
import numpy as np
import matplotlib.pyplot as plt
import calculator
import os

path = os.path.dirname(os.path.abspath(__file__)) 
os.chdir(path+"/out/")

param={'T_0':217,'Ma_0':0.9,'h_c':42800000,'T_t4':1670,'pi_c':20,'pi_f':4,'alpha':1,'gama':1.4,'C_p':1004}
step=100

# 绘制单位推力-压比关系图
alpha=[0.5,1,1.5,2,3,4,5,8,12]
param_temp=param.copy()
for i in alpha[:]:
  x=np.linspace(2,30,step,endpoint=True)
  y=np.empty((step))
  param_temp['alpha']=i
  j=0
  while j<len(x):
    param_temp['pi_c']=x[j]
    res=calculator.calc(param_temp)
    if res:
      y[j]=res['F_unit']
      j+=1
    else:
      x=np.delete(x,0)
      y=np.delete(y,0)
  plt.plot(x,y)
plt.savefig('F_unit.jpg')
plt.clf()

# 绘制单位燃油消耗率-压比关系图
alpha=[0.5,1,1.5,2,3,4,5,8,12]
param_temp=param.copy()
for i in alpha[:]:
  x=np.linspace(1,30,step,endpoint=True)
  y=np.empty((step))
  param_temp['alpha']=i
  j=0
  while j<len(x):
    param_temp['pi_c']=x[j]
    res=calculator.calc(param_temp)
    if res and res['S']<28e-6:
      y[j]=res['S']
      j+=1
    else:
      x=np.delete(x,0)
      y=np.delete(y,0)
  plt.plot(x,y)
plt.savefig('S.jpg')
plt.clf()

# 绘制效率-压比关系图
alpha=[0.5,1,1.5,2,3,4,5,8,12]
param_temp=param.copy()
for i in alpha[:]:
  x=np.linspace(1,30,step,endpoint=True)
  y=np.empty((step))
  z=np.empty((step))
  param_temp['alpha']=i
  j=0
  while j<len(x):
    param_temp['pi_c']=x[j]
    res=calculator.calc(param_temp)
    if res and res['eta_0']>0.2:
      y[j]=res['eta_p']
      z[j]=res['eta_0']
      j+=1
    else:
      x=np.delete(x,0)
      y=np.delete(y,0)
      z=np.delete(z,0)
  plt.plot(x,y)
  plt.plot(x,z)
plt.savefig('eta_t-eta_0.jpg')
plt.clf()

# 绘制热效率-压比关系图
x=np.linspace(1,30,step,endpoint=True)
y=np.empty((step))
param_temp=param.copy()
for i in range(step):
  param_temp['pi_c']=x[i]
  y[i]=calculator.calc(param_temp)['eta_t']
plt.plot(x,y)
plt.savefig('eta_t.jpg')
plt.clf()

# 绘制油气比-压比关系图
x=np.linspace(1,30,step,endpoint=True)
y=np.zeros((step))
param_temp=param.copy()
for i in range(step):
  param_temp['pi_c']=x[i]
  y[i]=calculator.calc(param_temp)['f']
plt.plot(x,y)
plt.savefig('f.jpg')
plt.clf()
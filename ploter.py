#coding:utf-8
from typing import Pattern
from matplotlib import patches
import numpy as np
import matplotlib.pyplot as plt
from numpy.core.numeric import zeros_like
import calculator
import os

path = os.path.dirname(os.path.abspath(__file__)) 
os.chdir(path+"/out/")

param={'T_0':227.15,'Ma_0':0.84,'h_c':42800000,'T_t4':1775,'pi_c':42,'pi_f':2,'alpha':9,'gama':1.4,'C_p':1004}
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
  plt.plot(x,y,color='black',linewidth=1)
  if len(x)>0:
    plt.text(x[-1]-13,y[-1]+15,'$\\alpha={}$'.format(i),ha='center',va='center')
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.xlabel('$\pi_c$')
plt.ylabel('$F/\dot{m}_0[N/(kg/s)]$')
plt.title(u'单位推力与涵道比、压比的关系\n',fontsize=13)
ax=plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.savefig('./pi_c/F_unit.jpg')
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
      y[j]=res['S']*1000000
      j+=1
    else:
      x=np.delete(x,0)
      y=np.delete(y,0)
  plt.plot(x,y,color='black',linewidth=1)
  if len(x)>0:
    plt.text(x[-1]-1,y[-1]+0.5,'$\\alpha={}$'.format(i),ha='center',va='center')
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.xlabel('$\pi_c$')
plt.ylabel('$S[mg/(N \cdot S)]$')
plt.title(u'单位燃油消耗率与涵道比、压比的关系\n',fontsize=13)
ax=plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.savefig('./pi_c/S.jpg')
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
      y[j]=res['eta_p']*100
      z[j]=res['eta_0']*100
      j+=1
    else:
      x=np.delete(x,0)
      y=np.delete(y,0)
      z=np.delete(z,0)
  plt.plot(x,y,linewidth=1,color='black')
  if len(x)>0:
    plt.text(x[0]-0.5,y[0]-1.2,'${}$'.format(i),ha='center',va='center')
  plt.plot(x,z,linewidth=1,color='black')
  if len(x)>0:
    plt.text(x[-1]+0.1,z[-1],'${}$'.format(i),va='center')
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.xlabel('$\pi_c$')
plt.ylabel('$\eta_o\qquad\qquad (\%) \qquad\qquad\eta_p$')
plt.title(u'推进效率、总效率与涵道比、压比的关系\n',fontsize=13)
ax=plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.savefig('./pi_c/eta_p-eta_0.jpg')
plt.clf()

# 绘制热效率与油气比-压比关系图
x=np.linspace(1,30,step,endpoint=True)
y=np.zeros((step))
z=np.zeros((step))
param_temp=param.copy()
fig=plt.figure()
ax1=fig.add_subplot(111)
i=0
while i<len(x):
  param_temp['pi_c']=x[i]
  res=calculator.calc(param_temp)
  if res:
    z[i]=res['eta_t']*100
    y[i]=res['f']
    i+=1
  else:
    x=np.delete(x,i)
    y=np.delete(y,i)
    z=np.delete(z,i)
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.xlabel('$\pi_c$')
plt.title(u'热效率-油气比与压比的关系\n',fontsize=13)
ax1.plot(x,y,color='black',linewidth=1)
ax1.set_ylabel('f')
ax1.spines['top'].set_visible(False)
ax1.annotate('',xy=(x[step//2]-3,y[step//2]),xytext=(x[step//2],y[step//2]),arrowprops=dict(arrowstyle="->"))
ax2=ax1.twinx()
ax2.plot(x,z,color='black',linewidth=1)
ax2.set_ylabel('$\eta_T$')
ax2.spines['top'].set_visible(False)
ax2.annotate('',xy=(x[step//2]+3,z[step//2]),xytext=(x[step//2],z[step//2]),arrowprops=dict(arrowstyle="->"))
plt.savefig('./pi_c/f-eta_t.jpg')
plt.clf()

#############################################
#############################################

# 绘制单位推力-马赫数关系图
alpha=[0.5,1,1.5,2,3,4,5,8,12]
param_temp=param.copy()
for i in alpha[:]:
  x=np.linspace(0,2.5,step,endpoint=True)
  y=np.empty((step))
  param_temp['alpha']=i
  j=0
  while j<len(x):
    param_temp['Ma_0']=x[j]
    res=calculator.calc(param_temp)
    if res:
      y[j]=res['F_unit']
      j+=1
    else:
      x=np.delete(x,j)
      y=np.delete(y,j)
  plt.plot(x,y,color='black',linewidth=1)
  if len(x)>0:
    plt.text(x[-1]+0.15,y[-1],'$\\alpha={}$'.format(i),ha='center',va='center')
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.xlabel('$Ma_0$')
plt.ylabel('$F/\dot{m}_0[N/(kg/s)]$')
plt.title(u'单位推力涵道比、马赫数的关系\n',fontsize=13)
ax=plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.savefig('./Ma_0/F_unit.jpg')
plt.clf()

# 绘制单位燃油消耗率-马赫数关系图
alpha=[0.5,1,1.5,2,3,4,5,8,12]
param_temp=param.copy()
for i in alpha[:]:
  x=np.linspace(0,2.5,step,endpoint=True)
  y=np.empty((step))
  param_temp['alpha']=i
  j=0
  while j<len(x):
    param_temp['Ma_0']=x[j]
    res=calculator.calc(param_temp)
    if res and res['S']<28e-6:
      y[j]=res['S']*1000000
      j+=1
    else:
      x=np.delete(x,j)
      y=np.delete(y,j)
  plt.plot(x,y,color='black',linewidth=1)
  if len(x)>0:
    plt.text(x[20]+0.03,y[20]-0.5,'${}$'.format(i),ha='center',va='center')
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.xlabel('$Ma_0$')
plt.ylabel('$S[mg/(N \cdot S)]$')
plt.title(u'单位燃油消耗率与涵道比、马赫数的关系\n',fontsize=13)
ax=plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.savefig('./Ma_0/S.jpg')
plt.clf()

# 绘制效率-马赫数关系图
alpha=[0.5,1,1.5,2,3,4,5,8,12]
param_temp=param.copy()
for i in alpha[:]:
  x=np.linspace(0,2.4,step,endpoint=True)
  y=np.empty((step))
  param_temp['alpha']=i
  j=0
  while j<len(x):
    param_temp['Ma_0']=x[j]
    res=calculator.calc(param_temp)
    if res and res['eta_0']>0.2:
      y[j]=res['eta_p']*100
      j+=1
    else:
      x=np.delete(x,j)
      y=np.delete(y,j)
  plt.plot(x,y,linewidth=1,color='black')
  if len(x)>0:
    plt.text(x[20]+0.02,y[20],'${}$'.format(i),ha='center',va='center')
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.xlabel('$Ma_0$')
plt.ylabel('$\eta_p(\%)$')
plt.title(u'推进效率与涵道比、马赫数的关系\n',fontsize=13)
ax=plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.savefig('./Ma_0/eta_p.jpg')
plt.clf()

# 绘制效率-马赫数关系图
alpha=[0.5,1,1.5,2,3,4,5,8,12]
param_temp=param.copy()
for i in alpha[:]:
  x=np.linspace(0,2.4,step,endpoint=True)
  y=np.empty((step))
  param_temp['alpha']=i
  j=0
  while j<len(x):
    param_temp['Ma_0']=x[j]
    res=calculator.calc(param_temp)
    if res and res['eta_0']>0.2:
      y[j]=res['eta_0']*100
      j+=1
    else:
      x=np.delete(x,j)
      y=np.delete(y,j)
  plt.plot(x,y,linewidth=1,color='black')
  if len(x)>0:
    plt.text(x[25]+0.02,y[25],'${}$'.format(i),ha='center',va='center')
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.xlabel('$Ma_0$')
plt.ylabel('$\eta_0(\%)$')
plt.title(u'总效率与涵道比、马赫数的关系\n',fontsize=13)
ax=plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.savefig('./Ma_0/eta_0.jpg')
plt.clf()

# 绘制热效率与油气比-马赫数关系图
x=np.linspace(0,2.5,step,endpoint=True)
y=np.empty((step))
z=np.empty((step))
param_temp=param.copy()
fig=plt.figure()
ax1=fig.add_subplot(111)
i=0
while i<len(x):
  param_temp['Ma_0']=x[i]
  res=calculator.calc(param_temp)
  if res:
    y[i]=res['f']
    z[i]=res['eta_t']*100
    i+=1
  else:
    x=np.delete(x,i)
    y=np.delete(y,i)
    z=np.delete(z,i)
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.xlabel('$Ma_0$')
plt.title(u'热效率、油气比与马赫数的关系\n',fontsize=13)
ax1.plot(x,y,color='black',linewidth=1)
ax1.set_ylabel('f')
ax1.spines['top'].set_visible(False)
ax1.annotate('',xy=(x[step//2]-0.3,y[step//2]),xytext=(x[step//2],y[step//2]),arrowprops=dict(arrowstyle="->"))
ax2=ax1.twinx()
ax2.plot(x,z,color='black',linewidth=1)
ax2.set_ylabel('$\eta_T$')
ax2.spines['top'].set_visible(False)
ax2.annotate('',xy=(x[step//2]+0.3,z[step//2]),xytext=(x[step//2],z[step//2]),arrowprops=dict(arrowstyle="->"))
plt.savefig('./Ma_0/f-eta_t.jpg')
plt.clf()

#############################################
#############################################

# 绘制单位推力-环境温度关系图
alpha=[0.5,1,1.5,2,3,4,5,8,12]
param_temp=param.copy()
for i in alpha[:]:
  x=np.linspace(230,300,step,endpoint=True)
  y=np.empty((step))
  param_temp['alpha']=i
  j=0
  while j<len(x):
    param_temp['T_0']=x[j]
    res=calculator.calc(param_temp)
    if res:
      y[j]=res['F_unit']
      j+=1
    else:
      x=np.delete(x,j)
      y=np.delete(y,j)
  plt.plot(x,y,color='black',linewidth=1)
  if len(x)>0:
    plt.text(x[-1]+0.15,y[-1]+20,'$\\alpha={}$'.format(i),ha='center',va='center')
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.xlabel('$T_0$(K)')
plt.ylabel('$F/\dot{m}_0[N/(kg/s)]$')
plt.title(u'单位推力与涵道比、环境温度的关系\n',fontsize=13)
ax=plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.savefig('./T_0/F_unit.jpg')
plt.clf()

# 绘制单位燃油消耗率-环境温度关系图
alpha=[0.5,1,1.5,2,3,4,5,8,12]
param_temp=param.copy()
for i in alpha[:]:
  x=np.linspace(230,300,step,endpoint=True)
  y=np.empty((step))
  param_temp['alpha']=i
  j=0
  while j<len(x):
    param_temp['T_0']=x[j]
    res=calculator.calc(param_temp)
    if res and res['S']<28e-6:
      y[j]=res['S']*1000000
      j+=1
    else:
      x=np.delete(x,j)
      y=np.delete(y,j)
  plt.plot(x,y,color='black',linewidth=1)
  if len(x)>0:
    plt.text(x[0]+3,y[0]+0.5,'$\\alpha={}$'.format(i),ha='center',va='center')
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.xlabel('$T_0$(K)')
plt.ylabel('$S[mg/(N \cdot S)]$')
plt.title(u'单位燃油消耗率与涵道比、环境温度的关系\n',fontsize=13)
ax=plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.savefig('./T_0/S.jpg')
plt.clf()

# 绘制效率-环境温度关系图
alpha=[0.5,1,1.5,2,3,4,5,8,12]
param_temp=param.copy()
for i in alpha[:]:
  x=np.linspace(230,300,step,endpoint=True)
  y=np.empty((step))
  param_temp['alpha']=i
  j=0
  while j<len(x):
    param_temp['T_0']=x[j]
    res=calculator.calc(param_temp)
    if res and res['eta_0']>0.2:
      y[j]=res['eta_p']*100
      j+=1
    else:
      x=np.delete(x,j)
      y=np.delete(y,j)
  plt.plot(x,y,linewidth=1,color='black')
  if len(x)>0:
    plt.text(x[-1]+3,y[-1]+1,'$\\alpha={}$'.format(i),ha='center',va='center')
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.xlabel('$T_0$(K)')
plt.ylabel('$\eta_p(\%)$')
plt.title(u'推进效率与涵道比、环境温度的关系\n',fontsize=13)
ax=plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.savefig('./T_0/eta_p.jpg')
plt.clf()

# 绘制效率-环境温度关系图
alpha=[0.5,1,1.5,2,3,4,5,8,12]
param_temp=param.copy()
for i in alpha[:]:
  x=np.linspace(230,300,step,endpoint=True)
  y=np.empty((step))
  param_temp['alpha']=i
  j=0
  while j<len(x):
    param_temp['T_0']=x[j]
    res=calculator.calc(param_temp)
    if res and res['eta_0']>0.2:
      y[j]=res['eta_0']*100
      j+=1
    else:
      x=np.delete(x,j)
      y=np.delete(y,j)
  plt.plot(x,y,linewidth=1,color='black')
  if len(x)>0:
    plt.text(x[-1]+3,y[-1]+1,'$\\alpha={}$'.format(i),ha='center',va='center')
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.xlabel('$T_0$(K)')
plt.ylabel('$\eta_0(\%)$')
plt.title(u'总效率与涵道比、环境温度的关系\n',fontsize=13)
ax=plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.savefig('./T_0/eta_0.jpg')
plt.clf()

# 绘制热效率与油气比-环境温度关系图
x=np.linspace(230,300,step,endpoint=True)
y=np.empty((step))
param_temp=param.copy()
fig=plt.figure()
i=0
while i<len(x):
  param_temp['T_0']=x[i]
  res=calculator.calc(param_temp)
  if res:
    y[i]=res['f']
    i+=1
  else:
    x=np.delete(x,i)
    y=np.delete(y,i)
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.xlabel('$T_0$(K)')
plt.title(u'油气比与环境温度的关系\n',fontsize=13)
plt.plot(x,y,color='black',linewidth=1)
plt.ylabel('f')
ax=plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.savefig('./T_0/f-eta_t.jpg')
plt.clf()
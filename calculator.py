# 输入参数： T_0环境滞止温度
#           Ma_0飞行马赫数
#           h_c燃料热值
#           T_t4涡轮前限制温度
#           pi_c压气机压比
#           pi_f风扇压比
#           alpha涵道比
#           gama绝热指数
#           C_p定压比热容
# 输出参数： F_unit单位推力
#           S单位燃油消耗率
#           eta_t热效率
#           eta_p推进效率
#           eta_0总效率
#           u_9内涵喷管出口速度
#           u_19外涵喷管出口速度
#           T_9内涵喷管出口温度
#           T_19外涵喷管出口温度

# 输入已知参数字典（采用国际标准单位）
# 输出计算结果字典（采用国际标准单位）

from math import *

def calc(input):
  T_0   =input['T_0']
  Ma_0  =input['Ma_0']
  h_c   =input['h_c']
  T_t4  =input['T_t4']
  pi_c  =input['pi_c']
  pi_f  =input['pi_f']
  alpha =input['alpha']
  gama  =input['gama']
  C_p   =input['C_p']

  tau_gama=1+(gama-1)/2*Ma_0**2
  a_0=sqrt((gama-1)*C_p*T_0)
  tau_lambda=T_t4/T_0
  tau_c=pi_c**((gama-1)/gama)
  tau_f=pi_f**((gama-1)/gama)
  tau_t=1-(tau_gama/tau_lambda)*((tau_c-1)+alpha*(tau_f-1))
  try:
    u_9=a_0*sqrt(2/(gama-1)*(tau_lambda/(tau_gama*tau_c))*(tau_gama*tau_c*tau_t-1))
  except ValueError:
    return 0
  u_19=a_0*sqrt(2/(gama-1)*(tau_f*tau_gama-1))
  tau_b=tau_lambda/(tau_c*tau_gama)
  T_9=T_0*tau_b
  T_19=T_0
  F_unit=a_0/(1+alpha)*((u_9/a_0-Ma_0)+alpha*(u_19/a_0-Ma_0))
  f=(C_p*T_0)/(h_c)*(tau_lambda-tau_gama*tau_c)
  S=f/((1+alpha)*F_unit)
  eta_t=1-1/(tau_gama*tau_c)
  u_0=Ma_0*a_0
  eta_p=2*(alpha*(u_19/u_0-1)+(u_9/u_0)-1)/(alpha*(u_19**2/u_0**2-1)+(u_9**2/u_0**2-1))
  eta_0=eta_p*eta_t

  output={'F_unit':F_unit,'S':S,'eta_t':eta_t,'eta_p':eta_p,'eta_0':eta_0,'u_9':u_9,'u_19':u_19,'T_9':T_9,'T_19':T_19,'f':f}
  return output

if __name__=="__main__":
  input={'T_0':217,'Ma_0':0.9,'h_c':42800000,'T_t4':1670,'pi_c':2,'pi_f':4,'alpha':1,'gama':1.4,'C_p':1004}
  print('\n'.join(list(map(str,calc(input).items()))))
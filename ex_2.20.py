#ex_2.20-2
import numpy as np
import scipy
import pandas
import matplotlib.pyplot as plt
import sympy
from scipy.integrate import solve_ivp
def fx(t,X,m,c,k):
    x1=X[0]
    x2=X[1]
    dXdt=[x2,-c/m*x2-k/m*x1]
    return dXdt

m=450.0
c=1000.0
k=26519.2
x0=0.539657
xd0=1.0
n=101
delta=2.5e-2
X0=[x0,xd0]
tspan=[0,n*delta]
t=np.linspace(0,n*delta,n+1)
ans=solve_ivp(fx,tspan,X0,args=(m,c,k),method='RK23',dense_output=True)
print(ans.t.shape)
fig,axs=plt.subplots(3,1,figsize=(9.6,6.4))
axs[0].plot(ans.t,ans.y[0],label='x(t)',color='r')
axs[1].plot(ans.t,ans.y[1],label='x(t)',color='b')
plt.show()
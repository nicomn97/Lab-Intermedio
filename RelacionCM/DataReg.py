import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from decimal import Decimal



dB=0.015/1000
Bref=np.array([5.18,5.16,5.20,5.20,5.18,5.23])
dI=0.05
dataReg=np.array([[0.58,1.00,1.48,2,2.51,3.01,3.51,4.02],[4.74,4.52,4.10,3.85,3.42,3.11,2.81,2.41],[4.75,4.53,4.11,3.64,3.38,3.10,2.68,2.31],[4.73,4.54,4.13,3.61,3.47,3.12,2.67,2.36]])
Rc=np.array([0.02,0.03,0.04,0.05])
dV=0.005


Bprom=[]
for i in range(np.shape(dataReg)[1]):
    Bprom.append(np.mean(dataReg[1:,i]))

Bprom=(np.mean(Bref)-np.array(Bprom))*0.001

def recta(x,m,b):
    return m*x+b

popt, pcov = curve_fit(recta, dataReg[0,:], Bprom,sigma=dB, absolute_sigma=True)

mReg=popt[0]
bReg=popt[1]
Bteo=recta(dataReg[0,:],mReg,bReg)

dm=np.sqrt(np.diag(pcov))[0]
print (dm)


t1="$B=$"+str('%.3E' % Decimal(mReg))+"$I+$"+str('%.3E' % Decimal(bReg))

plt.figure(figsize=(8,5))
plt.errorbar(dataReg[0,:],Bprom, yerr=dB, xerr=dI, fmt='o',label="Valores Observados")
plt.plot(dataReg[0,:], Bteo, label=t1)
plt.xlabel("$I\ (A)$")
plt.ylabel("$B\ (T)$")
plt.title("$B\ vs.\ I$")
plt.legend(loc="best")
plt.savefig("g1Prov.pdf")


V =np.array([125.5,150.5,175.1,200,224,250,274])
i2=np.array([2.54,2.93,3.12,3.40,3.60,3.87,4.06])
i3=np.array([1.43,1.72,1.93,2.12,2.24,2.39,2.51])
i4=np.array([1.01,1.28,1.41,1.55,1.67,1.77,1.87])
i5=np.array([0.85,1.02,1.14,1.23,1.33,1.41,1.49])

Bc2=recta(i2,mReg,0)**2
Bc3=recta(i3,mReg,0)**2
Bc4=recta(i4,mReg,0)**2
Bc5=recta(i5,mReg,0)**2

errB2=np.sqrt((2*mReg*(i2**2)*dm)**2+(2*i2*(mReg**2)*dI)**2)
errB3=np.sqrt((2*mReg*(i3**2)*dm)**2+(2*i3*(mReg**2)*dI)**2)
errB4=np.sqrt((2*mReg*(i4**2)*dm)**2+(2*i4*(mReg**2)*dI)**2)
errB5=np.sqrt((2*mReg*(i5**2)*dm)**2+(2*i5*(mReg**2)*dI)**2)


popt2, pcov2 = curve_fit(recta, Bc2,V, sigma=errB2, absolute_sigma=True)
popt3, pcov3 = curve_fit(recta, Bc3,V, sigma=errB3, absolute_sigma=True)
popt4, pcov4 = curve_fit(recta, Bc4,V, sigma=errB4, absolute_sigma=True)
popt5, pcov5 = curve_fit(recta,Bc5, V, sigma=errB5, absolute_sigma=True)



m=np.array([popt2[0],popt3[0],popt4[0],popt5[0]])
b=np.array([popt2[1],popt3[1],popt4[1],popt5[1]])



teo2=recta(Bc2,m[0],b[0])
teo3=recta(Bc3,m[1],b[1])
teo4=recta(Bc4,m[2],b[2])
teo5=recta(Bc5,m[3],b[3])

dm2=np.sqrt(np.diag(pcov2))[0]
dm3=np.sqrt(np.diag(pcov3))[0]
dm4=np.sqrt(np.diag(pcov4))[0]
dm5=np.sqrt(np.diag(pcov5))[0]

dmV=np.array([dm2,dm3,dm4,dm5])*m


t2="$B=$"+str('%.3E' % Decimal(m[0]))+"$I+$"+str(b[0])[:5]
t3="$B=$"+str('%.3E' % Decimal(m[1]))+"$I+$"+str(b[2])[:5]
t4="$B=$"+str('%.3E' % Decimal(m[2]))+"$I+$"+str(b[2])[:5]
t5="$B=$"+str('%.3E' % Decimal(m[3]))+"$I+$"+str(b[3])[:5]

plt.figure(figsize=(8,5))
plt.errorbar(Bc2,V, yerr=dV, xerr=errB2, fmt='o',label="2cm", color="b")
plt.errorbar(Bc3,V, yerr=dV, xerr=errB3, fmt='o',label="3cm",color="g")
plt.errorbar( Bc4,V, yerr=dV, xerr=errB4, fmt='o',label="4cm",color="r")
plt.errorbar( Bc5,V, yerr=dV, xerr=errB5, fmt='o',label="5cm",color="c")
plt.plot(Bc2, teo2, color="b", label=t2)
plt.plot(Bc3,teo3, color="g", label=t3)
plt.plot(Bc4, teo4,  color="r", label=t4)
plt.plot(Bc5, teo5, color="c", label=t5)
plt.xlabel("$B^{2} (T^2)$")
plt.ylabel("$V\ (V)$")
plt.title("$V\ vs.\ B^2$")
plt.legend(loc="best", ncol=2)
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.savefig("g2Prov.pdf")

em=2*m/(Rc**2)
dem=2*dmV/(Rc**2)

for i in range(np.size(em)):
    print ('%.3E' % Decimal(em[i]),'%.3E' % Decimal(dem[i]))


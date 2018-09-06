import numpy as np
import matplotlib.pyplot as plt


plt.figure(figsize=(8,5))
plt.errorbar(1,6.949, yerr=0.046, fmt='o',label="$Relacion B/I\ experimental$")
plt.scatter(2,6.926, label="$Relacion B/I\ Teorica$")
plt.ylabel("$B/I (T/A\\times 10^{-4})$")
plt.xticks([])
plt.title("$B\ vs.\ I$")
plt.legend(loc="best")
plt.savefig("g4.pdf")

plt.figure(figsize=(8,5))
plt.errorbar(1,1.52, yerr=0.24, fmt='o',label="$e/m\ para\ R=2cm$")
plt.errorbar(2,1.51, yerr=0.21, fmt='o',label="$e/m\ para\ R=3cm$")
plt.errorbar(3,1.45, yerr=0.19, fmt='o',label="$e/m\ para\ R=4cm$")
plt.errorbar(4,1.56, yerr=0.23, fmt='o',label="$e/m\ para\ R=5cm$")
plt.scatter(5,1.7588, label="$Valor\ e/m\ CODATA$")
plt.ylabel("$e/m\ (As/kg\\times 10^{11})$")
plt.xlim(0,8)
plt.xticks([])
plt.title("$B\ vs.\ I$")
plt.legend(loc=4)
plt.savefig("g5.pdf")

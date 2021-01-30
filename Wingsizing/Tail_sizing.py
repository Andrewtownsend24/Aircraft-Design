import numpy as np
import matplotlib.pyplot as plt

Vht = 0.75
Vvt = 0.04
taper_ratio_w = .5
ARw = 16 # aspect ratio
ARh = 4
ARv = 2
R1 = 1.25 #ft
R2 = .15 # ft
Sw = 130 #
bw = (ARw * Sw)**.5
print("bw: \t", bw)
c_avg_w = bw/ARw # average chord
print('c avg wing \t',c_avg_w)
Cr = 2 * c_avg_w / (1 + taper_ratio_w) # root chord
print('Chord root', Cr)
Ct = taper_ratio_w * Cr
print('Chord Tip', Ct)
MAC = (2/3) * Cr * ((1 + taper_ratio_w + taper_ratio_w**2) / (1 + taper_ratio_w))
print('MAC', MAC)

Lt = ((2 * Sw * (Vht * MAC + 0.02 * bw))/ (np.pi * (R1 + R2)))**0.5

print('Lt', Lt)
#print('stuff', ((2 *  * (Vht * MAC + 0.02 * bw))/ (np.pi * (R1 + R2))))
Sht = (Vht * Sw * MAC) / (Lt)
bht = (ARh * Sht)**0.5
c_avg_h = bht/ ARh

Svt = (Vvt * Sw * bw) / Lt
bvt = (ARv * Svt)**0.5
c_avg_v = bvt/ ARv


print('Tail arm %.5f' % Lt)
print('H tail Area %.5f' % Sht)
print('V Tail area %.5f' % Svt)
















Vht5 = .5
Vht6 = .6
Vht7 = .7 
Vht8 = .8 
Vht9 = .9 
Vht1 = 1 

Sref = 177
Cref = 5.08
Lht = np.linspace(2,16,100)
R1 = 5
R2 = .5
Sf = np.pi * (R1+R2)*Lht



Sht5 = (Vht5 * Sref * Cref) / Lht
Sht6 = (Vht6 * Sref * Cref) / Lht
Sht7 = (Vht7 * Sref * Cref) / Lht
Sht8 = (Vht8 * Sref * Cref) / Lht
Sht9 = (Vht9 * Sref * Cref) / Lht
Sht1 = (Vht1 * Sref * Cref) / Lht



Swet5 = Sf + 2*Sht5
Swet6 = Sf + 2*Sht6
Swet7 = Sf + 2*Sht7
Swet8 = Sf + 2*Sht8
Swet9 = Sf + 2*Sht9
Swet1 = Sf + 2*Sht1


Smin5 = min(Swet5)
index5 = np.where(Swet5 == Smin5)

Smin6 = min(Swet6)
index6 = np.where(Swet6 == Smin6)

Smin7 = min(Swet7)
index7 = np.where(Swet7 == Smin7)

Smin8 = min(Swet8)
index8 = np.where(Swet8 == Smin8)

Smin9 = min(Swet9)
index9 = np.where(Swet9 == Smin9)

Smin1 = min(Swet1)
index1 = np.where(Swet1 == Smin1)


Sht_min = (Vht1 * Sref * Cref) / Lht[index5]
print("H tail area for least drag = %.5f" % Sht_min)

print(" ")
#print(Swet.index('Smin'))
plt.plot(Lht, Sht5)
plt.plot(Lht, Sht6)
plt.plot(Lht, Sht7)
plt.plot(Lht, Sht8)
plt.plot(Lht, Sht9)
plt.plot(Lht, Sht1)

plt.plot(Lht, Sf)
plt.plot(Lht, Swet5)
plt.plot(Lht, Swet6)
plt.plot(Lht, Swet7)
plt.plot(Lht, Swet8)
plt.plot(Lht, Swet9)
plt.plot(Lht, Swet1)

plt.plot(Lht[index5],Smin5, 'ro')
plt.plot(Lht[index6],Smin6, 'ro')
plt.plot(Lht[index7],Smin7, 'ro')
plt.plot(Lht[index8],Smin8, 'ro')
plt.plot(Lht[index9],Smin9, 'ro')
plt.plot(Lht[index1],Smin1, 'ro')
plt.xlabel("Lht in ft")
plt.ylabel
plt.show()

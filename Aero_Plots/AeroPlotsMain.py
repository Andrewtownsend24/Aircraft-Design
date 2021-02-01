
import numpy as np
import matplotlib.pyplot as plt
import AeroPlot

weight = 12000
air_density = .00022
Sref = 177 #ft
vel = 469.333 # ft/ss

CL = (2 *weight) / (air_density * (vel**2) * Sref) 
#print(CL)

filename1 = "Aero_Plots/Wing/W1.polar"
filename2 = "Aero_Plots/Wing/W2.polar"
filename3 = "Aero_Plots/Wing/W3.polar"
filename4 = "Aero_Plots/Wing/Design1_V8.polar"

dragFile = "Aero_PLots/DragBuildup/Wing1_Cd0.csv"

a1 = AeroPlot.AeroPlot(45,filename1,dragFile)        
a2 = AeroPlot.AeroPlot(30,filename2,dragFile)        
a3 = AeroPlot.AeroPlot(30,filename3,dragFile)
a4 = AeroPlot.AeroPlot(30,filename4,dragFile)    
#labels
wing1 = "Wing 1"
wing2 = "Wing 2"
wing3 = "Wing 3"
wing4 = "Wing 4"
a1.get_CDtot()

# stuff1 = min(a1.get_CDi())
print('W 1 Cdi min @ %f'%  a1.get_AoA()[a1.get_CDi().index(min(a1.get_CDi()))])
print('W 1 Cdi min @ %f'%  a2.get_AoA()[a2.get_CDi().index(min(a2.get_CDi()))])
print('W 1 Cdi min @ %f'%  a3.get_AoA()[a3.get_CDi().index(min(a3.get_CDi()))])

# print('Cd min W1: ', min(a1.get_CDi()))
# print('Cd min W2: ', min(a2.get_CDi()))
# print('Cd min W3: ', 

# a1.append_CDtotal()
# a1.append_L_Dtotal()
# a2.append_CDtotal()
# a2.append_L_Dtotal()

# print(a1.get_CDtotal())
# print(a1.get_L_Dtotal())


fig = plt.figure() 
plt.plot(a1.get_AoA(),a1.get_CDi(),label= wing1)
plt.plot(a2.get_AoA(),a2.get_CDi(),label= wing2)
plt.plot(a3.get_AoA(),a3.get_CDi(),label= wing3)
plt.grid()
plt.xlabel("AoA")
plt.ylabel('CD Total')
plt.legend()

fig = plt.figure() 
plt.plot(a1.get_AoA(),a1.get_CL(),label= wing1)
plt.plot(a2.get_AoA(),a2.get_CL(),label= wing2)
plt.plot(a3.get_AoA(),a3.get_CL(),label= wing3)
plt.plot(a4.get_AoA(),a4.get_CL(),label= wing4)
plt.grid()
plt.xlabel("AoA")
plt.ylabel('CL')
plt.legend()


# fig = plt.figure() 
# plt.plot(a1.get_AoA(),a1.get_L_Dtotal(), label= wing1)
# plt.plot(a2.get_AoA(),a2.get_L_Dtotal(), label= wing2)
# plt.grid()
# plt.xlabel("AoA")
# plt.ylabel('L/D')
# plt.legend()

# fig = plt.figure() 
# plt.plot(a1.get_AoA(),a1.get_CMx(), label= wing1)
# plt.plot(a2.get_AoA(),a2.get_CMx(), label= wing2)
# plt.grid()
# plt.xlabel("AoA")
# plt.ylabel('CMx')
#plt.legend()

plt.show()



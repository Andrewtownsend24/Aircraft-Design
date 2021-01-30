# writen by Andrew Townsend
# for ploting CSV file results from Star CCM+
import CFD_Results as aero
import matplotlib.pyplot as plt
# import numpy as np


plt.style.use('classic')
# import math as m
#  print("hello")
plt.close('all')

path = ["Aero_Plots/Tokyo Drift/Design3.csv", "Aero_Plots/Tokyo Drift/Final.csv", "Aero_Plots/Tokyo Drift/Final_payload.csv",
        "Aero_Plots/Tokyo Drift/TD_final.csv", "Aero_Plots/Tokyo Drift/TD0.csv", "Aero_Plots/Tokyo Drift/TD1.csv"]

design_Names = ["Design3", "Final", "Final_payload", "TD_final", "TD0", "TD1"]


tempurature = 510 # degress rankin 
speed = 51.33345 #ft/s
alt = 1350 # ft
air_density = .00238 # slug/ft^3
chord = 10/12 # ft
half_span = 7.5/2 #ft 

# s0 = aero.AeroResults(path[0], tempurature, speed, alt, air_density, chord,half_span)
# s1 = aero.AeroResults(path[1], tempurature, speed, alt, air_density, chord,half_span)
# s2 = aero.AeroResults(path[2], tempurature, speed, alt, air_density, chord,half_span)
# s3 = aero.AeroResults(path[3], tempurature, speed, alt, air_density, chord,half_span)
# s4 = aero.AeroResults(path[4], tempurature, speed, alt, air_density, chord,half_span)
# s5 = aero.AeroResults(path[5], tempurature, speed, alt, air_density, chord,half_span)

airplane = []

for i in range(0,len(path)):
    temp = aero.AeroResults(path[i], tempurature, speed, alt, air_density, chord,half_span)
    airplane.append(temp)

f1 = plt.figure(1)
for i in range(0,len(path)):
    plt.plot(airplane[i].AoA,airplane[i].get_CL(),'-', label= design_Names[i])

f2 = plt.figure(2)
for i in range(0,len(path)):
    plt.plot(airplane[i].AoA,airplane[i].get_CD(),'-', label= design_Names[i])

f3 = plt.figure(3)

for i in range(0,len(path)):
    plt.plot(airplane[i].AoA,airplane[i].get_CM(),'-', label= design_Names[i])
    
f4 = plt.figure(4)
for i in range(0,len(path)):
    plt.plot(airplane[i].AoA,airplane[i].get_L_D(),'-', label= design_Names[i])

plt.show()
"""
f1 = plt.figure(1)

plt.plot(s0.AoA,s0.get_CL(),'-', label='TD0')
plt.plot(s1.AoA,s1.get_CL(),'-', label='TD1')
plt.plot(s2.AoA,s2.get_CL(),'-', label='TD2')
plt.plot(s3.AoA,s3.get_CL(),'-', label='TD3')
plt.legend()
plt.title('Cl vs AoA')

aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf2 = plt.figure(2)

plt.plot(s0.AoA,s0.get_CD(),'-', label='TD0')
plt.plot(s1.AoA,s1.get_CD(),'-', label='TD1')
plt.plot(s2.AoA,s2.get_CD(),'-', label='TD2')
plt.plot(s3.AoA,s3.get_CD(),'-', label='TD3')
plt.legend()
plt.title('Cl vs AoA')

f3 = plt.figure(3)

plt.plot(s0.AoA,s0.get_CM(),'-', label='TD0')
plt.plot(s1.AoA,s1.get_CM(),'-', label='TD1')
plt.plot(s2.AoA,s2.get_CM(),'-', label='TD2')
plt.plot(s3.AoA,s3.get_CM(),'-', label='TD3')
plt.legend()
plt.title('Cl vs AoA')

f4 = plt.figure(4)

plt.plot(s0.AoA,s0.get_L_D(),'-', label='TD0')
plt.plot(s1.AoA,s1.get_L_D(),'-', label='TD1')
plt.plot(s2.AoA,s2.get_L_D(),'-', label='TD2')
plt.plot(s3.AoA,s3.get_L_D(),'-', label='TD3')
plt.legend()
plt.title('Cl vs AoA')
plt.show()

"""
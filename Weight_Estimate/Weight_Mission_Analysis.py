import math as m
import numpy as np
import matplotlib.pyplot as plt
a =  -1.543 * (10**-5)
b = 0.57
L_Dmax = 10 # L_D max
SFC_cruise = .2 # lb/h/lb
SFC_c = .3 / (3600 * 550) # 1/ft
SFC_loiter = .2 # lb/h hp
SFC_ltr = .3/ (3600 * 550)
V_endurance = 250 * 1.46666667# mph * ft/s / mph) 
#V = 300 * 1.46667 # ft/s, velocity (mph * ft/mph)
n_p = .9 # prop effeceny 
R = 100 * 5280 # ft, Range -(mile * (ft/mile)) 
E = 4 * 3600  #s,Endurance hr * s/hr 
E2 = .75 * 3600  #s,Endurance hr * s/hr 
Wc = 175*2 # lb, Weight of Crew 
Wp =  3000 # lb, Weight of Payload

# weight fractions
#Design Mission
w2_w1 = 0.99 # Taxi takeoff 
w3_w2 = 0.99 # Climb
w4_w3 = m.exp( (-R* (SFC_c))/ (n_p * L_Dmax)) # cruise 
w5_w4 = 0.997 # Descent
w6_w5 = m.exp( (-E * SFC_ltr * V_endurance) / (n_p * L_Dmax))
w7_w8 = 0.99 # Climb
w9_w8 = m.exp( (-R* (SFC_c))/ (n_p * L_Dmax)) # cruise 
w10_w9 = 0.997 # approach landing 
w11_10 = 0.99 # climb
w12_w11 = m.exp( (-E2 * SFC_ltr * V_endurance) / (n_p * L_Dmax)) # reserve loiter
W13_w12 = 0.997 # approach landing 

w13_w1 = w2_w1 * w3_w2 * w4_w3 * w5_w4 * w6_w5 * w7_w8 * w9_w8 * w10_w9  * w11_10 * w12_w11 * W13_w12
Wfuel = 1.0 * (1 - w13_w1)
print(Wfuel)



# print(we_wto)
# print(Wto)
print("Wfuel", Wfuel)
print("w4/w3: ", w4_w3)
print("w9_w8: ", w6_w5)
print('w12_w11: ', w13_w1)


def get_MTOW(Wp,Wc, Wfuel, a, b, Max, Min):
    Wto = np.linspace(Min, Max, 1000, endpoint=True)
    we_wto = np.zeros(len(Wto))
    Wto_final = np.zeros(len(Wto))
    error = np.zeros(len(Wto))

    for i in range(0,len(Wto)):
        we_wto[i] =  (a * Wto[i]) + b
        Wto_final[i] = (Wp + Wc)/ (1 - Wfuel - we_wto[i])
        error[i] = abs((Wto[i] - Wto_final[i])/ Wto_final[i]) 

    MTOW = Wto_final[np.where(error == min(error))]
       
    return Wto,error, MTOW,


def get_MTOW_gudmundsson(Wp,Wc, Wfuel, a, b, Max, Min):
    Wto = np.linspace(Min, Max, 1000, endpoint=True)
    we_wto = np.zeros(len(Wto))
    Wto_final = np.zeros(len(Wto))
    error = np.zeros(len(Wto))

    for i in range(0,len(Wto)):
        we_wto[i] =  (a * m.log(Wto[i])) + b
        Wto_final[i] = (Wp + Wc)/ (1 - Wfuel - we_wto[i])
        error[i] = abs((Wto[i] - Wto_final[i])/ Wto_final[i]) 

    MTOW = Wto_final[np.where(error == min(error))]
       
    return Wto,error, MTOW,


wto1 ,error1, MTOW1= get_MTOW(Wp, Wc, Wfuel, (1.543 * (10**-5)), 0.57, 7000,100000) # GA single Engine
wto2 ,error2, MTOW2 = get_MTOW(Wp, Wc, Wfuel, (2.73 * (10**-4)), -9.08, 0,10000) # GA twin Engine
wto3 ,error3, MTOW3 = get_MTOW(Wp, Wc, Wfuel, (-8.2 * (10**-7)), 0.65, 0,10000) # Twin TurboProp
wto4 ,error4, MTOW4 = get_MTOW(Wp, Wc, Wfuel, ( 1.39 * (10**-6)), 0.64, 0,100000) # Jet Trainer
wto5 ,error5, MTOW5 = get_MTOW(Wp, Wc, Wfuel, (-1.1 * (10**-5)), 0.97, 0,100000) # Fighter


wto6 ,error6, MTOW6= get_MTOW_gudmundsson(Wp, Wc, Wfuel, (-0.03333), 0.8841, 1,100000) # GA single Engine
wto7 ,error7, MTOW7 = get_MTOW_gudmundsson(Wp, Wc, Wfuel, 0.0253, 0.4074, 1,10000) # GA twin Engine
wto8 ,error8, MTOW8 = get_MTOW_gudmundsson(Wp, Wc, Wfuel, 0.0066, 0.5319, 1,10000) # Twin TurboProp
Wto_final_A29 = (Wp + Wc)/ (1 - (171*6.8)/11905 - 7055/11905) # tucano
print(Wto_final_A29)

print("GA single Engine Error: %f MTOW: %f" % (min(error1), MTOW1))
print("GA 2 Engine Error: %f MTOW: %f" % (min(error2), MTOW2))
print("Twin Engine Error: %f MTOW: %f" % (min(error3), MTOW3))
print("Jet trainer  Error: %f MTOW: %f" % (min(error4), MTOW4))
print("fighter Error: %f MTOW: %f" % (min(error5), MTOW5))

print("GA single Engine Error: %f MTOW: %f" % (min(error6), MTOW6))
print("GA 2 Engine Error: %f MTOW: %f" % (min(error7), MTOW7))
print("Twin Engine Error: %f MTOW: %f" % (min(error8), MTOW8))

# #plt.plot(wto1 ,error1, label = 'GA 1')
# plt.plot(wto1, Wto)
# #plt.plot(wto2 ,error2, label = 'GA 2')
# #plt.plot(wto3 ,error3, label = 'Twin Turboprop')
# #plt.plot(wto4 ,error4, label = 'Jet Trainer')
# #plt.plot(wto5 ,error5, label = 'Fighter')
# plt.grid()
# plt.legend()
# plt.show()

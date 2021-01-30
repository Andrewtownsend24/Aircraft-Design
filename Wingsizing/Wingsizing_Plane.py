import matplotlib.pyplot as plt
from math import exp
import numpy as np

# values from book
g = 32.2
mu = .06 # ground friction
MTOW = 12000 #lb
v_max = 320  # KTAS
L_D = 10 # L/D Subsonic military 8-11
v_stall = 80  # KEAS
v_to = 1.1 * v_stall # Velocity at takeoff
ROC = 2700/60  # fps # rate of climb
ROC_c = 100/60  # fps 
S_to = 1200  # ft  
S_ceiling = 35000  # ft
CL_max = 2.7
n_p = .6  # variable pitch prop efficiency
n_p2 = .7  # prop efficiency
h = 550  # conversion factor to convert lb/(lb ft/sec) to lb/hp
h2 = 1.68781  # cefficency
AR = 6 #  Aspectonversion factor knots to ft/sec
e = .85 # Oswald  ratio
K = 1/(np.pi*e*AR)
# https://www.digitaldutch.com/atmoscalc/
air_density_3000 = .002175  # slug/ft^3
air_density_30000 = .00089  # slug/ft^3
air_density_35000 = .000738 # slug/ft^3
air_density_0 = .002378   # slug/ft^3
sigma = air_density_30000/air_density_0 # Max speed
sigma_c = air_density_35000/air_density_0 # cruise
CD_0 = .025 #
CL_c = .5 # CL at cruise
del_CL = 1 # change in lift due to flaps
CL_TO = CL_c + del_CL
CD_0_LG = .009
CD_0_HLD_T0 = .005
CD_0_TO = CD_0 + CD_0_LG + CD_0_HLD_T0 # profile drag at takeoff
CD_T0 = CD_0_TO + K*CL_TO**2 # total drag at takeff
CL_R = CL_max/(1.1**2)
CD_g = (CD_0_TO - mu*CL_TO) # takeoff ratation li

# Wing loading for stall speed is vertical line
w_s_stall = .5*air_density_0*(v_stall*h2)**2*CL_max
print(w_s_stall)

w_s = np.linspace(1, 100, 100)  # wing loading vector


# weight over power for max velocity
w_p_vmax = (n_p2/((.5*air_density_0*(v_max*h2)**3*CD_0*(1/w_s)) + ((2*K/(air_density_30000*sigma*(v_max*h2)))*w_s))) * h
W_P_vmax = 385/(6129.7/w_s + .317*w_s)  # lb/hp
vmax1 = 385/(6129.7/44.8 + .317*44.8)  # lb/hp
vmax2 = (n_p2/((.5*air_density_0*(v_max*h2)**3*CD_0*(1/44.8)) + ((2*K/(air_density_30000*sigma*(v_max*h2)))*44.8))) * h
##w_p_vmax2 = (n_p2/((.5*air_density_0*(v_max*h2)**3*CD_0*(1/1)) + ((2*K/(air_density_30000*sigma*(v_max*h2)))*1))) * h
#W_P_vmax2 = 385/(6129.7*(1/1) + .317*1)  # lb/hp


print("n_p", n_p2)
print("roe", air_density_0)
print("v_max", v_max)
print("CD_0", CD_0)
print("K", K)
print("vmax1", vmax1)
print("vmax1", vmax1)
#print("vmax:",w_p_vmax2)
#print("vmax1:", W_P_vmax2)
print(' ')

# weight over power for takeoff
w_p_sTO = []
W_P_sTO1 = []
for i in w_s:

    w_p_sTO.append((((1 - exp(0.6 * g * air_density_3000 * CD_g * S_to *(1/i))) /
                     (mu - (mu + CD_g / CL_R) * (exp(.6* g * air_density_3000 * CD_g * S_to * (1/i))))) * (n_p/(v_to*h2))) * h)
    W_P_sTO1.append(((1-exp(1.426/i))/(.04-(.053*exp(1.426/i))))*(.0046*550))  # used to evaluate equation

# Weight over power for rate of climb
w_p_ROC = (1/((ROC/n_p2) + (((2/(air_density_0*((3*CD_0)/K)**.5))*w_s)**.5)*(1.155/(L_D*n_p2))))*h

'''
print("ROC",ROC)
print("n_p2",n_p2)
print("air_density_0",air_density_0)
print("K",K)
print("CD_0",CD_0)
print("L_D",L_D)
print(" ")
print(" ")
'''

W_P_ROC1 = (1*550)/(64.3 + ((540.7*w_s)**.5*.092))  # used to evaluate equation

# Weight over power for cruise
w_p_cruise = (sigma_c/((ROC_c/n_p2) + (((2/(air_density_35000*((3*CD_0)/K)**.5))*w_s)**.5)*(1.155/(L_D*n_p2))))*h
W_P_cruise1 = (170.5/(2.38 + ((1742.3 * w_s)**.5)*0.092))  # used to evaluate equation
w_p_cruise1 = (0.31/((1.666/0.7) + (((2/(0.000738*((3*0.025)/0.031)**.5))*w_s)**.5)*(1.155/(18*0.7))))

'''
print("ROC_c",ROC_c)
print("n_p2",n_p2)
print("air_density_35000",air_density_35000)
print("K",K)
print("CD_0",CD_0)
print("L_D",L_D)
print("sigma_c",sigma_c)
print(" ")
'''



w_s2 = w_s_stall # design point
area = MTOW/w_s2
span1 = (AR*area)**.5
chord = area / span1
'''
print("MTOW", MTOW)
print("area",area)
print("v_max", v_max*h2)
print("AR:", AR)
print("Span",span1)
print("chord", chord)
print("L",(.5*air_density_35000*((v_max*h2)**2)*area))
print("CL = ", MTOW/(.5*air_density_35000*((v_max*h2)**2)*area))
print("re", air_density_0*v_max*h2 * 3 / (2.99135 * 10**-7))
'''

plt.vlines(w_s_stall, 0, 40, 'b', label='Stall velecosity')
plt.plot(w_s, w_p_ROC, 'r', label='ROC')
plt.plot(w_s, w_p_sTO, 'y', label='TO')
plt.plot(w_s, w_p_cruise, 'g', label='Ceiling')
plt.plot(w_s, w_p_vmax, 'k',label='Vmax')
# design point 

dp = (sigma_c/((ROC_c/n_p2) + (((2/(air_density_35000*((3*CD_0)/K)**.5))*w_s_stall)**.5)*(1.155/(L_D*n_p2))))*h
plt.plot(w_s_stall, dp, 'ko' )

'''
#Actual
#plt.vlines(w_s_stall, 0, 40, 'b--', label='Stall velecosity')
plt.plot(w_s, W_P_ROC1, 'r--', label='ROC')
plt.plot(w_s, W_P_sTO1, 'y--', label='TO')
plt.plot(w_s, W_P_cruise1, 'g--', label='Ceiling')
plt.plot(w_s, W_P_vmax, 'k--',label='Vmax')
'''



#lt.fill_between(w_s, w_p_ROC, 0)
#plt.fill_between(w_s, w_p_vmax, 0)




boundary_ROC = np.add(w_p_ROC, 1).tolist()
boundary_sTO = np.add(w_p_sTO, 1).tolist()
boundary_cruise = np.add(w_p_cruise, 1).tolist()
boundary_vmax = np.add(w_p_vmax, 1).tolist()

plt.axvspan(w_s_stall, w_s_stall + 5, facecolor='b', alpha=0.2, hatch='/')
#plt.fill_between(stall_vec, w_s , stall_vec2 , color='b', alpha=0.2, hatch='/')
plt.fill_between(w_s, w_p_ROC, boundary_ROC, color='r', alpha=0.2, hatch='/')
plt.fill_between(w_s, w_p_sTO, boundary_sTO, color='y', alpha=0.2, hatch='/')
plt.fill_between(w_s, w_p_cruise, boundary_cruise, color='g', alpha=0.2, hatch='/')
plt.fill_between(w_s, w_p_vmax, boundary_vmax, color='k', alpha=0.2, hatch='/')


plt.xlim(0, 70)
plt.ylim(0,10)
plt.grid()
plt.legend()
plt.title('Wing Sizing')
plt.xlabel('W/S') # wing loading 
plt.ylabel('W/P') # Power Loading
plt.show()

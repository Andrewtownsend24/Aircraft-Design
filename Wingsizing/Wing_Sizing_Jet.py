# written by Andrew 
# wing sizing
# from Mohammad H. Sadraey

import numpy as np
#W = 86000 # weight lbf
# values from book
g = 32.2
mu = .04 # ground friction value
MTOW = 86000 #lb
knot = 1.15077945 # mile per hour
Speed_mph = 615.15748 # mph
v_max = Speed_mph*knot # KTAS
L_D = 18
v_stall = 60  # KEAS
v_to = 1.1 * v_stall # Velocity at takeoff
ROC = 2700/60  # fps # rate of climb
ROC_c = 100/60  # fps 
S_to = 1200  # ft  
S_ceiling = 35000  # ft
CL_max = 2.7
n_p = .6  # prop efficiency
n_p2 = .7
h = 550  # conversion factor to convert lb/(lb ft/sec) to lb/hp
h2 = 1.68781  # conversion factor knots to ft/sec
e = .85 # Oswald efficency
AR = 12 #  Aspect ratio
K = 1/(np.pi*e*AR)
# https://www.digitaldutch.com/atmoscalc/
air_density_3000 = .002175  # slug/ft^3
air_density_30000 = .00089  # slug/ft^3
air_density_35000 = .000738 # slug/ft^3
air_density_0 = .002378   # slug/ft^3
sigma = air_density_30000/air_density_0
sigma_c = air_density_35000/air_density_0
CD_0 = .025
CL_c = .3
del_CL = .6 
CL_TO = CL_c + del_CL
CD_0_LG = .009
CD_0_HLD_T0 = .005
CD_0_TO = CD_0 + CD_0_LG + CD_0_HLD_T0
CD_T0 = CD_0_TO + K*CL_TO**2
CL_R = CL_max/(1.1**2)
CD_g = (CD_0_TO - mu*CL_TO)
# Andrew Townsend
# Nicolai
# Weight Estimates
import numpy as np





def get_Wing_Wt(Kpiv, Nult, MTOW, t_c_max, sweep_LE, AR_w, Sw,taper_ratio_w):
    # Nicolai
    # Verified
    Wing = 3.08 * ((((Kpiv * Nult * MTOW) / t_c_max) * (((((np.tan(sweep_LE * (np.pi / 180))) - ((2 * (1 - taper_ratio_w)) / (AR_w * (1 + taper_ratio_w))))**2) + 1.0) * 10**-6))**0.593) * \
        (((1 + taper_ratio_w)*AR_w)**0.89) * (Sw**0.741)

    return Wing

def get_Wing_Wt_navy(Kpiv, Nult, MTOW, t_c_max, sweep_LE, AR_w, Sw, taper_ratio_w):
    # Nicolai
    # verified
    wt_navy = 19.29 * ((((Kpiv * Nult * MTOW) / t_c_max) * (((((np.tan(sweep_LE * (np.pi / 180))) -
                                                     ((2 * (1 - taper_ratio_w)) / (AR_w * (1 + taper_ratio_w))))**2) + 1.0) * (10**-6)))**0.464) * \
        (((1 + taper_ratio_w)*AR_w)**0.70) * (Sw**0.58)
    
    return wt_navy

def get_Wing_Wt_Subsonic_Transport(MTOW, M0, Nult, sweep_ht_half,t_c_root_HT,AR_w ,Sw, taper_ratio_w):
    # Nicolai
    # Th is wing weight equation is valid for an M0 range of 0.4–0.8, a t/c range
    # of 0.08–0.15, and an aspect ratio (AR) range of 4–12.
    # verified
    top = AR_w * (M0 **0.43) * ((MTOW*Nult)**0.84) * (taper_ratio_w**0.14)
    bot = ((100*t_c_root_HT)**0.76) * (np.cos(sweep_ht_half * (np.pi / 180)))
    wt_sub = 0.00428 * (Sw**0.48) * (top/bot)
    return wt_sub
#print(get_Wing_Wt_Subsonic_Transport(MTOW, M0, Nult, sweep_ht_half, t_c_max,AR_w ,Sw, taper_ratio_w))


def get_Horizontal_Tail_Wt(MTOW, Nult, Sht, B_ht, t_c_root_HT, c_wing, Lt_HT):
    gamma = ((MTOW * Nult)**0.813) * (Sht**0.584) * ((B_ht/t_c_root_HT)**0.033) * ((c_wing/Lt_HT)**0.28)
    HT_wt = 0.0034 * (gamma**0.915)
    return HT_wt
#print(get_Horizontal_Tail_Wt(MTOW, Nult, Sht, B_ht, t_c_root_HT, c_wing, Lt_HT))

def get_Vertical_Tail_Wt(Ht_Hv, MTOW, Nult, Svt, M0, Lt_VT, AR_v, taper_ratio_v, sweep_vt_quater):

    gamma = ((1 + Ht_Hv)**0.5) * ((MTOW*Nult)**0.363) * (Svt**1.089) * (M0**0.601) * ((Lt_VT)**-0.726) * ((1 + 0.3)**0.217) * \
        (AR_v**0.337) * ((1 + taper_ratio_v)**0.363) * ((np.cos(sweep_vt_quater * (np.pi/180)))**-0.484)

    tail = 0.19* (gamma**1.014)
    return tail

def get_Fuselage_Wt(MTOW):
    # Nicolai
    #USAF and Commercial:
    return 62.21 * ((MTOW*.001)**0.84)

def get_Fuselage_Wt_USN(MTOW):
    # Nicolai
    #US Navy plane
    return 129.1* ((MTOW*.001)**0.66) 

def get_Fuel_System_Wt_Self_Sealing(fuel_weight):
    fuel_cell = 41.6 * ((fuel_weight * 0.01)**0.818)
    return fuel_cell

    
def get_Fuel_System_Wt_NonSelf_Sealing(fuel_weight):
    fuel_cell = 23.10 * ((fuel_weight * 0.01)**0.758)
    return fuel_cell

def get_In_Flight_Refueling_Wt(fuel_weight):
    refueling = 13.64 * ((fuel_weight*0.01)**.392)
    return refueling

def get_Fuel_Support_Wt(fuel_weight):
    # for self sealing and non self sealing
    support = 7.91 * ((fuel_weight*0.01)**.854)
    return support

def get_Dumping_Drain_System_Wt(fuel_weight):
    
    dumping = 7.38 * ((fuel_weight*0.01)**0.458)
    return dumping

def get_CG_System(fuel_weight):
    #Transfer Pumps and Monitor
    cg = 28.38 * ((fuel_weight*0.01)**0.442)
    return cg

def get_Engine_Controls_TurboProp_Wt(Lf, B_w, Nen):

    EngineControls = 56.84 * (((Lf + B_w)*Nen*0.01)**0.514)
    return EngineControls

def get_starter(Nen, Wengine):

    starter = 50.38 * ((Nen*Wengine*.001)**0.918)
    return starter

def get_Prop_Wt(Kp, Np, Nbl, Dp, HP):

    prop = Kp * Np * (Nbl**0.391) * ((Dp * HP *.001)**0.782) 
    return prop

def get_Prop_Controls_TurboProp(Nbl, Np, dp, HP):
    propControls = 0.322 *  ((Nbl**0.589) * (Np * dp *HP * .001)**1.178)
    return propControls

def get_Surface_controls_Hydrolic_Pneumatic(Ksc, MTOW):

    surface = Ksc *((MTOW * 0.001)**0.581)
    return surface

def get_Surface_controls_Hydrolic_Pneumatic_Attacker(MTOW):

    surface = 56.01 *((MTOW * 0.001)**1.10)
    return surface

def get_Flight_Instruments_Wt(Npil, MTOW):

    instrument = Npil *(15.0 + (0.032 * MTOW * 0.001))
    return instrument

def get_Engine_Instruments_Wt(Nen, MTOW):
    en_instrument = Nen * (4.80 + 0.006 * MTOW * 0.001)
    return en_instrument

def get_indicators(MTOW):
    indicators = .015 * (MTOW * 0.001)
    return indicators

def get_electrical_system_Wt(fuel_system, Wtron):
    tron = 426.17 * ((fuel_system * Wtron *0.001)** 0.510)
    return tron


def get_electrical_system_Wt_USN(fuel_system, Wtron):
    # US Navy eletrical system estimation
    tron_USN = 426.17 * ((fuel_system * Wtron *0.001)** 0.510)
    return tron_USN

def get_Seat_Wt(Npil, q):
    # Ejection seat weight
    seat = 22.89 * ((Npil * q * 0.01)**0.743)
    return seat

def get_emergency_equipment(Npil,MTOW):

    emergengy = 106.61 * ((Npil * MTOW * 0.00001)**0.585)
    return emergengy

def get_Anti_Ice(Kacai, Wtron, Npil):

    anti = Kacai * ((Wtron * 200 * Npil * 0.001)**0.538)
    return anti



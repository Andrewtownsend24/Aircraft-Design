import numpy as np
# andrew Townsend
# wing Weight
# Ramymer

# Andrew Townsend
# FIGHTER AIRCRAFT
# Raymer


# Weight of Wing
def get_Wing(Kdw, Kvs, Wdg, Nz, Sw, AR_w, t_c_root, taper_ratio, sweep, Scsw):
    # Raymer
    W_w = 0.0103 * Kdw * Kvs * ((Wdg*Nz)**0.5) * (Sw**0.622) * (AR_w**0.785) * t_c_root * ((1 + taper_ratio)**0.05) * \
        (np.cos(sweep * (np.pi/180))**-1.0) * (Scsw**0.04)
    return W_w

# Weight of horizontal Tail
def get_horizontal_tail(Fw, B_h, Wdg, Nz, Sht):
    # Raymer
    W_ht = 3.316 * ((1 + Fw/B_h)**-2.0) * (((Wdg * Nz) / 1000) ** 0.26) * (Sht**0.806)

    return W_ht

def get_vertical_tail(Kdwf, Ht_Hv, Svt, M, Sr, Wdg, Nz, AR_v, Lt, taper_ratio_vt, sweep):
    # Raymer
    W_vt = 0.452 * (Kdwf * (1 + Ht_Hv)**0.5) * ((Wdg * Nz)**0.488) * ((Svt)**0.718) * (M**0.341) * \
        (Lt**-1) * ((1 + Sr/Svt)**0.348) * (AR_v**0.223) * \
        ((1 + taper_ratio_vt)**0.25) * ((np.cos(sweep * (np.pi/180)))**-0.323)
    return W_vt

def get_fuselage(Kdwf, Wdg, Nz, Lm,L, D, W):
    # Raymer
    W_f = 0.499 * Kdwf * (Wdg**0.35) * (Nz**0.25) * (L**0.5) * (D**0.849) * (W**0.685)
    return W_f

def get_main_landing_gear(Kcb, Ktpg, Wl, Nl, Lm):
    # Raymer
    W_mlg = Kcb * Ktpg * ((Wl * Nl)**0.25) * (Lm**0.973)
    return W_mlg

def get_nose_landing_gear(Wl, Nl, Ln, Nnw):
    # Raymer
    W_nlg = ((Wl*Nl)**0.290) * (Ln**0.5) * (Nnw**0.525)
    return W_nlg

def get_engine_mount(Nen, T, Nz):  
    # Raymer
    W_em = 0.013 * (Nen**0.795) * (T**0.579) * Nz
    return W_em

def get_firewall(Sfw):
      # Raymer  
    W_fire = 1.13 * Sfw
    return W_fire

def get_engine_section(W_en, Nen, Nz):
    # Raymer
    W_es = 0.01 * (W_en**0.717) * Nen * Nz
    return W_es

def get_air_induction_system(Kvg, Ld,Ls, Kd, Nen, De):
    # Raymer
    if((Ls/Ld) < 0.25):

        W_ais = 13.29 * Kvg * (Ld**0.643) * (Kd**0.182)* (Nen**1.498) * ((.25)**-0.373) * De 
        return W_ais
    else:

        W_ais = 13.29 * Kvg * (Ld**0.643) * (Kd**0.182)* (Nen**1.498) * ((Ls/Ld)**-0.373) * De 
        return W_ais

def get_tailpipe(De, Ltp, Nen):
    # Raymer
    W_tailpipe = 3.5 * De * Ltp * Nen
    return W_tailpipe

def get_engine_cooling(De, Lsh, Nen):
    # Raymer
    W_cooling = 4.55 * De * Lsh * Nen
    return W_cooling

def get_oil_cooling(Nen):
    # Raymer
    W_oil = 37.82 * (Nen**1.023)
    return W_oil

def get_engine_controls(Nen, Lec):
    # Raymer
    W_econtrols = 10.5 * (Nen**1.008) * (Lec**0.222)
    return W_econtrols

def get_pneumatic_starter(Te, Nen):
    # Raymer
    W_starter = 0.025 * (Te**0.760) * (Nen*0.72)
    return W_starter

def get_fuel_system_tanks(Vt, Vi, Vp, Nt, T, SFC, Nen):
    # Raymer
    W_fuel = 7.45 * (Vt**0.47) * ((1 + Vi/Vt)**-0.095) * (1 + Vp/Vt) * (Nt**0.066) * (Nen **0.052) *((T * SFC / 1000)**0.249)
    
    return W_fuel

def get_flight_controls(M, Scs, Ns, Nc, ):
    # Raymer
    W_flight = 36.28 * (M**0.003) * (Scs**0.489) * (Ns**0.484) * (Nc**0.127)
    return W_flight

def get_instruments(Nen, Nt, Nci):
    # Raymer
    W_in = 8.0 + 36.37 * (Nen**0.676) * (Nt**0.237) + 26.4 * ((1 + Nci)**1.356)
    return W_in

def get_hydraulics(Kvsh,Nu):
    # Raymer
    W_hy = 37.23 *Kvsh * (Nu**0.664)
    return W_hy

def get_electrical(Kmc, Rkva, Nc, La, Ngen):
    # Raymer
    W_ele = 172.2 * Kmc * (Rkva**0.152) * (Nc**0.1) * (La**0.1) * (Ngen**0.091)
    return W_ele

def get_avionics(Wuav):
     # Raymer   
    W_av = 2.117 * (Wuav**0.933)
    return W_av

def get_furnishings(Nc):
    # Raymer
    # includes seats
    W_furnishings = 217.6 * Nc
    return W_furnishings

def get_air_anti_ice(Wuav, Nc):
    # Raymer
    W_ice = 201.6 * (((Wuav + 200*Nc)/1000)**0.735)
    return W_ice

def get_handling_gear(Wdg):
    # Raymer
    W_handle = (3.2*(10**-4)) * Wdg
    return W_handle



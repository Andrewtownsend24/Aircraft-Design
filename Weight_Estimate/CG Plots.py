import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import numpy as np
import FighterWeights_Raymer as fw
import FighterWeights_Nicolai as wt
from PIL import Image



# # andrew Townsend
# # wing Weight
# # Ramymer


roe = .00022  # density slug/ft^3
vel = 337  # ft/s
q = 0.5*roe*(vel**2)  # dynamic pressure lb/ft^2
Lt = 233/12  # tail lenght; wing quarter MAC to tail quater MAC, ft
Lt_HT = 233/12  # tail moment arm length, in feet; quater MAC to quater tail MAC
Lt_VT = 233/12  # tail moment arm length, in feet; quater MAC to quater tail MAC
MTOW = 12000  # max take off weight, lbs

AR_w = 6  # aspect ratio wing
AR_h = 3  # aspect Ratio horizontal tail
AR_v = 2  # aspect Ratio v vertical tail
B_ht = 8  # span of hrizontal tail span ft
B_vt = 5  # span of vertical tail span ft
B_w = 35  # wingspan ft
c_HT = 2.6  # Mean Aerodynamic Chord (MAC), in feet
c_VT = 2.5  # Mean Aerodynamic Chord (MAC),  in feet
D = 5  # fuselage structural depth ft
dp = 6  # propeller diameter in feet per propeller
De = 20/12  # engine diameteter ft
Fw = 18/12  # fuselage width at horizontal tail intersection, ft
fuel_weight = .4*MTOW  # can be estimated as (.4 * MTOW)
Ht = 0.0 # horizontal tail hgiht above fuselage, ft (Modify code vertical tail if t tail)
HP = 1600 # rated engine shaft power:
Ht_Hv = 0.0  # 0.0 for conventional tail, 1 for T tail 
hv = 1  # vertical tail height above fuselage ft (Modify code vertical tail if t tail)
I = 580*(10**-6) * (144)  # yawing moment of inertia lb-ft^2
Kacai = 212.00  # anti icing coefficient
# 212.00 if wing and tail anti icing
# 108.64 if no
Kcb = 1  # else 2.25  cross-beam (f-111) gear; 1.0 otherwise
Kd = 1  # Duct constant
Kdoor = 1  # 1 if no cargo door
# 1.06 if on side cargo door
# 1.12 if two cargo doors
# 1.25 if two cargos doors and aft clamshell door
Kpiv = 1  # for fixed wings/ 1.175 for variable geometry wings
Kdw = 1  # 0.758 for delta wing; 1 if otherwise
Kdwf = 1  # .774 for delta wing; 1 if otherwise
Kh = 0.05  # 0.05 for low subsonic with hydraulics for brakes and retracts only;
# 0.11 for medium subsonic wit hydraulics for flaps
# 0.12 for high subsonic with hydraulic flght controls;
# 0.13 for for light plane with hydralic brakes only and M =0.1
Klg = 1.12  # 1.12 if fuselagee niybted naub kabdubg gear 1.0 otherwise
Kmc = 1.45  # 1.45 if mission completion required after failure; 1 if otherwise
Kvs = 1  # 1.19 variable swept wing otherwise 1
Kmp = 1  # 1.126 for kneeling gear; 1 if otherwise
Kng = 1.0  # 1.017 for pylon-mounted nacelle; 1.0 if otherwise
Kp = 1.4  # 1.4 f0r engine with propeller; 1.0 otherwise
Kr = 1  # 1.133 if reciprocating engine; 1 if otherwise
Krht = 1.0  # 1.047 if rolling horizontal tail; 1 if otherwise (also known as tailerons)
Ktp = 0.798  # .0798 if turboprop; 1 if otherwise
Ktpg = 0.826  # 1.18 for tripod (A-7) gear; 1 if otherwise
Ktr = 1  #1.18  for jet with thrust reverser; 1 if otherwise
Ksc = 138.18  # 106.10 for elevon without horizontal tail
# 138.18 for horizontal tail surcface control coefficient
# 167.48 for variable sweep wing
# surcface control coefficient
Kuht = 1  # 1.143 for unit (all moving horizontal tail); 1 if otherwise
Kvg = 1  # 1.62 for variable geometry; 1 if otherwise
Kvs = 1  # 1.19 for variable sweep wing; 1 if otherwise
Kvsh = 1  # 1.425 for variable sweep wigng; 1 if otherwise
Ky = 0.3*Lt  # air pitching radius of gyration ft
Kz = Lt  # yawing radius of gyration ft


L = 32 # fuselage structuaral Length ft (excludes radome cowiling and tail cap) ft
La = 5  # electric routing distance ft generators to avionics to cockpit
Ld = 10  # duct lenght ft (only needed if jet)
Lec = 5  # routing distance from engine to cockpit total if multiengine
Lf = 35  # total fuselage Length
Lm = 36  # Extended length of main landing gear, in
Ln = 36  # extended nose gear lenght in
Ls = 1  # single duct length (only needed if jet)
Lsh = 2  # lenght of engine coolign shroud ft (only needed if jet)

Ltp = 2  # length of Tailpipe ft (only needed if jet)

M = 0.4  # Mach number
M0 = .4  # mach number at sea level

Nbl = 3  # numb of prop blades
Nc = 2  # Number of crew(.5 for UAV)
Nci = 1.2  # number of crew equivelents() 1 if single pilot 1.2 if pilor plus backseater; 
# 2 if pilot and copilot

Nen = 1  # number of engines
Nf = 5  # number of separate functions performed by suface controls, 
# including rudder, aileron, elevator, flaps, spoiler, and speed brakes
# typically(4-7)

Ngen = Nen  # number of generators(typically = Nen)
Ngear = 3  # number of gear
Nlt = 3  # nacelle length, ft
Nl = Ngear*1.5  # ultimate landing load factor ; Ngear x 1.5
Nlim = 7  # limit load factor

Nm = 3 # number of surface controls driven by mechanical actuation instead of hydraulics
# (must be <= Nf and is typically 0-3)

Nmss = 2  # number of main gear shock struts
Nms = 2  # number of main wheels
Nnw = 1  # number of nose wheels
Np = 2  # number of personnel onboard (crew and passengers)
Npil = Np  # number of pilots
Ns = 2  # number of flight control systems
Nt = 2  # number of fuel tanks
Nu = 10  # number of hydraylic utility functions (typically 5 - 15)

Nult = 13.5 # 13.5 for fi ghter aircraft 
# (based on a design limit load factor of +9.0 and a margin of safety of 1.5)
# Nult =  4.5 for bomber and transport aircraft (based on a design limit load factor of +3.0)

Nw = 1  # nacelle width, ft
Nz = Nlim * 1.5  # ultimate load factor


Pdelta = 8  # cabin pressure differential, psi
Rkva = 110 # system electrical rating,
# kv*A(typically 40-60 for transport)(typically 110-160 for fight/bombers)

Scs = 18  # total area of control surfaces ft^2
Scsw = 10  # total area of control surfaces wing mounted ft^2
Se = 6  # elevator area ft^2
Sf = 363.36 + 113.33  # fuselage wetted area ft^2
Sfw = np.pi * (2.5**2)  # firewall surface area ft^2
Sn = 0  # nacelle wetted area, ft
Sr = 4  # rudder area ft^2
Sstall = 60  # stall speed kt,
Svt = 12  # vertical; tail area ft^2
Sht = 21  # horizontal tail, area ft^2
Sw = 177  # wing area
sweep = 0  # wing sweep, deg
sweep_LE = 4  # Leading edge wing sweep
sweep_half_chord = 4  # sweep at half chord
sweep_ht_half = 4  # sweep at half chord of Horizontal tail deg
sweep_vt_half = 4  # sweep at half chord of vertical tail deg
sweep_vt_quater = 4  # sweeep at quater chord
SFC = .001  # engine specife fuel consumption at maximun thrust lb/hr/lb
T = (HP * 550)/vel  # total engine trhust,lb (for prop engine) (550 ft lbs / sec = 1 HP)
taper_ratio_w = .5  # (wing)
taper_ratio_v = 1/4  # (vertical tail)

t_c = .12  # thickness to chord ratio (At mean chord)
t_c_root = .12  # wing
t_c_max = .12  # max t/c Wing
t_c_root_HT = .12  # t/c for horizontal tail
t_c_root_VT = .12  # t/c for vertical tail
Vi = 40  # internal tak volume, gal
Vp = 40  # self-sealing " protected tanks volume " gal
Vpr = 0  # volume of pressurized section ft^3
Vt = 40  # total fuel volume, gal
W = 5  # total fuselage structural width ft
Wc = 25  # maximum cargo weight lb

Wdg = MTOW - fuel_weight  # # flight design weight, lb 
# (typically 50-60% of internal fuel for military aircraft)

Wengine = 270  # weight of engine, lbs

Wec = 2.331 * (Wengine**.901) * Kp * Ktr # weight engine weight and contens, each, lb

Wfw = 40*6.7  # weight of fuel in each wing, lb, (if zero ignore)
Wl = MTOW*.7  # landing design gross weight, lb
Wpress = 11.9 * ((Vpr*Pdelta)**0.271)
Wtron = 1000  # weight of electrical system
Wuav = 800 # unistalled avionics weight 800-1400lbs

Te = T/Wengine # thrust per engine lb
#
Kws = .75*((1 + 2 * taper_ratio_w)/(1 + taper_ratio_w)) * \
    (B_w / L) * np.tan(sweep * (np.pi/180))


# FIGHTER AIRCRAFT
# raymer Textbook
W_w = fw.get_Wing(Kdw, Kvs, Wdg, Nz, Sw, AR_w,
                  t_c_root, taper_ratio_w, sweep, Scsw)
W_ht = fw.get_horizontal_tail(Fw, B_ht, Wdg, Nz, Sht)
W_vt = fw.get_vertical_tail(Kdwf, Ht_Hv, Svt, M, Sr,
                            Wdg, Nz, AR_v, Lt, taper_ratio_v, sweep)
W_f = fw.get_fuselage(Kdwf, Wdg, Nz, Lm, L, D, W)
W_mlg = fw.get_main_landing_gear(Kcb, Ktpg, Wl, Nl, Lm)
W_nlg = fw.get_nose_landing_gear(Wl, Nl, Ln, Nnw)
W_em = fw.get_engine_mount(Nen, T, Nz)
W_fw = fw.get_firewall(Sfw)
W_es = fw.get_engine_section(Wengine, Nen, Nz)
W_ais = fw.get_air_induction_system(Kvg, Ld, Ls, Kd, Nen, De)
W_tailpipe = fw.get_tailpipe(De, Ltp, Nen)
W_cooling = fw.get_engine_cooling(1, 1, 1)
W_oil = fw.get_oil_cooling(Nen)
W_engine_controls = fw.get_engine_controls(Nen, Lec)
W_stater = fw.get_pneumatic_starter(Te, Nen)
W_fuel = fw.get_fuel_system_tanks(Vt, Vi, Vp, Nt, T, SFC, Nen)
W_flight = fw.get_flight_controls(M, Scs, Ns, Nc)
W_in = fw.get_instruments(Nen, Nt, Nci)
W_hy = fw.get_hydraulics(Kvsh, Nu)
W_ele = fw.get_electrical(Kmc, Rkva, Nc, La, Ngen)
W_av = fw.get_avionics(Wuav)
W_furnishings = fw.get_furnishings(Nc)
W_ice = fw.get_air_anti_ice(Wuav, Nc)
W_handle = fw.get_handling_gear(Wdg)

gross_weight_raymer = W_w + W_ht + W_vt + W_f + W_mlg + W_nlg + W_em + W_fw + W_es + W_ais + W_cooling + W_oil + \
    W_engine_controls + W_stater + W_fuel + W_flight + W_in + \
    W_hy + W_ele + W_av + W_furnishings + W_ice + W_handle

#print(gross_weight_raymer)


# Nicolai
wt_wing = wt.get_Wing_Wt(Kpiv, Nult, MTOW, t_c_max, sweep_LE, AR_w, Sw, taper_ratio_w)
wt_wing_USN = wt.get_Wing_Wt_navy(
    Kpiv, Nult, MTOW, t_c_max, sweep_LE, AR_w, Sw, taper_ratio_w)
wt_Wing_subsonic = wt.get_Wing_Wt_Subsonic_Transport(
    MTOW, M0, Nult, sweep_ht_half, t_c_max, AR_w, Sw, taper_ratio_w)
wt_h_tail = wt.get_Horizontal_Tail_Wt(
    MTOW, Nult, Sht, B_ht, t_c_root_HT, c_HT, Lt_HT)
wt_v_tail = wt.get_Vertical_Tail_Wt(
    Ht_Hv, MTOW, Nult, Svt, M0, Lt_VT, AR_v, taper_ratio_v, sweep_vt_quater)
wt_fuselage = wt.get_Fuselage_Wt(MTOW)
wt_fuselage_USN = wt.get_Fuselage_Wt_USN(MTOW)
wt_fuelsystemselfsealing = wt.get_Fuel_System_Wt_Self_Sealing(fuel_weight)
wt_fuelsystem = wt.get_Fuel_System_Wt_NonSelf_Sealing(fuel_weight)
wt_refueling = wt.get_In_Flight_Refueling_Wt(fuel_weight)
wt_fuelsupport = wt.get_Fuel_Support_Wt(fuel_weight)
wt_dump_drain = wt.get_Dumping_Drain_System_Wt(fuel_weight)
wt_cg = wt.get_CG_System(fuel_weight)
wt_enginecontrols = wt.get_Engine_Controls_TurboProp_Wt(Lf, B_w, Nen)
wt_starter = wt.get_starter(Nen, Wengine)
wt_prop = wt.get_Prop_Wt(Kp, Np, Nbl, dp, HP)
wt_propContols = wt.get_Prop_Controls_TurboProp(Nbl, Np, dp, HP)
wt_controlsurface = wt.get_Surface_controls_Hydrolic_Pneumatic(Ksc, MTOW)
wt_controlsurfaceAttacker = wt.get_Surface_controls_Hydrolic_Pneumatic_Attacker(
    MTOW)
wt_flightinstrument = wt.get_Flight_Instruments_Wt(Npil, MTOW)
wt_engineinstruments = wt.get_Engine_Instruments_Wt(Nen, MTOW)
wt_indicators = wt.get_indicators(MTOW)
wt_tronsystem = wt.get_electrical_system_Wt(wt_fuelsystemselfsealing, Wtron)
wt_tronsystemUSN = wt.get_electrical_system_Wt_USN(
    wt_fuelsystemselfsealing, Wtron)
wt_ejectorseat = wt.get_Seat_Wt(Npil, q)
wt_emergency = wt.get_emergency_equipment(Npil, MTOW)
wt_anti_ice = wt.get_Anti_Ice(Kacai, Wtron, Npil)

gross_weight_nicolai = wt_wing + wt_h_tail + wt_v_tail + wt_fuselage + wt_fuelsystemselfsealing + wt_refueling + wt_fuelsupport + wt_dump_drain + wt_cg + wt_enginecontrols + \
    wt_starter + wt_prop + wt_propContols + wt_controlsurfaceAttacker + wt_flightinstrument + \
    wt_engineinstruments + wt_indicators + \
    wt_ejectorseat + wt_emergency + wt_anti_ice # wt_tronsystem is left out


print("Raymer Textbook Weight Aproximation")
print(" ")
print("Wing Weight \t \t \t \t %.5f lbs" % W_w)
print("Horizontal Stabilizer Weight \t \t %.5f lbs" % W_ht)
print("vertical Stabilizer Weight \t \t %.5f lbs" % W_vt)
print("Fuselage Weight \t \t \t %.5f lbs" % W_f)
print("Main Landing Gear Weight \t \t %.5f lbs" % W_mlg)
print("Nose Landing Gear Weight \t \t %.5f lbs" % W_nlg)
print("Engine Mount Weight: \t \t \t %.5f lbs" % W_em)
print("firewall Weight \t \t \t %.5f lbs" % W_fw)
print("Engine Section Weight \t \t \t %.5f lbs" % W_es)
print("Air induction System Weight \t \t %.5f lbs" % W_ais)
print("Tailpipe Weght \t \t \t \t %.5f lbs" % W_tailpipe)
print("Engine cooling Wieght \t \t \t %.5f lbs" % W_cooling)
print("Oil cooling Weight \t \t \t %.5f lbs" % W_oil)
print("Engine Controls Weight \t \t \t %.5f lbs" % W_engine_controls)
print("Pneumatic Starter Weight \t \t %.5f lbs" % W_stater)
print("Fuel System and tanks Weight \t \t %.5f lbs" % W_fuel)
print("Flight Controls Weight \t \t \t %.5f lbs" % W_flight)
print("Intruments Weight \t \t \t %.5f lbs" % W_in)
print("Hydraulic Weight  \t \t \t %.5f lbs" % W_hy)
print("Electrical Weight  \t \t \t %.5f lbs" % W_ele)
print("Avionics Weight \t \t \t %.5f lbs" % W_av)
print("furnishings Weight \t \t \t %.5f lbs" % W_furnishings)
print("Air and Anti-Ice Weight \t \t %.5f lbs" % W_ice)
print("Handling gear Weight \t \t \t %.5f lbs" % W_handle)
print("gross Weight \t \t \t %.5f lbs" % gross_weight_raymer)
print(" ")
print(" ")
print(" ")
print("Nicolai Textbook Weight Estimate")
print(" ")
print("Wing Weight \t \t \t \t %.5f lbs" % wt_wing)
print("Wing Weight USN\t \t \t \t %.5f lbs" % wt_wing_USN)
print("Wing Weight Subsonic transport\t \t %.5f lbs" % wt_Wing_subsonic)
print("Horizontal tail Weight \t \t \t %.5f lbs" % wt_h_tail)
print("Vertical Tail Weight \t \t \t %.5f lbs" % wt_v_tail)
print("Fuselage Weight \t \t \t %.5f lbs" % wt_fuselage)
print("Fuselage USN Weight \t \t \t %.5f lbs" % wt_fuselage_USN)
print("Fuel System self sealing Weight \t %.5f lbs" % wt_fuelsystemselfsealing)
print("Fuel System nonself sealing Weight \t %.5f lbs" % wt_fuelsystem)
print("Refueling Weight \t \t \t %.5f lbs" % wt_refueling)
print("Fuel tank support Weight \t \t %.5f lbs" % wt_fuelsupport)
print("Dump and Drain Weight \t \t \t %.5f lbs" % wt_dump_drain)
print("CG control system Weight \t \t %.5f lbs" % wt_cg)
print("Engine Control Weight \t \t \t %.5f lbs" % wt_enginecontrols)
print("Engine Starter Weight \t \t \t %.5f lbs" % wt_starter)
print("Propeller Weight \t \t \t %.5f lbs" % wt_prop)
print("Prop Controls Weight \t \t \t %.5f lbs" % wt_propContols)
print("Control Surface Weight \t \t \t %.5f lbs" % wt_controlsurface)
print("Control surface Weight Attacker \t %.5f lbs" %
      wt_controlsurfaceAttacker)
print("flight Instrument Weight \t \t %.5f lbs" % wt_flightinstrument)
print("Engine Instrument Weight \t \t %.5f lbs" % wt_engineinstruments)
print("Other indicator Weight \t \t \t %.5f lbs" % wt_indicators)
# print(Wtron)
# print(wt_fuelsystemselfsealing)
# print("Electronic system Weight \t \t %.5f lbs" % wt_tronsystem)
# print("Electronic system USN Weight \t \t %.5f lbs" % wt_tronsystemUSN)
# print("Ejector Seat Weight \t \t \t %.5f lbs" % wt_ejectorseat)
print("Emergency supplies Weight \t \t %.5f lbs" % wt_emergency)
print("Anti ice System Weight \t \t \t %.5f lbs" % wt_anti_ice)
print("gross Weight \t \t \t \t %.5f lbs" % gross_weight_nicolai)

print(" percent differnce %.5f  " % ((gross_weight_nicolai - gross_weight_raymer)/ gross_weight_nicolai) )

width, height = Image.open('Design_v8.png').size

EngineX = 1.66 + (6.22/2)
EngineY = 7.5

fig, ax = plt.subplots(1,1)

print("Width: ", width)
print("Height:, ", height)
img = mpimg.imread('Design_v8.png')
imgplot = ax.imshow(img, extent=[0,40,0,20])
#ax.set_xticks([0,40])
#imgplot.xlim(0, 30)

# 7.48051935474855 = gallons per ft^3
aviation_fuel_density = 7.48051935474855 * 6.7 # lb/ft^3
volume = 10.77
num_gallons = volume*7.48051935474855
print(aviation_fuel_density)
print(num_gallons)

plt.plot(6,6, 'ro', label= 'wing1' )
plt.legend()

plt.show()

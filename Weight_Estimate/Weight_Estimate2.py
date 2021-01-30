import math

R_Cruise = # 
V_loiter = float(input('loiter velocity in mph: '))
E_loiter = float(input('time of loiter: '))
Crew = float(input('number of pasengers: '))

A = -0.144
B = 1.1162
warmup = 0.995
taxi = 0.997
takeoff = 0.998
climb = 0.992
descent = 0.993
shutdown = 0.993
np = 0.8 # Prop effency
SFC = 0.6 # Spefic fuel consumption
L_D_max_cruise = 9 
L_D_loiter = 11
np_loitter = 0.7
SFC_loiter = 0.6

cruise = ((math.exp(R_cruise * (np / SFC) * L_D_max))) ** -1)
loiter = (math.exp(Eltr * Vltr / (ldltr * (375 * (npltr / cpltr)))) ** -1)
loiterres = (math.exp(0.75 * Vltr / (ldltr * (375 * (npltr / cpltr)))) ** -1)

# equation calculates weight of needed fuel
Wfuel = (1 - warmup * taxi * takeoff * climb * descent * shutdown * loiter * cruise) * Wtoguess
Wresurves = (1 - climb * descent * loiterres * shutdown) * Wtoguess  # equation calculates weight of needed fuel reserves
Wcrew = 180*2

Wcrew = Crew * 200  # as per regulations 175 per person 25 per bag
Wtf = 2 * 7.5 + 0.5 * 6  # 2 gallons at 7.5 lbs a gallon of oil and 1/2 a gallon of unusable gasoline
We = 10 ** ((math.log10(Wtoguess) - A) / B)  # equation gives a guess for empty weight
Wempty = We + Wtf + Wcrew  # definition of empty weight
Wfuel= Wfused + Wres  # total Weight of fuel
Wto = Woe + Wf + Wpl  # Weight of take off based on empty wieght fuel weight and payload weight

print("Empty dry weight: " + str(We))
print("Empty weight: " + str(Woe))
print("Weight of fuel including reserves: " + str(Wf))
print("Total weight: " + str(Wto))

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('classic')
# import math as m
#  print("hello")
plt.close('all')

path = ["Aero_Plots/Tokyo Drift/Design3.csv", "Aero_Plots/Tokyo Drift/Final.csv", "Aero_Plots/Tokyo Drift/Final_payload.csv",
        "Aero_Plots/Tokyo Drift/TD_final.csv", "Aero_Plots/Tokyo Drift/TD0.csv", "Aero_Plots/Tokyo Drift/TD1.csv"]

design_Names = ["Design3", "Final", "Final_payload", "TD_final", "TD0", "TD1"]
#df = pd.read_csv('Tokyo Drift/Final.csv')
# print(df)
# print(df.columns)
# print(df.iloc[2,2])


class AeroResults:
    AoA = list(range(-5,11)) 
    beta = [0]*16

    def __init__(self, path, tempurature, speed, alt, air_density, chord,half_span):
        self.path = path
        m1 = FileReader(self.path)
        self.matrix = m1.readFile()
        

        
        self.lift = []
        self.drag = []
        self.CL = []
        self.CD = []
        self.CM = []
        self.c = []
        self.L_D = []
        self.temperature = tempurature
        self.u_inf1 = speed
        self.alt = alt
        self.air_density = air_density
        self.chord = chord
        self.half_span = half_span
        
        # Calculated values in the class
        self.speed_of_sound = np.sqrt(1.4*1716*self.temperature)
        self.mach = self.u_inf1/self.speed_of_sound # mach number
        self.u_inf = self.mach*self.speed_of_sound # oncoming airspeed.
        self.s_ref = self.chord*2*self.half_span # wing Area
        self.q_inf = .5*self.air_density*(self.u_inf1**2) # dynamic pressure
        # super().__init__()

    
    def get_lift(self):
        
        self.lift = []

        
        for i in range(0,len(self.matrix)):
            temp = self.matrix.iloc[i, 2]*np.cos(self.AoA[i]*np.pi/180)-self.matrix.iloc[i, 1]*np.sin(self.AoA[i]*np.pi/180)
            self.lift.append(temp)
        
        
    def get_drag(self):

        self.drag = []

        for i in range(0,len(self.matrix)):
            
            temp = self.matrix.iloc[i,1]*np.cos(self.AoA[i]*np.pi/180)*np.cos(self.beta[i]*np.pi/180) + \
            self.matrix.iloc[i,2]*np.sin(self.AoA[i]*np.pi/180)*np.cos(self.beta[i]*np.pi/180)+ self.matrix.iloc[i,5]*np.sin(self.beta[i]*np.pi/180)
            
            self.drag.append(temp)

    def get_c(self):
        
        for i in range(0,len(self.matrix)-1):
            temp = self.matrix.iloc[i,5]*np.cos(self.beta[i]*np.pi/180) - self.matrix.iloc[i,1]*np.cos(self.AoA[i]*np.pi/180) \
            *np.sin(self.beta[i]*np.pi/180) - self.matrix.iloc[i,2]*np.sin(self.AoA[i]*np.pi/180)*np.sin(self.beta[i]*np.pi/180)

            self.c.append(temp)
        
    def get_CL(self):

        self.CL = []
        self.get_lift()
                
        for i in range(0,len(self.matrix)):
            cl = 2*self.lift[i]/(self.q_inf*self.s_ref)

            self.CL.append(cl)
        return self.CL
    
    def get_CD(self):

        #self.CL = []
        self.get_drag()
        
        for i in range(0,len(self.matrix)):
            cd = 2*self.drag[i]/(self.q_inf*self.s_ref)

            self.CD.append(cd)

        return self.CD
        
    def get_CM(self):

        for i in range(0,len(self.matrix)):
            cm = 2*self.matrix.iloc[i,3]/(self.q_inf*self.s_ref*self.chord)

            self.CM.append(cm)
        return self.CM

    def get_L_D(self):
        self.get_drag()
        self.get_lift()

        for i in range(0,len(self.matrix)):
            temp = self.lift[i]/self.drag[i]

            self.L_D.append(temp)
        
        return self.L_D

class FileReader:
    
    def __init__(self,filepath):

        self.filepath = filepath
        
    def readFile(self):    
        name2 = ["Iteration", "Axial_Force(lbf)", "Normal_Force(lbf)", "Pitch_Moment(lbf-ft)",
                 "Roll_Moment(lbf-ft)", "Side_Force(lbf)", "Yaw_Moment(lbf-ft)"]

        name1 = ["Iteration",
                 "Axial Force Monitor 2: Axial Force Monitor 2 (lbf)",
                 "Normal Force Monitor 2: Normal Force Monitor 2 (lbf)",
                 "Pitch Moment Monitor 2: Pitch Moment Monitor 2 (lbf-ft)",
                 "Roll Moment Monitor 2: Roll Moment Monitor 2 (lbf-ft)",
                 "Side Force Monitor 2: Side Force Monitor 2 (lbf)",
                 "Yaw Moment Monitor 2: Yaw Moment Monitor 2 (lbf-ft)"]
        
        df1 = pd.read_csv(self.filepath)
        
        df1 = df1.rename(columns={name1[0]: name2[0]})
        df1 = df1.rename(columns={name1[1]: name2[1]})
        df1 = df1.rename(columns={name1[2]: name2[2]})
        df1 = df1.rename(columns={name1[3]: name2[3]})
        df1 = df1.rename(columns={name1[4]: name2[4]})
        df1 = df1.rename(columns={name1[5]: name2[5]})
        df1 = df1.rename(columns={name1[6]: name2[6]})
        
        #print(df1)
       
        #return df1.drop([0, 15, 16, 18, 19, 20])
        return df1



tempurature = 510 # degress rankin 
speed = 51.33345 #ft/s
alt = 1350 # ft
air_density = .00238 # slug/ft^3
chord = 10/12 # ft
half_span = 7.5/2 #ft 

s0 = AeroResults(path[0], tempurature, speed, alt, air_density, chord,half_span)
s1 = AeroResults(path[1], tempurature, speed, alt, air_density, chord,half_span)
s2 = AeroResults(path[2], tempurature, speed, alt, air_density, chord,half_span)
s3 = AeroResults(path[3], tempurature, speed, alt, air_density, chord,half_span)
s4 = AeroResults(path[4], tempurature, speed, alt, air_density, chord,half_span)
s5 = AeroResults(path[5], tempurature, speed, alt, air_density, chord,half_span)


airplane = []

for i in range(0,len(path)):
    temp = AeroResults(path[i], tempurature, speed, alt, air_density, chord,half_span)
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
    
#plt.label()

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

f2 = plt.figure(2)

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
#print(s1.get_Matrix())
# for i in range(0, 5):
#    print(path[i])
#    print(matrix[i])


'''
df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                   columns=['a', 'b', 'c'])

name1 =['a', 'b', 'c']
name2 = ['A', 'B', 'C']
df2 = df2.rename(columns={name1[0]: name2[0]})
df2 = df2.rename(columns={name1[1]: name2[1]})
df2 = df2.rename(columns={name1[2]: name2[2]})
print(df2)
'''

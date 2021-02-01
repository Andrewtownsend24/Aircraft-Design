#import pandas as pd
#import pprint as pp
import matplotlib.pyplot as plt
import pandas as pd

class AeroPlot(object):

    def __init__(self, numpoints,filename, dragFileName):
        
        
        self.numpoints = numpoints
        self.filename = filename
        self.dragFileName = dragFileName

        contents = open(self.filename).read()
        self.matrix = [item.split() for item in contents.split('\n')[:-1]]

        self.Beta = []
        self.Mach = []
        self.AoA = []
        self.Re_1e6 = []
        self.CL = []
        self.CDo = []
        self.CDi = []
        self.CDtot = []
        self.CS = []
        self.L_D_VSP = []
        self.E = []
        self.CFx = []
        self.CFy = []
        self.CFz = []
        self.CMx = []
        self.CMy = []
        self.CMz = []
        self.CMl = []
        self.CMm = []
        self.CMn  = []
        self.CDtotal = []
        self.L_Dtotal = []

        for i in range(1,numpoints):
            self.Beta.append(float(self.matrix[i][0]))
            self.Mach.append(float(self.matrix[i][1]))
            self.AoA.append(float(self.matrix[i][2]))
            self.Re_1e6.append(float(self.matrix[i][3]))
            self.CL.append(float(self.matrix[i][4]))
            self.CDo.append(float(self.matrix[i][5]))
            self.CDi.append(float(self.matrix[i][6]))
            self.CDtot.append(float(self.matrix[i][7]))
            self.CS.append(float(self.matrix[i][8]))
            self.L_D_VSP.append(float(self.matrix[i][9]))
            self.E.append(float(self.matrix[i][10]))
            self.CFx.append(float(self.matrix[i][11]))
            self.CFy.append(float(self.matrix[i][12]))
            self.CFz.append(float(self.matrix[i][13]))
            self.CMx.append(float(self.matrix[i][14]))
            self.CMy.append(float(self.matrix[i][15]))
            self.CMz.append(float(self.matrix[i][16]))
            self.CMl.append(float(self.matrix[i][17]))
            self.CMm.append(float(self.matrix[i][18]))
            self.CMn .append(float(self.matrix[i][19])) 

        
        with open(self.dragFileName , 'r') as temp_f:
            # get No of columns in each line
            col_count = [ len(l.split(",")) for l in temp_f.readlines() ]

        ### Generate column names  (names will be 0, 1, 2, ..., maximum columns - 1)
        column_names = [i for i in range(0, max(col_count))]

        ### Read csv
        self.df = pd.read_csv(self.dragFileName, header=None, delimiter=",", names=column_names)
        

    def get_Beta(self):
        return self.Beta
    
    def get_Mach(self):
        return self.Mach
    
    def get_AoA(self):
        return self.AoA

    def get_Re(self):
        return self.Re_1e6

    def get_CL(self):
        return self.CL
    
    def get_CDo(self):
        #print(self.df.get_CD0())
        return self.df.iloc[17,11]

    def get_CDi(self):
        return self.CDi

    def get_CDtot(self):
        return self.CDtot

    def append_CDtotal(self):
        
        for i in range(0,self.numpoints - 1):
            
            self.CDtotal.append(self.CDi[i] + float(self.df.iloc[17,11]))

    def get_CDtotal(self):
        return self.CDtot
    
    def get_CS(self):
        return self.CS
    
    def append_L_Dtotal(self):
        
        for i in range(0,self.numpoints - 1):
            print(self.CL[i]/self.CDtotal[i])
            self.L_Dtotal.append(self.CL[i]/self.CDtotal[i])

    def get_L_D_VSP(self):
        return self.L_D_VSP
    
    def get_L_Dtotal(self):
        return self.L_Dtotal

    def get_E(self):
        return self.E

    def get_CFx(self):
        return self.CFx
    
    def get_CFy(self):
        return self.CFy

    def get_CFz(self):
        return self.CFz

    def get_CMx(self):
        return self.CMx

    def get_CMy(self):
        return self.CMy
    
    def get_CMz(self):
        return self.CMz

    def get_CMl(self):
        return self.CMl
    
    def get_CMm(self):
        return self.CMm
    
    def get_CMn(self):
        return self.CMn


class readDragBuildup(object):

    def __init__(self,filename):

        self.filename = filename
        with open(self.filename , 'r') as temp_f:
            # get No of columns in each line
            col_count = [ len(l.split(",")) for l in temp_f.readlines() ]

        ### Generate column names  (names will be 0, 1, 2, ..., maximum columns - 1)
        column_names = [i for i in range(0, max(col_count))]

        ### Read csv
        self.df = pd.read_csv(self.filename, header=None, delimiter=",", names=column_names)
        #print(df.iloc[17,11])

    def get_CD0(self):

        return self.df.iloc[17,11]


#df = pd.read_csv("Aero_PLots/DragBuildup/Design1_V8.csv")

# with open("Aero_PLots/DragBuildup/Design1_V8.csv", 'r') as temp_f:
#     # get No of columns in each line
#     col_count = [ len(l.split(",")) for l in temp_f.readlines() ]

# ### Generate column names  (names will be 0, 1, 2, ..., maximum columns - 1)
# column_names = [i for i in range(0, max(col_count))]

# ### Read csv
# df = pd.read_csv("Aero_PLots/DragBuildup/Design1_V8.csv", header=None, delimiter=",", names=column_names)
# print(df.iloc[17,11])
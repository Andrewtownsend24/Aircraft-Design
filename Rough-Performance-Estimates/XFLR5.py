# By Andrew Townsend
# Read XFLR5 polars from wing
# 2/1/2021
import csv
import matplotlib.pyplot as plt
import math

class _XFLR5Wing:

    def __init__(self, filename):

        file = open(filename, "r")
        data = []

        for i in file:

            data.append(i)

        file.close()      
        
        self._alpha = []
        _alpha_index = -1
        self._Beta = []
        _Beta_index = -1
        self._CL = []
        _CL_index = -1
        self._CDi = []
        _CDi_index = -1
        self._CDv = []
        _CDv_index = -1
        self._CD = []
        _CD_index = -1
        self._Cm = []
        _Cm_index = -1
        
        self._start_angle = 0
        self._end_angle = 0
        self._got_angles = False

        got_column_titles = False
        for i in data:

            data_set = i.split()
            #print(data_set)
            index = 0

            if len(data_set) > 0:

                if _is_number(data_set[0]) is False and not got_column_titles:

                    string_split = i.split()

                    for j in string_split:

                        if "alpha" in j:

                            _alpha_index = index

                        if "Beta" in j:

                            _Beta_index = index

                        if "CL" in j:

                            _CL_index = index
                    
                        if "CDi" in j:

                            _CDi_index = index

                        if "CDv" in j:

                            _CDv_index = index

                        if "CD" in j:

                            _CD_index = index
                        
                        if "Cm" in j:

                            _Cm_index = index

                        index += 1

                        if _alpha_index > -1 and _Beta_index > -1 and _CL_index > -1:

                            got_column_titles = True
                            break

                if got_column_titles and _is_number(data_set[0]):

                    self._alpha.append(float(data_set[_alpha_index]))
                    self._Beta.append(float(data_set[_Beta_index]))
                    self._CL.append(float(data_set[_CL_index]))
                    self._CDi.append(float(data_set[_CDi_index]))
                    self._CDv.append(float(data_set[_CDv_index]))
                    self._CD.append(float(data_set[_CD_index]))
                    self._Cm.append(float(data_set[_Cm_index]))

    def get_alpha(self):

        return self._alpha

    def get_Beta(self):

        return self._Beta

    def get_CL(self):

        return self._CL

    def get_CDi(self):

        return self._CDi

    def get_CDv(self):

        return self._CDv

    def get_CD(self):

        return self._CD

    def get_Cm(self):

        return self._Cm

    def get_start_angle(self):

        return self._alpha[0]

    def get_end_angle(self):

        return self._alpha[-1]

# private method to determine in an input is a number
def _is_number(s):

    try:

        float(s)
        return True

    except ValueError:

        pass

    try:

        import unicodedata
        unicodedata.numeric(s)
        return True

    except (TypeError, ValueError):

        pass

    return False
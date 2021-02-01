import Plane as  p
import XFLR5 as XFLR5
import matplotlib.pyplot as plt
fileObject = open("Rough-Performance-Estimates/AirFoils/NACA_2412.txt", "r")
data = fileObject.read()
#print(data)

a1 = XFLR5._XFLR5Wing("Rough-Performance-Estimates/AirFoils/Cy1_T1-143_0 m_s-LLT.txt")
#a2 = p._XFLR5Data("Rough-Performance-Estimates/AirFoils/NACA_2412_Re5.256.txt")
print(" ")
print(a1.get_alpha())
print(" ")
print(a1.get_Beta())
print(" ")
print(a1.get_CL())
print(" ")
print(a1.get_CD())
print(" ")
print(a1.get_start_angle())
print(" ")
print(a1.get_end_angle())

plt.plot(a1.get_alpha(),a1.get_CL())
plt.show()
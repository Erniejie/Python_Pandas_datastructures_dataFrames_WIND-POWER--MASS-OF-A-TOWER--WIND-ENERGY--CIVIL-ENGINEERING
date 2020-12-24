##-Performing Operations with DataFrames_Data Structures

#WIND POWER- MASS OF A TOWER- WIND ENERGY- CIVIL ENGINEERING

import math
import  pandas as pd
import numpy as np

L = np.array([13,13,13,13,13]) # Height <L> of Tower in [m]
d = np.array([0.7,0.7,0.7,0.7,0.7]) # Diameter <d> at the top of tower in [m]
m = np.array([2.4,2.4,2.4,2.4,2.4]) #Shape Factor <m> [a real number]
t = np.array([0.2,0.2,0.2,0.2,0.2])  #Thickness <t> of Hollow Tube in[m]
s = np.array([7850,7850,7850,7850,7850])  # Density  <s> of Wind Turbine Tower in [kg/m^3]

df = pd.DataFrame({"L":L,"d":d,"m":m,"t":t,"s":s})

df["BaseDiameter[m]"] = df.m*df.d
df["TowerVolume[m^3]"] = math.pi*df.m*df.d  *df.L*df.t*(df.m + float(1))/(float(2)*df.m)
df["TowerMass[kg]"] = (math.pi*df.m*df.d  *df.L*df.t*(df.m + float(1))/(float(2)*df.m))*df.s 

print(round(df,2))

# round to digits ="%.2f"%



# Example 3- Vertical Deflection of a Simply  Supported Beam  with UDL
"""
import  pandas as pd
import numpy as np

L = np.array([8,8,8,8,8]) # Span in [m]
q = np.array([22.8,24,24,24,24]) # UDL in [kN/m]
E = np.array([210000,210000,210000,210000,210000]) #Young Modulus in [N/mm^2]
I = np.array([37100,41000,45700,48900,63800])  #Second Moment of Inertia in[cm^4]

df = pd.DataFrame({"L":L,"q":q,"E":E,"I":I})

df["Beam Deflection in mm"]= float(5e8)*(df.q*(df.L)**4)/(float(384)*df.E*df.I)   # in [mm]

print(round(df,2))
"""






"""
import  pandas as pd
import numpy as np

b = np.array([20,25,35,40]) # cm
h = np.array([40,45,46,50]) # cm
df = pd.DataFrame({"b":b,"h":h})

df["Second Moment of Inertia"]= round((df.b*(df.h)**3)/12,2) # in cm^4
print(df)
"""

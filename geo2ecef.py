
#Geodesicos a ECEF: lat,lon,h to x,y,z

import numpy as np
import math
import csv
from StringIO import StringIO

def geo2ecef (lat,lon,h): #definiendo la funcion
    a = 6378137.0 #semimajor axis length a;
    e = 0.0818#e = #la exentricidad del elipsoide
    N = a/math.sqrt(1-e**2* math.sin(lat)**2)

    x = (N+h) * math.cos(lat) *math.cos(lon)
    y = (N+h) * math.cos(lat) *math.sin(lon)
    z= ((1-e**2) * N+h) *math.sin(lat)

    return [x,y,z]

#termina funcion
#Calling function
#Leyendo el poligono realizado por mission planner

poligono  = open("poligono.poly", "r")
#dat = np.loadtxt('Poligonodos.poly')

data = poligono.read()
poligono.close()
data = np.genfromtxt(StringIO(data))
data=np.matrix(data) #Transformar array de arrays en matriz
a = data.shape
(m,n)=data.shape
ecef = np.zeros((m,3),float)
h = 2243
i=0

for i in range (0,m):
 #[x,y,z] = geo2ecef(data[i,1]), geo2ecef(data[i,2]), geo2ecef([180/math.pi])
  [x,y,z] = geo2ecef(math.radians(data[i,0]), math.radians(data[i,1]), h)
  ecef [i,0]=x
  ecef [i,1]=y
  ecef [i,2]=z

#print data[0,0]
print(ecef)

#lat=1
#lon=2
#h=3
#print(geo2ecef(lat,lon,h))

#ecef to geodesic x,y,z to lat lon h
import numpy as np
import math
import csv
from StringIO import StringIO

def ecef2geo (x,y,z):
    a = 6378137.0 #semimajor axis length a;
    e = 0.0818#e = #la exentricidad del elipsoide
    b = 6356752.3142
    a2 = a**2 #a^2
    e2 = e**2 #e^2
    b2 = b**2 #b^2

    ep2 = ((a2-b2)/b2)
    p = math.sqrt((x**2) + (y**2))
    th = math.atan((z*a)/(p*b))

    lat1 = math.atan(z+(ep2*b*math.sin(th)**3))/(p-(e2*a*math.cos(th)**3))
    lat = (math.atan(z+(ep2*b*math.sin(th)**3))/(p-(e2*a*math.cos(th)**3))*180/math.pi)
    lon = ((math.atan2(y,x))*180/math.pi)
    N = a/math.sqrt(1-e**2* math.sin(lat1)**2)
    alt = (p/math.cos(lat1)-N)

    return [lat,lon,alt]

poligono  = open("eceftogeo.txt", "r")
data = poligono.read()
poligono.close()
data = np.genfromtxt(StringIO(data))
data=np.matrix(data) #Transformar array de arrays en matriz
a = data.shape
(m,n)=data.shape
geo = np.zeros((m,3),float)
i=0

for i in range (0,m):
    [lat,lon,alt] = ecef2geo(data[i,0],(data[i,1]), data[i,2])
    geo [i,0]=lat
    geo [i,1]=lon
    geo [i,2]=alt

print (geo)

# Energy And Environmental Technologies For Building Systems : Assignment 01, Step-1
 
# Submitted By : IMAD AHMED
 
# Assignment Based On Exercise-D (Heat Loss Through A Composite Wall)
 
# Assumption : One-dimentional heat transfer through the wall ; Width of wall considered for unit block = 1m
 
# Given Data :
Y = 3 #y is the height of the wall in m
print "the height of the wall is "+str(Y)+ "m"
X = 5 #X is the width of the wall in m
print "the width of the wall is "+str(X)+ "m"
print " "
print "We're going to calculate the rate of heat transfer through the brick at first"
print " "
Tinfinity1 = 20.0 #Tinfinity1 corresponds to then indoor temperature
print "the indoor temperature T infinity1 is "+str(Tinfinity1)+ " degrees"
print " "
Tinfinity2 = -10.0 #Tinfinity2 corresponds to the outer temperature
print "the outer temperature T infinity2 is "+str(Tinfinity2)+ " degrees"
print " "
Kbrick = 0.72 #Kbr is the conduction coefficient of the brick
print "The conduction coefficient of the brick is "+str(Kbrick)+ " W/m.degrees"
print " "
Kf = 0.026 #Kf is the conduction coefficient of the foam
print "The conduction coefficient of the foam is "+str(Kf)+ " W/m.degrees"
print " "
Kplast = 0.22 #Kplast is the conduction coefficient of plaster layers
print "The conduction coefficient of plaster layer is "+str(Kplast)+ "W/m.degrees"
print " "
h1 = 10.0 #h1 is the convection coefficient of the inner side
print "The convection coefficient of the inner side is "+str(h1)+ " W/m^2"
print " "
h2 = 25.0 #h2 is the convection coefficient of the outer side
print "The convection coefficient of the outer side is "+str(h2)+ " W/m^2"
print " "
print "considering 1m deep and o,25m high portion of the wall"
print " "
A = 0.25*1 #A is the cross section area
Ri= 1/(h1*A) #Ri is the thermal resistance of inner convection side
L1= 0.03 #L1 is the length of the foam layer
R1= L1/(Kf*A) #R1 is the thermal resistance of the foam layer
L2=0.02 #L2 is the length of the vertical plaster layers from both sides
R2= L2/(Kplast*A) #R2 is the thermal resistance of the left plaster layer
R6= R2 #R6 is the thermal resistance of the right plaster layer
L3= 0.16 #L3 is the lenght of the horizontal central plaster
A3= 0.015*1 #A3 is the cross section area of the central plaster
R3= L3/(Kplast*A3) #R3 is the thermal resistance of the upper horizontal plaster layer
R5=R3 #R5 is the parallel thermal resistance of the lower horizontal plaster layer
A4= 0.22*1 #A4 is the cross section area of the brick
R4= L3/(Kbrick*A4) #R4 is the thermal resistance of the brick
Ro= 1/(h2*A) #Ro is the thermal resistance of the outer side
Rtot= Ri+R1+R2+1/(1/R3+1/R4+1/R5)+R6+Ro #Rtot is the total resistance of the whole heat trasnfer
print "The total thermal resistance of the medium is "+str(Rtot)+ " degrees/W"
print " "
Q= (Tinfinity1-Tinfinity2)/Rtot 
print "This implies that the steady rate of heat transfer through the 0.25 m^2 surface area is "+str(Q)+ " W"
print " "
print "since our wall is 5m deep and according to the 0.25 surface area that gives 12 similar units in 3m height"
print " "
Qtot= Q*12*5
print "Hence, the rate of heat trasnfer through the entire wall becomes "+str(Qtot)+ " W"
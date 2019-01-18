#Diffie Hellman Exchange

import math
import random

#p and g.
p=input("Please enter the value of p\n")
g=input("Please enter the value of g\n")

#SA and SB, two random numbers generated.
SA=random.randint(0, 9)
SB=random.randint(0, 9)

#TA and TB calculated.
TA=int((math.pow(g, SA))%p)
TB=int((math.pow(g, SB))%p)

#TA and TB are exchanged.

#Secret key calculated.
Secretkey_A=int((math.pow(TB, SA))%p)
Secretkey_B=int((math.pow(TA, SB))%p)

if(Secretkey_A==Secretkey_B):
    print "Secret Key is: "
    print Secretkey_A

#RSA
#message m, key parts i.e. e and n are taken as inputs from user.
#to produce ciphertext c.

import math

m=input("Please enter the message m\n")
print "Please enter the key" 
e=input("First enter e\n")
n=input("Now enter n\n")

c=int((math.pow(m, e))%n)
print c
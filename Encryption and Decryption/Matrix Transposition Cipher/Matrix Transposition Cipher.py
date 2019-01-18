#Will handle all cases independent of size of plaintext and key. Example taken from
#Handout Notes. % is considered as space as mentioned in lecture and notes as well.
#And hence this program has been written considering % instead of spaces.

import math

pt="you%guessed%it!"
key=(3,4,1,2)

ct=""
ct_list=[]
pt_list=[]


def encrypt(key_f,pt_f):
    key_length=len(key_f)
    pt_chars = list(pt_f)
    initial_length=len(pt_chars)
    max_value=max(key_f)
    a=float(len(pt_chars))/float(max_value)
    r=int(math.ceil(a))
    r=r*max_value
    for m in range(initial_length,r):
        pt_chars.insert( m, "%")
        
    for i in range(0,key_length):
        ct_list.append(pt_chars[key_f[i]-1])
        limit=key_f[i]-1+max_value
        while (limit < r):
            ct_list.append(pt_chars[limit])
            limit=limit+max_value
            
    ct = ''.join(ct_list)
    print "Encrypted ciphertext is "+ct
    return ct

def decrypt(key_f,ct_f):
    max_value=max(key_f)
    key_length=len(key_f)
    ct_chars = list(ct_f)
    length = len(ct_chars)
    pt_list=[""] * length
    
    x=0
    for i in range(0,key_length):
        pt_list[key_f[i]-1]=ct_chars[x]
        x=x+1
        limit=key_f[i]-1+max_value
        while (limit < length):
            pt_list[limit]=ct_chars[x]
            x=x+1
            limit=limit+max_value
            
    while (pt_list[-1] == "%"):
        pt_list.pop(-1)
            
    pt_decrypted = ''.join(pt_list)
    print "Decrypted plaintext is "+pt_decrypted
    return

ct=encrypt(key,pt)
decrypt(key,ct)

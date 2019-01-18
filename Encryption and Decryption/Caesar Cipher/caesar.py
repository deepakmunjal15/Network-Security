#This will handle all cases independent of value of key and plaintext. This program
#has been written in a way to first encrpt a plaintext based on the key enetered by
#user and then decrypt the ciphertext with the same key. However, if we want to
#explicitly decrypt a ciphertext, then that can be done by passing the required
#values in the decypt function. Example taken from Handout Notes.

key=4

pt=raw_input("Please enter the message m\n")

#pt="HELLO"
ct=""
ct_list=[]
pt_list=[]


def encrypt(key_f,pt_f):
    e_chars = list(pt_f)
    for i in range(0,len(pt_f)):
        if ord(e_chars[i]) in range(97,123):
            mod_e_chars_ascii=(((ord(e_chars[i])%97)+1+key_f)%26)+96
            if(mod_e_chars_ascii-97<0):
                mod_e_chars_ascii=mod_e_chars_ascii+26
            elif(mod_e_chars_ascii-97>=0 and mod_e_chars_ascii-97<=25):
                mod_e_chars_ascii=mod_e_chars_ascii
            elif(mod_e_chars_ascii-97>25):
                mod_e_chars_ascii=mod_e_chars_ascii-26
        elif ord(e_chars[i]) in range(65,91):
            mod_e_chars_ascii=(((ord(e_chars[i])%65)+1+key_f)%26)+64
            if(mod_e_chars_ascii-65<0):
                mod_e_chars_ascii=mod_e_chars_ascii+26
            elif(mod_e_chars_ascii-65>=0 and mod_e_chars_ascii-65<=25):
                mod_e_chars_ascii=mod_e_chars_ascii
            elif(mod_e_chars_ascii-65>25):
                mod_e_chars_ascii=mod_e_chars_ascii-26
        ct_list.append(chr(mod_e_chars_ascii))
        
    ct = ''.join(ct_list)
    print "Encrypted ciphertext is "+ct
    return ct

def decrypt(key_f,ct_f):
    d_chars = list(ct_f)
    for i in range(0,len(ct_f)):
        if ord(d_chars[i]) in range(97,123):
            mod_d_chars_ascii=(26-(key_f-((ord(d_chars[i])%97)+1))%26)+96
            if(mod_d_chars_ascii-97<0):
                mod_d_chars_ascii=mod_d_chars_ascii+26
            elif(mod_d_chars_ascii-97>=0 and mod_d_chars_ascii-97<=25):
                mod_d_chars_ascii=mod_d_chars_ascii
            elif(mod_d_chars_ascii-97>25):
                mod_d_chars_ascii=mod_d_chars_ascii-26
        elif ord(d_chars[i]) in range(65,91):
            mod_d_chars_ascii=(26-(key_f-((ord(d_chars[i])%65)+1))%26)+64
            if(mod_d_chars_ascii-65<0):
                mod_d_chars_ascii=mod_d_chars_ascii+26
            elif(mod_d_chars_ascii-65>=0 and mod_d_chars_ascii-65<=25):
                mod_d_chars_ascii=mod_d_chars_ascii
            elif(mod_d_chars_ascii-65>25):
                mod_d_chars_ascii=mod_d_chars_ascii-26
        pt_list.append(chr(mod_d_chars_ascii))
        
    pt_decrypted = ''.join(pt_list)
    print "Decrypted plaintext is "+pt_decrypted
    return


ct=encrypt(key,pt)
decrypt(key,ct)

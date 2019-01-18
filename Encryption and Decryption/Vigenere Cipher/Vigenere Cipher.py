#Will handle all cases independent of size of plaintext and key. And it has been
#written in such a way that it won't just handle the cases where plaintext is longer
#than key but will also handle even if plaintext is smaller than key. Example taken from
#Handout Notes.

pt="HELLOWORLD"
key="SECRET"
ct=""
ct_list=[]
pt_list=[]

a=26
b=26
vig_table=[[0 for i in range(a)] for j in range(b)]
alpha_table=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

for p in range(0,26):
    r=0
    for q in range(0,26):
        vig_table[p][q]=alpha_table[(r+p)%26]
        r=r+1



def encrypt(key_f,pt_f):
    pt_chars = list(pt_f)
    key_chars = list(key_f)
    
    for m in range(0,len(pt_chars)):
        g=ord(pt_chars[m])-65
        h=ord(key_chars[m%len(key_chars)])-65
        ct_list.append(vig_table[g][h])
        
    ct = ''.join(ct_list)
    print "Encrypted ciphertext is "+ct
    return ct

def decrypt(key_f,ct_f):
    ct_chars = list(ct_f)
    key_chars = list(key_f)
    
    for m in range(0,len(ct_chars)):
        col=ord(key_chars[m%len(key_chars)])-65
        for row in range(0,26):
            if(vig_table[row][col]==ct_chars[m]):
                break
        pt_list.append(chr(row+65))
        
    pt_decrypted = ''.join(pt_list)
    print "Decrypted plaintext is "+pt_decrypted
    return

ct=encrypt(key,pt)
decrypt(key,ct)

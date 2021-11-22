import math

# RSA Encryption and Decryption Implementation
# variable : 
# p and q are primes
# n = p.q
# sigma(n) = (p-1)(q-1)
# e is the encryption key, GCD(e,sigma(n)) should be 1
# d is the decryption key, d==e^-1 mod (sigma(n))
# m = plaintexs
# c = cyphertext

# MENCARI KUNCI PRIVATE
def findPrivate(e,sigman):
    k = 1
    d = (1 + k*sigman)/e
    while (d - (d//1) > 0):
        k += 1
        d = (1+k*sigman)/e
    return d

# Encryption Function
# p and q are primes
def rsa_encry(m,p,q,e):
    result = []
    n = p*q
    sigma = (p-1)*(q-1)
    d = findPrivate(e,sigma)
    save_key(e,n,d)
    m_list = list(m)
    plain = []
    for i in range(len(m_list)):
        if (m_list[i] != ' '):
            plain.append(ord(m_list[i]) - 65)
    
    # print('plain = ',plain)
    # print('n = ',n)
    # print('sigma(n) = ',sigma)
    # print('faktor prima terbesar = ', math.gcd(sigma,e))
    
    if (math.gcd(sigma,e) != 1):
        # print('[!] Nilai PBB bukan 1. Silahkan pilih nilai lain untuk p, q, atau e')
        return 0
        
    else:
        separated = gabung_blok(plain)
        #ENCRYPT
        for i in range(len(separated)):
            x = pow(separated[i],e,n)
            # print(separated[i],'pangkat ',e,' mod ',n,' = ',x)
            result.append(x)
        return result
        
    # 'r' open for reading (default)
    # 'w' open for writing, truncating the file first
    # 'x' open for exclusive creation, failing if the file already exists
    # 'a' open for writing, appending to the end of the file if it exists
        
def save_key(e,n,d):
    # public key
    file = open("./key/rsa.pub", "w") 
    file.write(str(e) + ' ' + str(n))
    file.close()

    # private key
    file = open("./key/rsa.pri", "w") 
    file.write(str(d)+' '+str(n)) 
    file.close()
    
def save_key_pri(e,n,d):

    # private key
    file = open("./key/rsa.pri", "w") 
    file.write(str(d)+' '+str(n)) 
    file.close() 

def save_key_pub(e,n,d):
    # public key
    file = open("./key/rsa.pub", "w") 
    file.write(str(e) + ' ' + str(n))
    file.close()

# KELOMPOKKAN MENJADI SEPERTI 4 BIT
def gabung_blok(m):
    result = []

    for i in range(0,len(m),2):
        if (i % 2 == 0) and ( i + 1 == len(m)):
            a = m[i] * 100
        else :
            a = m[i]*100 + m[i+1]
        # print(a)
        result.append(a)
    return result


def rsa_decry(c,p,q,e):
    # ciphertext dalam bentuk 4 4 dan integer
    n = p*q
    sigman = (p-1)*(q-1)
    d = findPrivate(e,sigman)
    result = []
    plain = []
    for i in range(len(c)):
        x = pow(c[i],int(d),n)
        plain.append(x)
    # print(plain)

    for i in range(len(plain)):
        y = plain[i] // 100
        z = plain[i] % 100
        result.append(y)
        result.append(z)
    
    final = []
    # TRANSLATE TO ASCII
    for i in range(len(result)):
        word = chr(result[i] + 65)
        final.append(word)
    return final

# def main():
#     print('Contoh : HELLO ALICE 47 71 79')
#     m = input('Masukkan plainteks : ')
#     p = int(input('Masukkan nilai prima untuk p : '))
#     q = int(input('Masukkan nilai prima untuk q : '))
#     e = int(input('Masukkan nilai dari e : '))
#     c = rsa_encry(m,p,q,e)
#     print('Hasil enkripsi : ',c)
#     d = rsa_decry(c,p,q,e)
#     print('Hasil dekripsi : ',d)

# if __name__ == '__main__':
#     main()
    
#     # e = int(input('e : '))
#     # sigman = int(input('sigman: '))
#     # x = findPrivate(e,sigman)
#     # print(x)
#     # c = [328,301,2653,2986,1164,1900]
#     # rsa_decry(c,47,71,79)
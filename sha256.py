# SHA 256 Hash Function Implementation

# def string2binary(m):
#     result = ''.join(format(ord(i),'08b') for i in m)
#     return result

def rotr(num, bits, n):
    for i in range(n):
        num &= (2**bits-1)
        bit = num & 1
        num >>= 1
        if(bit):
            num |= (1 << (bits-1))

    return num

def shr(num, n):
    return num >> n

def xor(num1, num2):
    return num1 ^ num2

def bit_not(num, bits):
    return (1 << bits) - 1 - num

def ch(x,y,z, bits):
    return xor((x & y),(bit_not(x,bits) & z))

def maj(x,y,z,bits):
    return xor(xor((x&y),(x&z)),(y&z))

def concat(num1,num2,bits):
    return ( num1 << bits ) + num2

def string2bin(m):
    m_list = list(m)
    _m = []
    for i in range(len(m_list)):
        _m.append(ord(m_list[i]))
    return _m

def find_nzero(m):
    l = 8*len(m)
    k = 0
    for k in range(512):
        if ((l + 1 + k) % 512) == 448:
            return k 

def sigmoid0(x):
    return (xor(xor(rotr(x,32,7),rotr(x,32,18)),shr(x,3)))    
def sigmoid1(x):
    return (xor(xor(rotr(x,32,17),rotr(x,32,19)),shr(x,10)))

def up_sigma1(x):
    return (xor(xor(rotr(x,32,6),rotr(x,32,11)),rotr(x,32,25)))

def up_sigma0(x):
    return (xor(xor(rotr(x,32,2),rotr(x,32,13)),rotr(x,32,22)))

def sha256(m):
    #1. Convert message to binary
    _m = string2bin(m)
    # print(_m)
    
    #concate
    #2. Padding the message
    # until the number of bits reaches the nearest of 512
    #2.1 Append a 1 at the end
    #2.2 Padding with 0s ( length + 1 + k = 448 mod 512) + message block

    m_concat = _m[0]
    for i in range(len(_m)-1):
        m_concat = concat(m_concat,_m[i+1],8)
    # print('concat dari message : ',bin(m_concat))
    n_of_zero = find_nzero(_m)
    # print(n_of_zero)
    
    m_concat = concat(m_concat,1,1)
    for i in range(n_of_zero - 54):
        m_concat = concat(m_concat,0,1)
    # print('message: ',bin(m_concat))

    panjang_m = len(_m)*8
    message_block_zero = 64 - panjang_m.bit_length()
    for i in range(message_block_zero):
        m_concat = concat(m_concat,0,1)
    m_concat = concat(m_concat,panjang_m,message_block_zero)
    # print(bin(m_concat))
    
    
    #3 Parsing the padded message
    #3.1 Divide message block into 16 32bit words
    #3.2 Expand message schedule by creating 48 32bit words using the formula
    k = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
     0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
     0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
     0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
     0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
     0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
     0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
     0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
     0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
     0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
     0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
     0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
     0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
     0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
     0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
     0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]
    # print(k)
    
    w = []
    content = m_concat
    # print(content.bit_length())
    for i in range(16):
        x = content & 0xFFFFFFFF
        w.append(x)
        content = content >> 32
    w = w[::-1]
    # print(w)
    for t in range(16,64):
        x = sigmoid1(w[t-2] + w[t-7] + sigmoid0(w[t-15])+w[t-16])
        w.append(x)
    # print(w)
    
    # w_test = []
    # for i in range(len(w)):
    #     w_test.append(bin(w[i]))
    # print(w_test)
    
    _h = [0x6A09E667,0xBB67AE85,0x3C6EF372,0xA54FF53A,0x510E527F,0x9B05688C,0x1F83D9AB,0x5BE0CD19]
    a = _h[0]
    b = _h[1]
    c = _h[2]
    d = _h[3]
    e = _h[4]
    f =_h[5]
    g =_h[6]
    h = _h[7]

    for i in range(64):
        t1 = h + up_sigma1(e) + ch(e,f,g,8) + k[i] + w[i]
        t2 = up_sigma0(a) + maj(a,b,c,8)
        h = g
        g = f
        f = e
        e = d + t1
        d = c
        c = b
        b = a
        a = t1 + t2
    
    a = a + _h[0]
    b = b + _h[1]
    c = c + _h[2]
    d = d + _h[3]
    e = e + _h[4]
    f = f + _h[5]
    g = g + _h[6]
    h = h + _h[7]
    return(hex(a)+hex(b)+hex(c)+hex(d)+hex(e)+hex(f)+hex(g)+hex(h))

def main():
    # print(rotr(3,4,5))
    # print(bit_not(2,4))
    # _m = string2bin('AHalo guys')
    sha256('abc')

if __name__ == '__main__':
    main()
    
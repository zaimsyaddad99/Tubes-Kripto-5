import digital_signature as ds
import rsa 
print("1. Pembangkitan kunci RSA")
print("2. Make digital signature:")
print("3. Verification digital signature:")
n = int(input("Silahkan pilih menu:"))
if(n == 1):
    print("masukin algoritma RSA disini")
    p = int(input('Masukkan nilai prima untuk p : '))
    q = int(input('Masukkan nilai prima untuk q : '))
    e = int(input('Masukkan nilai dari e : '))
    n = p*q
    sigman = (p-1)*(q-1)
    privat = rsa.findPrivate(e,sigman)
    publick = 1 #cara nemu key publik kalian gmn?
    print("ini key privat nya: " ,privat)
    print("ini key publick nya: ", publick)
elif(n == 2):
    print("1. disimpan dalam 1 file")
    print("2. disimpan dalam file terpisah")
    m = int(input("Silahkan pilih menu:"))
    file_path=input("masukan file path dari text: ")
    privat = int(input("masukan nilai key privat: "))
    n = int(input("masukan nilai n: "))
    S = ds.make_digital_signature(file_path,privat,n)
    if(m == 1):
        ds.add_digital_signature(S,file_path)
        
    elif(m == 2):
        file_path_ds = input("masukan file path tempat menyimpan ds: ")
        ds.add_digital_signature(S,file_path_ds)

elif(n == 3):
    print("1. dalam 1 file")
    print("2. dalam file terpisah")
    m = int(input("Silahkan pilih menu:"))
    file_path=input("masukan file path: ")
    publick = int(input("masukan nilai key public: "))
    n = int(input("masukan nilai n: "))
    if(m == 1):
        ds.verification_ds(file_path,file_path,publick,n)
    if(m == 2):
        file_path_ds = input("masukan file path tempat menyimpan ds: ")
        ds.verification_ds(file_path,file_path_ds,publick,n)
else:
    print("menu yang dipilih tidak valid")
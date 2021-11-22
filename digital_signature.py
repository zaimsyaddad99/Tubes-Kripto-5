import sha256
conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                    5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                    13: 'D', 14: 'E', 15: 'F'}



def make_digital_signature(file_path,privat_K,n):
    text = get_text(file_path,"no")
    H = str(sha256.sha256(text))
    h = int(H,36)
    S = pow(h,privat_K)%n
    print(S)
    return S

def decimalToHexadecimal(decimal):
    hexadecimal = ''
    while(decimal > 0):
        remainder = decimal % 16
        hexadecimal = conversion_table[remainder] + hexadecimal
        decimal = decimal // 16
  
    return hexadecimal

#add digital signature
def add_digital_signature(S,path_file):
    digital_signature = decimalToHexadecimal(S)
    ds = ["\n","\n","<ds>\n",digital_signature,"\n","</ds>"]
    with open(path_file, "a+") as file:
        file.seek(0)
        file.writelines(ds)
        file.close()

def get_ds(file_path):
    file = open(file_path)
    
    #find len file
    count = 0
    for x in file:
        count += 1

    #read digital signature
    file.seek(0)
    content = file.readlines()
    return(content[count-2])

def get_text(file_path,status):
    file = open(file_path)
    
    #find len file
    count = 0
    text = ""
    for x in file:
        count += 1

    #read digital signature
    file.seek(0)
    content = file.readlines()
    
    #status Yes = terdapat digital signature pada text
    #status No = tidak terdapat signature paada text
    if(status == "Yes"):
        for i in range(count-3):
            text += str(content[i])
    else:
        for i in range(count):
            text += str(content[i])
    return (text)

    
def verification_ds(file_path,file_path_ds,publick,n,status):
    ds = get_ds(file_path_ds)
    ds = int(ds,16)
    print("ini ds nya",ds)
    h_ = pow(ds,publick)%n
    text = get_text(file_path,status)
    H = str(sha256.sha256(text))
    dh = int(H,36)
    h = dh % n
    
    print(h_)
    print(h)
    if(h_ == h):
        return( "Tanda tangan valid")
    else:
        return( "Tanda tangan tidak valid")
    
# H = hes("contoh")
# S = make_digital_signature("tes.txt",171635,223427)
# print(S)
# add_digital_signature(89567,"tes.txt")
# ds = get_ds("contoh.txt")
# print(ds)
# verification_ds("tes.txt","tes.txt",731,223427,"Yes")
# text = get_text("tes.txt","No")
# print(str(sha256.sha256(text))[4:])

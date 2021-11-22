conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                    5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                    13: 'D', 14: 'E', 15: 'F'}

def hesh(text):
    return("A4C05176E1440FC879C06C72FA603A24")

def make_digital_signature(file_path,privat_K,n):
    text = get_text(file_path,"no")
    H = hesh(text) #ganti pake punya zaim
    h = int(H,16)
    S = pow(h,privat_K)%n
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
    h_ = pow(ds,publick)%n
    text = get_text(file_path,status)
    H = hesh(text)  #ganti pake punya zaim
    dh = int(H,16)
    h = dh % n

    if(h_ == h):
        return "Tanda tangan valid"
    else:
        return "Tanda tangan tidak valid"
    
# H = hes("contoh")
# S = make_digital_signature(H,171635,223427)
# add_digital_signature(S,"contoh.txt")
# ds = get_ds("contoh.txt")
# print(ds)
# verification_ds("contoh.txt",731,223427)
# text = get_text("C:/Users/user/Documents/Kriptografi/tugas 5/Tubes-Kripto-5/contoh.txt","No")
# print(text)

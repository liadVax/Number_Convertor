
def decToBin(d):
    bin=0
    dec=int(d)
    wegiht=1
    while dec>0:
        mod=dec%2
        bin=bin+(mod*wegiht)
        wegiht=wegiht*10
        dec=int(dec/2)
    #print("Binary:",bin)
    return bin

def binToDec(b):
    dec=0
    bin=int(b)
    wegiht=0
    while bin>0:
        mod=bin%10
        dec=dec+mod*pow(2,wegiht)
        wegiht+=1
        bin=int(bin/10)
    #print("Decimal:",dec)
    return dec

def binToHex(b):
    hexDic={0:'0',1:'1',10:'2',11:'3',100:'4',101:'5',110:'6',111:'7',1000:'8',1001:'9',
         1010:'A',1011:'B',1100:'C',1101:'D',1110:'E',1111:'F'}
    hex=""
    bin=int(b)
    while bin>0:
        mod=bin%10000
        hex=(hexDic.get(mod,"[?]"))+hex
        bin=int(bin/10000)
    #print("Hexadecimal:",hex)
    return hex

def hexToBin(h):
    hexDic = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001',
                  'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}
    bin = ""
    hex =str(h)
    hex=hex.upper()
    for i in range(len(hex)):
        bin=bin+hexDic.get(hex[i],"[?]")
    #print("Binary:",bin)
    return bin

def binToOctal(b):
    octalDic={0:'0',1:'1',10:'2',11:'3',100:'4',101:'5',110:'6',111:'7',1000:'10',1001:'11',
         1010:'12',1011:'13',1100:'14',1101:'15',1110:'16',1111:'17'}
    octal=""
    bin=int(b)
    while bin>0:
        mod=bin%1000
        octal=(octalDic.get(mod,"[?]"))+octal
        bin=int(bin/1000)
    print(octal)




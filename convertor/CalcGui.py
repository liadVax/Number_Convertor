import tkinter as tk
from tkinter import font
import Convertor as conv
HEIGHT=500
WIDTH=600

def wrongIn():
    label['text']='Wrong input,try again'

def checkEntryHex(entry):
    hexDic=['A','B','C','D','E','F','a','b','c','d','e','f']
    for digit in entry:
        if (digit.isdigit())==False and (digit in hexDic)==False:
            wrongIn()
            return False
    return True

def checkEntryBin(entry):
    for digit in entry:
        if digit!='1' and digit!='0':
            wrongIn()
            return False
    return True

def convert_func(entry,state):
    str=''
    if state=='Dec':
        if (entry.isnumeric())==True:
            dec=entry
            bin=conv.decToBin(entry)
            hex=conv.binToHex(bin)
        else:
            wrongIn()
            return
    elif state=='Hex':
        if checkEntryHex(entry)==True:
            hex=entry.upper()
            bin=conv.hexToBin(entry)
            dec=conv.binToDec(bin)
        else:
            return
    elif state=='Bin':
        if checkEntryBin(entry)== True:
            bin=entry
            dec=conv.binToDec(entry)
            hex=conv.binToHex(entry)
        else:
            return
    str="Binary: %s\nDecimal: %s\nHexadecimal: %s\n"%(bin,dec,hex)
    print(str)
    label['text']=str

root = tk.Tk()
root.title("Convertor")

canvas=tk.Canvas(root,height=HEIGHT ,width=WIDTH )
canvas.pack()
backgroung_image=tk.PhotoImage(file="image.png")
backgroung_label=tk.Label(root,image=backgroung_image)
backgroung_label.place(relwidth=1,relheight=1)

frame=tk.Frame(root,bg='#D6C1FF',bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')

clicked=tk.StringVar()
clicked.set("Bin")
drop= tk.OptionMenu(frame, clicked,"Bin","Dec","Hex")
drop.place(relheight=1,relwidth=0.13)

entry= tk.Entry(frame,bg='#FEF9E7',font=('Courier',14))
entry.place(relx=0.15,relwidth=0.519,relheight=1)

button = tk.Button(frame,text="Convert",bg='#A6C8F7',font=40,command= lambda:convert_func(entry.get(),clicked.get()))
button.place(relx=0.68,relheight=1,relwidth=0.32)

lowerFrame= tk.Frame(root,bg='#D6C1FF',bd=10)
lowerFrame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')

label=tk.Label(lowerFrame,bg='#FEF9E7',font=('Courier',16))
label.place(relwidth=1,relheight=1)

root.mainloop()

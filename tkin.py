from tkinter import *
from tkinter import ttk

from unitcalc import conversion_dict as cdict

def setunit(*args):
    unitfrom['values']=tuple(cdict[quantVar.get().lower()].keys())
    unitto['values']=tuple(cdict[quantVar.get().lower()].keys())


def calculate(*args):
    result= "{0:.20f}".format(cdict[quantVar.get().lower()][fromVar.get()][toVar.get()](val.get()))
    result_string=val.get(), fromVar.get(),"=", result, toVar.get()
    resultVar.set(result_string)

root = Tk()
root.title("Unit Converter")
root.configure(bg="gray60")

Label(root, text="QUANTITY",fg='DodgerBlue4',bg='seashell4',font='Times 10  bold').grid(row=0, column=0,columnspan=4,sticky= W)

quantVar= StringVar()

quantity= ttk.Combobox(root, textvariable=quantVar, state="readonly",values=tuple([x.capitalize()for x in cdict.keys()]))

quantity.bind("<<ComboboxSelected>>",setunit)
quantity.grid(row=0,column=4)

Label(root, text="CONVERT",fg='DodgerBlue4',bg='seashell4',font='Times 10  bold').grid(row=1,column=0)

val= DoubleVar()
Entry(root, textvariable=val, width=10).grid(row=1,column=1)

fromVar= StringVar()
unitfrom= ttk.Combobox(root, textvariable=fromVar, state='readonly')
unitfrom.grid(row=1,column=2)

Label(root, text="to").grid(row=1,column=3)

toVar= StringVar()
unitto= ttk.Combobox(root,textvariable=toVar, state='readonly')
unitto.grid(row=1,column=4)

Button(root, text='CALCULATE',command=calculate).grid(row=2,columnspan=5)

resultVar= StringVar()
resultLabel=Label(root,textvariable=resultVar).grid(row=3, column=0,columnspan=5,sticky=W)

for child in root.winfo_children():
    child.grid_configure(padx=7,pady=7)



root.mainloop()
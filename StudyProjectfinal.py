import tkinter as tk
import math
from tkinter import *
from tkinter import scrolledtext
from functools import partial
from tkinter.font import Font
from tkinter import ttk
from PIL.Image import new
from unitcalc import conversion_dict as cdict
import random
import numpy as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import json
from tkinter import messagebox as mb
from PIL import ImageTk
def new_window1():
    try:
        if root1.state() == "normal": root1.focus()
    except NameError as e:
        print(e)
    def fresh():
        answer.delete(1.0,END)
    def exit():
        root.destroy()

    #Sphere
    def sphereMethod():
        global radius,valueFrame
        valueFrame = Frame(root,bg='#008037')
        value = Label(valueFrame,text="Enter the length of the radius of the sphere:",bg='#008037',fg='white',font=("Times New Roman",15,"bold"))
        value.grid(row=0,column=0)
        radius = Entry(valueFrame)
        radius.grid(row=0,column=1,pady=5,ipadx=5)
        valueFrame.pack(side=TOP,pady=5,padx=5,ipadx=5)
        result= Button(valueFrame,text="Get Answer!",bg="#ed7117",command=sphere_v)
        result.grid(row=0,column=2)

    #Cube
    def cubeMethod():
        global side,valueFrame
        valueFrame = Frame(root,bg='#008037')
        value = Label(valueFrame, text="Enter the length of the side of the cube:",bg='#008037',fg='white',font=("Times New Roman",15,"bold"))
        value.grid(row=0, column=0)
        side = Entry(valueFrame)
        side.grid(row=0, column=1, pady=5, ipadx=5)
        valueFrame.pack(side=TOP, pady=5, padx=5, ipadx=5)
        result = Button(valueFrame, text="Get Answer!", bg="#ed7117",command=cube_v)
        result.grid(row=0, column=2)
    #Prism
    def rectengularprismMethod():
        global length , height,width,valueFrame
        valueFrame = Frame(root,bg='#008037')
        value = Label(valueFrame,text="Enter the length of the rectengular prism:  ",bg='#008037',fg='white',font=("Times New Roman",15,"bold"))
        value.grid(row=0, column=0)
        length = Entry(valueFrame)
        length.grid(row=0,column=1,pady=5)
        value = Label(valueFrame, text="Enter the height of the rectengular prism :  ",bg='#008037',fg='white',font=("Times New Roman",15,"bold"))
        value.grid(row=1, column=0)
        height = Entry(valueFrame)
        height.grid(row=1, column=1, pady=5)
        value = Label(valueFrame, text="Enter the width of the rectengular prism:  ",bg='#008037',fg='white',font=("Times New Roman",15,"bold"))
        value.grid(row=2, column=0)
        width = Entry(valueFrame)
        width.grid(row=2, column=1, pady=5)
        result = Button(valueFrame, text="Get Answer!", bg="#ed7117", command=rprism_v)
        result.grid(row=2, column=2)
        valueFrame.pack(side=TOP,pady=5,padx=5,ipadx=5)
    #Cone
    def coneMethod():
        global radius, height, side3,valueFrame
        valueFrame = Frame(root,bg='#008037')
        value =Label(valueFrame,text= "Enter the length of the radius of the cone :",bg='#008037',fg='white',font=("Times New Roman",15,"bold"))
        value.grid(row=0,column=0)
        radius = Entry(valueFrame)
        radius.grid(row=0,column=1)
        value = Label(valueFrame, text="Enter the height of the cone :",bg='#008037',fg='white',font=("Times New Roman",15,"bold"))
        value.grid(row=1, column=0)
        height = Entry(valueFrame)
        height.grid(row=1, column=1)
        result = Button(valueFrame, text="Get Answer!", bg="#ed7117", command=cone_v)
        result.grid(row=1, column=2)
        valueFrame.pack(side=TOP, pady=5, padx=5, ipadx=5)
    #Cylinder
    def cylinderMethod():
        global radius, height,valueFrame
        valueFrame = Frame(root,bg='#008037')
        value = Label(valueFrame,text="Enter the length of the radius of the cylinder:  ",bg='#008037',fg='white',font=("Times New Roman",15,"bold"))
        value.grid(row=0, column=0)
        radius = Entry(valueFrame)
        radius.grid(row=0,column=1,pady=5)
        value = Label(valueFrame, text="Enter the height of the cylinder :  ",bg='#008037',fg='white',font=("Times New Roman",15,"bold"))
        value.grid(row=1, column=0)
        height = Entry(valueFrame)
        height.grid(row=1, column=1, pady=5)
        result = Button(valueFrame, text="Get Answer!", bg="#ed7117", command=cylinder_v)
        result.grid(row=1, column=2)
        valueFrame.pack(side=TOP,pady=5,padx=5,ipadx=5)
    #Spyramid
    def squarepyramidMethod():
        global side,height,valueFrame
        valueFrame = Frame(root,bg='#008037')
        value = Label(valueFrame, text="Enter the length of the side of the square pyramid:",bg='#008037',fg='white',font=("Times New Roman",15,"bold"))
        value.grid(row=0, column=0)
        side = Entry(valueFrame)
        side.grid(row=0, column=1, pady=5, ipadx=5)
        value = Label(valueFrame, text="Enter the height of the side of the square pyramid:",bg='#008037',fg='white',font=("Times New Roman",15,"bold"))
        value.grid(row=1, column=0)
        height = Entry(valueFrame)
        height.grid(row=1, column=1, pady=5, ipadx=5)
        result = Button(valueFrame, text="Get Answer!", bg="#ed7117",command=squarepyramid_v)
        result.grid(row=1, column=2)
        valueFrame.pack(side=TOP, pady=5, padx=5, ipadx=5)
    #Triprism
    def triprismMethod():
        global base, height, length,valueFrame
        valueFrame = Frame(root,bg='#008037')
        value = Label(valueFrame,text="Enter the base of triangular prism:  ",bg='#008037',fg='white',font=("Times New Roman",15,"bold"))
        value.grid(row=0, column=0)
        base = Entry(valueFrame)
        base.grid(row=0,column=1)
        value = Label(valueFrame,text="Enter the height of triangular prism:  ",bg='#008037',fg='white',font=("Times New Roman",15,"bold"))
        value.grid(row=1, column=0)
        height = Entry(valueFrame)
        height.grid(row=1,column=1)
        value = Label(valueFrame, text="Enter the length of triangular prism:  ",bg='#008037',fg='white',font=("Times New Roman",15,"bold"))
        value.grid(row=2, column=0)
        length = Entry(valueFrame)
        length.grid(row=2, column=1)
        result = Button(valueFrame, text="Get Answer!", bg="#ed7117", command=triprism_v)
        result.grid(row=2, column=2)
        valueFrame.pack(side=TOP,pady=5,padx=5,ipadx=5)
    #Sector
    def sectorofsphereMethod():
        global radius, height,valueFrame
        valueFrame = Frame(root,bg='#008037')
        value = Label(valueFrame,text="Enter the radius of sphere of sector:  ",bg='#008037',fg='white',font=("Times New Roman",15,"bold"))
        value.grid(row=0, column=0)
        radius = Entry(valueFrame)
        radius.grid(row=0,column=1,pady=5)
        value = Label(valueFrame, text="Enter the height of sector:  ",bg='#008037',fg='white',font=("Times New Roman",15,"bold"))
        value.grid(row=1, column=0)
        height = Entry(valueFrame)
        height.grid(row=1, column=1, pady=5)
        result = Button(valueFrame, text="Get Answer!", bg="#ed7117", command=spheresec_v)
        result.grid(row=1, column=2)
        valueFrame.pack(side=TOP,pady=5,padx=5,ipadx=5)

    def sphere_v():
        r = radius.get()
        answer.delete(1.0,END)
        volumeofsphere = 4*3.14*float(r)*float(r)/3
        answer.insert(INSERT,"Volume of Sphere = 4pi*r^2/3 \n=> ")
        answer.insert(INSERT, " 4pi/3 x ")
        answer.insert(INSERT, r)
        answer.insert(INSERT, " x ")
        answer.insert(INSERT, r)
        answer.insert(INSERT, " = ")
        answer.insert(INSERT,volumeofsphere)
        answer.insert(INSERT, " is your answer")
    def cube_v():
        s = side.get()
        answer.delete(1.0,END)
        volumeofcube = float(s)*float(s)*float(s)
        answer.insert(INSERT,"Volume of Cube = a^3\n=> ")
        answer.insert(INSERT, s)
        answer.insert(INSERT, " × ")
        answer.insert(INSERT, s)
        answer.insert(INSERT, " × ")
        answer.insert(INSERT, s)
        answer.insert(INSERT, " = ")
        answer.insert(INSERT,volumeofcube)
        answer.insert(INSERT, " is your answer")
    def rprism_v():
        l = length.get()
        w = width.get()
        h=height.get()
        volumeofprism = float(l)*float(w)*float(h)
        answer.delete(1.0,END)
        answer.insert(INSERT,"Volume of Rectengular Prism = LENGTH x WIDTH x HEIGHT\n=> ")
        answer.insert(INSERT, l)
        answer.insert(INSERT, " x ")
        answer.insert(INSERT, w)
        answer.insert(INSERT, " x ")
        answer.insert(INSERT, h)
        answer.insert(INSERT," = ")
        answer.insert(INSERT,volumeofprism)
        answer.insert(INSERT," is your answer")
    def cone_v():
        r = radius.get()
        h = height.get()
        volumeofcone= 3.14*float(r)*float(r)*float(h)/3
        answer.delete(1.0,END)
        answer.insert(INSERT, "\nVolume of Cone = pi*r*r*h/3 \n=> ")
        answer.insert(INSERT, "pi/3 ")
        answer.insert(INSERT, " x ")
        answer.insert(INSERT, r)
        answer.insert(INSERT, " x ")
        answer.insert(INSERT, r)
        answer.insert(INSERT, " x ")
        answer.insert(INSERT, h)
        answer.insert(INSERT," = ")
        answer.insert(INSERT, volumeofcone)
        answer.insert(INSERT, " is your answer")
    def cylinder_v():
        r = radius.get()
        h = height.get()
        volumeofcylinder = float(r)*float(h)*float(r)*3.14
        answer.delete(1.0,END)
        answer.insert(INSERT,"Volume of Cylinder\n=> ")
        answer.insert(INSERT, " pi x ")
        answer.insert(INSERT, r)
        answer.insert(INSERT, 'x')
        answer.insert(INSERT, r)
        answer.insert(INSERT, 'x')
        answer.insert(INSERT, h)
        answer.insert(INSERT," = ")
        answer.insert(INSERT,volumeofcylinder)
        answer.insert(INSERT," is your answer")
    def squarepyramid_v():
        s = side.get()
        h=height.get()
        answer.delete(1.0,END)
        volumeofsquarepyramid = float(s)*float(h)/3
        answer.insert(INSERT, "Volume of Square Pyramid = a*h/3\n=>")
        answer.insert(INSERT, s)
        answer.insert(INSERT, " × ")
        answer.insert(INSERT, h)
        answer.insert(INSERT, " x h/3 ")
        answer.insert(INSERT, " = ")
        answer.insert(INSERT, volumeofsquarepyramid)
        answer.insert(INSERT, " is your answer")
    def triprism_v():
        b = base.get()
        h = height.get()
        l = length.get()
        volumeoftriprism = float(b)*float(h)*float(l)/3
        answer.delete(1.0,END)
        answer.insert(INSERT, "Volume of TriangularPrism BASE X HEIGHT X LENGTH\n=> ")
        answer.insert(INSERT, b)
        answer.insert(INSERT, 'x')
        answer.insert(INSERT, h)
        answer.insert(INSERT, " x")
        answer.insert(INSERT, l)
        answer.insert(INSERT, " /3")
        answer.insert(INSERT, " = ")
        answer.insert(INSERT, volumeoftriprism)
        answer.insert(INSERT, " is your answer")
    def spheresec_v():
        pi = 3.14
        r = radius.get()
        h=height.get()
        answer.delete(1.0,END)
        volumeofsectorsphere = 2*pi*float(r)*float(r)*float(h)/3
        answer.insert(INSERT,"Volume of Sector of sphere = 2pi*r^2*h/3 \n=> ")
        answer.insert(INSERT, r)
        answer.insert(INSERT, " x ")
        answer.insert(INSERT, r)
        answer.insert(INSERT, " x ")
        answer.insert(INSERT, h)
        answer.insert(INSERT, " x 2pi /3 ")
        answer.insert(INSERT, " = ")
        answer.insert(INSERT,volumeofsectorsphere)
        answer.insert(INSERT, " is your answer")

    class FullScreenApp(object):
        def __init__(self, master, **kwargs):
            self.master=master
            pad=3
            self._geom='200x200+0+0'
            master.geometry("{0}x{1}+0+0".format(
                master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
            master.bind('<Escape>',self.toggle_geom)            
        def toggle_geom(self,event):
            geom=self.master.winfo_geometry()
            print(geom,self._geom)
            self.master.geometry(self._geom)
            self._geom=geom

    root = tk.Toplevel()
    app=FullScreenApp(root)
    # root.attributes('-fullscreen', True)
    root.title("VOLUME Calculator")
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    positionRight = int(root.winfo_screenwidth()/3 - windowWidth/3)
    positionDown = int(root.winfo_screenheight()/2.5 - windowHeight/2.5)
    root.geometry("+{}+{}".format(positionRight,positionDown))
    # root.geometry("1400x660")
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    positionRight = int(root.winfo_screenwidth()/6 - windowWidth/6)
    positionDown = int(root.winfo_screenheight()/8.5 - windowHeight/8.5)
    root.geometry("+{}+{}".format(positionRight,positionDown))


    frame3 = Frame(root,bg="cyan4")
    answer = Text(frame3,height=15, width=100,wrap=WORD)
    answer.grid(padx=5,pady=5)
    frame3.pack(anchor = "w", side = "bottom")
    def clearFrame():
        # destroy all widgets from frame
        global valueFrame
        for widget in valueFrame.winfo_children():
            widget.destroy()
        valueFrame.forget()
    valueFrame=Frame(root,bg='#008037')
    valueFrame.but = Button(valueFrame,bg='#008037')
    valueFrame.but.grid(row=10, column=10, padx=100, pady=180)
    valueFrame.pack()
    root.configure(bg="#008037")

    clearlastselection_btn= PhotoImage(file='clearlastselection.png')
    img_label2=Label(image=clearlastselection_btn)
    my_button2= Button(root, image= clearlastselection_btn,command=clearFrame,borderwidth=0)
    my_button2.place(x = 0, y = 250)

    clearboard_btn= PhotoImage(file='clearboard.png')
    img_label3=Label(image=clearboard_btn)
    my_button3= Button(root, image= clearboard_btn,command=fresh,borderwidth=0)
    my_button3.place(x = 500, y = 250)


    titlevolume_btn= PhotoImage(file='volumetitle.png')
    img_label4=Label(image=titlevolume_btn)
    my_button4= Button(root, image= titlevolume_btn, borderwidth=0)
    my_button4.place(x = 0, y = 0)

    back_btn= PhotoImage(file='back.png')
    img_label=Label(image=back_btn)
    my_button= Button(root, image= back_btn, command= exit, borderwidth=0)
    my_button.place(x = 0, y = 0)

    # Add item to listbox
    my_list = ttk.Combobox(root, width = 30)
    my_list['values'] = ["--Select figure--","Sphere", "Cube", "Conus","Prism","Cylinder","Spyramid","Tripism","Sector"]
    def select_figure():
        if(my_list.get() == 'Sphere'):
            sphereMethod()
        elif(my_list.get() == 'Cube'):
            cubeMethod()
        elif(my_list.get()== 'Conus'):
            coneMethod()
        elif(my_list.get()== 'Prism'):
            rectengularprismMethod()
        elif(my_list.get()== 'Cylinder'):
            cylinderMethod()
        elif(my_list.get()=='Spyramid'):
            squarepyramidMethod()
        elif(my_list.get()== 'Tripism'):
            triprismMethod()
        elif(my_list.get()== 'Sector'):
            sectorofsphereMethod()



    my_list.current(0)
    my_list.pack(side = LEFT,ipady = 5, pady = 5, padx = 3)

    btn = Button(root, text = "Select", width = 10, bd = 0, fg = "#fff", bg = "#008037",command = lambda: select_figure())
    btn.pack(side = LEFT,ipady = 5,pady = 5)

    mainloop()

def new_window2(): 
    try:
        if root1.state() == "normal": root1.focus()
    except NameError as e:
        print(e)
    def fresh():
        answer.delete(1.0,END)
    
    def exit():
        root.destroy()
    # CIRCLE
    def circleMethod():
        global radius, valueFrame1
        valueFrame1 = Frame(root)
        value = Label(valueFrame1, text="Enter value of radius:")
        value.grid(row=0, column=0)
        radius = Entry(valueFrame1)
        radius.grid(row=0, column=1, pady=5, ipadx=5)
        valueFrame1.pack(side=TOP, pady=5, padx=5, ipadx=5)
        result = Button(valueFrame1, text="Get Answer!",bg="#ed7117", command=C_area)
        result.grid(row=0, column=2)

    # SQAURE

    def squareMethod():
        global side,valueFrame1
        valueFrame1 = Frame(root)
        value = Label(valueFrame1, text="Enter value of side:")
        value.grid(row=0, column=0)
        side = Entry(valueFrame1)
        side.grid(row=0, column=1, pady=5, ipadx=5)
        valueFrame1.pack(side=TOP, pady=5, padx=5, ipadx=5)
        result = Button(valueFrame1, text="Get Answer!",bg="#ed7117", command=S_area)
        result.grid(row=0, column=2)
    # RECTANGLE

    def rectangleMethod():
        global length, breadth,valueFrame1
        valueFrame1 = Frame(root)
        value = Label(valueFrame1, text="Length:  ")
        value.grid(row=0, column=0)
        length = Entry(valueFrame1)
        length.grid(row=0, column=1, pady=5)
        value = Label(valueFrame1, text="Breadth:  ")
        value.grid(row=1, column=0)
        breadth = Entry(valueFrame1)
        breadth.grid(row=1, column=1, pady=5)
        result = Button(valueFrame1, text="Get Answer!",bg="#ed7117", command=R_area)
        result.grid(row=1, column=2)
        valueFrame1.pack(side=TOP, pady=5, padx=5, ipadx=5)
    # TRIANGLE

    def triangleMethod():
        global side1, side2, side3, valueFrame1
        valueFrame1 = Frame(root)
        value = Label(valueFrame1, text="Side1 :",)
        value.grid(row=0, column=0)
        side1 = Entry(valueFrame1)
        side1.grid(row=0, column=1)
        value = Label(valueFrame1, text="Side2 :")
        value.grid(row=1, column=0)
        side2 = Entry(valueFrame1)
        side2.grid(row=1, column=1)
        value = Label(valueFrame1, text="Side3 :")
        value.grid(row=2, column=0)
        side3 = Entry(valueFrame1)
        side3.grid(row=2, column=1)
        result = Button(valueFrame1, text="Get Answer!",
                        bg="#ed7117", command=T_area)
        result.grid(row=2, column=2)
        valueFrame1.pack(side=TOP, pady=5, padx=5, ipadx=5)

    # PARALLELOGRAM

    def parallelogramMethod():
        global base, altitude, valueFrame1
        valueFrame1 = Frame(root)
        value = Label(valueFrame1, text="Base:  ")
        value.grid(row=0, column=0)
        base = Entry(valueFrame1)
        base.grid(row=0, column=1, pady=5)
        value = Label(valueFrame1, text="Altitude:  ")
        value.grid(row=1, column=0)
        altitude = Entry(valueFrame1)
        altitude.grid(row=1, column=1, pady=5)
        result = Button(valueFrame1, text="Get Answer!", bg="#ed7117", command=P_area)
        result.grid(row=1, column=2)
        valueFrame1.pack(side=TOP, pady=5, padx=5, ipadx=5)
    # HEXAGONAL

    def hexagonalMethod():
        global side,valueFrame1
        valueFrame1 = Frame(root)
        value = Label(valueFrame1, text="Enter value of side:")
        value.grid(row=0, column=0)
        side = Entry(valueFrame1)
        side.grid(row=0, column=1, pady=5, ipadx=5)
        valueFrame1.pack(side=TOP, pady=5, padx=5, ipadx=5)
        result = Button(valueFrame1, text="Get Answer!",bg="#ed7117", command=H_area)
        result.grid(row=0, column=2)
    # TRAPEZOID

    def trapezoidMethod():
        global base1, base2, altitude,valueFrame1
        valueFrame1 = Frame(root)
        value = Label(valueFrame1, text="Base1:  ")
        value.grid(row=0, column=0)
        base1 = Entry(valueFrame1)
        base1.grid(row=0, column=1)
        value = Label(valueFrame1, text="Base2:  ")
        value.grid(row=1, column=0)
        base2 = Entry(valueFrame1)
        base2.grid(row=1, column=1)
        value = Label(valueFrame1, text="Altitude:  ")
        value.grid(row=2, column=0)
        altitude = Entry(valueFrame1)
        altitude.grid(row=2, column=1)
        result = Button(valueFrame1, text="Get Answer!",bg="#ed7117", command=Tr_area)
        result.grid(row=2, column=2)
        valueFrame1.pack(side=TOP, pady=5, padx=5, ipadx=5)
    # RHOMBUS

    def rhombusMethod():
        global diogonal1, diogonal2,valueFrame1
        valueFrame1 = Frame(root)
        value = Label(valueFrame1, text="Diogonal1:  ")
        value.grid(row=0, column=0)
        diogonal1 = Entry(valueFrame1)
        diogonal1.grid(row=0, column=1, pady=5)
        value = Label(valueFrame1, text="Diogonal2:  ")
        value.grid(row=1, column=0)
        diogonal2 = Entry(valueFrame1)
        diogonal2.grid(row=1, column=1, pady=5)
        result = Button(valueFrame1, text="Get Answer!",bg="#ed7117", command=Rh_area)
        result.grid(row=1, column=2)
        valueFrame1.pack(side=TOP, pady=5, padx=5, ipadx=5)
        
    # Area of circle
    def C_area():
        pi = 3.1415
        r = radius.get()
        answer.delete(1.0, END)
        areaOfCircle = pi*float(r)*float(r)
        answer.insert(INSERT, "Area of Circle = п*r^2\n=> ")
        answer.insert(INSERT, r)
        answer.insert(INSERT, " X ")
        answer.insert(INSERT, r)
        answer.insert(INSERT, " = ")
        answer.insert(INSERT, areaOfCircle)
        answer.insert(INSERT, " is your answer")

    # Area of square

    def S_area():
        s = side.get()
        answer.delete(1.0, END)
        areaofSquare = float(s)*float(s)
        answer.insert(INSERT, "Area of Square = a^2\n=> ")
        answer.insert(INSERT, s)
        answer.insert(INSERT, " × ")
        answer.insert(INSERT, s)
        answer.insert(INSERT, " = ")
        answer.insert(INSERT, areaofSquare)
        answer.insert(INSERT, " is your answer")

    # Area of rectangle

    def R_area():
        l = length.get()
        b = breadth.get()

        areaofRectangle = float(l)*float(b)
        answer.delete(1.0, END)
        answer.insert(INSERT, "Area of rectangle = LENGTH x BREATH\n=> ")
        answer.insert(INSERT, l)
        answer.insert(INSERT, " X ")
        answer.insert(INSERT, b)
        answer.insert(INSERT, " = ")
        answer.insert(INSERT, areaofRectangle)
        answer.insert(INSERT, " is your answer")

    # Area of triangle

    def T_area():
        s1 = side1.get()
        s2 = side2.get()
        s3 = side3.get()
        s = 1/2*(float(s1)+float(s2)+float(s3))
        areaofTriangle = math.sqrt(s*(s-float(s1))*(s-float(s2))*(s-float(s3)))
        answer.delete(1.0, END)
        answer.insert(INSERT, "p = 1/2(a+b+c)\n=>")
        answer.insert(INSERT, s)
        answer.insert(INSERT, " is half of the perimeter")
        answer.insert(INSERT, "\nArea of Triangle = sqrt(p(p-a)(p-b)(p-c))\n=> ")
        answer.insert(INSERT, areaofTriangle)
        answer.insert(INSERT, " is your answer")

    # Area of parallelogram

    def P_area():
        a = altitude.get()
        b = base.get()
        areaofParallelogram = float(a)*float(b)
        answer.delete(1.0, END)
        answer.insert(INSERT, "Area of parallelogram\n=> ")
        answer.insert(INSERT, a)
        answer.insert(INSERT, " × ")
        answer.insert(INSERT, b)
        answer.insert(INSERT, " = ")
        answer.insert(INSERT, areaofParallelogram)
        answer.insert(INSERT, " is your answer")

    # Area of hexagonal

    def H_area():
        s1 = side.get()
        answer.delete(1.0, END)
        areaofhexagonal = (3*(float(s1)**2)*math.sqrt(3))/2
        answer.insert(INSERT, "Area of hexagonal = (3×a^2×√3)/2\n=>")
        answer.insert(INSERT, "(3 × ")
        answer.insert(INSERT, s1)
        answer.insert(INSERT, "^2 × √3 ) / 2 = ")
        answer.insert(INSERT, areaofhexagonal)
        answer.insert(INSERT, " is your answer")

    # Area of trapezoid

    def Tr_area():
        b1 = base1.get()
        b2 = base2.get()
        a = altitude.get()
        areaofTrapezoid = ((float(b1) + float(b2))/2)*float(a)
        answer.delete(1.0, END)
        answer.insert(INSERT, "Area of trapezoid\n=> ")
        answer.insert(INSERT, "( ")
        answer.insert(INSERT, b1)
        answer.insert(INSERT, " + ")
        answer.insert(INSERT, b2)
        answer.insert(INSERT, " )")
        answer.insert(INSERT, " / 2 × ")
        answer.insert(INSERT, a)
        answer.insert(INSERT, " = ")
        answer.insert(INSERT, areaofTrapezoid)
        answer.insert(INSERT, " is your answer")

    # Area of rhombus

    def Rh_area():
        d1 = diogonal1.get()
        d2 = diogonal2.get()
        areaofRhombus = (float(d1)*float(d2))/2
        answer.delete(1.0, END)
        answer.insert(INSERT, "Area of rhombus\n=> ")
        answer.insert(INSERT, "( ")
        answer.insert(INSERT, d1)
        answer.insert(INSERT, " × ")
        answer.insert(INSERT, d2)
        answer.insert(INSERT, " ) / 2 = ")
        answer.insert(INSERT, areaofRhombus)
        answer.insert(INSERT, " is your answer")

    class FullScreenApp(object):
        def __init__(self, master, **kwargs):
            self.master=master
            pad=3
            self._geom='200x200+0+0'
            master.geometry("{0}x{1}+0+0".format(
                master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
            master.bind('<Escape>',self.toggle_geom)            
        def toggle_geom(self,event):
            geom=self.master.winfo_geometry()
            print(geom,self._geom)
            self.master.geometry(self._geom)
            self._geom=geom


    root = tk.Toplevel()
    app=FullScreenApp(root)
    root.title("Area Calculator")
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    positionRight = int(root.winfo_screenwidth()/3 - windowWidth/3)
    positionDown = int(root.winfo_screenheight()/2.5- windowHeight/2.5)
    root.geometry("+{}+{}".format(positionRight,positionDown))
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    positionRight = int(root.winfo_screenwidth()/6 - windowWidth/6)
    positionDown = int(root.winfo_screenheight()/8.5 - windowHeight/8.5)
    root.geometry("+{}+{}".format(positionRight,positionDown))

    frame3 = Frame(root,bg="cyan4")
    answer = Text(frame3,height=15, width=100,wrap=WORD)
    answer.grid(padx=5,pady=5)
    frame3.pack(anchor = "w", side = "bottom")
    def clearFrame():
        # destroy all widgets from frame
        global valueFrame1
        for widget in valueFrame1.winfo_children():
            widget.destroy()
        valueFrame1.forget()
    valueFrame1=Frame(root,bg='#008037')
    valueFrame1.but = Button(valueFrame1,bg='#008037')
    valueFrame1.but.grid(row=10, column=10, padx=100, pady=180)
    valueFrame1.pack()
    root.configure(bg="#008037")

    clearboard_btn= PhotoImage(file='clearboard.png')
    img_label3=Label(image=clearboard_btn)
    my_button3= Button(root, image= clearboard_btn,command=fresh,borderwidth=0)
    my_button3.place(x = 500, y = 250)

    clearlastselection_btn= PhotoImage(file='clearlastselection.png')
    img_label2=Label(image=clearlastselection_btn)
    my_button2= Button(root, image= clearlastselection_btn,command=clearFrame,borderwidth=0)
    my_button2.place(x = 0, y = 250)


    titlevolume_btn= PhotoImage(file='areatitle.png')
    img_label4=Label(image=titlevolume_btn)
    my_button4= Button(root, image= titlevolume_btn, borderwidth=0)
    my_button4.place(x = 0, y = 0)

    back_btn= PhotoImage(file='back.png')
    img_label=Label(image=back_btn)
    my_button= Button(root, image= back_btn, command= exit, borderwidth=0)
    my_button.place(x = 0, y = 0)

    # Add item to listbox
    my_list = ttk.Combobox(root, width=30)
    my_list['values'] = ["--Select figure--", "Circle", "Square", "Rectangle", "Triangle", "Parallelogram", "Hexagonal", "Trapesoid", 'Rhombus']

    def select_figure():
        if(my_list.get() == 'Circle'):
            circleMethod()
        elif(my_list.get() == 'Square'):
            squareMethod()
        elif(my_list.get() == 'Rectangle'):
            rectangleMethod()
        elif(my_list.get() == 'Triangle'):
            triangleMethod()
        elif(my_list.get() == 'Parallelogram'):
            parallelogramMethod()
        elif(my_list.get() == 'Hexagonal'):
            hexagonalMethod()
        elif(my_list.get() == 'Trapesoid'):
            trapezoidMethod()
        elif(my_list.get() == 'Rhombus'):
            rhombusMethod()

    my_list.current(0)
    my_list.pack(side = LEFT,ipady = 5, pady = 5, padx = 3)

    btn = Button(root, text = "Select", width = 10, bd = 0, fg = "#fff", bg = "#008037",command = lambda: select_figure())
    btn.pack(side = LEFT,ipady = 5,pady = 5)


    mainloop()

def new_window3():
    try:
        if root1.state() == "normal": root1.focus()
    except NameError as e:
        print(e)

    def exit():
        main_window.quit()
    def exit_p():
        root1.destroy()
    def gcd_finder(list_of_numbers):
        do, gcd = 0, 1
        while True:
            if do == 0:
                try:
                    first = list_of_numbers[0]
                    second = list_of_numbers[1]
                except IndexError:
                    return 0
            else:
                first = list_of_numbers[0]
                second = gcd
            if first % second == 0:
                gcd = second
            elif second % first == 0:
                gcd = first
            if first > second:
                while True:
                    remainder = first % second
                    if remainder == 0:
                        gcd = second
                        break
                    first = second
                    second = remainder
            elif second > first:
                while True:
                    remainder = second % first
                    if remainder == 0:
                        gcd = first
                        break
                    second = first
                    first = remainder
            else:
                gcd = first

            if do == 0:
                del list_of_numbers[:2]
            else:
                del list_of_numbers[0]
            if len(list_of_numbers) == 0:
                break
            do += 1
        return gcd

    def lcm_finder(list_of_numbers):
        lcm = 1
        while True:
            found = 0
            for i in list_of_numbers:
                if lcm % i == 0:
                    found += 1
            if found == len(list_of_numbers):
                break
            lcm += 1
        return int(lcm)

    def main(numbers_list):
        def refresh():
            try:
                gcd_label.destroy()
                lcm_label.destroy()
            except NameError:
                pass

            try: 
                error_label.destroy()
            except NameError:
                pass

        global gcd_label, lcm_label, error_label
        error = 0
        # Getting numbers from the list and deleting ' ' and ','
        numbers_ns = numbers_list.get()
        refresh()
        numbers_ps = list(numbers_ns.split(", "))
        try:
            numbers = [int(float(conv)) for conv in numbers_ps]
        except ValueError:
            error += 1
        if error == 0:
            # Counting the GCD and LCM
            gcd = gcd_finder(numbers.copy())
            lcm = lcm_finder(numbers.copy())
            # Showing the GCD and the LCM with labels
            if gcd != 0:
                gcd_label = tk.Label(main_window, text = f"The GCD of these numbers is {gcd}.", font=black, fg = "white", bg = "#008037")
                lcm_label = tk.Label(main_window, text = f"The LCM of these numbers is {lcm}.", font=black ,fg = "white", bg = "#008037")
                gcd_label.place(x = 50, y = 400)
                lcm_label.place(x = 50, y = 455)
            else:
                # Shows the Error
                error_label = tk.Label(main_window, text = "Error: The input form is incorrect.\nPlease, try to enter the values again.", font = arial, fg = "#D41313", bg = "#488D66")
                error_label.place(x = 160, y = 118)
        else:
            # Shows the Error
            error_label = tk.Label(main_window, text = "Error: The input form is incorrect.\nPlease, try to enter the values again.", font = arial, fg = "#D41313", bg = "#488D66")
            error_label.place(x = 160, y = 118)
        return

    def delete_entry():
        numbers_entry.delete(first = "0", last = "1000")
        try:
            gcd_label.destroy()
            lcm_label.destroy()
        except NameError:
            pass 

        try:
            error_label.destroy()
        except NameError:
            pass

    class FullScreenApp(object):
        def __init__(self, master, **kwargs):
            self.master=master
            pad=3
            self._geom='200x200+0+0'
            master.geometry("{0}x{1}+0+0".format(
                master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
            master.bind('<Escape>',self.toggle_geom)            
        def toggle_geom(self,event):
            geom=self.master.winfo_geometry()
            print(geom,self._geom)
            self.master.geometry(self._geom)
            self._geom=geom

    main_window = tk.Toplevel(root1)
    app=FullScreenApp(main_window)
    bg = PhotoImage(file = "gcdlcmbackground.png")
    label1 = Label( main_window, image = bg)
    label1.place(x = 0, y = 0)
    frame1 = Frame(main_window)
    frame1.pack(pady = 20 )
        # Fonts
    arial = Font(family = "arial", size = 15, weight = "bold")
    bank = Font(family = "BankGothic Md BT", size = 12, weight = "bold")
    black = Font(family = "Arial Black", size = 13, weight = "bold")
    windowWidth = main_window.winfo_reqwidth()
    windowHeight = main_window.winfo_reqheight()
    positionRight = int(main_window.winfo_screenwidth()/6 - windowWidth/6)
    positionDown = int(main_window.winfo_screenheight()/8.5 - windowHeight/8.5)
    main_window.geometry("+{}+{}".format(positionRight,positionDown))
    
    main_window.title("GCD and LCM finder")
        # Welcome page with possibility to enter numbers
    welcome = tk.Label(main_window, text = "Welcome to the GCD and LCM finder function", font = arial, fg = "white", bg = "#008037")
    welcome.place(x = 700, y = 0)
    numbers_label = tk.Label(main_window, text = "Please enter the numbers that you want to calculate", font = bank,fg = "white",  bg = "#008037")
    numbers_label.place(x = 675, y = 35)
    hint = tk.Label(main_window, text = "Enter the numbers separated with comma and a space('2, 5, 8').", font = bank,fg = "white",  bg = "#008037")
    hint.place(x =621, y = 56)
    numbers_list = tk.StringVar()
    numbers_entry = tk.Entry(main_window, textvariable = numbers_list, width = 25, justify = 'center', fg = "black", bg = "white")
    numbers_entry.place(x = 590, y = 90)
        # Opportunity to move to the main function 
    to_main = partial(main, numbers_list)
    continue_button = tk.Button(main_window, text = "Continue", width = 7, command = to_main, fg = "black", bg = "green2")
    continue_button.place(x = 790, y = 85)
        # Button that clears all inputs from entry box
    delete_input = tk.Button(main_window, text = "Clear", width = 5, command = delete_entry, fg = "white", bg = "#D41313")
    delete_input.place(x = 525, y = 85)
        # Quit function for exiting the GCD and LCM calculator

    back_btn= PhotoImage(file='back.png')
    img_label=Label(image=back_btn)
    back_button = Button(main_window, image= back_btn,command = main_window.destroy, borderwidth=0)
    back_button.place(x = 0, y = 0)
    main_window.mainloop()
    

def new_window4():
    try:
        if root1.state() == "normal": root1.focus()
    except NameError as e:
        print(e)
        ######################
    def exit():
        root.destroy()
        #################
    def setunit(*args):
        unitfrom['values']=tuple(cdict[quantVar.get().lower()].keys())
        unitto['values']=tuple(cdict[quantVar.get().lower()].keys())


    def calculate(*args):
        result= "{0:.5f}".format(cdict[quantVar.get().lower()][fromVar.get()][toVar.get()](val.get()))
        result_string=val.get(), fromVar.get(),"=", result, toVar.get()
        resultVar.set(result_string)
    
    def delete_entry():
        numbers_entry.delete(first = "0", last = "1000")

    def delete_label():
        resultLabel.grid_forget()



    class FullScreenApp(object):
        def __init__(self, master, **kwargs):
            self.master=master
            pad=3
            self._geom='200x200+0+0'
            master.geometry("{0}x{1}+0+0".format(
                master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
            master.bind('<Escape>',self.toggle_geom)            
        def toggle_geom(self,event):
            geom=self.master.winfo_geometry()
            print(geom,self._geom)
            self.master.geometry(self._geom)
            self._geom=geom


    root = tk.Toplevel(root1)
    app=FullScreenApp(root)

    root.title("Unit Converter")
    bg = PhotoImage(file = "unitbg.png")
  
    # Show image using label
    label1 = Label( root, image = bg)
    label1.place(x = 0, y = 0)
    frame1 = Frame(root)
    frame1.pack(pady = 20 )

    quantVar= StringVar()

    quantity= ttk.Combobox(root, textvariable=quantVar,font=("Times New Roman", 15, "bold"), state="readonly",values=tuple([x.capitalize()for x in cdict.keys()]))
    quantity.bind("<<ComboboxSelected>>",setunit)
    quantity.place(x=100,y=400,height=50, width=300)

    val= DoubleVar()

    numbers_entry = Entry(root, textvariable = val, width = 25,font=("Times New Roman", 15, "bold"))
    numbers_entry.place(x=500,y=400,height=50, width=300)

    fromVar= StringVar()
    unitfrom= ttk.Combobox(root, textvariable=fromVar, state='readonly', font=("Times New Roman", 15, "bold"))
    unitfrom.place(x=100,y=500, height=50, width=300)

    toVar= StringVar()
    unitto= ttk.Combobox(root,textvariable=toVar, state='readonly',font=("Times New Roman", 15, "bold"))
    
    unitto.place(x=100, y=600,height=50, width=300)

    calculateinput_btn= PhotoImage(file='calculate.png')
    img_label3=Label(image=calculateinput_btn)
    my_button3= Button(root, image= calculateinput_btn,command=calculate,borderwidth=0)
    my_button3.place(x = 850, y = 600)


    back_btn= PhotoImage(file='back.png')
    img_label=Label(image=back_btn)
    my_button= Button(root, image= back_btn, command= exit, borderwidth=0)
    my_button.place(x=0, y=0)


    resultVar = StringVar()
    resultLabel=Label(root,textvariable=resultVar,font=("Times New Roman", 15, "bold"))
    resultLabel.place(x=500, y=500)

    clearinput_btn= PhotoImage(file='clearunit.png')
    img_label3=Label(image=clearinput_btn)
    my_button3= Button(root, image= clearinput_btn,command=delete_entry,borderwidth=0)
    my_button3.place(x = 850, y = 400)


    root.mainloop()
    
def new_window6():
    try:
        if root1.state() == "normal": root1.focus()
    except NameError as e:
        print(e)
    class FullScreenApp(object):
        def __init__(self, master, **kwargs):
            self.master=master
            pad=3
            self._geom='200x200+0+0'
            master.geometry("{0}x{1}+0+0".format(
                master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
            master.bind('<Escape>',self.toggle_geom)            
        def toggle_geom(self,event):
            geom=self.master.winfo_geometry()
            print(geom,self._geom)
            self.master.geometry(self._geom)
            self._geom=geom


    window = tk.Toplevel()
    app=FullScreenApp(window)
    bg = PhotoImage(file = "graphbg.png")
    label1 = Label(window, image = bg)
    label1.place(x = 0, y = 0)
    frame1 = Frame(window)
    frame1.pack(pady = 20 )
    window.title("Functions")
    windowWidth = window.winfo_reqwidth()
    windowHeight = window.winfo_reqheight()
    positionRight = int(window.winfo_screenwidth()/6 - windowWidth/6)
    positionDown = int(window.winfo_screenheight()/8.5 - windowHeight/8.5)
    window.geometry("+{}+{}".format(positionRight,positionDown))
    window.config(bg="#008037")
    def exit():
        window.destroy()
    def sinus():
        fig = Figure(figsize=(5.4, 4), dpi=140)
        t = np.arange(0, 15, .01)
        fig.add_subplot().plot(t,  np.sin(t))
        canvas = FigureCanvasTkAgg(fig, master = window) 
        canvas.draw()
        toolbar = NavigationToolbar2Tk(canvas, window)
        toolbar.update()
        toolbar.place(x = 1150, y = 750)
        canvas.get_tk_widget().place(x = 900, y = 150)

    def cosinus():
        fig = Figure(figsize=(5.4, 4), dpi=140)
        t = np.arange(0, 15, 0.01)
        fig.add_subplot().plot(t,  np.cos(t))
        canvas = FigureCanvasTkAgg(fig, master = window) 
        canvas.draw()
        toolbar = NavigationToolbar2Tk(canvas, window)
        toolbar.update()
        toolbar.place(x = 1150, y = 750)
        canvas.get_tk_widget().place(x = 900, y = 150)

    def cubic():
        fig = Figure(figsize=(5.4, 4), dpi=140)
        t = np.arange(-5, 5, .01)
        fig.add_subplot(111).plot(t, t**3)
        canvas = FigureCanvasTkAgg(fig, master = window) 
        canvas.draw()
        toolbar = NavigationToolbar2Tk(canvas, window)
        toolbar.update()
        toolbar.place(x = 1150, y = 750)
        canvas.get_tk_widget().place(x = 900, y = 150)

    def sqrt_func():
        fig = Figure(figsize=(5.4, 4), dpi=140)
        x = np.arange(0, 100, .01)
        fig.add_subplot(111).plot(x, x**(1/2))
        canvas = FigureCanvasTkAgg(fig, master = window) 
        canvas.draw()
        toolbar = NavigationToolbar2Tk(canvas, window)
        toolbar.update()
        toolbar.place(x = 1150, y = 750)
        canvas.get_tk_widget().place(x = 900, y = 150)

    def x_denominator_func():
        fig = Figure(figsize=(5.4, 4), dpi=140)
        x = np.arange(1, 100, .01)
        fig.add_subplot(111).plot(x, 1/x)
        canvas = FigureCanvasTkAgg(fig, master = window) 
        canvas.draw()
        toolbar = NavigationToolbar2Tk(canvas, window)
        toolbar.update()
        toolbar.place(x = 1150, y = 750)
        canvas.get_tk_widget().place(x = 900, y = 150)

    def quadratic():
        fig = Figure(figsize=(5.4,4),dpi=140)
        x=np.linspace(-100,100,50)
        y=x**2
        fig.add_subplot(111).plot(x,y) 
        canvas = FigureCanvasTkAgg(fig, master = window) 
        canvas.draw()
        toolbar = NavigationToolbar2Tk(canvas, window)
        toolbar.update()
        toolbar.place(x = 1150, y = 750)
        canvas.get_tk_widget().place(x = 900, y = 150)
    my_list = ttk.Combobox(window, width=30)
    my_list['values'] = ["--Select Functions--", "Sinus","Cosinus", "Cubic", "√x", "1/x", "Parabola"]

    def select_graph():
        if(my_list.get() == 'Sinus'):
            sinus()
        elif(my_list.get() == 'Cosinus'):
            cosinus()
        elif(my_list.get() == 'Cubic'):
            cubic()
        elif(my_list.get() == '√x'):
            (sqrt_func())
        elif(my_list.get() == '1/x'):
            x_denominator_func()
        elif(my_list.get() == 'Parabola'):
            quadratic()

    btn = Button(window, text = "Select", width = 10, bd = 0, fg = "#fff", bg = "grey", command = lambda: select_graph())
    btn.pack(side = LEFT,ipady = 0,pady = 5)
    back_btn= PhotoImage(file='back.png')
    img_label=Label(image=back_btn)
    my_button= Button(window, image= back_btn, command= exit, borderwidth=0)
    my_button.place(x = 0, y = 0)
      
    my_list.current(0)
    my_list.pack(side = LEFT,ipady = 5, pady = 6, padx = 6)

    window.mainloop()
  

def new_window7():

    class FullScreenApp(object):
        def __init__(self, master, **kwargs):
            self.master=master
            pad=3
            self._geom='200x200+0+0'
            master.geometry("{0}x{1}+0+0".format(
                master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
            master.bind('<Escape>',self.toggle_geom)            
        def toggle_geom(self,event):
            geom=self.master.winfo_geometry()
            print(geom,self._geom)
            self.master.geometry(self._geom)
            self._geom=geom


    root = Toplevel()
    app=FullScreenApp(root)
    bg = PhotoImage(file = "quizbg.png")
    label1 = Label( root, image = bg)
    label1.place(x = 0, y = 0)
    frame1 = Frame(root)
    frame1.pack(pady = 20 )
    back_btn= PhotoImage(file='back.png')
    img_label=Label(image=back_btn)
    my_button= Button(root, image= back_btn, command= root.destroy, borderwidth=0)
    my_button.place(x = 0, y = 0)
    

    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    positionRight = int(root.winfo_screenwidth()/6 - windowWidth/6)
    positionDown = int(root.winfo_screenheight()/8.5 - windowHeight/8.5)
    root.geometry("+{}+{}".format(positionRight,positionDown))
    root.config(bg="#008037")
    root.title("Quiz")
    with open('quiz.json') as f:
        obj = json.load(f)
    q = (obj['ques'])
    options = (obj['options'])
    a = (obj['ans'])
    z=zip(q,options,a)
    l=list(z)
    random.shuffle(l)
    q,options,a=zip(*l)

    class Quiz:
        def __init__(self):
            self.qn = 0
            self.qno=1
            self.quest=StringVar()
            self.ques = self.question(self.qn)
            self.opt_selected = IntVar()
            self.opts = self.radiobtns()
            self.display_options(self.qn)
            self.buttons()
            self.correct = 0

        def question(self, qn):
            t = Label(root, text="Quiz", width=100, bg="#008037" , fg="white", font=("times", 20, "bold"))
            t.place(x=255, y=0)
   
            self.quest.set(str(self.qno)+". "+q[qn])
            qn = Label(root, textvariable=self.quest, width=60,bg="#008037", font=("times", 16, "bold"), anchor="w")
            qn.place(x=70, y=250)
            return qn

        def radiobtns(self):
            val = 0
            # initialize the list with an empty list of options
            b = []
            # position of the first option
            yp = 300
            # adding the options to the list
            while val < 4:
                btn = Radiobutton(root, text=" ", variable=self.opt_selected, value=val + 1,bg="#008037", font=("times", 14))
                b.append(btn)
                btn.place(x=100, y=yp)
                val += 1
                yp += 40
            return b
        
        def display_options(self, qn):
            val = 0
            # deselecting the options
            self.opt_selected.set(0)
            self.ques['text'] = q[qn]
            # looping over the options to be displayed for the
            # text of the radio buttons.
            for op in options[qn]:
                self.opts[val]['text'] = op
                val += 1

        def buttons(self):
            nbutton = Button(root, text="Next",command=self.nextbtn, width=10,bg="green",fg="white",font=("times",16,"bold"))
            nbutton.place(x=380,y=480)
            
        # This method checks the Answer after we click on Next
        def checkans(self, qn):
            if self.opt_selected.get() == a[qn]:
                return True
            
        def nextbtn(self):
            # Check if the answer is correct
            if self.checkans(self.qn):
                # if the answer is correct it increments the correct by 1
                self.correct += 1
            self.qn += 1
            self.qno +=1
            # checks if the q_no size is equal to the data size
            if self.qn == len(q):
                self.display_result()
            else:
                self.quest.set(str(self.qno)+". "+q[self.qn])
                self.display_options(self.qn)       
            

        def display_result(self):
            score = int(self.correct / len(q) * 100)
            result = "Score: " + str(score) + "%"
            wc = len(q) - self.correct
            correct = "No. of correct answers: " + str(self.correct)
            wrong = "No. of wrong answers: " + str(wc)
            mb.showinfo("Result", "\n".join([result, correct, wrong]))

    quiz=Quiz()
    root.mainloop()

def exit():
    root1.quit()
    
def new_window8():
    newWindow = Toplevel()
    newWindow.title("Home Page")

    app=FullScreenApp(newWindow)
    bg = PhotoImage(file = "maisonn.png")
  
    # Show image using label
    label1 = Label( newWindow, image = bg)
    label1.place(x = 0, y = 0)
    frame1 = Frame(newWindow)
    frame1.pack(pady = 20 )

    volume_btn= PhotoImage(file='volume.png')
    img_label=Label(image=volume_btn)
    my_button= Button(frame1, image= volume_btn ,command= new_window1,borderwidth=0)
   
    my_button.pack(side='left', fill='both', padx=0, pady=0, expand=True)
    
    area_btn= PhotoImage(file='area.png')
    img_label=Label(image=area_btn)
    my_button= Button(frame1, image= area_btn, command= new_window2, borderwidth=0)
    my_button.pack(side='left', fill='both', padx=0, pady=0, expand=True)


    gcdlcm_btn= PhotoImage(file='gcdlcm.png')
    img_label=Label(image=gcdlcm_btn)
    my_button= Button(frame1, image= gcdlcm_btn, command= new_window3, borderwidth=0)
    my_button.pack(side='left', fill='both', padx=0, pady=0, expand=True)

    graphs_btn= PhotoImage(file='graphs.png')
    img_label=Label(image=graphs_btn)
    my_button= Button(frame1, image= graphs_btn, command= new_window6, borderwidth=0)
    my_button.pack(side='left', fill='both', padx=0, pady=0, expand=True)

    unit_btn= PhotoImage(file='unit.png')
    img_label=Label(image=graphs_btn)
    my_button= Button(frame1, image= unit_btn, command= new_window4, borderwidth=0)
    my_button.pack(side='left', fill='both', padx=0, pady=0, expand=True)
   
    quiz_btn= PhotoImage(file='quiz.png')
    img_label=Label(image=quiz_btn)
    my_button= Button(frame1, image= quiz_btn, command= new_window7, borderwidth=0)
    my_button.pack(side='left', fill='both', padx=0, pady=0, expand=True)

    newWindow.mainloop()      

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

root1 = tk.Tk()
app=FullScreenApp(root1)
root1.title("Welcome Page")
root1.resizable(True, True)
canvas = Canvas()
canvas.pack(fill=tk.BOTH, expand=True)
image = ImageTk.PhotoImage(file="mathmetric.png")
canvas.create_image(-10, -10, image=image, anchor=NW)

home_btn= PhotoImage(file='home.png')
img_label=Label(image=home_btn)
my_button1= Button(root1, image= home_btn, command= new_window8, borderwidth=0)
my_button1.place(x =90, y = 870)
root1.mainloop()
import tkinter as tk
from tkinter import ttk
from tkinter import *

from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from pandas import DataFrame
from sympy import symbols
from sympy import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import math

# Create window object
app = tk.Tk()

# window properties
app.title("Matrix Acidizing Program")
app.geometry('2000x750')
valbetta = tk.StringVar()
valbetta2 = tk.StringVar()
# Custom functions
β,Ca,Vm,Va,Mwm,Mwa,X,ρa,ρm = symbols('β Ca Vm Va Mwm Mwa X ρa ρm')

vhdata = []
rwhdata = []


def gravimetricdissolvingpowerofacid():
    β = float(Ca.get()) * (float(Vm.get()) * float(Mwm.get())) / (float(Va.get()) * float(Mwa.get()))
    valbetta.set(N(β,2))
    # β :lbm mineral/lbm solution
    # Ca: weight fraction of acid in the acid solution
    # Vm: stoichiometry number of mineral
    # Va:stoichiometry number of acid
    # MWm: molecular weight of mineral
    # MWa:molecular weight of acid
    return β

def select():
    # print ([tree.item(x) for x in tree.selection()])
    for child in listBox.get_children():
        print(listBox.item(child)["values"])

def plot():
    data2 = {'Vh': vhdata,
             'rwh': rwhdata
             }

    for child in listBox.get_children():
        rawdat=(listBox.item(child)["values"])
        vhdata.append(rawdat[0])
        rwhdata.append(float(rawdat[1]))



    df2 = DataFrame(data2,columns = ['Vh','rwh'])

    print(data2)

    figure2 = plt.Figure(figsize = (10,4),dpi = 100)
    ax2 = figure2.add_subplot(111)
    line2 = FigureCanvasTkAgg(figure2,tab3)
    line2.get_tk_widget().pack(side = tk.LEFT,fill = tk.BOTH)
    df2 = df2[['Vh','rwh']].groupby('Vh').sum()
    df2.plot(kind = 'line',legend = True,ax = ax2,color = 'r',marker = 'o',fontsize = 10)
    ax2.set_title('Wormhole Propagation')
    ax2.set(ylabel = "rwh")


def volumetricdissolvingpowerofacid():
    β = float(Ca.get()) * (float(Vm.get()) * float(Mwm.get())) / (float(Va.get()) * float(Mwa.get()))
    X = (β * float(ρa.get())) / float(ρm.get())
    valbetta2.set(N(X,3))
    pass


# Create Tab Widget
tabControl = ttk.Notebook(app)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)
tab6 = ttk.Frame(tabControl)
tab7 = ttk.Frame(tabControl)
tab8 = ttk.Frame(tabControl)
tab9 = ttk.Frame(tabControl)
tab10 = ttk.Frame(tabControl)
tab11 = ttk.Frame(tabControl)
tab12 = ttk.Frame(tabControl)

tabControl.add(tab1,text = 'Dissolving Power of Acid')
tabControl.add(tab2,text = 'Wormhole Propagation')
tabControl.add(tab3,text = 'rwh/volume graph')
tabControl.add(tab4,text = 'Tab 4')
tabControl.add(tab5,text = 'Skin Effect')
tabControl.add(tab6,text = 'Skin Effect Graph')
tabControl.add(tab7,text = 'Acid Injection Rate')
tabControl.add(tab8,text = 'Acid Injection Pressure')
tabControl.add(tab9,text = 'Productivity Index')
tabControl.add(tab10,text = 'Productivity Index Graph')
tabControl.add(tab11,text = 'Production Rate')
tabControl.add(tab12,text = 'Production Rate Graph')
tabControl.pack(expand = 1,fill = "both")

# fill Tab with widgets
# Top labels and entry for tab1(gravimetric and volumetric dissolving power)
mineralhead = ttk.Label(tab1,text = "Mineral Data").grid(column = 0,row = 6,pady = 10,sticky = 'W')
acidhead = ttk.Label(tab1,text = "Acid Data").grid(column = 0,row = 2,pady = 10,sticky = 'W')

Ca = tk.StringVar()
ttk.Label(tab1,text = "Ca(weight fraction of acid in the acid solution)").grid(column = 0,row = 1,pady = 5,sticky = 'W')
Ca = tk.Entry(tab1,textvariable = Ca,width = 10)
Ca.grid(column = 1,row = 1,pady = 5,sticky = 'W')

Vm = tk.StringVar()
ttk.Label(tab1,text = "Vmineral(stoichiometry number of mineral)").grid(column = 0,row = 7,pady = 5,sticky = 'W')
Vm = tk.Entry(tab1,textvariable = Vm,width = 10)
Vm.grid(column = 1,row = 7,pady = 5,sticky = 'W')

Va = tk.StringVar()
ttk.Label(tab1,text = "Vacid").grid(column = 0,row = 3,pady = 5,sticky = 'W')
Va = tk.Entry(tab1,textvariable = Va,width = 10)
Va.grid(column = 1,row = 3,pady = 5,sticky = 'W')

Mwa = tk.StringVar()
ttk.Label(tab1,text = "Mwa").grid(column = 0,row = 4,pady = 5,sticky = 'W')
Mwa = tk.Entry(tab1,textvariable = Mwa,width = 10)
Mwa.grid(column = 1,row = 4,pady = 5,sticky = 'W')

Mwm = tk.StringVar()
ttk.Label(tab1,text = "Mwmineral").grid(column = 0,row = 8,pady = 5,sticky = 'W')
Mwm = tk.Entry(tab1,textvariable = Mwm,width = 10)
Mwm.grid(column = 1,row = 8,pady = 5,sticky = 'W')

ρa = tk.StringVar()
ttk.Label(tab1,text = "ρa").grid(column = 0,row = 5,pady = 5,sticky = 'W')
ρa = tk.Entry(tab1,textvariable = ρa,width = 10)
ρa.grid(column = 1,row = 5,pady = 5,sticky = 'W')

ρm = tk.StringVar()
ttk.Label(tab1,text = "ρm").grid(column = 0,row = 9,pady = 5,sticky = 'W')
ρm = tk.Entry(tab1,textvariable = ρm,width = 10)
ρm.grid(column = 1,row = 9,pady = 5,sticky = 'W')
# Gravimetric label and entry #######################################

# Button Calculate
ttk.Button(tab1,text = "Calculate β",command = gravimetricdissolvingpowerofacid).grid(column = 0,row = 10,pady = 5)

ttk.Label(tab1,text = "β(lbmmineral/lbm solution):").grid(column = 0,row = 11,pady = 10,sticky = 'W')
ttk.Label(tab1,textvariable = valbetta).grid(column = 1,row = 11,pady = 5,sticky = 'W')

# ttk.Button(tab1, text="Calculate", command=volumetricdissolvingpowerofacid).grid(column=, row=10, pady=5)
ttk.Button(tab1,text = "Calculate X",command = volumetricdissolvingpowerofacid).place(x = 200,y = 285)

ttk.Label(tab1,text = "X(ft3 mineral/ft3 solution):                 ").grid(column = 2,row = 11,pady = 10,sticky = 'W')
ttk.Label(tab1,textvariable = valbetta2).grid(column = 3,row = 11,pady = 5,sticky = 'W')

# Contents of tab2################################################################################################

ttk.Label(tab2,text = "Wormhole Radius Data Requirements").grid(column = 0,row = 0,padx = 30,pady = 30)
ttk.Label(tab2,text = "Wormhole Propagation Rate(Upscaling model)", font = ("Times",10,"bold")).grid(column = 0,row = 7,padx = 30,pady = 30)
ttk.Label(tab2,text = "Acid Volume Required", font = ("Times",10,"bold","underline")).grid(column = 0,row = 14,padx = 30,pady = 30)

valbetta3 = tk.StringVar()
valbetta4 = tk.StringVar()
valbett = tk.StringVar()

# functions
import math
rwh,Vh,ϕ1,PVbt,rw,Vh1,vwh,vi, viopt, PVbtopt, ζ, Vh4, ϕ2, rw5, rwh2, PVbt2  = symbols('rwh Vh ϕ1 PVbt rw Vh1 vwh vi viopt PVbtopt ζ Vh4 ϕ2 rw5 rwh2 PVbt2')


plot_button = ttk.Button(tab3,text = "Graph It",command = plot)
plot_button.place(x = 300,y = 285)
plot_button.pack()

def wormholevelocity():
    vwh = (float(vi.get())/float(PVbtopt.get()))*((float(vi.get())/float(viopt.get()))**(-float(ζ.get())))*(1-math.exp(-4*(float(vi.get())/float(viopt.get()))**2)**2)
    valbetta4.set(N(vwh,3))
    pass

def volume():
    Vh4 = math.pi * float(ϕ2.get()) *( ((float(rwh2.get()))**(2)) -  (float(rw5.get()))**(2)   )*(float(PVbt2.get()) )* 7.482
    valbett.set(Vh4)
    pass    

def wormholeradius():
    rwh = (     ((float(rw.get()))**2) +  (float(Vh.get())*0.13369)/(math.pi*float(ϕ1.get()) *float(PVbt.get()) )         )**(1/2)
    valbetta3.set(N(rwh,6))
    pass

#For Tab 2 
def addvalue():
    rwh = ((int(Vh1.get())* 0.13369 / (math.pi * float(ϕ1.get()) * float(PVbt.get()))) + (float(rw.get())) ** 2) ** (1 / 2)
    listBox.insert('','end',value = (int(Vh1.get()),N(rwh,3)))


#For tab 2
ttk.Label(tab2,text = "Vh").place(x = 880)
# grid(row=0,column=1)
Vh1 = tk.StringVar()
Vh1 = tk.Entry(tab2)
Vh1.grid(row = 0,column = 4,sticky = 'E')
Vh1.place(x = 900)

cols = ('Vh','rwh')
listBox = ttk.Treeview(tab2,columns = cols,show = 'headings')
for col in cols:
    listBox.heading(col,text = col)
    listBox.grid(row = 9,column = 6,columnspan = 2)
    listBox.place(x = 900,y = 100)

ttk.Label(tab2, text ="Plot graph in next tab ", font = ("Times",30,"bold")).place(x= 900, y= 400)    

b = tk.Button(tab2,text = 'add value',command = addvalue)
b.grid(row = 0,column = 6,sticky = 'E')
b.place(x = 990)

Vh = tk.IntVar()
ttk.Label(tab2,text = "V/h(injection volume in gal/ft)").grid(column = 0,row = 1,pady = 5,sticky = 'W')
Vh = tk.Entry(tab2,textvariable = Vh,width = 10)
Vh.grid(column = 1,row = 1,pady = 5,sticky = 'W')

ϕ1 = tk.IntVar()
ttk.Label(tab2,text = "ϕ(porosity)").grid(column = 0,row = 2,pady = 5,sticky = 'W')
ϕ1 = tk.Entry(tab2,textvariable = ϕ1,width = 10)
ϕ1.grid(column = 1,row = 2,pady = 5,sticky = 'W')

PVbt = tk.IntVar()
ttk.Label(tab2,text = "PVbt").grid(column = 0,row = 3,pady = 5,sticky = 'W')
PVbt = tk.Entry(tab2,textvariable = PVbt,width = 10)
PVbt.grid(column = 1,row = 3,pady = 5,sticky = 'W')

rw = tk.IntVar()
ttk.Label(tab2,text = "rw").grid(column = 0,row = 4,pady = 5,sticky = 'W')
rw = tk.Entry(tab2,textvariable = rw,width = 10)
rw.grid(column = 1,row = 4,pady = 5,sticky = 'W')

vi = tk.IntVar()
ttk.Label(tab2,text = "vi(interstial velocity of acid)(cm/min)", font = ("Times",10,"bold")).grid(column = 0,row = 8,pady = 5,sticky = 'W')
vi = tk.Entry(tab2,textvariable = vi,width = 10)
vi.grid(column = 1,row = 8,pady = 5,sticky = 'W')

viopt = tk.IntVar()
ttk.Label(tab2,text = "vi,opt(interstial velocity at optimum conditions)(cm/min)", font = ("Times",10,"bold")).grid(column = 0,row = 9,pady = 5,sticky = 'W')
viopt = tk.Entry(tab2,textvariable = viopt,width = 10)
viopt.grid(column = 1,row = 9,pady = 5,sticky = 'W')

PVbtopt = tk.IntVar()
ttk.Label(tab2,text = "PVbtopt(pore volume of acid to breakthrough at optimal conditions)", font = ("Times",10,"bold")).grid(column = 0,row = 10,pady = 5,sticky = 'W')
PVbtopt = tk.Entry(tab2,textvariable = PVbtopt,width = 10)
PVbtopt.grid(column = 1,row = 10,pady = 5,sticky = 'W')

ζ = tk.IntVar()
ttk.Label(tab2,text = "ζ  (the loss in wormholing efficiency at velocities greater than optimum)", font = ("Times",10,"bold")).grid(column = 0,row = 11,pady = 5,sticky = 'W')
ζ = tk.Entry(tab2,textvariable = ζ,width = 10)
ζ.grid(column = 1,row = 11,pady = 5,sticky = 'W')

ttk.Button(tab2,text = "Calculate rwh",command = wormholeradius).grid(column = 0,row = 5,pady = 5)

ttk.Label(tab2,text = "rwh",font = ("Times",20,"bold")).grid(column = 0,row = 6,pady = 10,sticky = 'W')
ttk.Label(tab2,textvariable = valbetta3,font = ("Times",20,"bold")).grid(column = 1,row = 6,pady = 5,sticky = 'W')

ttk.Button(tab2,text = "Calculate vwh",command = wormholevelocity).grid(column = 0,row = 12,pady = 5)

ttk.Label(tab2,text = "vwh(cm/min)",font = ("Times",20,"bold")).grid(column = 0,row = 13,pady = 10,sticky = 'W')
ttk.Label(tab2,textvariable = valbetta4,font = ("Times",20,"bold")).grid(column = 1,row = 13,pady = 5,sticky = 'W')

ϕ2 = tk.IntVar()
ttk.Label(tab2,text = "ϕ(porosity)").grid(column = 0,row = 15,pady = 5,sticky = 'W')
ϕ2 = tk.Entry(tab2,textvariable = ϕ2,width = 10)
ϕ2.grid(column = 1,row = 15,pady = 5,sticky = 'W')

rw5 = tk.IntVar()
ttk.Label(tab2,text = "rw(wellbore radius)(ft)").grid(column = 0,row = 16,pady = 5,sticky = 'W')
rw5 = tk.Entry(tab2,textvariable = rw5,width = 10)
rw5.grid(column = 1,row = 16,pady = 5,sticky = 'W')

rwh2 = tk.IntVar()
ttk.Label(tab2,text = "rwh(Penetrated radius by wormhole)(ft)").grid(column = 0,row = 17,pady = 5,sticky = 'W')
rwh2 = tk.Entry(tab2,textvariable = rwh2,width = 10)
rwh2.grid(column = 1,row = 17,pady = 5,sticky = 'W')

PVbt2 = tk.IntVar()
ttk.Label(tab2,text = "Pvbt (number of pore volumes of acid injected) ").grid(column = 0,row = 18,pady = 5,sticky = 'W')
PVbt2 = tk.Entry(tab2,textvariable = PVbt2,width = 10)
PVbt2.grid(column = 1,row = 18,pady = 5,sticky = 'W')

ttk.Button(tab2,text = "Calculate volume",command = volume).grid(column = 0,row = 19,pady = 5)

ttk.Label(tab2,text = "Vh",font = ("Times",20,"bold")).grid(column = 0,row = 20,pady = 18,sticky = 'W')
ttk.Label(tab2,textvariable = valbett,font = ("Times",20,"bold")).grid(column = 1,row = 20,pady = 5,sticky = 'W')



# Contents of tab2#####################################################################################################

# Graph of tab2 in tab3,tab4 so we go next to tab 5


# Contents of tab 5#################################################################################################################
ttk.Label(tab5, text ="Plot graph in next tab ", font = ("Times",30,"bold")).place(x= 900, y= 400)    
S,k,ks,rs,rw1,Vh2,Pvbt,ϕ,S2,k1,ks1,rs1,rw2 = symbols('S k ks rs rw1 Vh2 Pvbt ϕ S2 k1 ks1 rs1 rw2')
valbetta5 = tk.StringVar()
valbetta6 = tk.StringVar()
ttk.Label(tab5,text = "Skin before matrix acidizing ", font = ("Times",20,"bold")).grid(column = 0,row = 0,padx = 30,pady = 30)
ttk.Label(tab5,text = "Skin after matrix acidizing ", font = ("Times",20,"bold")).grid(column = 0,row = 7,padx = 30,pady = 30)

import numpy as np  

#For Tab 5 
def addvalue1():
    S2 = ((-float(k1.get()))/(2* float(ks1.get()))) * np.log( ((float(rw2.get())/float(rs1.get()))**2) + (float(Vh3.get())*0.13369)/(float(Pvbt.get())*3.14159*((float(rs1.get()))**2)*float(ϕ.get()))) - np.log(float(rs1.get())/float(rw2.get()))
    listBox1.insert('','end',value = (float(Vh3.get()),N(S2,3)))


def skinbefore():
    S = (((float(k.get())/float(ks.get())-1))*np.log(float(rs.get())/float(rw1.get())))
    valbetta5.set(N(S,4))
    pass

def skinafter():
    S2 = ((-float(k1.get()))/(2* float(ks1.get()))) * np.log( ((float(rw2.get())/float(rs1.get()))**2) + (float(Vh2.get())*0.13369)/(float(Pvbt.get())*3.14159*((float(rs1.get()))**2)*float(ϕ.get()))) - np.log(float(rs1.get())/float(rw2.get()))
    valbetta6.set(N(S2,3))
    pass   


k = tk.IntVar()
ttk.Label(tab5,text = "k(permeabilty of undamged formation)").grid(column = 0,row = 1,pady = 5,sticky = 'W')
k = tk.Entry(tab5,textvariable = k,width = 10)
k.grid(column = 1,row = 1,pady = 5,sticky = 'W')

ks = tk.IntVar()
ttk.Label(tab5,text = "ks(permeability in damaged zone)").grid(column = 0,row = 2,pady = 5,sticky = 'W')
ks = tk.Entry(tab5,textvariable = ks,width = 10)
ks.grid(column = 1,row = 2,pady = 5,sticky = 'W')

rs = tk.IntVar()
ttk.Label(tab5,text = "rs(radius of damaged zone)(ft)").grid(column = 0,row = 3,pady = 5,sticky = 'W')
rs = tk.Entry(tab5,textvariable = rs,width = 10)
rs.grid(column = 1,row = 3,pady = 5,sticky = 'W')

rw1 = tk.IntVar()
ttk.Label(tab5,text = "rw(radius of wellbore)(ft)").grid(column = 0,row = 4,pady = 5,sticky = 'W')
rw1 = tk.Entry(tab5,textvariable = rw1,width = 10)
rw1.grid(column = 1,row = 4,pady = 5,sticky = 'W')


k1 = tk.IntVar()
ttk.Label(tab5,text = "k(permeabilty of undamged formation)").grid(column = 0,row = 8,pady = 5,sticky = 'W')
k1 = tk.Entry(tab5,textvariable = k1,width = 10)
k1.grid(column = 1,row = 8,pady = 5,sticky = 'W')

ks1 = tk.IntVar()
ttk.Label(tab5,text = "ks(permeability in damaged zone)").grid(column = 0,row = 9,pady = 5,sticky = 'W')
ks1 = tk.Entry(tab5,textvariable = ks1,width = 10)
ks1.grid(column = 1,row = 9,pady = 5,sticky = 'W')

rs1 = tk.IntVar()
ttk.Label(tab5,text = "rs(radius of damaged zone)(ft)").grid(column = 0,row = 10,pady = 5,sticky = 'W')
rs1 = tk.Entry(tab5,textvariable = rs1,width = 10)
rs1.grid(column = 1,row = 10,pady = 5,sticky = 'W')

rw2 = tk.IntVar()
ttk.Label(tab5,text = "rw(radius of wellbore)(ft)").grid(column = 0,row = 11,pady = 5,sticky = 'W')
rw2 = tk.Entry(tab5,textvariable = rw2,width = 10)
rw2.grid(column = 1,row = 11,pady = 5,sticky = 'W')

Vh2 = tk.IntVar()
ttk.Label(tab5,text = "Vh(Injected volume needed)").grid(column = 0,row = 12,pady = 5,sticky = 'W')
Vh2 = tk.Entry(tab5,textvariable = Vh2,width = 10)
Vh2.grid(column = 1,row = 12,pady = 5,sticky = 'W')

Pvbt = tk.IntVar()
ttk.Label(tab5,text = "Pvbt").grid(column = 0,row = 13,pady = 5,sticky = 'W')
Pvbt = tk.Entry(tab5,textvariable = Pvbt,width = 10)
Pvbt.grid(column = 1,row = 13,pady = 5,sticky = 'W')

ϕ = tk.IntVar()
ttk.Label(tab5,text = "ϕ").grid(column = 0,row = 14,pady = 5,sticky = 'W')
ϕ = tk.Entry(tab5,textvariable = ϕ,width = 10)
ϕ.grid(column = 1,row = 14,pady = 5,sticky = 'W')

ttk.Button(tab5,text = "Calculate",command = skinbefore).grid(column = 0,row = 5,pady = 5)

ttk.Label(tab5,text = "S(before)",font = ("Times",20,"bold")).grid(column = 0,row = 6,pady = 10,sticky = 'W')
ttk.Label(tab5,textvariable = valbetta5,font = ("Times",20,"bold")).grid(column = 1,row = 6,pady = 5,sticky = 'W')

ttk.Button(tab5,text = "Calculate",command = skinafter).grid(column = 0,row = 15,pady = 5)

ttk.Label(tab5,text = "S(after)",font = ("Times",20,"bold")).grid(column = 0,row = 16,pady = 10,sticky = 'W')
ttk.Label(tab5,textvariable = valbetta6,font = ("Times",20,"bold")).grid(column = 1,row = 16,pady = 5,sticky = 'W')

def select1():
    # print ([tree.item(x) for x in tree.selection()])
    for child in listBox1.get_children():
        print(listBox1.item(child)["values"])

ttk.Label(tab5,text = "Vh").place(x = 880)
# grid(row=0,column=1)
Vh3 = tk.StringVar()
Vh3 = tk.Entry(tab5) 
Vh3.grid(row = 0,column = 4,sticky = 'E')
Vh3.place(x = 900)

c = tk.Button(tab5,text = 'add value',command = addvalue1)
c.grid(row = 1,column = 6,sticky = 'E')
c.place(x = 990)

cols1 = ('Volume used(gal/ft)','Skin Factor')
listBox1 = ttk.Treeview(tab5,columns = cols1,show = 'headings')
for col in cols1:
    listBox1.heading(col,text = col)
    listBox1.grid(row = 9,column = 6,columnspan = 2)
    listBox1.place(x = 900,y = 100)

vh3data = []
skindata = []


def plot1():
    data2 = {'Volume used(gal/ft)': vh3data,
             'Skin Factor': skindata
             }

    for child in listBox1.get_children():
        rawdat=(listBox1.item(child)["values"])
        vh3data.append(rawdat[0])
        skindata.append(float(rawdat[1]))



    df2 = DataFrame(data2,columns = ['Volume used(gal/ft)','Skin Factor'])

    print(data2)

    figure2 = plt.Figure(figsize = (10,4),dpi = 100)
    ax2 = figure2.add_subplot(111)
    line2 = FigureCanvasTkAgg(figure2,tab6)
    line2.get_tk_widget().pack(side = tk.LEFT,fill = tk.BOTH)
    df2 = df2[['Volume used(gal/ft)','Skin Factor']].groupby('Volume used(gal/ft)').sum()
    df2.plot(kind = 'line',legend = True,ax = ax2,color = 'r',marker = 'o',fontsize = 10)
    ax2.set_title('Skin Factor')
    ax2.set(ylabel = "S")

#Graph on tab 6
plot_button1 = ttk.Button(tab6,text = "Plot Graph",command = plot1)
plot_button1.place(x = 300,y = 285)
plot_button1.pack()


# Contents of tab 5#################################################################################################################
#graph in tab 6 so move to tab 7

# Contents of tab 7#################################################################################################################
ttk.Label(tab7,text = "Maximum Injection rate ", font = ("Times",10,"underline")).grid(column = 0,row = 1,padx = 30,pady = 30)

# ttk.Label(tab8,text = "Frictional Pressure Drop", font = ("Times",10,"underline")).grid(column = 0,row = 1,padx = 30,pady = 30)
valbetta9 = tk.StringVar()
qi,k2,h,pbd,pr,psf,re,rw3,μa,s  = symbols(' qi k2 h pbd pr psf re rw3 μa s')

def maxpress():
    qi = ( 4.917*10**(-6) * float(k2.get()) * (float(h.get())*float(pbd.get())-float(pr.get())-float(psf.get())) )/( float(μa.get()) * (  np.log((0.472* float(re.get()))/(float(rw3.get())))    + float(s.get()) )         )
    valbetta9.set(N(qi,3))
    pass

k2 = tk.IntVar()
ttk.Label(tab7,text = "k(permeability of undamaged formation)(md)").grid(column = 0,row = 2,pady = 5,sticky = 'W')
k2 = tk.Entry(tab7,textvariable= k2 ,width = 10)
k2.grid(column = 1,row = 2,pady = 5,sticky = 'W')

h = tk.IntVar()
ttk.Label(tab7,text = "h(thickness of payzone to be treated)(ft)").grid(column = 0,row = 3,pady = 5,sticky = 'W')
h = tk.Entry(tab7,textvariable= h ,width = 10)
h.grid(column = 1,row = 3,pady = 5,sticky = 'W')

pbd = tk.IntVar()
ttk.Label(tab7,text = "pbd(formation breakdown pressure)(psia)").grid(column = 0,row = 4,pady = 5,sticky = 'W')
pbd = tk.Entry(tab7,textvariable= pbd ,width = 10)
pbd.grid(column = 1,row = 4,pady = 5,sticky = 'W')

psf = tk.IntVar()
ttk.Label(tab7,text = "psf(safety margin can be between 200-500)(psi)").grid(column = 0,row = 5,pady = 5,sticky = 'W')
psf = tk.Entry(tab7,textvariable= psf ,width = 10)
psf.grid(column = 1,row = 5,pady = 5,sticky = 'W')

re = tk.IntVar()
ttk.Label(tab7,text = "re(drainage radius)(ft)").grid(column = 0,row = 6,pady = 5,sticky = 'W')
re = tk.Entry(tab7,textvariable= re ,width = 10)
re.grid(column = 1,row = 6,pady = 5,sticky = 'W')

rw3 = tk.IntVar()
ttk.Label(tab7,text = "rw(wellbore radius)(ft)").grid(column = 0,row = 7,pady = 5,sticky = 'W')
rw3 = tk.Entry(tab7,textvariable= rw3 ,width = 10)
rw3.grid(column = 1,row = 7,pady = 5,sticky = 'W')

μa = tk.IntVar()
ttk.Label(tab7,text = "μa(viscosity of acid solution)cp ").grid(column = 0,row = 8,pady = 5,sticky = 'W')
μa = tk.Entry(tab7,textvariable= μa ,width = 10)
μa.grid(column = 1,row = 8,pady = 5,sticky = 'W')

s = tk.IntVar()
ttk.Label(tab7,text = "Skin factor (ft) ").grid(column = 0,row = 9,pady = 5,sticky = 'W')
s = tk.Entry(tab7,textvariable= s ,width = 10)
s.grid(column = 1,row = 9,pady = 5,sticky = 'W')

pr = tk.IntVar()
ttk.Label(tab7,text = "P(reservoir pressure) ").grid(column = 0,row = 10,pady = 5,sticky = 'W')
pr = tk.Entry(tab7,textvariable= pr ,width = 10)
pr.grid(column = 1,row = 10,pady = 5,sticky = 'W')



ttk.Button(tab7,text = "Calculate",command = maxpress).grid(column = 0,row = 11,pady = 5)

ttk.Label(tab7,text = "qi(maximum injection rate)bbl/min =",font = ("Times",20,"bold")).grid(column = 0,row = 12,pady = 10,sticky = 'W')
ttk.Label(tab7,textvariable = valbetta9,font = ("Times",20,"bold")).grid(column = 1,row = 12,pady = 5,sticky = 'W')

qi2,qi1,k3,h1,pf1,pr1,μ1,re1,rw4,s1,Lh,Iani,zw,L1,kh,kv,k4  = symbols('qi2 qi1 k3 h1 pf1 pr1 μ1 re1 rw4 s1 Lh Iani zw L1 kh kv k4')

ttk.Label(tab7, text ="Upscaling Model ", font = ("Times",10,"underline","bold")).grid(column = 0,row = 13,pady = 5,sticky = 'W')
valbetta10 = tk.StringVar()
valbetta11 = tk.StringVar()

def verticalinjrate(): #under development (values not accurate)
    oi = np.log((0.472*float(re1.get()))/(float(rw4.get())))
    qi1 = (float(k3.get())*float(h1.get())*(float(pf1.get())-float(pr1.get())))/(141.2*float(μ1.get())*oi + float(s1.get()))
    valbetta10.set(N(qi1,8))
    pass

def horizonatlinjrate(): #under development (values not accurate)
    k4 = (float(kh.get())*float(kv.get()))**(1/2)
    Iani = ((float(kh.get()))/(float(kv.get())))**(1/2)
    vz = 0.5* (np.log(((8*float(h1.get())*Iani)/(3.1415926*float(rw4.get())*((Iani)+1)))*(math.tan(math.radians((pi*float(zw.get()))/(2*float(h1.get())))))**(-1)))
    ou = 0.5*(float(s1.get())-(((float(h1.get())-float(zw.get()))*(Iani))/(float(L1.get()))))
    qi2 = ((7.08*10**(-3))  * float(Lh.get()) *(k4) *(float(pf1.get())-float(pr1.get())) ) /((float(μ1.get())) * ( vz + ou) )
    valbetta11.set(N(qi2,8))
    pass


k3 = tk.IntVar()
ttk.Label(tab7,text = "k formation permeabilty(md) ").grid(column = 0,row = 14,pady = 5,sticky = 'W')
k3 = tk.Entry(tab7,textvariable= k3 ,width = 10)
k3.grid(column = 1,row = 14,pady = 5,sticky = 'W')

h1 = tk.IntVar()
ttk.Label(tab7,text = "h total thickness of reservoir(ft) ").grid(column = 0,row = 27,pady = 5,sticky = 'W')
h1 = tk.Entry(tab7,textvariable= h1 ,width = 10)
h1.grid(column = 1,row = 27,pady = 5,sticky = 'W')

pf1 = tk.IntVar()
ttk.Label(tab7,text = "Pf fracture pressure (psia) ").grid(column = 0,row = 16,pady = 5,sticky = 'W')
pf1 = tk.Entry(tab7,textvariable= pf1 ,width = 10)
pf1.grid(column = 1,row = 16,pady = 5,sticky = 'W')

pr1 = tk.IntVar()
ttk.Label(tab7,text = "Pr (reservoir pressure (psia)) ").grid(column = 0,row = 17,pady = 5,sticky = 'W')
pr1 = tk.Entry(tab7,textvariable= pr1 ,width = 10)
pr1.grid(column = 1,row = 17,pady = 5,sticky = 'W')

μ1 = tk.IntVar()
ttk.Label(tab7,text = "μ (viscosity of fluid)(cp) ").grid(column = 0,row = 18,pady = 5,sticky = 'W')
μ1 = tk.Entry(tab7,textvariable= μ1 ,width = 10)
μ1.grid(column = 1,row = 18,pady = 5,sticky = 'W')

re1 = tk.IntVar()
ttk.Label(tab7,text = "re (drainage radius)(ft) ").grid(column = 0,row = 19,pady = 5,sticky = 'W')
re1 = tk.Entry(tab7,textvariable= re1 ,width = 10)
re1.grid(column = 1,row = 19,pady = 5,sticky = 'W')

rw4 = tk.IntVar()
ttk.Label(tab7,text = "rw (wellbore radius)(ft) ").grid(column = 0,row = 20,pady = 5,sticky = 'W')
rw4 = tk.Entry(tab7,textvariable= rw4 ,width = 10)
rw4.grid(column = 1,row = 20,pady = 5,sticky = 'W')

s1 = tk.IntVar()
ttk.Label(tab7,text = "skin (ft) ").grid(column = 0,row = 21,pady = 5,sticky = 'W')
s1 = tk.Entry(tab7,textvariable= s1 ,width = 10)
s1.grid(column = 1,row = 21,pady = 5,sticky = 'W')

Lh = tk.IntVar()
ttk.Label(tab7,text = "Lh(Horizonatl well length)(ft) ").grid(column = 0,row = 22,pady = 5,sticky = 'W')
Lh = tk.Entry(tab7,textvariable= Lh ,width = 10)
Lh.grid(column = 1,row = 22,pady = 5,sticky = 'W')

kh = tk.IntVar()
ttk.Label(tab7,text = "kh(Horizontal permeability)(md) ").grid(column = 0,row = 23,pady = 5,sticky = 'W')
kh = tk.Entry(tab7,textvariable= kh ,width = 10)
kh.grid(column = 1,row = 23,pady = 5,sticky = 'W')

kv = tk.IntVar()
ttk.Label(tab7,text = "kv(vertical permeabilty)(md) ").grid(column = 0,row = 24,pady = 5,sticky = 'W')
kv = tk.Entry(tab7,textvariable= kv ,width = 10)
kv.grid(column = 1,row = 24,pady = 5,sticky = 'W')

zw = tk.IntVar()
ttk.Label(tab7,text = "zw(elevation of well from reservoir bottom)(ft) ").grid(column = 0,row = 25,pady = 5,sticky = 'W')
zw = tk.Entry(tab7,textvariable= zw ,width = 10)
zw.grid(column = 1,row = 25,pady = 5,sticky = 'W')

L1 = tk.IntVar()
ttk.Label(tab7,text = "L (length of wormhole)(assumed half of core length)ft ").grid(column = 0,row = 26,pady = 5,sticky = 'W')
L1 = tk.Entry(tab7,textvariable= L1 ,width = 10)
L1.grid(column = 1,row = 26,pady = 5,sticky = 'W')

ttk.Button(tab7,text = "Calculate for Horizontal",command = horizonatlinjrate).grid(column = 14,row = 23,pady = 5)

ttk.Label(tab7,text = "q(maximum horizonatl injection rate)bbl/min =",font = ("Times",20,"bold")).grid(column = 13,row = 24,pady = 10,sticky = 'W')
ttk.Label(tab7,textvariable = valbetta11,font = ("Times",20,"bold")).grid(column = 16,row = 24,pady = 5,sticky = 'W')

ttk.Button(tab7,text = "Calculate for vertical",command = verticalinjrate).grid(column = 14,row = 27,pady = 5)

ttk.Label(tab7,text = "q(maximum vertical injection rate)bbl/min =",font = ("Times",20,"bold")).grid(column = 13,row = 28,pady = 10,sticky = 'W')
ttk.Label(tab7,textvariable = valbetta10,font = ("Times",20,"bold")).grid(column = 16,row = 28,pady = 5,sticky = 'W')





# Contents of tab 8#################################################################################################################
ttk.Label(tab8,text = "Surface Injection Pressure", font = ("Times",10,"underline")).grid(column = 0,row = 9,padx = 30,pady = 30)
ttk.Label(tab8,text = "Frictional Pressure Drop", font = ("Times",10,"underline")).grid(column = 0,row = 1,padx = 30,pady = 30)
valbetta7 = tk.StringVar()
valbetta8 = tk.StringVar()

psi,pwf,ph,pf,ρ,q,μ,D,L  = symbols('psi pwf ph pf ρ q μ D L ')

def frictionalpress():
    pf = (518 * (float(ρ.get())**0.79) * (float(q.get())**1.79) * (float(μ.get())**0.207) * float(L.get()))/(1000 * (float(D.get())**4.79))
    valbetta7.set(N(pf,5))
    pass

def injectionpress():
    pf = (518 * (float(ρ.get())**0.79) * (float(q.get())**1.79) * (float(μ.get())**0.207) * float(L.get()))/(1000 * (float(D.get())**4.79))
    psi = (float(pwf.get())) - (float(ph.get())) + (float(pf))
    valbetta8.set(N(psi, 5))
    pass    

ρ = tk.IntVar()
ttk.Label(tab8,text = "ρ(density of fluid)(g/cm3)").grid(column = 0,row = 2,pady = 5,sticky = 'W')
ρ = tk.Entry(tab8,textvariable= ρ  ,width = 10)
ρ.grid(column = 1,row = 2,pady = 5,sticky = 'W')

q = tk.IntVar()
ttk.Label(tab8,text = "q(injection rate)(bbl/min)").grid(column = 0,row = 3,pady = 5,sticky = 'W')
q = tk.Entry(tab8,textvariable= q  ,width = 10)
q.grid(column = 1,row = 3,pady = 5,sticky = 'W')

μ = tk.IntVar()
ttk.Label(tab8,text = "μ(fluid viscosity)(cp)").grid(column = 0,row = 4,pady = 5,sticky = 'W')
μ = tk.Entry(tab8,textvariable= μ  ,width = 10)
μ.grid(column = 1,row = 4,pady = 5,sticky = 'W')

D = tk.IntVar()
ttk.Label(tab8,text = "D(tubing diameter)(in)").grid(column = 0,row = 5,pady = 5,sticky = 'W')
D = tk.Entry(tab8,textvariable= D  ,width = 10)
D.grid(column = 1,row = 5,pady = 5,sticky = 'W')

L = tk.IntVar()
ttk.Label(tab8,text = "L(tubing length)(ft)").grid(column = 0,row = 6,pady = 5,sticky = 'W')
L = tk.Entry(tab8,textvariable= L  ,width = 10)
L.grid(column = 1,row = 6,pady = 5,sticky = 'W')

ttk.Button(tab8,text = "Calculate",command = frictionalpress).grid(column = 0,row = 7,pady = 5)

ttk.Label(tab8,text = "Pf(psia) =",font = ("Times",20,"bold")).grid(column = 0,row = 8,pady = 10,sticky = 'W')
ttk.Label(tab8,textvariable = valbetta7,font = ("Times",20,"bold")).grid(column = 1,row = 8,pady = 5,sticky = 'W')

pwf = tk.IntVar()
ttk.Label(tab8,text = "pwf(flowing bottom hole pressure)(psia)").grid(column = 0,row = 10,pady = 5,sticky = 'W')
pwf = tk.Entry(tab8,textvariable= pwf  ,width = 10)
pwf.grid(column = 1,row = 10,pady = 5,sticky = 'W')

ph = tk.IntVar()
ttk.Label(tab8,text = "ph(hydrostatic pressure drop)(psia)").grid(column = 0,row = 11,pady = 5,sticky = 'W')
ph = tk.Entry(tab8,textvariable= ph  ,width = 10)
ph.grid(column = 1,row = 11,pady = 5,sticky = 'W')

ttk.Button(tab8,text = "Calculate",command = injectionpress).grid(column = 0,row = 12,pady = 5)

ttk.Label(tab8,text = "Psi(psia) =",font = ("Times",20,"bold")).grid(column = 0,row = 13,pady = 10,sticky = 'W')
ttk.Label(tab8,textvariable = valbetta8,font = ("Times",20,"bold")).grid(column = 1,row = 13,pady = 5,sticky = 'W')

#contents of tab 9#####################################################################################Productivity index
#PI before matrix acidizing (skin varies)

valbetta13 = StringVar()
valbetta14 = StringVar()
Jd, re9, rw9, s9, Jd2, re91, rw91, s91, s92 = symbols(' Jd re9 rw9 s9 Jd2 re91 rw91 s91 s92 ')

def prodindexbefore():
    Jd = (1)/(np.log((float(re9.get()))/(float(rw9.get()))) -0.75 + float(s9.get()))
    valbetta13.set(N(Jd,5))
    pass

def prodindexafter():
    Jd2 = (1)/(np.log((float(re91.get()))/(float(rw91.get()))) -0.75 + float(s91.get()))
    valbetta14.set(N(Jd2,5))
    pass    


ttk.Label(tab9,text = "Productivity Index Before ", font = ("Times",10,"underline")).grid(column = 0,row = 1,padx = 30,pady = 30)
ttk.Label(tab9,text = "Productivity Index After ", font = ("Times",10,"underline")).grid(column = 0,row = 7,padx = 30,pady = 30)


re9 = tk.IntVar()
ttk.Label(tab9,text = "re(drainage radius)(ft)").grid(column = 0,row = 2,pady = 5,sticky = 'W')
re9 = tk.Entry(tab9,textvariable= re9  ,width = 10)
re9.grid(column = 1,row = 2,pady = 5,sticky = 'W')

rw9 = tk.IntVar()
ttk.Label(tab9,text = "rw(wellbore radius)(ft)").grid(column = 0,row = 3,pady = 5,sticky = 'W')
rw9 = tk.Entry(tab9,textvariable= rw9  ,width = 10)
rw9.grid(column = 1,row = 3,pady = 5,sticky = 'W')

s9 = tk.IntVar()
ttk.Label(tab9,text = "S (skin)").grid(column = 0,row = 4,pady = 5,sticky = 'W')
s9 = tk.Entry(tab9,textvariable= s9  ,width = 10)
s9.grid(column = 1,row = 4,pady = 5,sticky = 'W')

ttk.Button(tab9,text = "Calculate",command = prodindexbefore).grid(column = 0,row = 5,pady = 5)

ttk.Label(tab9,text = "JD(after) =",font = ("Times",20,"bold")).grid(column = 0,row = 6,pady = 10,sticky = 'W')
ttk.Label(tab9,textvariable = valbetta13,font = ("Times",20,"bold")).grid(column = 1,row = 6,pady = 5,sticky = 'W')

re91 = tk.IntVar()
ttk.Label(tab9,text = "re(drainage radius)(ft)").grid(column = 0,row = 8,pady = 5,sticky = 'W')
re91 = tk.Entry(tab9,textvariable= re91  ,width = 10)
re91.grid(column = 1,row = 8,pady = 5,sticky = 'W')

rw91 = tk.IntVar()
ttk.Label(tab9,text = "rw(wellbore radius)(ft)").grid(column = 0,row = 9,pady = 5,sticky = 'W')
rw91 = tk.Entry(tab9,textvariable= rw91  ,width = 10)
rw91.grid(column = 1,row = 9,pady = 5,sticky = 'W')

s91 = tk.IntVar()
ttk.Label(tab9,text = "S (skin)").grid(column = 0,row = 10,pady = 5,sticky = 'W')
s91 = tk.Entry(tab9,textvariable= s91  ,width = 10)
s91.grid(column = 1,row = 10,pady = 5,sticky = 'W')

ttk.Button(tab9,text = "Calculate",command = prodindexafter).grid(column = 0,row = 11,pady = 5)

ttk.Label(tab9,text = "JD(after) =",font = ("Times",20,"bold")).grid(column = 0,row = 12,pady = 10,sticky = 'W')
ttk.Label(tab9,textvariable = valbetta14,font = ("Times",20,"bold")).grid(column = 1,row = 12,pady = 5,sticky = 'W')

def addvalue9():
    Jd = (1)/(np.log((float(re9.get()))/(float(rw9.get()))) -0.75 + float(s92.get()))
    listBox9.insert('','end',value = (float(s92.get()),N(Jd,3)))

def select9():
    # print ([tree.item(x) for x in tree.selection()])
    for child in listBox9.get_children():
        print(listBox9.item(child)["values"])

ttk.Label(tab9,text = "Skin factor").place(x = 800)
# grid(row=0,column=1)
s92 = tk.StringVar()
s92 = tk.Entry(tab9) 
s92.grid(row = 0,column = 4,sticky = 'E')
s92.place(x = 900)

c9 = tk.Button(tab9,text = 'add value',command = addvalue9)
c9.grid(row = 1,column = 6,sticky = 'E')
c9.place(x = 990)

cols9 = ('Skin factor','Productivity Index')
listBox9 = ttk.Treeview(tab9,columns = cols9,show = 'headings')
for col in cols9:
    listBox9.heading(col,text = col)
    listBox9.grid(row = 9,column = 6,columnspan = 2)
    listBox9.place(x = 900,y = 100)

skindata = []
jddata = []


def plot9():
    data2 = {'Skin factor': skindata,
             'Productivity Index': jddata
             }

    for child in listBox9.get_children():
        rawdat=(listBox9.item(child)["values"])
        skindata.append(rawdat[0])
        jddata.append(float(rawdat[1]))



    df2 = DataFrame(data2,columns = ['Skin factor','Productivity Index'])

    print(data2)

    figure2 = plt.Figure(figsize = (10,4),dpi = 100)
    ax2 = figure2.add_subplot(111)
    line2 = FigureCanvasTkAgg(figure2,tab10)
    line2.get_tk_widget().pack(side = tk.LEFT,fill = tk.BOTH)
    df2 = df2[['Skin factor','Productivity Index']].groupby('Skin factor').sum()
    df2.plot(kind = 'line',legend = True,ax = ax2,color = 'r',marker = 'o',fontsize = 10)
    ax2.set_title('Productivity Index')
    ax2.set(ylabel = "Jd")

#Graph on tab 6
plot_button9 = ttk.Button(tab10,text = "Plot Graph",command = plot9)
plot_button9.place(x = 300,y = 285)
plot_button9.pack()


#contents of tab 9#####################################################################################

#####Contents of tab 11##################################################################Production Rate
valbetta16 = StringVar()
qo, k11, pr11, pwf11, μ11, Bo, re11, rw11, s11, h11, s112 = symbols(' qo k11 pr11 pwf11 μ11 Bo re11 rw11 s11 h11 s112')

ttk.Label(tab11,text = "Production Rate ", font = ("Times",10,"underline")).grid(column = 0,row = 1,padx = 30,pady = 30)


def productionrate():
    zee = float(Bo.get()) *(np.log((float(re11.get()))/(float(rw11.get())))-0.75 + float(s11.get()))
    qo = (float(k11.get())*float(h11.get()) *(float(pr11.get())-float(pwf11.get()) ))/ (141.2 *float(μ11.get()) * zee )
    valbetta16.set(N(qo,7))
    pass


k11 = tk.IntVar()
ttk.Label(tab11,text = "k(permeability )(md)").grid(column = 0,row = 2,pady = 5,sticky = 'W')
k11 = tk.Entry(tab11,textvariable= k11  ,width = 10)
k11.grid(column = 1,row = 2,pady = 5,sticky = 'W')

pr11 = tk.IntVar()
ttk.Label(tab11,text = "Pr (reservoir pressure)").grid(column = 0,row = 3,pady = 5,sticky = 'W')
pr11 = tk.Entry(tab11,textvariable= pr11  ,width = 10)
pr11.grid(column = 1,row = 3,pady = 5,sticky = 'W')

pwf11 = tk.IntVar()
ttk.Label(tab11,text = "Pwf(wellbore pressure)").grid(column = 0,row = 4,pady = 5,sticky = 'W')
pwf11 = tk.Entry(tab11,textvariable= pwf11  ,width = 10)
pwf11.grid(column = 1,row = 4,pady = 5,sticky = 'W')

μ11 = tk.IntVar()
ttk.Label(tab11,text = "μ (viscosity of oil)(cp)").grid(column = 0,row = 5,pady = 5,sticky = 'W')
μ11 = tk.Entry(tab11,textvariable= μ11  ,width = 10)
μ11.grid(column = 1,row = 5,pady = 5,sticky = 'W')

Bo = tk.IntVar()
ttk.Label(tab11,text = "Bo(formation volume factor)").grid(column = 0,row = 6,pady = 5,sticky = 'W')
Bo = tk.Entry(tab11,textvariable= Bo  ,width = 10)
Bo.grid(column = 1,row = 6,pady = 5,sticky = 'W')

re11 = tk.IntVar()
ttk.Label(tab11,text = "re(drainage radius)(ft)").grid(column = 0,row = 7,pady = 5,sticky = 'W')
re11 = tk.Entry(tab11,textvariable= re11  ,width = 10)
re11.grid(column = 1,row = 7,pady = 5,sticky = 'W')

rw11 = tk.IntVar()
ttk.Label(tab11,text = "rw(wellbore radius)(ft)").grid(column = 0,row = 8,pady = 5,sticky = 'W')
rw11 = tk.Entry(tab11,textvariable= rw11  ,width = 10)
rw11.grid(column = 1,row = 8,pady = 5,sticky = 'W')

s11 = tk.IntVar()
ttk.Label(tab11,text = "S(skin)").grid(column = 0,row = 9,pady = 5,sticky = 'W')
s11 = tk.Entry(tab11,textvariable= s11  ,width = 10)
s11.grid(column = 1,row = 9,pady = 5,sticky = 'W')

h11 = tk.IntVar()
ttk.Label(tab11,text = "h(thickness )ft").grid(column = 0,row = 10,pady = 5,sticky = 'W')
h11 = tk.Entry(tab11,textvariable= h11  ,width = 10)
h11.grid(column = 1,row = 10,pady = 5,sticky = 'W')

ttk.Button(tab11,text = "Calculate",command = productionrate).grid(column = 0,row = 11,pady = 5)

ttk.Label(tab11,text = "qo =",font = ("Times",20,"bold")).grid(column = 0,row = 12,pady = 10,sticky = 'W')
ttk.Label(tab11,textvariable = valbetta16,font = ("Times",20,"bold")).grid(column = 1,row = 12,pady = 5,sticky = 'W')

def addvalue11():
    zee = float(Bo.get()) *(np.log((float(re11.get()))/(float(rw11.get())))-0.75 + float(s112.get()))
    qo = (float(k11.get())*float(h11.get()) *(float(pr11.get())-float(pwf11.get()) ))/ (141.2 *float(μ11.get()) * zee )    
    listBox11.insert('','end',value = (float(s112.get()),N(qo,6)))

def select11():
    # print ([tree.item(x) for x in tree.selection()])
    for child in listBox11.get_children():
        print(listBox11.item(child)["values"])

ttk.Label(tab11,text = "Skin factor").place(x = 800)
# grid(row=0,column=1)
s112 = tk.StringVar()
s112 = tk.Entry(tab11) 
s112.grid(row = 0,column = 4,sticky = 'E')
s112.place(x = 900)

c11 = tk.Button(tab11,text = 'add value',command = addvalue11)
c11.grid(row = 1,column = 6,sticky = 'E')
c11.place(x = 990)

cols11 = ('Skin factor','Production Rate')
listBox11 = ttk.Treeview(tab11,columns = cols11,show = 'headings')
for col in cols11:
    listBox11.heading(col,text = col)
    listBox11.grid(row = 9,column = 6,columnspan = 2)
    listBox11.place(x = 900,y = 100)

skin11data = []
prodata = []


def plot11():
    data2 = {'Skin factor': skin11data,
             'Production Rate': prodata
             }

    for child in listBox11.get_children():
        rawdat=(listBox11.item(child)["values"])
        skin11data.append(rawdat[0])
        prodata.append(float(rawdat[1]))



    df2 = DataFrame(data2,columns = ['Skin factor','Production Rate'])

    print(data2)

    figure2 = plt.Figure(figsize = (10,4),dpi = 100)
    ax2 = figure2.add_subplot(111)
    line2 = FigureCanvasTkAgg(figure2,tab12)
    line2.get_tk_widget().pack(side = tk.LEFT,fill = tk.BOTH)
    df2 = df2[['Skin factor','Production Rate']].groupby('Skin factor').sum()
    df2.plot(kind = 'line',legend = True,ax = ax2,color = 'r',marker = 'o',fontsize = 10)
    ax2.set_title('Production Rate')
    ax2.set(ylabel = "qo")

#Graph on tab 12
plot_button11 = ttk.Button(tab12,text = "Plot Graph",command = plot11)
plot_button11.place(x = 300,y = 285)
plot_button11.pack()

# Start program
app.mainloop()

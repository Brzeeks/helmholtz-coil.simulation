# -----------------------------------------------------------
# Computer code calculating and graphing wanted coil specifications
#
# (C) 2022 Andrea Brzica, Zagreb, Croatia
# email andrea.brzica@hotmail.com
#
# A big thanks goes to Davor Dobrota for helping me out with the theoretical aspect of creating this simulation
#
# -----------------------------------------------------------
# PARAMETERS
# B-magnetic field strength
# I-current
# R-coil resistance
# V-voltage across coil
# rho-resistivity of a material (copper in our case)
# P-power consuption by a coil
# L-length of a coil
# N-number of turns
# r-coil radius
# S-wire cross section
# Sb-core magnetization magnetic field strength
# D-distance from the object along the x-axis
# b-thickness of a coil
# -----------------------------------------------------------
#importing what is needed
import matplotlib.pyplot as plt
import numpy as np
from math import*
# -----------------------------------------------------------
#defining functions

def calc_power(V,R): #function for calculating coil power consuption
    P= V**2/R
    print("Calculating coil power consuption...")
    print("The calculated power of your coil is:",P, "W")
    print("-----------------------------------------------------------")
    return

def calc_numb_turns(L,r): #function for calculating the number of coil turns
    N=L/(2*3.141592654*r)
    print("Calculating bumber of turns...")
    print("The calculated number of turns your coil has is:", N)
    print("-----------------------------------------------------------")
    return

def calc_cross_sec(N, rho, r, R): #function for calculating the cross sectional area of a wire
    S=(N*rho*2*3.141592654*r)/R
    print("Calculating the cross sectional area of a wire...")
    print("The calculated cross section of your wire is:",S, "m^2")
    print("-----------------------------------------------------------")
    return

def calc_resist(rho, L, S): #function for calculating the coil resistance
    R=rho*(L/S)
    print("Calculating coil resistance...")
    print("The calculated wire resistance is: ", R , "Ohm")
    print("-----------------------------------------------------------")
    return

def graph_mfield_coil(N,I,b,D,r,): #function for graphin magnetic field of coil 
    print("Graphing the magnetic field of a single coil...")
    x = np.linspace(-3*r,3*r,100)
    y = ((4*3.14e-7)/2)*((N*I)/b)*((x+D/2+b/2)/(np.sqrt((x+D/2+b/2)**2 + r**2))-(x+D/2-b/2)/(np.sqrt((x+D/2-b/2)**2 + r**2)))
    plt.xlabel('Displacment from the coil centre / m')
    plt.ylabel('Magnetic field strength / T')
    plt.plot(x,y, 'b')
    plt.show()
    print("-----------------------------------------------------------")
    return

def graph_mfield_core(Sb,b,D,r): #function for graphing magnetic field of magnetized core
    print("Graphing the magnetic field of a single core...")
    x = np.linspace(-3*r,3*r,100)
    z = ((Sb)/2)*((x+D/2+b/2)/(np.sqrt((x+D/2+b/2)**2 + r**2))-(x+D/2-b/2)/(np.sqrt((x+D/2-b/2)**2 + r**2)))
    plt.xlabel('Displacment from the core centre / m')
    plt.ylabel('Magnetic field strength / T')
    plt.plot(x,z, 'r')
    plt.show()
    print("-----------------------------------------------------------")
    return

def graph_mfield_coil_core(N,I,b,D,r,Sb):
    print("Graphing the magnetic field of a single coil with a core...")
    x = np.linspace(-3*r,3*r,100)
    q=((4*3.14e-7)/2)*((N*I)/b)*((x+D/2+b/2)/(np.sqrt((x+D/2+b/2)**2 + r**2))-(x+D/2-b/2)/(np.sqrt((x+D/2-b/2)**2 + r**2)))+((Sb)/2)*((x+D/2+b/2)/(np.sqrt((x+D/2+b/2)**2 + r**2))-(x+D/2-b/2)/(np.sqrt((x+D/2-b/2)**2 + r**2)))
    plt.xlabel('Displacment from the coil-core centre / m')
    plt.ylabel('Magnetic field strength / T')
    plt.plot(x,q, 'g')
    plt.show()
    print("-----------------------------------------------------------")
    return
    

def graph_mfield_coil_core_both(N,I,b,D,r,Sb): #function for graphing magnetic field strenght in front of coil with core
    print("Graphing the magnetic field of a single coil, single core, and a coil with a core...")
    x = np.linspace(-3*r,3*r,100)
    y = ((4*3.14e-7)/2)*((N*I)/b)*((x+D/2+b/2)/(np.sqrt((x+D/2+b/2)**2 + r**2))-(x+D/2-b/2)/(np.sqrt((x+D/2-b/2)**2 + r**2)))
    z = ((Sb)/2)*((x+D/2+b/2)/(np.sqrt((x+D/2+b/2)**2 + r**2))-(x+D/2-b/2)/(np.sqrt((x+D/2-b/2)**2 + r**2)))
    q =((4*3.14e-7)/2)*((N*I)/b)*((x+D/2+b/2)/(np.sqrt((x+D/2+b/2)**2 + r**2))-(x+D/2-b/2)/(np.sqrt((x+D/2-b/2)**2 + r**2)))+((Sb)/2)*((x+D/2+b/2)/(np.sqrt((x+D/2+b/2)**2 + r**2))-(x+D/2-b/2)/(np.sqrt((x+D/2-b/2)**2 + r**2)))
    plt.xlabel('Displacment from the system centre / m')
    plt.ylabel('Magnetic field strength / T')
    plt.plot(x,y, 'b', label='coil')
    plt.plot(x,z, 'r', label='core')
    plt.plot(x,q, 'g', label='coil with core')
    plt.legend(loc='upper right')
    plt.show()
    print("-----------------------------------------------------------")
    return

def graph_mfield_2coils(N,I,b,D,r,):
    print("Graphing the magnetic field between two coils...")
    x = np.linspace(-3*r,3*r,100)
    y = ((4*3.14e-7)/2)*((N*I)/b)*((x+D/2+b/2)/(np.sqrt((x+D/2+b/2)**2 + r**2))-(x+D/2-b/2)/(np.sqrt((x+D/2-b/2)**2 + r**2)))+((4*3.14e-7)/2)*((N*I)/b)*((x-D/2+b/2)/(np.sqrt((x-D/2+b/2)**2 + r**2))-(x-D/2-b/2)/(np.sqrt((x-D/2-b/2)**2 + r**2)))
    plt.xlabel('Displacment from the coil system centre / m')
    plt.ylabel('Magnetic field strength / T')
    plt.plot(x,y, 'b')
    plt.show()
    print("-----------------------------------------------------------")
    return
    
def graph_mfield_2cores(N,I,b,D,r,Sb):
    print("Graphing the magnetic field between two cores...")
    x = np.linspace(-3*r,3*r,100)
    z = (Sb/2)*((x+D/2+b/2)/(np.sqrt((x+D/2+b/2)**2 + r**2))-(x+D/2-b/2)/(np.sqrt((x+D/2-b/2)**2 + r**2)))+(Sb/2)*((x-D/2+b/2)/(np.sqrt((x-D/2+b/2)**2 + r**2))-(x-D/2-b/2)/(np.sqrt((x-D/2-b/2)**2 + r**2)))
    plt.xlabel('Displacment from the coil system centre / m')
    plt.ylabel('Magnetic field strength / T')
    plt.plot(x,z, 'r')
    plt.show()
    print("-----------------------------------------------------------")
    return
    
def graph_mfield_2coil_cores(N,I,b,D,r,Sb):
    print("Graphing the magnetic field between two coils with cores...")
    x = np.linspace(-3*r,3*r,100)
    q=((4*3.14e-7)/2)*((N*I)/b)*((x+D/2+b/2)/(np.sqrt((x+D/2+b/2)**2 + r**2))-(x+D/2-b/2)/(np.sqrt((x+D/2-b/2)**2 + r**2)))+((4*3.14e-7)/2)*((N*I)/b)*((x-D/2+b/2)/(np.sqrt((x-D/2+b/2)**2 + r**2))-(x-D/2-b/2)/(np.sqrt((x-D/2-b/2)**2 + r**2)))+((4*3.14e-7)/2)*((N*I)/b)*((x+D/2+b/2)/(np.sqrt((x+D/2+b/2)**2 + r**2))-(x+D/2-b/2)/(np.sqrt((x+D/2-b/2)**2 + r**2)))+(Sb/2)*((x+D/2+b/2)/(np.sqrt((x+D/2+b/2)**2 + r**2))-(x+D/2-b/2)/(np.sqrt((x+D/2-b/2)**2 + r**2)))+(Sb/2)*((x-D/2+b/2)/(np.sqrt((x-D/2+b/2)**2 + r**2))-(x-D/2-b/2)/(np.sqrt((x-D/2-b/2)**2 + r**2)))
    plt.xlabel('Displacment from the coil system centre / m')
    plt.ylabel('Magnetic field strength / T')
    plt.plot(x,q, 'g')
    plt.show()
    print("-----------------------------------------------------------")
    return

def graph_mfield_2coils_2cores_both(N,I,b,D,r,Sb):
    print("Graphing the magnetic field between two coils, cores, and coils with cores")
    x = np.linspace(-3*r,3*r,100)
    y = ((4*3.14e-7)/2)*((N*I)/b)*((x+D/2+b/2)/(np.sqrt((x+D/2+b/2)**2 + r**2))-(x+D/2-b/2)/(np.sqrt((x+D/2-b/2)**2 + r**2)))+((4*3.14e-7)/2)*((N*I)/b)*((x-D/2+b/2)/(np.sqrt((x-D/2+b/2)**2 + r**2))-(x-D/2-b/2)/(np.sqrt((x-D/2-b/2)**2 + r**2)))
    z = (Sb/2)*((x+D/2+b/2)/(np.sqrt((x+D/2+b/2)**2 + r**2))-(x+D/2-b/2)/(np.sqrt((x+D/2-b/2)**2 + r**2)))+(Sb/2)*((x-D/2+b/2)/(np.sqrt((x-D/2+b/2)**2 + r**2))-(x-D/2-b/2)/(np.sqrt((x-D/2-b/2)**2 + r**2)))
    q=((4*3.14e-7)/2)*((N*I)/b)*((x+D/2+b/2)/(np.sqrt((x+D/2+b/2)**2 + r**2))-(x+D/2-b/2)/(np.sqrt((x+D/2-b/2)**2 + r**2)))+((4*3.14e-7)/2)*((N*I)/b)*((x-D/2+b/2)/(np.sqrt((x-D/2+b/2)**2 + r**2))-(x-D/2-b/2)/(np.sqrt((x-D/2-b/2)**2 + r**2)))+((4*3.14e-7)/2)*((N*I)/b)*((x+D/2+b/2)/(np.sqrt((x+D/2+b/2)**2 + r**2))-(x+D/2-b/2)/(np.sqrt((x+D/2-b/2)**2 + r**2)))+(Sb/2)*((x+D/2+b/2)/(np.sqrt((x+D/2+b/2)**2 + r**2))-(x+D/2-b/2)/(np.sqrt((x+D/2-b/2)**2 + r**2)))+(Sb/2)*((x-D/2+b/2)/(np.sqrt((x-D/2+b/2)**2 + r**2))-(x-D/2-b/2)/(np.sqrt((x-D/2-b/2)**2 + r**2)))
    plt.xlabel('Displacment from the coil system centre / m')
    plt.ylabel('Magnetic field strength / T')
    plt.plot(x,y, 'b', label='two coils')
    plt.plot(x,z, 'r', label='two cores')
    plt.plot(x,q, 'g', label='two coils with cores')
    print("-----------------------------------------------------------")
    return
    
# -----------------------------------------------------------
#choosing what to calculate/ graph



print("If you need to calculate: ")
print("coil power - input 1")
print("number of turns - input 2")
print("wire cross section - input 3")
print("wire resistance - input 4")
print("coil magnetic field (along z axis) - input 5")
print("-----------------------------------------------------------")
print("If you need to graph: ")
print("coil magnetic field - input a")
print("core magnetic field - input b")
print("both coil-core system magnetic field - input c")
print("option 1,2,3 combined - input d")
print("magnetic field between two identical coils - input f")
print("magnetic field between two identical cores - input g")
print("magnetic field between two identical coils with cores - input h")
print("option 5,6,7 combined - input i")
    
while True:
    ans=input("Input the operation you want to perform: ")
    print("-----------------------------------------------------------")
    if ans=="1":
        V=float(input("Input voltage:"))
        R=float(input("Input coil resistance: ",))
        print("")
        calc_power(V,R)
    
    elif ans=="2":
        L=float(input("Input coil length: "))
        r=float(input("Input coil radius: "))
        print("")
        calc_numb_turns(L,r)
    
    elif ans=="3":
        N=float(input("Input number of turns: "))
        question1=input("Are you using copper wire? (Y/N) ")
        if question1=="Y":
            print("You do not have to input wire resistivity. It is stored inside the system.")
            rho=1.72e-8
        elif question1=="N":
            rho=float(input("Input wire resistivity: "))
        else:
            print("Answer the question with either Y or N ")
        r=float(input("Input coil radius:" ))
        R=float(input("Input coil resistance:" ))
        print("")
        calc_cross_sec(N,rho,r,R)
    
    elif ans=="4":
        question1=input("Are you using copper wire? (Y/N) ")
        if question1=="Y":
            print("You do not have to input wire resistivity. It is stored inside the system.")
            rho=1.72e-8
        elif question1=="N":
            rho=float(input("Input wire resistivity: "))
        else:
            print("Answer the question with either Y or N ")
        L=float(input("Input coil length: "))
        S=float(input("Input wire cross section: "))
        print("")
        calc_resist(rho,L,S)
    
    elif ans=="a":
        N=float(input("Input number of turns: "))
        I=float(input("Input the current going through the coil: "))
        b=float(input("Input the thickness of the coil:"))
        r=float(input("Input the radius of the coil: "))
        D=float(input("Input the distance from the coil along the x-axis: "))
        print("")
        graph_mfield_coil(N, I, b, D, r)
    elif ans=="b":
        Sb=float(input("Input the magnetic field strength of core magnetization: "))
        b=float(input("Input the thickness of the core:"))
        r=float(input("Input the radius of the core: "))
        D=float(input("Input the distance from the core along the x-axis: "))
        print("")
        graph_mfield_core(Sb, b, D, r)
    elif ans=="c":
        N=float(input("Input number of turns: "))
        I=float(input("Input the current going through the coil: "))
        b=float(input("Input the thickness of the coil:"))
        r=float(input("Input the radius of the coil: "))
        D=float(input("Input the distance from the coil along the x-axis: "))
        Sb=float(input("Input the magnetic field strength of core magnetization: "))
        print("")
        graph_mfield_coil_core(N, I, b, D, r, Sb)
    elif ans=="d":
        N=float(input("Input number of turns: "))
        I=float(input("Input the current going through the coil: "))
        b=float(input("Input the thickness of the coil/core system:"))
        r=float(input("Input the radius of the coil/core system: "))
        D=float(input("Input the distance from the coil/core system along the x-axis: "))
        Sb=float(input("Input the magnetic field strength of core magnetization: "))
        print("")
        graph_mfield_coil_core_both(N, I, b, D, r, Sb)
    elif ans=="f":
        N=float(input("Input number of turns: "))
        I=float(input("Input the current going through one of the coils: "))
        b=float(input("Input the thickness of one of the coils: "))
        r=float(input("Input the radius of the one of the coils:  "))
        D=float(input("Input the distance between the two coils: "))
        print("")
        graph_mfield_2coils(N, I, b, D, r)
    elif ans=="g":
        N=float(input("Input number of turns: "))
        I=float(input("Input the current going through one of the coils: "))
        b=float(input("Input the thickness of one of the cores: "))
        r=float(input("Input the radius of the one of the cores:  "))
        D=float(input("Input the distance between the two cores: "))
        Sb=float(input("Input the magnetic field strength of core magnetization: "))
        print("")
        graph_mfield_2cores(N, I, b, D, r,Sb)
    elif ans=="h":
        N=float(input("Input number of turns: "))
        I=float(input("Input the current going through one of the coils: "))
        b=float(input("Input the thickness of one of the cores: "))
        r=float(input("Input the radius of the one of the cores:  "))
        D=float(input("Input the distance between the two cores: "))
        Sb=float(input("Input the magnetic field strength of core magnetization: "))
        print("")
        graph_mfield_2coil_cores(N, I, b, D, r, Sb)
    elif ans=="i":
        N=float(input("Input number of turns: "))
        I=float(input("Input the current going through one of the coils: "))
        b=float(input("Input the thickness of one of the coils: "))
        r=float(input("Input the radius of the one of the coil:  "))
        D=float(input("Input the distance between the two coils with cores: "))
        Sb=float(input("Input the magnetic field strength of core magnetization: "))
        print("")
        graph_mfield_2coils_2cores_both(N, I, b, D, r, Sb)
    else:
        print("Error")
        break

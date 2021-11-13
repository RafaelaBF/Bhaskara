# -*- coding: utf-8 -*-
"""
@author: Rafaela BF

Faça um programa que resolva Bhaskara por meio de uma equação completa do segundo grau.
"""

eq = input("Entre com a equação: ")
aux =[""]*3

i = eq.find("²", 0)
aux[0] = eq[0:(i+1)] 
j = eq.find("x", i)
aux[1] = eq[(i+1):(j+1)]
aux[2] = eq[(j+1):len(eq)]

i = 0
j = 0

#A
if len(aux[0]) < 3:
    aux[0] = 1
    
elif aux[0].find('-', 0) != -1:
    if len(aux[0]) < 4:
        aux[0] = -1
    else:
        i = aux[0].find("x²", 0)
        aux[0] = int(aux[0][0:i])
else:
    i = aux[0].find("x²", 0)
    aux[0] = int(aux[0][0:i])


#B
if len(aux[1]) < 2:
    aux[1] = 1
    
elif aux[1].find('-', 0) != -1:
    if len(aux[1]) < 3:
        aux[1] = -1
    else:
        i = aux[1].find("x", 0)
        aux[1] = int(aux[1][0:i])
else:
    i = aux[1].find("x", 0)
    aux[1] = int(aux[1][0:i])
    
#C
aux[2] = int(aux[2])

#Equação
print()
print(f"A equação: {eq}")
print(f"Onde A = {aux[0]} B = {aux[1]} C = {aux[2]}")

#Raízes
print()
print("Tem raízes: ")

x1 = (-aux[1] + (aux[1]**2 - 4*aux[0]*aux[2])**(1/2))/(2*aux[0])
print(f"X1 = {(x1):.2f}")

x2 = (-aux[1] - (aux[1]**2 - 4*aux[0]*aux[2])**(1/2))/(2*aux[0])
print(f"X2 = {(x2):.2f}")

#Vértices
print()
print("Vértices: ")
print(f"Xv = {((-aux[1])/(2*aux[0])):.2f}")
print(f"Yv = {((-(aux[1]**2 - 4*aux[0]*aux[2]))/(4*aux[0])):.2f}")

#Forma Fatorada
print()
print("sua Forma Fatorada é: ")
print(f"{aux[0]} * (X - ({(x1):.2f})) * (X - ({(x2):.2f})) = 0")

#Concavidade da parábola
print()
print("Concavidade da parábola é:", end=" ")

if aux[0] > 0:
    print("voltada para cima")
else:
    print("voltada para baixo")



    
    
    
    
    
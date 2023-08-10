#Faça um Programa que leia três números e mostre o menor deles.

number01 = int(input("Digite o número 01: \n"))
number02 = int(input("Digite o número 02: \n"))
number03 = int(input("Digite o número 03: \n"))

menor = number01 

if (number02 < menor):
    menor = number02
if (number03 < menor):
    menor = number03

print (f" o menor número é {menor} ")
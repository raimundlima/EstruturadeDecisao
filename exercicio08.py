#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.


produto01 = float(input("Digite o preço do produto 01: \n"))
produto02 = float(input("Digite o preço do produto 02: \n"))
produto03 = float(input("Digite o preço do produto 03: \n"))

menor = produto01 

if (produto02 < menor):
    menor = produto02
if (produto03 < menor):
    menor = produto03

print (f" O produto mais barato é  {menor} ")
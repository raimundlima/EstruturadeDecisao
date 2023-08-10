# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.


nota1 = float(input("Digite a sua nota 1:\n"))
nota_invalida = nota1 < 0 or nota1 > 10
while nota_invalida:
    print("A nota de ser entre 0 e 10")
    nota1 = float(input("Digite a sua nota 1:\n"))
    nota_invalida = nota1 < 0 or nota1 > 10

nota2 = float(input("Digite a sua nota 2:\n"))
nota_invalida = nota2 < 0 or nota2 > 10
while nota_invalida:
    print("A nota de ser entre 0 e 10")
    nota2 = float(input("Digite a sua nota 2:\n"))
    nota_invalida = nota2 < 0 or nota2 > 10

media = (nota1 + nota2 ) /2

aprovado = media > 7 and media < 9.9
reprovado = media < 7 
aprovado_dist = media == 10

if aprovado:
    print (f"Parabéns você vc foi aprovado com a média {media}!")

elif reprovado:
    print (f"Você foi reprovado com a média {media} tente novamente!")

elif aprovado_dist:
    print (f"Parabéns você foi aprovado com Distinção com a média {media}!!!!")
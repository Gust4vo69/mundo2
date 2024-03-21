print("Calculo de aprovação de media anual")
i = 0
notas = [0,0,0,0]
while i < 4:
    nota = float(input("Digite a {} nota:\n".format(i +1)))
    notas[i] = nota
    i = i + 1
    
notaf = sum(notas)/4
if notaf < 5:
    print("Reprovado, nota {}".format(notaf))
elif 5 <= notaf < 7:
    print("Recuperação, nota {}".format(notaf))
else:
    print("Aprovado com Sucesso, nota {}".format(notaf))


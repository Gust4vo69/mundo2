print("Bem vindo a simulação do seu emprestimo bancario!")
casa = float(input("Nos informe o valor desejado:\n"))
anos = float(input("\nEm quantos anos você quer pagar?\n"))
salario =  float(input("\nQual é o seu salário mensal?\n"))

qparcelas = anos*12
vparcelas = casa/qparcelas
limite = salario*0.30

print("O valor das parcelas será de {:.2f} reais".format(vparcelas))
if limite < vparcelas:
    print("""O valor das parcelas excede o limite de 30% ({}) do seu salário.
          Emprestimo negado""".format(limite))
else:
    print("Emprestimo aprovado!")


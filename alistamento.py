import datetime
ano_atual = datetime.datetime.now().year
print("Seja bem vindo a consulta de alistamento!")
ano_nascimento = int(input('Digite o ano  em que nasceu:\n'))
idade = ano_atual - ano_nascimento
print(idade)
if idade < 18:
    print("Ainda não chegou a hora de se alistar!")
elif idade == 18:
    print("Chegou a hora de se alistar, por favor procure o orgão responsavel")
else: 
    print("Idade superior ao alistamento.")        

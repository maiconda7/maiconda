ef Consulta_de_nome():

    nome = input("Digite seu nome" )

    if not nome:
        nome = "você"

    print(f"{nome} caso acerte ganhará um 1")



def A_B():

    A = int(input("digite um valor."))
    B = int(input("digite outro valor."))

    print(f"o primeiro valor é igual{B}. " )
    print(f"o segundo valor é igual{A}. " )

def CLT():

    salario = int(input(f"informe seu salário. "))
    aumento = int(input(f"o aumento. "))

    reajuste = salario * (aumento/100)
    novo_salario = salario + reajuste

    print(f"{novo_salario}")


while True:
    escolha = int(input("Escolha algo"))

    if escolha == 1:
        CLT()

    elif escolha == 2:
        Consulta_de_nome()

    elif escolha == 3:
        A_B()

    else:
        print("vai se ")
        break

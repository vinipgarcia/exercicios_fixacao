# colocando os descontos dentro de uma função #
def calcular_custo(paginas, servico):
    custo_por_pagina = 0

    if servico == "DIG":
        custo_por_pagina = 1.10
    elif servico == "ICO":
        custo_por_pagina = 1.00
    elif servico == "IBO":
        custo_por_pagina = 0.40
    elif servico == "FOT":
        custo_por_pagina = 0.20

    if paginas < 20:
        return paginas * custo_por_pagina
    elif 20 <= paginas < 200:
        return paginas * custo_por_pagina * 0.85  # Aplica desconto de 15%
    elif 200 <= paginas < 2000:
        return paginas * custo_por_pagina * 0.80  # Aplica desconto de 20%
    elif 2000 <= paginas < 20000:
        return paginas * custo_por_pagina * 0.75  # Aplica desconto de 25%
    else:
        print("Não aceitamos pedidos com mais de 20.000 páginas.")
        return None

# Mensagem de boas vindas ao usuário #

print("Bem vindo ao COPY do Vinicius Paulo Garcia")

def escolha_servico():
    while True:
        print("Entre com o tipo de serviço desejado")
        print("DIG - Digitalização")
        print("ICO - Impressão Colorida")
        print("IBO - Impressão Preto e Branco")
        print("FOT - Fotocópia")
        entrada = input("Digite aqui >> ").upper()
        if entrada in ["DIG", "ICO", "IBO", "FOT"]:
            return entrada
        else:
            print("Serviço incorreto.")
            print("Entre com o tipo de serviço desejado novamente.")

def numero_paginas():
    while True:
        try:
            paginas = int(input("Entre com o número de páginas desejada: "))
            if paginas <= 0:
                print("Por favor, insira um número de páginas maior que zero.")
            elif paginas >= 20000:
                print("Não aceitamos pedidos com mais de 20.000 páginas.")
            else:
                return paginas
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

def servico_adicional():
    print("Deseja adicionar mais algum serviço?")
    print("1 - Encadernação simples: R$ 10,00")
    print("2 - Encadernação capa dura: R$ 25,00")
    print("0 - Não desejo mais nada")
    entrada_adicional = int(input("Digite aqui >> "))
    return entrada_adicional

# Solicitação de serviço
servico = escolha_servico()

# Solicitação de número de páginas
paginas = numero_paginas()

# Cálculo do custo
custo_total = calcular_custo(paginas, servico)

# Serviço adicional
extra = servico_adicional()
if extra == 1:
    custo_total += 10
elif extra == 2:
    custo_total += 25

# Exibição do serviço, número de páginas, serviço adicional e custo total
print("Serviço escolhido:", servico)
print("Número de páginas:", paginas)
print("Serviço adicional:", extra)
print("Custo total: R$", custo_total)

# Professor não consegui colocar da forma que o professor colocou o total, fiz meu máximo com o material disponibilizado



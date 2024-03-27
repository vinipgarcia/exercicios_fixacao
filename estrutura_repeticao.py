#iniciando o código com a impressão para o usuário#
print("   Bem vindo ao Açai do Vinicius Paulo Garcia   ")
print("--------------------CARDÁPIO--------------------")
print("-----| TAMANHO | CUPUAÇU (CP) | AÇAI (AC) |-----")
print("-----|    P    |   R$ 10,00   |  R$ 12,00 |-----")
print("-----|    M    |   R$ 15,00   |  R$ 17,00 |-----")
print("-----|    G    |   R$ 19,00   |  R$ 21,00 |-----")

#inserindo o input#
total = 0
while True:
    entrada = input("Escolha o Sabor Desejado (CP/AC): ")
    if (entrada != "cp" and entrada != "ac"):
        print("Sabor inválido. Tente novamente!")
        continue
    tamanho = input("Entre com o tamanho desejado: ")
    if (tamanho != "p" and tamanho != "m" and tamanho != "g"):
        print("Tamanho inválido. Tente novamente!")
        continue
    if(entrada == "cp" and tamanho == "p"):
        print("Você pediu CUPUAÇU no tamanho P: R$ 10,00")
        #Adiciona valor ao total#
        total += 10
    elif (entrada == "cp" and tamanho == "m"):
        print("Você pediu CUPUAÇU no tamanho M: R$ 15,00")
        total += 15
    elif (entrada == "cp" and tamanho == "g"):
        print("Você pediu CUPUAÇU no tamanho G: R$ 19,00")
        total += 19
    elif (entrada == "ac" and tamanho == "p"):
        print("Você pediu AÇAI no tamanho P: R$ 12,00")
        total += 12
    elif (entrada == "ac" and tamanho == "m"):
        print("Você pediu AÇAI no tamanho M: R$ 17,00")
        total += 17
    elif (entrada == "ac" and tamanho == "g"):
        print("Você pediu AÇAI no tamanho G: R$ 21,00")
        total += 21
    adicional = input("Você deseja adicionar alguma coisa (s/digite outra tecla): " )
    if(adicional == "n"):
        break

print("Total a pagar: R$", format(total, '.2f'))






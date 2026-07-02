# questao 3

def calcula_consumo(potencia, horas):
    consumo = (potencia * horas * 30) / 1000
    return consumo


def calcula_total(lista_aparelhos):
    total = 0
    for item in lista_aparelhos:
        c = calcula_consumo(item[1], item[2])
        total = total + c
    return total


def calcula_custo(total_kwh, tarifa):
    custo = total_kwh * tarifa
    return custo


def maior_consumo(lista_aparelhos):
    nome_maior = ""
    valor_maior = 0

    for item in lista_aparelhos:
        c = calcula_consumo(item[1], item[2])
        if c > valor_maior:
            valor_maior = c
            nome_maior = item[0]

    return nome_maior


def classifica_consumo(total_kwh):
    if total_kwh <= 150:
        classe = "BAIXO CONSUMO"
    elif total_kwh <= 300:
        classe = "CONSUMO MODERADO"
    else:
        classe = "ALTO CONSUMO"
    return classe


def mostra_recomendacao(nome_aparelho):
    if nome_aparelho == "Ar-condicionado":
        print("Recomendação: Verifique a temperatura configurada e mantenha filtros limpos.")
    elif nome_aparelho == "Chuveiro":
        print("Recomendação: Reduza o tempo de banho e utilize a posição verão quando possível.")
    elif nome_aparelho == "Geladeira":
        print("Recomendação: Verifique a vedação da borracha e evite abrir a porta sem necessidade.")
    elif nome_aparelho == "Televisão":
        print("Recomendação: Evite deixar a TV ligada sem uso e ajuste o brilho da tela.")
    else:
        print("Recomendação: Evite manter o aparelho ligado sem necessidade.")



aparelhos = []

tarifa_kwh = 1.05

qtd = int(input("Quantos aparelhos deseja cadastrar? "))

for i in range(qtd):
    print("Aparelho", i+1)
    nome = input("Nome do aparelho: ")
    potencia = float(input("Potência (watts): "))
    horas = float(input("Horas de uso por dia: "))

    aparelho = (nome, potencia, horas)
    aparelhos.append(aparelho)

print()
print("===== RELATÓRIO DE CONSUMO =====")
print()

for item in aparelhos:
    consumo_item = calcula_consumo(item[1], item[2])
    print("%s: %.2f kWh" % (item[0], consumo_item))

total_kwh = calcula_total(aparelhos)
custo = calcula_custo(total_kwh, tarifa_kwh)
classe = classifica_consumo(total_kwh)
maior = maior_consumo(aparelhos)

print()
print("Consumo total: %.2f kWh" % total_kwh)
print("Custo estimado: R$ %.2f" % custo)
print("Classificação: %s" % classe)
print()
print("Aparelho de maior consumo:", maior)
mostra_recomendacao(maior)
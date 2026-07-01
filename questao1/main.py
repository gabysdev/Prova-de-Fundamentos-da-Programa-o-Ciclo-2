# questao01 lista de mercado

def calcula_total(lista_compras):
    total = 0
    for item in lista_compras:
        total = total + item[2]
    return total


def calcula_fruver(lista_compras):
    total_fv = 0
    for item in lista_compras:
        if item[1] == "fruta" or item[1] == "verdura":
            total_fv = total_fv + item[2]
    return total_fv


def calcula_desconto(idade, fidelidade, total_fv):
    desc = 0

    if idade > 60:
        desc = desc + 10

    if fidelidade == True:
        desc = desc + 5

    if total_fv > 30:
        desc = desc + 5

    if desc > 20:
        desc = 20

    return desc


def mostra_resumo(total, total_fv, desc):
    valor_final = total - (total * desc / 100)
    print("===== RESUMO DA COMPRA =====")
    print("Valor original: R$ %.2f" % total)
    print("Valor de frutas e verduras: R$ %.2f" % total_fv)
    print("Desconto aplicado: %d%%" % desc)
    print("Valor final: R$ %.2f" % valor_final)


compras = []

qtd = int(input("Quantos produtos o cliente vai comprar? "))

for i in range(qtd):
    print("Produto", i+1)
    nome = input("Nome do produto: ")
    categoria = input("Categoria (fruta, verdura, mercado, limpeza): ")
    valor = float(input("Valor do produto: R$ "))

    produto = (nome, categoria, valor)
    compras.append(produto)

resp_fid = input("Cliente é fidelidade? (s/n): ")

if resp_fid == "s" or resp_fid == "S":
    cliente_fidelidade = True
else:
    cliente_fidelidade = False

idade_cliente = int(input("Idade do cliente: "))

total = calcula_total(compras)
total_fv = calcula_fruver(compras)
desconto = calcula_desconto(idade_cliente, cliente_fidelidade, total_fv)

mostra_resumo(total, total_fv, desconto)
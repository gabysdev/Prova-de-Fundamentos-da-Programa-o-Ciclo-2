# Hackathon-fundamentos-grupo-4/

GRUPO 4

Nome dos integrantes:
Carlos Constantino
Denis Torres
Gabrielle Pinheiro
Viviane Norberto

Descrição resumida das questões:
Questão 1 — Sistema de descontos da feira comunitária

Uma feira comunitária deseja incentivar clientes a comprarem alimentos frescos. O sistema deverá receber uma lista de compras e calcular o desconto de acordo com o perfil do cliente.

Cada compra será representada por uma tupla no formato:

(nome_produto, categoria, valor)

Exemplo:

compras = [

    ("Banana", "fruta", 8.50),

    ("Arroz", "mercado", 25.00),

    ("Tomate", "verdura", 12.00),

    ("Sabão", "limpeza", 18.00)

]

O sistema deverá receber também as informações do cliente:

cliente_fidelidade = True

idade_cliente = 67

Regras de desconto

    Clientes com mais de 60 anos recebem 10% de desconto no valor total.
    Clientes fidelidade recebem 5% de desconto no valor total.
    Caso o cliente seja fidelidade e tenha mais de 60 anos, os descontos podem ser acumulados.
    Caso o valor total de frutas e verduras ultrapasse R$ 30,00, o cliente recebe mais 5% de desconto.
    O desconto total não pode ultrapassar 20%.

Sua equipe deverá desenvolver

    Uma função para calcular o valor total das compras.
    Uma função para calcular o valor gasto apenas em frutas e verduras.
    Uma função para calcular o percentual total de desconto.
    Uma função para exibir o resumo final da compra.
    Uso obrigatório de:

        lista;
        tupla;
        estrutura de repetição;
        estrutura condicional;
        funções.

Saída esperada

===== RESUMO DA COMPRA =====

Valor original: R$ 63.50

Valor de frutas e verduras: R$ 20.50

Desconto aplicado: 15%

Valor final: R$ 53.98

Instrução para executar os programas:

Divisão de responsabilidades:

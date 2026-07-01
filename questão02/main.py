# Lista que armazenará as vagas
vagas = []

def cadastrar_vagas():
    quantidade = int(input("Digite a quantidade de vagas: "))

    for i in range(quantidade):
        print(f"\nCadastro da vaga {i + 1}")

        numero = int(input("Número da vaga: "))
        tipo = input("Tipo da vaga (comum/idoso/pcd): ").lower()

        resposta = input("A vaga está ocupada? (s/n): ").lower()

        if resposta == "s":
            ocupada = True
        else:
            ocupada = False

        vagas.append((numero, tipo, ocupada))

def mostrar_relatorio():
    total = len(vagas)
    ocupadas = 0
    livres = 0

    comum = 0
    idoso = 0
    pcd = 0

    for vaga in vagas:
        if vaga[2]:
            ocupadas += 1
        else:
            livres += 1

            if vaga[1] == "comum":
                comum += 1
            elif vaga[1] == "idoso":
                idoso += 1
            elif vaga[1] == "pcd":
                pcd += 1

    print("\n===== ESTACIONAMENTO SHOPPING CENTRAL =====")
    print("Total de vagas:", total)
    print("Vagas ocupadas:", ocupadas)
    print("Vagas livres:", livres)
    print("Vagas comuns livres:", comum)
    print("Vagas para idosos livres:", idoso)
    print("Vagas PCD livres:", pcd)

    print("Status do estacionamento:", verificar_status(livres))

def verificar_status(livres):
    if livres == 0:
        return "LOTADO"
    elif livres <= 2:
        return "QUASE LOTADO"
    else:
        return "DISPONÍVEL"


def buscar_vaga():
    numero = int(input("\nDigite o número da vaga: "))

    for vaga in vagas:
        if vaga[0] == numero:
            if vaga[2]:
                situacao = "ocupada"
            else:
                situacao = "livre"

            print(f"A vaga {vaga[0]} é destinada a {vaga[1]} e está {situacao}.")
            return

    print("Vaga não encontrada.")

cadastrar_vagas()
mostrar_relatorio()
buscar_vaga()
# Lista de pacientes (tuplas)
pacientes = [
    ("Ana", 29, 37.2, False),
    ("Carlos", 68, 38.5, True),
    ("Mariana", 42, 39.1, False),
    ("João", 15, 36.7, False)
]

def classificar_prioridade(paciente):
    nome, idade, temperatura, doenca_cronica = paciente

    if (temperatura >= 39) or \
       (idade >= 60 and temperatura >= 38) or \
       (doenca_cronica and temperatura >= 38):
        return "alta"

    elif (37.8 <= temperatura <= 38.9) or (idade < 12 or idade > 60):
        return "média"

    else:
        return "baixa"

alta = []
media = []
baixa = []

print("===== TRIAGEM DE PACIENTES =====\n")

for paciente in pacientes:
    nome = paciente[0]
    prioridade = classificar_prioridade(paciente)

    print(f"{nome} - Prioridade {prioridade}")

    if prioridade == "alta":
        alta.append(paciente)
    elif prioridade == "média":
        media.append(paciente)
    else:
        baixa.append(paciente)

def contar(lista):
    return len(lista)

print("\nResumo:\n")
print(f"Prioridade alta: {contar(alta)} pacientes")
print(f"Prioridade média: {contar(media)} pacientes")
print(f"Prioridade baixa: {contar(baixa)} pacientes")

if len(alta) > 0:
    proximo = "PRIORIDADE ALTA"
elif len(media) > 0:
    proximo = "PRIORIDADE MÉDIA"
else:
    proximo = "PRIORIDADE BAIXA"

print(f"\nO próximo grupo a ser atendido é: {proximo}")
# Atividade 03 - Classificacao de disciplinas do mestrado e aproveitamento para o doutorado (paradigma funcional).

def ler_notas(quantidade):
    notas = []
    for i in range(quantidade):
        nota = float(input("  Nota " + str(i + 1) + ": "))
        notas.append(nota)
    return notas


def calcular_media(notas):
    soma = 0.0
    for nota in notas:
        soma = soma + nota
    return soma / len(notas)


def gerar_classificacao(media):
    if media >= 9.5:
        return "A"b
    elif media >= 8.0:
        return "B"
    elif media >= 7.5:
        return "C"
    elif media >= 6.0:
        return "D"
    else:
        return "E"


def gerar_classificacoes(medias):
    classificacoes = []
    for media in medias:
        classificacoes.append(gerar_classificacao(media))
    return classificacoes


def gerar_aproveitamento(classificacao):
    if classificacao == "A" or classificacao == "B":
        return "Aproveita"
    else:
        return "Nao aproveita"


def gerar_aproveitamentos(classificacoes):
    aproveitamentos = []
    for classificacao in classificacoes:
        aproveitamentos.append(gerar_aproveitamento(classificacao))
    return aproveitamentos


# --- programa principal ---

print("=== CLASSIFICACAO DE DISCIPLINAS DO MESTRADO ===\n")

disciplinas = []
medias = []

quantidade_disciplinas = int(input("Quantidade de disciplinas: "))

for i in range(quantidade_disciplinas):
    print("\n--- Disciplina " + str(i + 1) + " ---")
    nome = input("Nome da disciplina: ")
    quantidade_notas = int(input("Quantidade de notas: "))
    notas = ler_notas(quantidade_notas)

    disciplinas.append(nome)
    medias.append(calcular_media(notas))

classificacoes = gerar_classificacoes(medias)
aproveitamentos = gerar_aproveitamentos(classificacoes)

print("\n=== RESULTADO ===\n")

for i in range(quantidade_disciplinas):
    print("Disciplina: " + disciplinas[i])
    print("Media: %.2f" % medias[i])
    print("Classificacao: " + classificacoes[i])
    print("Doutorado: " + aproveitamentos[i])
    print("")

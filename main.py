lista_de_espera = []
processos = []
concluidos = []
ordem = []

p1 = {
    "nome":"P1",
    "chegada":0,
    "execucao":5,
    "inicio":-1,
    "final":0
}
p2 = {
    "nome":"P2",
    "chegada":1,
    "execucao":3,
    "inicio":-1,
    "final":0
}
p3 = {
    "nome":"P3",
    "chegada":2,
    "execucao":6,
    "inicio":-1,
    "final":0
}

lista_de_espera.append(p1)
lista_de_espera.append(p2)
lista_de_espera.append(p3)

tempo = 0

while tempo < 2000:
    for p in lista_de_espera:
        if p["chegada"] == tempo:
            processos.append(p)
            lista_de_espera.remove(p)
    primeiro = processos[0]
    if primeiro["inicio"] == -1:
        primeiro["inicio"] = tempo

    if tempo % 2 == 0:
        ordem.append(primeiro["nome"])
        if primeiro["execucao"] > 2:
            primeiro["execucao"] -= 2
            processos.append(primeiro)
            processos.pop(0)
        elif primeiro["execucao"] <= 2:
            primeiro["execucao"] -= 2
            primeiro["final"] = tempo + primeiro["execucao"]
            concluidos.append(primeiro)
            processos.pop(0)

    tempo += 1

print(*ordem)
tempo_total = 0
for p in concluidos:
    print("tempo de resposta:" + str(p["inicio"] - p["chegada"]))
    tempo_total += p["inicio"] - p["chegada"]
print("tempo de resposta medio: " + str(tempo_total / len(concluidos)))

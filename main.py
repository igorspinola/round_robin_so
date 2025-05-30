lista_de_espera = []
processos = []
concluidos = []
ordem = []

p1 = {"nome": "P1", "chegada": 0, "execucao": 5, "inicio": -1, "final": 0}
p2 = {"nome": "P2", "chegada": 1, "execucao": 3, "inicio": -1, "final": 0}
p3 = {"nome": "P3", "chegada": 2, "execucao": 6, "inicio": -1, "final": 0}

lista_de_espera.extend([p1, p2, p3])
numero_processos = len(lista_de_espera)
tempo = 0
quantum = 2

while len(concluidos) != numero_processos:
    for p in lista_de_espera[:]:
        if p["chegada"] <= tempo:
            processos.append(p)
            lista_de_espera.remove(p)

    if len(processos) == 0:
        tempo += 1
        continue

    primeiro = processos.pop(0)
    if primeiro["inicio"] == -1:
        primeiro["inicio"] = tempo

    ordem.append(primeiro["nome"])

    if primeiro["execucao"] > quantum:
        primeiro["execucao"] -= quantum
        tempo += quantum
        for p in lista_de_espera[:]:
            if p["chegada"] <= tempo:
                processos.append(p)
                lista_de_espera.remove(p)
        processos.append(primeiro)
    else:
        tempo += primeiro["execucao"]
        primeiro["final"] = tempo
        primeiro["execucao"] = 0
        concluidos.append(primeiro)

print("Ordem de execução:", *ordem)

tempo_total_resposta = 0
tempo_total_espera = 0
tempo_total_processo = 0

for p in concluidos:
    resposta = p["inicio"] - p["chegada"]
    tempo_total = p["final"] - p["chegada"]
    espera = tempo_total - (p["final"] - p["inicio"])

    print(f"{p['nome']}:")
    print(f"  Tempo de resposta: {resposta}")
    print(f"  Tempo de espera: {espera}")
    print(f"  Tempo total do processo: {tempo_total}")

    tempo_total_resposta += resposta
    tempo_total_espera += espera
    tempo_total_processo += tempo_total

n = len(concluidos)
print("\nMédias:")
print("Tempo de resposta médio:", tempo_total_resposta / n)
print("Tempo de espera médio:", tempo_total_espera / n)
print("Tempo total médio dos processos:", tempo_total_processo / n)

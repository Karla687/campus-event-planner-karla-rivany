from datetime import datetime

listaEventos = []

def displayMenu(): 
    print("=== Planejador de Eventos do Campus ===")
    print("1. Adicionar Evento")    
    print("2. Ver Todos os Eventos")
    print("3. Filtrar por Categoria")
    print("4. Marcar Evento como Participado")
    print("5. Gerar Relatório")
    print("6. Sair")

def getEscolhaDoUsuario():
    while (True):
        escolha = input()
        if (1 <= escolha <= 6):
            break
        else:
            print("Alternativa inválida")
            displayMenu()
    return escolha

def validarData(dataStr):
    try:
        datetime.strptime(dataStr, "%Y-%m-%d")
        return True
    except (ValueError, TypeError):
        return False


def adicionarEvento(listaEventos, nome, data, local, categoria):
    if not nome.strip():
        return False

    if not validarData(data):
        return False

    if not local.strip():
        return False

    if not categoria.strip():
        return False

    evento = {
        "id": len(listaEventos) + 1,
        "nome": nome,
        "data": data,
        "local": local,
        "categoria": categoria
    }

    listaEventos.append(evento)

    return True




adicionarEvento(
    listaEventos,
    "Workshop de Python",
    "2026-09-15",
    "Laboratorio 1",
    "Tecnologia"
)


def listarEventos(listaEventos):
    return listaEventos

print(listarEventos(listaEventos))

def procurarEventoPorNome(listaEventos, nome):
    resultados = []

    for evento in listaEventos:
        if nome.lower() in evento["nome"].lower():
            resultados.append(evento)

    return resultados

def filtrarEventosPorCategoria(listaEventos, categoria):
    resultados = []
    for evento in listaEventos:
        if categoria.lower() in evento["categoria"].lower():
            resultados.append(evento)

    return resultados

print(procurarEventoPorNome(listaEventos, "Python"))

def deletarEvento(listaEventos, id):
    for evento in listaEventos:
        if evento["id"] == id:
            listaEventos.remove(evento)
            return True

    return False

print(deletarEvento(listaEventos, 1))
print(listaEventos)

def gerarRelatorio(listaEventos):
    print("\n--- RELATÓRIO DE EVENTOS ---")

    # Total de eventos
    totalEventos = len(listaEventos)
    print(f"Total de Eventos: {totalEventos}")

    # Quantidade de eventos por categoria
    categorias = {}

    for evento in listaEventos:
        categoria = evento["categoria"]

        if categoria in categorias:
            categorias[categoria] += 1
        else:
            categorias[categoria] = 1

    print(f"Por Categoria: {categorias}")

    # Quantidade de eventos participados
    participados = 0

    for evento in listaEventos:
        if evento["participado"] == True:
            participados += 1

    # Porcentagem de participação
    if totalEventos > 0:
        porcentagem = (participados / totalEventos) * 100
    else:
        porcentagem = 0

    print(f"Participados: {porcentagem:.0f}% ({participados}/{totalEventos})")

def marcarEventoAtendido(listaEventos, id):
    for evento in listaEventos:
        if evento["id"] == id:
            evento["participado"] = True
            return True

    return False
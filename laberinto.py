#Las coordenadas estan dadas por: (fila,columna)
laberinto = [
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['P', 'P', 'C', 'C', 'C', 'C', 'C', 'P'],
    ['P', 'P', 'C', 'P', 'P', 'P', 'C', 'P'],
    ['P', 'P', 'C', 'C', 'C', 'P', 'C', 'P'],
    ['P', 'P', 'P', 'P', 'C', 'P', 'C', 'S'],
    ['P', 'P', 'C', 'P', 'C', 'P', 'P', 'P'],
    ['P', 'C', 'C', 'C', 'C', 'C', 'P', 'P'],
    ['P', 'P', 'C', 'P', 'P', 'P', 'P', 'P'],
    ['P', 'P', 'E', 'P', 'P', 'P', 'P', 'P']
]

movimientos = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def es_valido(x, y, visitado):
    return (0 <= x < len(laberinto) and 0 <= y < len(laberinto[0]) and
            laberinto[x][y] != 'P' and not visitado[x][y])

def buscar_salida(inicio):
    pila = [inicio]  
    visitado = [[False] * len(laberinto[0]) for _ in range(len(laberinto))]
    visitado[inicio[0]][inicio[1]] = True
    
    while pila:
        x, y = pila[-1]  
        if laberinto[x][y] == 'S':
            return list(pila)  

        movido = False
        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            if es_valido(nx, ny, visitado):
                pila.append((nx, ny))
                visitado[nx][ny] = True
                movido = True
                break

        if not movido:
            pila.pop()  

    return []  

for i in range(len(laberinto)):
    for j in range(len(laberinto[i])):
        if laberinto[i][j] == 'E':
            camino = buscar_salida((i, j))
            if camino:
                print("Camino a la salida encontrado:", camino)
            else:
                print("No hay camino a la salida.")
            break

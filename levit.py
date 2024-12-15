from collections import deque

def levit_shortest_path(graph, start):
    # Количество вершин в графе
    n = len(graph)

    # Инициализация расстояний и очередей
    distances = [float('inf')] * n
    distances[start] = 0

    # Очереди: m1 — текущие, m2 — для уточнения
    m0, m1, m2 = set(range(n)), deque([start]), set()

    while m1:
        current = m1.popleft()  # Извлекаем вершину из m1
        m0.discard(current)

        # Обрабатываем всех соседей текущей вершины
        for neighbor, weight in graph[current]:
            if neighbor in m0:
                # Если сосед не посещен, обновляем расстояние и добавляем в m1
                distances[neighbor] = distances[current] + weight
                m0.remove(neighbor)
                m1.append(neighbor)
            elif neighbor in m1 or neighbor in m2:
                # Если сосед уже в m1 или m2, проверяем и обновляем расстояние
                if distances[neighbor] > distances[current] + weight:
                    distances[neighbor] = distances[current] + weight
                    if neighbor in m2:
                        m2.remove(neighbor)
                        m1.append(neighbor)

        # Добавляем обработанную вершину в m2
        m2.add(current)

    return distances

# Пример использования
graph= {
    0: [(1, 1)],
    1: [(2, 2)],
    2: [],
    3: [(4, 3)],
    4: []
}

start_vertex = 0
result = levit_shortest_path(graph, start_vertex)
print("Кратчайшие расстояния от вершины {}:".format(start_vertex))
print(result)

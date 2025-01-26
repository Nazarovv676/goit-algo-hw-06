import networkx as nx

# Використовуємо граф із попереднього завдання
city_transport = nx.Graph()

# Вузли (станції)
stations = [
    "Station A", "Station B", "Station C", "Station D",
    "Station E", "Station F", "Station G", "Station H"
]
city_transport.add_nodes_from(stations)

# Ребра (з'єднання) з вагами (наприклад, час у хвилинах між станціями)
connections_with_weights = [
    ("Station A", "Station B", 4),
    ("Station B", "Station C", 2),
    ("Station C", "Station D", 3),
    ("Station D", "Station E", 6),
    ("Station E", "Station F", 5),
    ("Station F", "Station G", 2),
    ("Station G", "Station H", 4),
    ("Station A", "Station C", 5),
    ("Station D", "Station F", 3),
]
city_transport.add_weighted_edges_from(connections_with_weights)

# Алгоритм Дейкстри для пошуку найкоротших шляхів
def dijkstra(graph, start):
    shortest_paths = {node: float('inf') for node in graph.nodes}  # Початкові відстані
    shortest_paths[start] = 0
    previous_nodes = {node: None for node in graph.nodes}
    unvisited_nodes = set(graph.nodes)
    
    while unvisited_nodes:
        # Вибір вузла з найменшою відстанню
        current_node = min(
            unvisited_nodes, key=lambda node: shortest_paths[node]
        )
        unvisited_nodes.remove(current_node)

        # Оновлення відстаней до сусідів
        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            new_distance = shortest_paths[current_node] + weight
            if new_distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = new_distance
                previous_nodes[neighbor] = current_node

    return shortest_paths, previous_nodes

# Функція для отримання найкоротшого шляху
def get_path(previous_nodes, start, target):
    path = []
    current = target
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
    path.reverse()
    return path

# Знаходимо найкоротші шляхи з кожної вершини
for start_station in stations:
    shortest_paths, previous_nodes = dijkstra(city_transport, start_station)
    print(f"\nНайкоротші шляхи з {start_station}:")
    for target_station in stations:
        if start_station != target_station:
            path = get_path(previous_nodes, start_station, target_station)
            print(f"  До {target_station}: Шлях {path}, Відстань {shortest_paths[target_station]}")
            
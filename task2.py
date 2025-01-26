import networkx as nx

# Використовуємо граф із попереднього завдання
city_transport = nx.Graph()

# Вузли (станції)
stations = [
    "Station A", "Station B", "Station C", "Station D",
    "Station E", "Station F", "Station G", "Station H"
]
city_transport.add_nodes_from(stations)

# Ребра (з'єднання)
connections = [
    ("Station A", "Station B"),
    ("Station B", "Station C"),
    ("Station C", "Station D"),
    ("Station D", "Station E"),
    ("Station E", "Station F"),
    ("Station F", "Station G"),
    ("Station G", "Station H"),
    ("Station A", "Station C"),
    ("Station D", "Station F"),
]
city_transport.add_edges_from(connections)

# Алгоритм DFS
def dfs(graph, start, goal, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()
    
    path.append(start)
    visited.add(start)
    
    if start == goal:
        return path
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, path.copy(), visited)
            if result:
                return result
    return None

# Алгоритм BFS
def bfs(graph, start, goal):
    queue = [(start, [start])]
    visited = set()
    
    while queue:
        current, path = queue.pop(0)
        if current == goal:
            return path
        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return None

# Вхідні дані для пошуку
start_station = "Station A"
goal_station = "Station H"

# Пошук за допомогою DFS
dfs_path = dfs(city_transport, start_station, goal_station)
print(f"Шлях DFS від {start_station} до {goal_station}: {dfs_path}")

# Пошук за допомогою BFS
bfs_path = bfs(city_transport, start_station, goal_station)
print(f"Шлях BFS від {start_station} до {goal_station}: {bfs_path}")

# Порівняння шляхів
print("\nПорівняння:")
print(f"DFS шлях: {dfs_path}")
print(f"BFS шлях: {bfs_path}")

# Порівняння:
# DFS шлях: ['Station A', 'Station B', 'Station C', 'Station D', 'Station E', 'Station F', 'Station G', 'Station H']
# BFS шлях: ['Station A', 'Station C', 'Station D', 'Station F', 'Station G', 'Station H']
# Чому шляхи відрізняються?
# DFS фокусується на глибині і може обрати довші маршрути через сусідні вершини.
# BFS обчислює всі можливі шляхи на певному рівні, тому завжди повертає найкоротший шлях за кількістю ребер.

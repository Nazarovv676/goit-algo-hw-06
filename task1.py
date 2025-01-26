import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
city_transport = nx.Graph()

# Додавання вузлів (станцій)
stations = [
    "Station A", "Station B", "Station C", "Station D",
    "Station E", "Station F", "Station G", "Station H"
]
city_transport.add_nodes_from(stations)

# Додавання ребер (з'єднань між станціями)
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

# Візуалізація графа
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(city_transport)  # Розташування вузлів
nx.draw(
    city_transport,
    pos,
    with_labels=True,
    node_size=700,
    node_color="skyblue",
    edge_color="gray",
    font_size=10,
    font_color="black"
)
plt.title("City Transport Network", fontsize=16)
plt.show()

# Аналіз основних характеристик
print("Основні характеристики графа:")
print(f"Кількість вершин (станцій): {city_transport.number_of_nodes()}")
print(f"Кількість ребер (з'єднань): {city_transport.number_of_edges()}")

# Ступінь вершин
print("\nСтупінь кожної вершини (кількість з'єднань):")
for station, degree in city_transport.degree():
    print(f"{station}: {degree}")

# Середній ступінь вершин
avg_degree = sum(dict(city_transport.degree()).values()) / city_transport.number_of_nodes()
print(f"\nСередній ступінь вершин: {avg_degree:.2f}")
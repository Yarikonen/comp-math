from collections import defaultdict

def dfs(v, graph, visited, stack):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor, graph, visited, stack)
    stack.append(v)

def transpose(graph):
    transposed_graph = defaultdict(list)
    for v, neighbors in graph.items():
        for neighbor in neighbors:
            transposed_graph[neighbor].append(v)
    return transposed_graph

def get_strongly_connected_components(graph, reversed_graph, n):
    visited = [False] * n
    stack = []
    for v in range(n):
        if not visited[v]:
            dfs(v, graph, visited, stack)
    visited = [False] * n
    components = []
    while stack:
        v = stack.pop()
        if not visited[v]:
            component = []
            dfs(v, reversed_graph, visited, component)
            components.append(component)
    return components

def check_feasibility(mid, fuel_costs):
    n = len(fuel_costs)
    graph = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if fuel_costs[i][j] <= mid:
                graph[i].append(j)
    reversed_graph = transpose(graph)
    components = get_strongly_connected_components(graph, reversed_graph, n)
    return len(components) == 1

def find_optimal_fuel_tank_size(fuel_costs):
    n = len(fuel_costs)
    left = 0
    right = 10**9
    while left <= right:
        mid = (left + right) // 2
        if check_feasibility(mid, fuel_costs):
            right = mid - 1
        else:
            left = mid + 1
    return left

# Чтение входных данных
n = int(input())
fuel_costs = []
for _ in range(n):
    row = list(map(int, input().split()))
    fuel_costs.append(row)

# Вычисление оптимального размера бака
optimal_size = find_optimal_fuel_tank_size(fuel_costs)

# Вывод результата
print(optimal_size)

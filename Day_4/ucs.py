import heapq

def uniform_cost_search(graph, start, goal):
    # Priority queue (cost, node, path)
    pq = [(0, start, [start])]
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node == goal:
            return path, cost

        if node not in visited:
            visited.add(node)
            for neighbor, edge_cost in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(pq, (cost + edge_cost, neighbor, path + [neighbor]))

    return None, float("inf")

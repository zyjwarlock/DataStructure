import heapq
import math

def init_distance(graph, s):
    distance = {s: 0}
    for node in graph:
        if node != s:
            distance[node] = math.inf
    return distance


def dijkstra(graph, s):
    pqueue = []
    heapq.heappush(pqueue, (0, s))
    seen = set()
    node_from = {s: None}
    distance = init_distance(graph, s)

    while pqueue:

        pair = heapq.heappop(pqueue)
        dist = pair[0]
        vert = pair[1]

        if vert in seen: continue

        nodes = graph[vert].keys()

        for node in nodes:
            if node not in seen:
                curr_dist = dist + graph[vert][node]
                if dist + graph[vert][node] < distance[node]:
                    heapq.heappush(pqueue, (curr_dist, node))
                    node_from[node] = vert
                    distance[node] = curr_dist

        seen.add(vert)

    return node_from, distance


def main():

    graph = {
        "A": {"B": 5, "C": 1},
        "B": {"A": 5, "C": 2, "D": 1},
        "C": {"A": 1, "B": 2, "D": 4, "E":8},
        "D": {"B": 1, "C": 4, "E": 3, "F": 6},
        "E": {"C": 8, "D": 3},
        "F": {"D": 6}

    }

    path, distance = dijkstra(graph, "A")

    print(path)
    print(distance)

if __name__=="__main__":
    main()

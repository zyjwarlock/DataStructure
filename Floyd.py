import math

def Floyd(graph, path):

    tmp = [[math.inf for i in range(len(graph))] for j in range(len(graph))]

    for key in graph:
        i = ord(key.lower()) - 97
        tmp[i][i] = 0
        for value in graph[key].keys():
            j = ord(value.lower()) - 97
            tmp[i][j] = graph[key][value]


    for key in graph:
        k = ord(key.lower()) - 97
        for i in range(len(tmp)):
            for j in range(len(tmp[i])):
                if k==i or k==j or i==j: continue
                if tmp[i][j] > tmp[i][k] + tmp[k][j]:
                    tmp[i][j] = tmp[i][k] + tmp[k][j]
                    path[i][j] = k

def shortestPath(u, v, path):

    if not path[u][v]: print(chr(u+97).upper(), chr(v+97).upper())
    else:
        shortestPath(u, path[u][v], path)
        shortestPath(path[u][v], v, path)






def main():

    graph = {
        "A": {"B": 5, "D": 7},
        "B": {"C": 4, "D": 2},
        "C": {"A": 3, "B": 3, "D": 2},
        "D": {"C": 1}
    }


    path = [[None for i in range(len(graph))] for j in range(len(graph))]

    Floyd(graph, path)

    shortestPath(ord("A".lower())-97, ord("C".lower())-97, path)


if __name__=="__main__":
    main()
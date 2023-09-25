from sys import stdin
def adj_matrix_to_adj_list():
    n = int(stdin.readline())
    graph = [[] for i in range(n)]
    for i in range(n):
        line = list(map(int, stdin.readline().strip().split()))
        for j in range(len(line)):
            if line[j] == 1:
                graph[i].append(j + 1)

    for i in graph:
        print(len(i), end=" ")
        for j in i:
            print(j, end=" ")
        print()



if __name__ == "__main__":
    adj_matrix_to_adj_list()

from sys import stdin
def cities_and_roads():
    n = int(stdin.readline())
    temp = []
    for i in range(n):
        line = list(map(int, stdin.readline().strip().split()))
        for j in range(len(line)):
            if line[j] == 1 and [j,i] not in temp:
                temp.append([i,j])
    print(len(temp))


if __name__ == "__main__":
    cities_and_roads()


if __name__ == '__main__':
    N = int(input())
    lst = []
    for i in range(N):
        line = list(input().strip().split())
        command = line[0]
        if command == 'insert':
            lst.insert(int(line[1]), int(line[2]))
        elif command == 'print':
            print(lst)
        elif command == 'remove':
            if int(line[1]) in lst:
                lst.remove(int(line[1]))
        elif command == 'append':
            lst.append(int(line[1]))
        elif command == 'sort':
            lst.sort()
        elif command == 'pop':
            if lst:
                lst.pop()
        elif command == 'reverse':
            lst.reverse()
            

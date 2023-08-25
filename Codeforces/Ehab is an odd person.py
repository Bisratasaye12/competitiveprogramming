import random
from sys import stdin
import copy

n = int(stdin.readline())
elements = list(map(int, stdin.readline().strip().split()))
flag = False

f1 = False
f2 = False
for num in elements:
    if num % 2 == 0:
        f1 = True
    if num % 2 != 0:
        f2 = True
    if f1 and f2:
        break

if f1 and f2:
    elements.sort()
print(' '.join(map(str, elements)))
 

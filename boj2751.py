import collections
import sys

N = int(sys.stdin.readline().rstrip())

card = collections.deque(i for i in range(1, N + 1))

while len(card) > 1 :
    card.popleft()
    card.append(card.popleft())

print(card[0])

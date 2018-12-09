from collections import deque

max_players = 466
last_marble = 71436 # * 100 for part 2
board       = deque([0])
players     = [0 for x in range(max_players)]
player      = 0

for x in range(1, last_marble+1):
    if x % 23 == 0:
        board.rotate(7)
        players[player] += x + board.pop()
        board.rotate(-1)
    else:
        board.rotate(-1)
        board.append(x)

    player = (player + 1) % max_players

print(f"Part 1: {max(players)}")
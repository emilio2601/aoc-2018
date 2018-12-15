from collections import defaultdict
from tqdm import tqdm
import secrets
import sys

class TrackObject:
    def __init__(self, char):
        if char == ">" or char == "<":
            self.track   = "-"
            self.hasCart = True
            self.cartDir = char
            self.lastMoved = -1
            self.cartID  = secrets.token_hex(16)
        elif char == "v" or char == "^":
            self.track   = "|"
            self.hasCart = True
            self.lastMoved = -1
            self.cartDir = char
            self.cartID  = secrets.token_hex(16)
        else:
            self.track = char
            self.hasCart = False
        
        self.x = 0
        self.y = 0
    
    def set_coords(self, x, y):
        self.x = x
        self.y = y
    
    def print(self):
        if not self.hasCart:
            return self.track
        else:
            return self.cartDir
    
    def __repr__(self):
        if self.hasCart:
            return f"TrackObject at {self.x},{self.y}, track: {self.track}, hasCart: {self.hasCart}, cartDir: {self.cartDir}, cartID: {self.cartID[0:4]}, lastMoved: {self.lastMoved}"
        else:
            return f"TrackObject at {self.x},{self.y}, track: {self.track}, hasCart: {self.hasCart}"
board = []
with open("day13", "r") as f:
    for line in f:
        board.append([TrackObject(char) for char in line if char != "\n"])

def print_board(board):
    for line in board:
        print("".join([x.print() for x in line]))

def move_cart(src_to, dst_to, tick):
    global hasNotFinishedPart1

    if src_to.lastMoved == tick:
        return False

    src_to.hasCart = False
    dst_to.lastMoved = tick

    if dst_to.hasCart:
        if hasNotFinishedPart1:
            print(f"Part 1: {dst_to.y},{dst_to.x}")
        dst_to.hasCart = False
        src_to.hasCart = False
        return True

    if dst_to.track == "|" or dst_to.track == "-": #straight road
        dst_to.hasCart = True
        dst_to.cartDir = src_to.cartDir
        dst_to.cartID  = src_to.cartID
    
    if dst_to.track == "\\" or dst_to.track == "/": #change in direction
        dst_to.hasCart = True
        dst_to.cartID  = src_to.cartID

        if dst_to.track == "\\":
            if src_to.cartDir == ">":
                dst_to.cartDir = "v"
            elif src_to.cartDir == "^":
                dst_to.cartDir = "<"
            elif src_to.cartDir == "v":
                dst_to.cartDir = ">"
            elif src_to.cartDir == "<":
                dst_to.cartDir = "^"
        
        elif dst_to.track == "/":
            if src_to.cartDir == ">":
                dst_to.cartDir = "^"
            elif src_to.cartDir == "^":
                dst_to.cartDir = ">"
            elif src_to.cartDir == "v":
                dst_to.cartDir = "<"
            elif src_to.cartDir == "<":
                dst_to.cartDir = "v"
    
    if dst_to.track == "+": #intersection
        dst_to.hasCart = True
        dst_to.cartID  = src_to.cartID

        cartEvents[dst_to.cartID] += 1

        if cartEvents[dst_to.cartID] % 3 == 1: # turn left
            if src_to.cartDir == ">":
                dst_to.cartDir = "^"
            elif src_to.cartDir == "^":
                dst_to.cartDir = "<"
            elif src_to.cartDir == "v":
                dst_to.cartDir = ">"
            elif src_to.cartDir == "<":
                dst_to.cartDir = "v"
        elif cartEvents[dst_to.cartID] % 3 == 2:# straight
            dst_to.cartDir = src_to.cartDir
        elif cartEvents[dst_to.cartID] % 3 == 0: # turn right
            if src_to.cartDir == ">":
                dst_to.cartDir = "v"
            elif src_to.cartDir == "^":
                dst_to.cartDir = ">"
            elif src_to.cartDir == "v":
                dst_to.cartDir = "<"
            elif src_to.cartDir == "<":
                dst_to.cartDir = "^"
            
        
hasCrashed = False
hasNotFinishedPart1 = True
cartEvents = defaultdict(int)

for tick in range(1,10216):
    for xidx, line in enumerate(board):
        for yidx, to in enumerate(line):
            to.set_coords(xidx, yidx)
            if to.hasCart:
                if to.cartDir == ">":
                    hasCrashed = move_cart(to, board[xidx][yidx+1], tick)
                elif to.cartDir == "<":
                    hasCrashed = move_cart(to, board[xidx][yidx-1], tick)
                elif to.cartDir == "v":
                    hasCrashed = move_cart(to, board[xidx+1][yidx], tick)
                elif to.cartDir == "^":
                    hasCrashed = move_cart(to, board[xidx-1][yidx], tick)
            if hasCrashed and hasNotFinishedPart1:
                hasNotFinishedPart1 = False
    
    carts = 0
    lastLoc = 0
    for xidx, line in enumerate(board):
        for yidx, to in enumerate(line):
            if to.hasCart:
                carts += 1
                lastLoc = (yidx, xidx)

    if carts == 1:
        print(f"Part 2: {lastLoc[0]},{lastLoc[1]}")
        sys.exit()   

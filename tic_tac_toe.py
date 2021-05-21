import dis

def display(grid):
    print(f' {grid[6]} | {grid[7]} | {grid[8]}')
    print(f'------------')
    print(f' {grid[3]} | {grid[4]} | {grid[5]}')
    print(f'------------')
    print(f' {grid[0]} | {grid[1]} | {grid[2]}')
    
def check_win(loc, grid):
    r = loc // 3 * 3
    c = loc % 3
    s = grid[loc]

    row = grid[r:r + 3]
    col = grid[c::3]
    d1 = grid[0::4]
    d2 = grid[2::2]

    lines = row, col, d1, d2

    for line in lines:
        if line.count(s) == 3:
            return True
        
    return False

def get_move(symbol, grid):
    while True:
        loc = input(symbol + ' where? ')

        if loc.isnumeric():
            loc = int(loc) - 1

            if 0 <= loc <= 8 and type(grid[loc]) == int:
                return int(loc)

        print('nope')

def play():
    grid = list(range(1, 10))
    turn = over = moves = 0
    display(grid)
    
    while not over:
        symbol = 'XO'[turn]
        loc = get_move(symbol, grid)
        grid[loc] = symbol
        over = check_win(loc, grid)
        print()
        display(grid)
        moves += 1
        
        if over:
            print(symbol + ' wins')
        elif moves == 9:
            print('tie')
            over = True
        else:
            turn = (turn + 1) % 2

# Go!
print('tic tac toe\n')
playing = True

while playing:
    play()
    playing = input('again? (y/n) ') == 'y'

print('bye')

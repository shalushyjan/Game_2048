import random
def start_game():
    game_box =[]
    for i in range(4):
        game_box.append([0] * 4)
    print("Control keys : ")
    print("press key 1  : Move Left")
    print("press key 2  : Move Right")
    print("press key 3  : Move Up")
    print("press key 4  : Move Down")
    add_new_2(game_box)
    for i in range(4):
	    print(game_box[i])
    return game_box
def add_new_2(game_box):
    r = random.randint(0, 3)
    c = random.randint(0, 3)
    while(game_box[r][c] != 0):
        r = random.randint(0, 3)
        c = random.randint(0, 3)
    game_box[r][c] = 2
  
def get_current_state(game_box):
	for i in range(4):
		for j in range(4):
			if(game_box[i][j]== 2048):
				return 'WON'
	for i in range(4):
		for j in range(4):
			if(game_box[i][j]== 0):
				return 'GAME NOT OVER'
	for i in range(3):
		for j in range(3):
			if(game_box[i][j]== game_box[i + 1][j] or game_box[i][j]== game_box[i][j + 1]):
				return 'GAME NOT OVER'

	for j in range(3):
		if(game_box[3][j]== game_box[3][j + 1]):
			return 'GAME NOT OVER'

	for i in range(3):
		if(game_box[i][3]== game_box[i + 1][3]):
			return 'GAME NOT OVER'
	return 'LOST'


def compress(game_box):
	changed = False
	new_game_box = []
	for i in range(4):
		new_game_box.append([0] * 4)
	for i in range(4):
		pos = 0
		for j in range(4):
			if(game_box[i][j] != 0):
				new_game_box[i][pos] = game_box[i][j]
				
				if(j != pos):
					changed = True
				pos += 1
	return new_game_box, changed


def merge(game_box):
	
	changed = False
	
	for i in range(4):
		for j in range(3):
			if(game_box[i][j] == game_box[i][j + 1] and game_box[i][j] != 0):
				game_box[i][j] = game_box[i][j] * 2
				game_box[i][j + 1] = 0
				changed = True

	return game_box, changed
def reverse(game_box):
	new_game_box =[]
	for i in range(4):
		new_game_box.append([])
		for j in range(4):
			new_game_box[i].append(game_box[i][3 - j])
	return new_game_box


def transpose(game_box):
	new_game_box = []
	for i in range(4):
		new_game_box.append([])
		for j in range(4):
			new_game_box[i].append(game_box[j][i])
	return new_game_box
def move_left(grid):
	new_grid, changed1 = compress(grid)
	new_grid, changed2 = merge(new_grid)
	changed = changed1 or changed2
	new_grid, temp = compress(new_grid)
	return new_grid, changed
def move_right(grid):
	new_grid = reverse(grid)
	new_grid, changed = move_left(new_grid)
	new_grid = reverse(new_grid)
	return new_grid, changed
def move_up(grid):
	new_grid = transpose(grid)
	new_grid, changed = move_left(new_grid)
	new_grid = transpose(new_grid)
	return new_grid, changed

def move_down(grid):
	new_grid = transpose(grid)
	new_grid, changed = move_right(new_grid)
	new_grid = transpose(new_grid)
	return new_grid, changed

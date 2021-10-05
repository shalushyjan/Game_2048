import logic

if __name__ == '__main__':
    game_box = logic.start_game()
    print("------Welcome! 2048------ :\n ")
while(True):
    x = input('\nENTER A KEY\n')
    if(x == '3'):
	    game_box, flag = logic.move_up(game_box)
	    status = logic.get_current_state(game_box)
	    print(status)
	    if(status == 'GAME NOT OVER'):
		    logic.add_new_2(game_box)
	    else:
		    break
    elif(x == '4'):
	    game_box, flag = logic.move_down(game_box)
	    status = logic.get_current_state(game_box)
	    print(status)
	    if(status == 'GAME NOT OVER'):
		    logic.add_new_2(game_box)
	    else:
		    break
    elif(x == '1'):
	    game_box, flag = logic.move_left(game_box)
	    status = logic.get_current_state(game_box)
	    print(status)
	    if(status == 'GAME NOT OVER'):
		    logic.add_new_2(game_box)
	    else:
		    break
    elif(x == '2'):
	    game_box, flag = logic.move_right(game_box)
	    status = logic.get_current_state(game_box)
	    print(status)
	    if(status == 'GAME NOT OVER'):
		    logic.add_new_2(game_box)
	    else:
		    break
    else:
	    print("Invalid key")

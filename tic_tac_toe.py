import tkinter


"""Defining the global variables 
main_lst (List) - This list stores the player moves at a specific position ,
coord_lst (List) - This list stores the coordinates required to display an image on the window,
image1 (tkinter-Image) - This variable stores the images being imported to the program,
play_chance (str) - It holds the current player name,
score (List) - It stores the score of X and O in a list, respectively, 
players (List) - It stores the images of the players(X/O) which are imported to the program,
counter (int) - It counts the number of positions filled throughout the game. Once it is 10; the game is a draw,
canvas (tkinter-Canvas) - This is the GUI component which holds the grid lines,
msg_lbl (tkinter-Label) - This holds any messages that should be displayed on the screen,
X_chance_lbl (tkinter-Label) - This label is raised when player X has its turn,
O_chance_lbl (tkinter-Label) - This label is raised when player O has its turn,
X_score_lbl (tkinter-Label) - It displays the player X's score,
O_score_lbl (tkinter-Label) - It displays the player O's score
"""

main_lst = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
coord_lst = [45, 122, 196]
image1 = ""
play_chance = 'X'
score = [0, 0]
players = []
counter = 1
win_game = False
canvas, msg_lbl, X_chance_lbl, O_chance_lbl, X_score_lbl, O_score_lbl = " ", " ", " ", " ", " ", " "


def update_chance():
    """This function is used to update the chance of a player(X/O) and in the game.
    It also updates the player labels accordingly."""

    global play_chance, X_chance_lbl, O_chance_lbl
    if play_chance == 'X':
        play_chance = 'O'
        X_chance_lbl.configure(relief="flat")
        O_chance_lbl.configure(relief="raised")
    else:
        play_chance = 'X'
        X_chance_lbl.configure(relief="raised")
        O_chance_lbl.configure(relief="flat")


def update_main_lst(upd_pos):
    """This function is used to update the main_lst after the player has played his turn,
    it displays the player(X/O) at the position that the player has clicked.

    Parameters -
    upd_pos (int)-  It holds the recently played position number and that is updated in the
                    main_lst with the player name."""

    global main_lst, play_chance
    ret_var = False
    for pos, i in enumerate(main_lst):
        for sub_pos, j in enumerate(i):
            if j == upd_pos:
                main_lst[pos][sub_pos] = play_chance
                ret_var = True
                return ret_var

    return ret_var


def player_display(pos_val):
    """This function prints the image of the player(X/O) after clicking on a specific position.

    Parameters -
    pos_val (int) - It holds the recently played position value which is then used to
                    display the current player image on the window at that position."""

    global play_chance, coord_lst
    counter_ = 0

    for i in coord_lst:
        for j in coord_lst:
            if counter_ == pos_val:
                if play_chance == 'X':
                    return canvas.create_image(j, i, tag='X_player', image=players[0])
                else:
                    return canvas.create_image(j, i, tag='O_player', image=players[1])

            counter_ += 1


def load_images():
    """This function is used to load the images into the program."""

    global image1
    player_lst = ['X', 'O']

    for i in player_lst:
        name = "Images-tic_tac_toe/{}.png".format(i)
        image1 = tkinter.PhotoImage(file=name)
        players.append(image1)


def get_coordinates(event):
    """This function is responsible for getting the X and Y coordinates of the canvas where the click
    event has occurred.

    Parameters -
    event (tkinter-Event)- It holds the value of the event that occurs on the canvas. The event is a mouse click and
                           thus it holds X and Y coordinate values."""

    tags = canvas.itemcget("current", "tags")
    if tags != "grid_line current" and (event.x in range(14, 230) and event.y in range(14, 224)) and win_game is False:
        return True


def create_grid():
    """This function is used to create the entire grid on the canvas.
    It works by getting the current height and width of the canvas and creates lines on the canvas with
    those readings."""

    canvas.update()
    w = canvas.winfo_width()
    h = canvas.winfo_height()
    canvas.delete('grid_line')

    for i in range(0, w, 80):
        if i not in (0, 240):
            canvas.create_line([(i, 15), (i, h - 15)], tag='grid_line', width=5, fill="#089398")

    for i in range(0, h, 80):
        if i != 0:
            canvas.create_line([(15, i), (w - 15, i)], tag='grid_line', width=5, fill="#089398")


def match_decision_and_winning_lines():
    """This function is responsible for checking whether a player has won the game and if so,
    returning the coordinates of the winning lines."""

    global main_lst, coord_lst, win_game
    return_var, win_line = None, None
    i_alt = 0

    w = canvas.winfo_width()
    h = canvas.winfo_height()

    for i in range(len(main_lst)):
        if main_lst[i_alt][i] == main_lst[i_alt + 1][i] == main_lst[i_alt + 2][i]:
            return_var = main_lst[i_alt][i]
            win_line = [(coord_lst[i], 22), (coord_lst[i], h - 22)]
            win_game = True

        elif main_lst[i][i_alt] == main_lst[i][i_alt + 1] == main_lst[i][i_alt + 2]:
            return_var = main_lst[i][i_alt]
            win_line = [(22, coord_lst[i]), (w - 22, coord_lst[i])]
            win_game = True

    if main_lst[i_alt][i_alt] == main_lst[i_alt + 1][i_alt + 1] == main_lst[i_alt + 2][i_alt + 2]:
        return_var = main_lst[i_alt][i_alt]
        win_line = [(28, 28), (h - 30, h - 30)]
        win_game = True

    elif main_lst[i_alt][i_alt + 2] == main_lst[i_alt + 1][i_alt + 1] == main_lst[i_alt + 2][i_alt]:
        return_var = main_lst[i_alt][i_alt + 2]
        win_line = [(h - 30, 28), (28, h - 30)]
        win_game = True

    return return_var, win_line


def assign_position(x, y):
    """This function is responsible to place the player image at particular coordinates according to the players choice,
    after the p[layer has played his turn.

    Parameters -
    x (float) - It holds the X coordinate values,
    y (float) - It holds the Y coordinate values."""

    coordinate_lst = [(14, 76), (84, 156), (164, 230)]
    ret_var = 0
    for i in coordinate_lst:
        for j in coordinate_lst:
            if x in range(j[0], j[1]) and y in range(i[0], i[1]):
                return ret_var
            ret_var += 1


def available_position():
    """This function is used to check how many free positions are available in the game."""

    global main_lst
    avail_pos = set()
    for lst in main_lst:
        for v in lst:
            if type(v) is int:
                avail_pos.add(v)

    return avail_pos


def new_game():
    """The function resets all the global variables to the default value except the player scores.
    It is executed when the new game button is clicked."""

    global main_lst, play_chance, counter, canvas, msg_lbl, win_game
    main_lst = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    play_chance = 'X'
    counter = 1
    win_game = False
    canvas.delete('win_line', 'X_player', 'O_player')
    msg_lbl.configure(text=" ")
    X_chance_lbl.configure(relief="raised")
    O_chance_lbl.configure(relief="flat")


def reset():
    """The function resets the entire game, i.e. global variables along with the player scores.
    It is executed when the reset button is clicked."""

    global main_lst, play_chance, score, counter, canvas, X_score_lbl, O_score_lbl, \
        X_chance_lbl, O_chance_lbl, msg_lbl, win_game
    main_lst = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    play_chance = 'X'
    score = [0, 0]
    counter = 1
    win_game = False
    canvas.delete('win_line', 'X_player', 'O_player')
    X_score_lbl.configure(text="0")
    O_score_lbl.configure(text="0")
    X_chance_lbl.configure(relief="raised")
    O_chance_lbl.configure(relief="flat")
    msg_lbl.configure(text=" ")


def play_game(x, y):
    """This function is responsible for driving a single game.
    It calls all the sub functions in a particular order for providing a game flow.

    Parameters -
    x (float) - It holds the X coordinate values,
    y (float) - It holds the Y coordinate values."""

    global X_score_lbl, O_score_lbl, score, counter, msg_lbl
    pos_val = assign_position(x, y)
    update_lst = update_main_lst(pos_val)
    if update_lst:
        player_display(pos_val)

        result, win_line = match_decision_and_winning_lines()
        if result is None and update_lst:
            update_chance()
            counter += 1

        else:
            msg_lbl.configure(text="{} wins!".format(result))
            canvas.create_line(win_line, tag='win_line', width=5, fill="#ffffff")
            if result == 'X':
                score[0] += 1
            else:
                score[1] += 1
            X_score_lbl.configure(text=score[0])
            O_score_lbl.configure(text=score[1])

        if counter == 10:
            msg_lbl.configure(text="It's a Draw! Well Played")


def setup(event=None):
    """This function consists of sub functions which are responsible for setting up the game.
    It runs when the canvas configure function is executed.

    Parameters -
    event (tkinter-Event)- It holds the value of the event that occurs on the canvas. The event is a mouse click and
                           thus it holds X and Y coordinate values. Default value is None."""

    load_images()
    create_grid()


def main_flow(event):
    """This function consists of sub functions which are responsible to get the canvas event i.e. mouse click 
    and proceed with the program flow.

    Parameters -
    event (tkinter-Event)- It holds the value of the event that occurs on the canvas. The event is a mouse click and
                           thus it holds X and Y coordinate values."""

    if get_coordinates(event):
        play_game(event.x, event.y)


def create_window():
    """This function is responsible for the entire GUI building of the game.
    All the required canvas, buttons, labels are created and added to the window here."""

    global canvas, msg_lbl, X_chance_lbl, O_chance_lbl, X_score_lbl, O_score_lbl, play_chance
    mainWindow = tkinter.Tk()

    mainWindow.title("Tic tac toe")
    mainWindow.geometry("240x326")
    mainWindow.resizable(0, 0)

    canvas = tkinter.Canvas(mainWindow, bg="#067579", highlightthickness=0, height=237, width=237)

    canvas.bind("<Button-1>", main_flow)
    canvas.bind('<Configure>', setup)
    canvas.grid(row=0, column=0, sticky="ew")

    frame = tkinter.Frame(mainWindow, width=239, height=89, bg="#067579")
    frame.grid(row=1, column=0, sticky="nesw")

    X_score_lbl = tkinter.Label(frame, text="0", bg="#11a1a6", fg="#ffffff", width=2)
    X_score_lbl.grid(row=0, column=0, sticky='ne', padx=(3.5, 0), pady=(3.5, 0))

    X_chance_lbl = tkinter.Label(frame, text="X", fg="#ffffff", width=10, bg="#11a1a6", relief="raised")
    X_chance_lbl.grid(row=0, column=1, sticky='nw', padx=(3, 12.5), pady=(3.5, 0))

    O_chance_lbl = tkinter.Label(frame, text="O", fg="#ffffff", width=10, bg="#11a1a6", relief="flat")
    O_chance_lbl.grid(row=0, column=2, sticky='nw', padx=(12.5, 3), pady=(3.5, 0))

    O_score_lbl = tkinter.Label(frame, text="0", bg="#11a1a6", fg="#ffffff", width=2)
    O_score_lbl.grid(row=0, column=3, sticky='nw', padx=(0, 3.5), pady=(3.5, 0))

    msg_frame = tkinter.Frame(frame, highlightthickness=2, highlightbackground="#ccffa3")
    msg_frame.grid(row=2, column=0, columnspan=4, sticky='w', padx=(5, 5), pady=(3.5, 3.5))
    msg_lbl = tkinter.Label(msg_frame, fg="#D3D3D3", width=32, bg="#067579")
    msg_lbl.grid(row=0, column=0)

    new_game_btn = tkinter.Button(frame, text="New Game", width=9, fg="#ffffff", bg="#11a1a6",
                                  activebackground='#11a1a6', activeforeground='#ffffff', command=new_game)
    new_game_btn.grid(row=3, column=1, sticky='ne', padx=(2, 12.5), pady=(0, 3.5))

    reset_game_btn = tkinter.Button(frame, text="Reset", width=9, fg="#ffffff", bg="#11a1a6",
                                    activebackground='#11a1a6', activeforeground='#ffffff', command=reset)
    reset_game_btn.grid(row=3, column=2, sticky='nw', padx=(12.5, 2), pady=(0, 3.5))

    mainWindow.mainloop()


if __name__ == "__main__":
    """To begin the program flow and execution, the create_window() function is called first."""
    create_window()

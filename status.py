def status(input):
    mystatus = input.split()
    mines_split = mystatus.index("MINES")
    players_split = mystatus.index("PLAYERS")
    bombs_split = mystatus.index("BOMBS")
    
    
    x = float(mystatus[1])
    y = float(mystatus[2])
    dx = float(mystatus[3])
    dy = float(mystatus[4])
    num_mines = int(mystatus[mines_split+1])
    num_players = int(mystatus[players_split+1])
    num_bombs = int(mystatus[bombs_split+1])    

    players = []
    bombs = []

    for i in range(num_players):
        if num_players == 0:
            break
        players.append({"x":float(mystatus[players_split+2+i*0]),"y":float(mystatus[players_split+2+i*1]),"dx":float(mystatus[players_split+2+i*2]),"dy":float(mystatus[players_split+2+i*3])})
    
    for i in range(bombs_split):
        if num_bombs == 0:
            break
        bombs.append({"x":float(mystatus[bombs_split+2+i*0]),"y":float(mystatus[bombs_split+2+i*1])})
        
    return {"x":x, "y":y, "dx":dx, "dy":dy, "mines":num_mines, "players":players,"bombs":bombs}
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

    mines = []
    players = []
    bombs = []

    for i in range(num_mines):
        if num_mines == 0:
            break
        mines.append({"x":float(mystatus[mines_split+3+i*3]),"y":float(mystatus[mines_split+4+i*3])})

    for i in range(num_players):
        if num_players == 0:
            break
        players.append({"x":float(mystatus[players_split+2+i*4]),"y":float(mystatus[players_split+3+i*4]),"dx":float(mystatus[players_split+3+i*4]),"dy":float(mystatus[players_split+3+i*4])})
    
    for i in range(num_bombs):
        if num_bombs == 0:
            break
        bombs.append({"x":float(mystatus[bombs_split+2+i*2]),"y":float(mystatus[bombs_split+3+i*2])})
              
    return {"x":x, "y":y, "dx":dx, "dy":dy, "mines":mines "players":players,"bombs":bombs}

def scoreboard(input):
    scores = []
    myscoreboard = input.split()[1:]
    num_teams = int(len(myscoreboard)/3)
    for i in range(num_teams):
        scores.append({"name":myscoreboard[3*i+0],"score":int(myscoreboard[3*i+1]),"mines":int(myscoreboard[3*i+2])})
    return scores

def configurations(input):
    myconfigs = input.split()[1:]
    configs = {"mapwidth":int(myconfigs[1]), "mapheight":int(myconfigs[3]), "captureradius":float(myconfigs[5]),"visionradius":float(myconfigs[7]),"friction":float(myconfigs[9]),"brakefriction":float(myconfigs[11]),"bombplaceradius":float(myconfigs[13]),"bombeffectradius":float(myconfigs[15]),"bombdelay":float(myconfigs[17]),"bombpower":float(myconfigs[19]),"scanradius":float(myconfigs[21]),"scandelay":float(myconfigs[23])}
    return configs

def scan(input):
    myscan = input.split()[1:]
    mines_split = myscan.index("MINES")
    players_split = myscan.index("PLAYERS")
    bombs_split = myscan.index("BOMBS")
    
    num_mines = int(myscan[mines_split+1])
    num_players = int(myscan[players_split+1])
    num_bombs = int(myscan[bombs_split+1])    

    mines = []
    players = []
    bombs = []

    for i in range(num_mines):
        if num_mines == 0:
            break
        mines.append({"x":float(myscan[mines_split+3+i*3]),"y":float(myscan[mines_split+4+i*3])})

    for i in range(num_players):
        if num_players == 0:
            break
        players.append({"x":float(myscan[players_split+2+i*4]),"y":float(myscan[players_split+3+i*4]),"dx":float(myscan[players_split+3+i*4]),"dy":float(myscan[players_split+3+i*4])})
    
    for i in range(num_bombs):
        if num_bombs == 0:
            break
        bombs.append({"x":float(myscan[bombs_split+2+i*2]),"y":float(myscan[bombs_split+3+i*2])})
        
    return {"mines":mines, "players":players,"bombs":bombs}

scantest="SCAN_OUT  MINES 0 PLAYERS 1 6859.416121534596 6988.998490048922 9.899999999995158 7.21474662271831E-12 BOMBS 0"
scantest2="SCAN_OUT  MINES 2 -- 9791.988798920302 859.919907528256 -- 432.2832063170068 510.75312424783027 PLAYERS 0 BOMBS 0"
print(scan(scantest2))
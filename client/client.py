from transmit import connect, send

USER, PASSWORD = "algowinthis", "unicorns578"
#USER, PASSWORD = "a", "a"

sock = connect(USER, PASSWORD)
send(sock, "SCAN 1 1")
send(sock, "SCOREBOARD");
send(sock, "CONFIGURATIONS")
#send(sock, "BRAKE")
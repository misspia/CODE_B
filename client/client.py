from transmit import connect, send

USER, PASSWORD = "algowinthis", "unicorns578"
#USER, PASSWORD = "a", "a"

sock = connect(USER, PASSWORD)
send(sock, "ACCELERATE 1 1")
send(sock, "ACCELERATE 2 1")
#send(sock, "BRAKE")
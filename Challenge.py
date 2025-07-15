command=""
started=False
while True:
    command=input(">>> ").lower()
    if command=="start":
        if started==True:
            print("already started")
        else:
            started=True
            print("Car started:")
    elif command == "stop":
        if not started:
            print("already stopped")
        else:
            started=False
            print("Car stopped:")
    elif command == "quit":
        break
    elif command == "help":
        print("""
start --- to start the car
stop--- to stop the car
quit--- exit to game
        """)
    else:
        print("I dont understand")
board = [["_","_","_"],["_","_","_"],["_","_","_"]]
change = ("x")
while True:
    for i in range(3):
        print("" )
        for j in range(3):
            print (board[i][j] , end=" ")
    board2 = (input("Enter the position you want to place your mark "+ change))
    print(board)

    splt = board2.split(",")
    row = int(splt[0])
    col = int(splt[1])
    for i in range(1):
         print ("" )
    board [row][col] = (change)

    if board [0][1] == (change) and :
        print (change +"won the game")
    #change x to o, o to x
    if change == "x":
            change = "o" 
    else:
            change = "x"




    
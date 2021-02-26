print("welcome to adventure game ")
print(
    "You have been left alone in a Room ,say Room1. Now to escape you have to reach to Room 5 by crossing maximum 4 doors.")
print("'**RULES**'")
print("1.MAXIMUM 2 HITS ARE ALLOWED . IF YOU HIT THE WALL 3RD TIME ,THE GAME ENDS.")
print("2.ONCE YOU FALL IN THE MUDPOOL BY ENTERING INTO A WRONG DOOR ,THE GAME ENDS.")
print("U-FORWARD ,  B-BACK , R-RIGHT , L-LEFT.    THESE ARE YOUR POSSIBLE DIRECTIONS TO MOVE .")
print("NOW LET US START THE GAME . CONGRATULATIONS")
game = {1: ['R', 'L'], 2: ['U', 'D'], 3: ['L', 'R'], 4: ['R', 'D'], 5: []}
(mud, hit, i) = (0, 2, 1)
while mud == 0 and hit >= 1 and i <= 4:
    print("you are in room ", i)
    print("There are 2 doors in the room. ")
    print('enter the direction (U/B/R/L)')
    ch = input()
    if ch in game[i]:
        if ch == game[i][0]:
            i = i + 1
        else:
            mud = 1
    else:
        hit = hit - 1
        print("Oops you hit the wall.Try again")
if i == 5:
    print('Congrats you won!')
    print('you ended up in', i)
elif mud == 1:
    print("Oops you fell in mudpool ")
    print('you ended up in', i)
elif hit == 0:
    print("maximum hit chances succeded")
    print('you ended up in room ', i)


'''
check by brute force
all the possible pieces walk and check
any left square for the king's move

note: The 'S' definetly bugged if the one piece change the another one to 'S'
      The 'S' that's just change won't change the another one if it can.
      Ex [['R', 'x', 'R']  ---> [['R', 'x', 'S']  The first change the second but 
          ['.', '.', 'x']]       ['.', '.', 'x']] the second one never change the first TT
'''
import copy

def long_walk(pos, direction, brd):
    '''for pieces like B R Q'''
    for direct in direction:
        cal_pos = [pos[0], pos[1]]
        while True:
            try:
                cal_pos[0] += direct[0]
                cal_pos[1] += direct[1]
                if cal_pos[0] < 0 or cal_pos[1] < 0:
                    break
                elif brd[cal_pos[0]][cal_pos[1]] == "." or brd[cal_pos[0]][cal_pos[1]] == "o":
                    brd[cal_pos[0]][cal_pos[1]] = "x"
                elif brd[cal_pos[0]][cal_pos[1]] in ["P", "B", "R", "Q"]:
                    brd[cal_pos[0]][cal_pos[1]] = "S" # s is for the destination that another picese can be stealth to kill
            except IndexError:
                break

def checkmate(board):
    '''checkmate'''
    check_mate = True
    king_pos = []
    brd = board.split('\n')
    brd = [list(row) for row in brd]
    # [[.....],
    # [...K.],
    # [..Q..]]


    pos = [0, 0] # init row column

    for i in brd:
        for j in i:
            if j == 'P':
                try:
                    if brd[pos[0]-1][pos[1]-1] >= 0 or brd[pos[0]-1][pos[1]+1] >= 0:
                        cal_pos = [pos[0], pos[1]]
                        if brd[pos[0]-1][pos[1]-1] == "o" or  brd[cal_pos[0]][cal_pos[1]] == "o":
                            brd[pos[0]-1][pos[1]-1] = "x" #(-1, -1)
                            brd[pos[0]-1][pos[1]+1] = "x" #(-1, +1)
                        elif brd[pos[0]-1][pos[1]-1] in ["P", "B", "R", "Q"]:
                            brd[cal_pos[0]][cal_pos[1]] = "S"
                except IndexError:
                    pass

            if j == 'B':
                direction = ([-1, -1], [-1, 1], [1, -1], [1, 1])
                long_walk(pos, direction, brd)

            if j == 'R':
                direction = ([1, 0], [-1, 0], [0, -1], [0, 1])
                long_walk(pos, direction, brd)

            if j == 'Q':
                direction = ([1, 0], [-1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1])
                long_walk(pos, direction, brd)

            if j =='K':
                king_pos = [pos[0], pos[1]] # found king position!!!
                direction = ([1, 0], [-1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1])
                for direct in direction:
                    cal_pos = [pos[0], pos[1]]
                    cal_pos[0] += direct[0]
                    cal_pos[1] += direct[1]
                    try:
                        if brd[cal_pos[0]][cal_pos[1]] == ".":
                            brd[cal_pos[0]][cal_pos[1]] = "o"
                    except IndexError:
                        pass
            pos[1] += 1
        pos[1] = 0
        pos[0] += 1

    # recheck if the king can counter attack
    direction = ([1, 0], [-1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1])
    for direct in direction:
        cal_pos = copy.deepcopy(king_pos)
        cal_pos[0] += direct[0]
        cal_pos[1] += direct[1]
        try:
            if cal_pos[0] >= 0 and cal_pos[1] >= 0:
                if brd[cal_pos[0]][cal_pos[1]] in ["P", "B", "R", "Q"]: # if find any pieces for kill
                    brd[king_pos[0]][king_pos[1]] = "."
                    brd[cal_pos[0]][cal_pos[1]] = "K"
                    check_mate = False
        except IndexError:
            pass

    for i in brd:
        if "o" in i:
            check_mate = False
        print(i) # You wanna see the board?

    if check_mate:
        print("Success")
    else:
        print("Fail")

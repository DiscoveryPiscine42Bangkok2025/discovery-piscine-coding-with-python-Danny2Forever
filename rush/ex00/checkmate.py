'''checkmate'''
def long_walk(pos, direction, brd):
    '''docstring'''
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
            except IndexError:
                break

def checkmate(board):
    '''docstring'''
    check_mate = True
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
                    brd[pos[0]-1][pos[1]-1] = "x" #(-1, -1)
                    brd[pos[0]-1][pos[1]+1] = "x" #(-1, +1)
                except IndexError:
                    pass

            if j == 'B':
                direction = ([-1, -1], [-1, 1], [1, -1], [1, 1])
                long_walk(pos, direction, brd)

            if j == 'R':
                direction = ([1, 0], [-1, 0], [0, -1], [0, 1])
                long_walk(pos, direction, brd)

            if j =='K':
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

            if j == 'Q':
                direction = ([1, 0], [-1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1])
                long_walk(pos, direction, brd)

            pos[1] += 1
        pos[1] = 0
        pos[0] += 1

    for i in brd:
        if "o" in i:
            check_mate = False
        #print(i) # You wanna see the board?

    if check_mate:
        print("Success")
    else:
        print("Fail")

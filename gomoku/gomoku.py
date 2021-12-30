
def is_empty(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != " ":
                return False
    return True

def is_bounded(board, y_end, x_end, length, d_y, d_x):
    open_ends = 0

    s = (y_end - (length * d_y))
    z = (x_end - (d_x * length))
    ss = s <= 7
    zz = z <= 7
    sss = s >= 0
    zzz = z >= 0
    s1 = (y_end + d_y)
    z1 = (x_end + d_x)
    ss1 = s1 <= 7
    zz1 = z1 <= 7
    sss1 = s1 >= 0
    zzz1 = z1 >= 0
    if ss1 and zz1 and sss1 and zzz1:
        if board[y_end + d_y][x_end + d_x] == " ":
            open_ends += 1
    if  ss and zz and sss and zzz:
        if board[y_end - (length * d_y)][x_end - (d_x * length)] == " ":
            open_ends += 1
    if open_ends == 2:
        return "OPEN"
    elif open_ends == 1:
        return "SEMIOPEN"
    elif open_ends == 0:
        return "CLOSED"
      

def is_win(board):
    if detect_rows(board, "w", 5)[1] > 0:
        return "White won"
    elif detect_rows(board, "w", 5)[0] > 0:
        return "White won"
    elif closed_detect_rows(board, "w", 5) > 0:
        return "White won"
    elif detect_rows(board, "b", 5)[1] > 0:
        return "Black won"
    elif detect_rows(board, "b", 5)[0] > 0:
        return "Black won"
    elif closed_detect_rows(board, "b", 5) > 0:
        return "Black won"
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == " ":
                return "Continue playing"
    return "Draw"


'' The Remaining functions were written by Michael Guerzhoy ''

def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    open_seq_count, semi_open_seq_count = 0, 0
    count = 0
    i = 0
    seq_coord = []
    while i < 8:
        s = y_start + (i * d_y)
        z = x_start + (i * d_x)
        s1 = s >= 0
        z1 = z >= 0
        s2 = s<= 7
        z2 = z <= 7
        if s1 and s2 and z1 and z2:
            if board[y_start + (i * d_y)][x_start + (i * d_x)] == col:
                while s1 and s2 and z1 and z2 and board[y_start + (i* d_y)][x_start + (i * d_x)] == col:
                    count += 1
                    i += 1
                    s = y_start + ((i) * d_y)
                    z = x_start + ((i) * d_x)
                    s1 = s >= 0
                    z1 = z >= 0
                    s2 = s<= 7
                    z2 = z <= 7
                if count == length:
                    seq_coord.append([y_start + ((i-1) * d_y) , x_start + ((i-1) * d_x)])
                    count = 0
                    i += 1
                else:
                    count = 0
                    i += 1
            else:
                i += 1
        else:
            i += 1
    for i in range(len(seq_coord)):
        if is_bounded(board, seq_coord[i][0], seq_coord[i][1], length, d_y, d_x) == "OPEN":
            open_seq_count += 1
        elif is_bounded(board, seq_coord[i][0], seq_coord[i][1], length, d_y, d_x) == "SEMIOPEN":
            semi_open_seq_count += 1


    return open_seq_count, semi_open_seq_count

def closed_detect_row(board, col, y_start, x_start, length, d_y, d_x):
    closed_seq_count = 0
    count = 0
    i = 0
    seq_coord = []
    while i < 8:
        s = y_start + (i * d_y)
        z = x_start + (i * d_x)
        s1 = s >= 0
        z1 = z >= 0
        s2 = s<= 7
        z2 = z <= 7
        if s1 and s2 and z1 and z2:
            if board[y_start + (i * d_y)][x_start + (i * d_x)] == col:
                while s1 and s2 and z1 and z2 and board[y_start + (i* d_y)][x_start + (i * d_x)] == col:
                    count += 1
                    i += 1
                    s = y_start + ((i) * d_y)
                    z = x_start + ((i) * d_x)
                    s1 = s >= 0
                    z1 = z >= 0
                    s2 = s<= 7
                    z2 = z <= 7
                if count == length:
                    seq_coord.append([y_start + ((i-1) * d_y) , x_start + ((i-1) * d_x)])
                    count = 0
                    i += 1
                else:
                    count = 0
                    i += 1
            else:
                i += 1
        else:
            i += 1
    for i in range(len(seq_coord)):
        if is_bounded(board, seq_coord[i][0], seq_coord[i][1], length, d_y, d_x) == "CLOSED":
            closed_seq_count += 1

    return closed_seq_count

def closed_detect_rows(board, col, length):
    closed_seq_count = 0
    for i in range(len(board)):
        a = (closed_detect_row(board, col, 0, i, length, 1,0))
        closed_seq_count += a
    for i in range(len(board)):
        c = (closed_detect_row(board, col, i, 0, length, 0,1))
        closed_seq_count += c
    for i in range(len(board)):
        e = (closed_detect_row(board, col, 0, i, length, 1,1))
        closed_seq_count += e
    for i in range(1,len(board)):
        e1 =(closed_detect_row(board, col, i, 0, length, 1,1))
        closed_seq_count += e1
    for i in range(len(board)):
        g = (closed_detect_row(board, col, 0, i, length, 1,-1))
        closed_seq_count += g
    for i in range(1, len(board)):
        g1 = (closed_detect_row(board, col, i, 7, length, 1,-1))
        closed_seq_count += g1
    return closed_seq_count



def detect_rows(board, col, length):
    open_seq_count, semi_open_seq_count = 0, 0
    for i in range(len(board)):
        a = (detect_row(board, col, 0, i, length, 1,0))[0]
        b = (detect_row(board, col, 0, i, length, 1,0))[1]
        open_seq_count += a
        semi_open_seq_count += b
    for i in range(len(board)):
        c = (detect_row(board, col, i, 0, length, 0,1))[0]
        d = (detect_row(board, col, i, 0, length, 0,1))[1]
        open_seq_count += c
        semi_open_seq_count += d
    for i in range(len(board)):
        e = (detect_row(board, col, 0, i, length, 1,1))[0]
        f = (detect_row(board, col, 0, i, length, 1,1))[1]
        open_seq_count += e
        semi_open_seq_count += f
    for i in range(1,len(board)):
        e1 =(detect_row(board, col, i, 0, length, 1,1))[0]
        f1 =(detect_row(board, col, i, 0, length, 1,1))[1]
        open_seq_count += e1
        semi_open_seq_count += f1
    for i in range(len(board)):
        g = (detect_row(board, col, 0, i, length, 1,-1))[0]
        h = (detect_row(board, col, 0, i, length, 1,-1))[1]
        open_seq_count += g
        semi_open_seq_count += h
    for i in range(1, len(board)):
        g1 = (detect_row(board, col, i, 7, length, 1,-1))[0]
        h1 = (detect_row(board, col, i, 7, length, 1,-1))[1]
        open_seq_count += g1
        semi_open_seq_count += h1

    return open_seq_count, semi_open_seq_count

def search_max(board):
    fake_board = board
    possible_scores = []
    pos_scores_coord = []
    move_y, move_x = 0, 0

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == " ":
                fake_board[i][j] = "b"
                possible_scores.append([score(fake_board),i,j])
                fake_board[i][j] = " "
    for i in range(len(possible_scores)):
        pos_scores_coord.append(possible_scores[i][0])


    pop_o = pos_scores_coord.index(max(pos_scores_coord))
    possible_scores[pos_scores_coord.index(max(pos_scores_coord))]
    move_y = possible_scores[pop_o][1]
    move_x = possible_scores[pop_o][2]
    return move_y, move_x

def score(board):
    MAX_SCORE = 100000

    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}

    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)


    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE

    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE

    return (-10000 * (open_w[4] + semi_open_w[4])+
            500  * open_b[4]                     +
            50   * semi_open_b[4]                +
            -100  * open_w[3]                    +
            -30   * semi_open_w[3]               +
            50   * open_b[3]                     +
            10   * semi_open_b[3]                +
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])




def print_board(board):

    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"

    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1])

        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"

    print(s)


def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board



def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))






def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])

    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)

        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res





        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res



def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x


def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")


def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)

    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)

    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0

    y = 3; x = 5; d_x = -1; d_y = 1; length = 2

    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)

    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #

    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);

    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #
    #
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0




if __name__ == '__main__':
    play_gomoku(8)
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    board = make_empty_board(8)
    x = 0; y = 0; d_x = 1; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    test_search_max()
    print(detect_rows(board, "b", 3))


#returns True iff list1 is at least as long as list2, and the first len(list2) elements of list1 are the same as list2
def list1_start_with_list2(list1, list2):
    if len(list1) < len(list2):
        return False
    for i in range(len(list2)):
        if list1[i] != list2[i]:
            return False
    return True

L = [1,2,3,4]
M = [1,2,3]

#returns True iff the pattern list2 appears in list1
def match_pattern(list1, list2):
    counter = 0
    if len(list2) > len(list1):
        return False
    for i in range(len(list1) - len(list2)):
        if list1[i] != list2[0]:
             counter += 1
        elif list1[i] == list2[0]:
            check = True
            for j in range(len(list2)):
                if list1[counter + j] != list2[j]:
                    check = False
                    counter +=1
                    break
            if check == True:
                return True

    return False



L = [2, 2, 2, 3, 50, 100]
M = [2, 3, 50]

#returns True iff list0 contains at least two adjacent elements with the same value.
def repeats(list0):
    for i in range (len(list0) - 1):
        if list0[i] == list0[i+1]:
            return True
        return False

M = [[5,  6, 7],
     [0, -3, 5],
     [0,  2,  4]]
v = [1,1,1]
N = [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]]

#prints the dimensions of Matrix M stored as a list of lists
def print_matrix_dim(M):
    row = len(M)
    column = len(M[1])
    print(row, "x", column)

#Multiplies a matrix M by a vector v
def mult_M_v(M, v):
    Mv = []
    if len(M[0]) != len(v):
        return False
    for i in range (len(M)):
        x = 0
        for j in range(len(M[0])):
            x += M[i][j] * v[j]
        Mv.append(x)
    return Mv

#Performs matrix multiplication
def mult_M_N(M, N):
    MN = []
    row = []
    if len(M[0]) != len(N):
        return False
    for i in range (len(M)):
        row = []

        for j in range(len(M[0])):
            x = 0
            for k in range(len(N[0])):
                x += M[i][j] * N[j][k]
            row.append(x)
        MN.append(row)
    return MN



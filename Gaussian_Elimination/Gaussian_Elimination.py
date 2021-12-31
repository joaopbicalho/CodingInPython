#Needed for array() and dot()
from numpy import *

from math import gcd

#Printing matrices using NumPy:

#Convert a list of lists into an array:
M_listoflists = [[1,-2,3],[3,10,1],[1,5,3]]
M = array(M_listoflists)
#Now print it:
print(M)




#Compute M*x for matrix M and vector x by using
#dot. To do that, we need to obtain arrays
#M and x
M = array([[1,-2,3],[3,10,1],[1,5,3]])
x = array([75,10,-11])
b = dot(M,x)

print(M)
#[[ 1 -2  3]
# [ 3 10  1]
# [ 1  5  3]]

#To obtain a list of lists from the array M, we use .tolist()
M_listoflists = M.tolist()

print(M_listoflists) #[[1, -2, 3], [3, 10, 1], [1, 5, 3]]

def print_matrix(M_lol):
    print(array(M_lol))

def get_lead_ind(row):
    for i in range(len(row)):
        if row[i] != 0:
            return i
    return len(row)

# def get_row_to_swap(M, start_i):
#     for j in range(len(M[0])):
#         for i in range(len(M) - (start_i + 1)):
#             if M[start_i + 1 + i][j] != 0 and M[start_i + i][j] == 0:
#                 return start_i + 1 + i

def get_row_to_swap(M, start_i):
    index = get_lead_ind(M[start_i])
    rows = []
    for i in range(len(M) - (start_i + 1)):
        cur_lead_ind = get_lead_ind(M[i + start_i + 1])
        if cur_lead_ind < index:
            rows.append([i + start_i + 1, cur_lead_ind])
    if(rows == []):
        return start_i

    low = len(M[0])
    index = 0
    for k in range(len(rows)):
        if rows[k][1] < low:
            low = rows[k][1]
            index = k

    return rows[index][0]

def add_rows_coefs(r1, c1, r2, c2):
    r3 = [0]* len(r1)
    for i in range(len(r3)):
        r3[i] = r1[i] * c1 + r2[i] * c2

    if(len(r3)) == 1 or get_lead_ind(r3) == len(r3):
        return r3

    fac = r3[get_lead_ind(r3)]
    for j in range(len(r3)):
        if(r3[j] != 0):
            fac = gcd(fac, r3[j])
    if fac == 1:
        return r3
    for k in range(len(r3)):
        r3[k] //= fac
    return r3

def eliminate(M, row_to_sub, best_lead_ind):
    for i in range(len(M) - (row_to_sub + 1)):
        r1 = []
        r2 = []
        for j in range(len(M[0])):
            r1.append(M[row_to_sub][j])
            r2.append(M[row_to_sub + 1 + i][j])

        factor1 = r2[best_lead_ind]
        factor2 = r1[best_lead_ind]
        if(factor2 != 0):
            M[row_to_sub + 1 + i] = add_rows_coefs(r1, factor1*-1, r2, factor2)

def eliminate2(M, row_to_sub, last_ind):
    for i in range(row_to_sub):
        r1 = []
        r2 = []
        for j in range(len(M[0])):
            r1.append(M[row_to_sub][j])
            r2.append(M[row_to_sub - 1 - i][j])

        factor1 = r2[last_ind]
        factor2 = r1[last_ind]
        if(factor2 != 0):
            M[row_to_sub -1 - i] = add_rows_coefs(r1, factor1*-1, r2, factor2)


def forward_step(M):
    index = 0
    i = 0
    while(i < len(M) and index < len(M[0])):
        #swap
        swap_row = get_row_to_swap(M, i)
        temp = []
        for j in range(len(M[0])):
            temp.append(M[i][j])
        M[i] = M[swap_row]
        M[swap_row] = temp
        #eliminate
        if(M[i][index] == 0):
            i -= 1
        else:
            eliminate(M, i, index)
        print(M)
        index += 1
        i += 1

def backward_step(M):
    index = get_lead_ind(M[len(M) - 1])
    if(index == len(M[0])):
        index -= 1
    else:
        index = len(M[0]) - 1
    i = len(M) - 1
    while(i > -1 and index > -1):
        #eliminate
        if(M[i][index] == 0):
            index += 1
        else:
            eliminate2(M, i, index)
        print(M)
        index -= 1
        i -= 1

def solve(M, b):
    Aug = []
    for i in range(len(M)):
        Aug.append(M[i])
        Aug[i].append(b[i])
    print(Aug)
    forward_step(Aug)
    backward_step(Aug)
    print(Aug)

    # Check for empty columns
    for j in range(len(Aug[0])):
        zero_column = True
        for i in range(len(Aug)):
            if Aug[i][j] != 0:
                zero_column = False
        if(zero_column == True):
            return "Infinite Solutions"
    #Check for empty rows, unsolvable rows, etc
    for i in range(len(Aug)):
        num_nonzero = 0
        for j in range(len(Aug[0])):
            if Aug[i][j] != 0:
                num_nonzero += 1
        if(num_nonzero == 1):
            return "No Solution"
        if(num_nonzero == 0):
            del Aug[-1]
        if(num_nonzero > 2):
            return "Infinite Solutions"
    #Solve systems
    x = [0] * (len(Aug[0]) - 1)
    x[len(Aug) - 1] = Aug[len(Aug) - 1][len(Aug[0]) - 1] / Aug[len(Aug) - 1][len(Aug[0]) - 2]
    for j in range(len(Aug) - 2, -1, -1):
        x[j] = (-1*x[j+1]*Aug[j][j + 1])/Aug[j][j]
    return x



M = [[5, 6, 7, 8],
    [0, 0, 1, 1],
    [0, 0, 5, 2],
    [0, 0, 7, 0]]
M_listoflists = [[0,-2,3],[0,0,1],[0,5,3]]
get_row_to_swap(M, 1)

add_rows_coefs([1,2,5], 2, [5,2,1], 2)

M = [[0, 0, 1, 0, 2],
    [1, 0, 2, 3, 4],
    [3, 0, 4, 2, 1],
    [1, 0, 1, 1, 2]]

M = [[3, 1], [2, 2], [3, 2]]
b = [5, 6, 7]
print(solve(M, b))
forward_step(M)
backward_step(M)

M = [[1, 0],[0,1]]
b = [5, 10]
solve(M, b)


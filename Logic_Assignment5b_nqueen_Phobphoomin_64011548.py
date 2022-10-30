from turtle import *
n = int(input("Enter a number between 1-9: "))
if n >= 10 or n < 1:
    print("invalid input")
    exit()

board = []


# Check whether 'clause' contains complementary literals
def tautology(clause):
    for lit in clause:
        neg_lit = '~' + lit if lit[0] != '~' else lit[1:]
        if neg_lit in clause:
            return True
    return False


# Apply simple DPLL algorithm to check satisfiability
def sat(cnf):
    # Empty clause exists means unsatisfiable
    if [] in cnf:
        return None

    # Remove tautologies
    new_cnf = [c for c in cnf if not tautology(c)]

    # Empty set of clauses is obviously satisfiable
    if len(new_cnf) == 0:
        return {}

    # Select a propositional letter
    lit = new_cnf[0][0]
    p = lit if lit[0] != '~' else lit[1:]

    # Try p true
    new_cnf_p = [c for c in new_cnf if p not in c]
    new_cnf_p = [[l for l in c if l != '~' + p] for c in new_cnf_p]
    result = sat(new_cnf_p)
    if result is not None:
        result[p] = True
        return result
    else:
        # Try p false
        new_cnf_notp = [c for c in new_cnf if '~' + p not in c]
        new_cnf_notp = [[l for l in c if l != p] for c in new_cnf_notp]
        result = sat(new_cnf_notp)
        if result is not None:
            result[p] = False
            return result
        else:
            return None



#getting propositional letters which represent the n*n board with the help of python
for i in range(1,n+1):
    for j in range(1,n+1):
        board.append("p"+str(i)+str(j))



#index 0 = literal , index1= row ,index2=column
original = []
for ele in board:
    original.append(ele)


print('board',original)


#underAttack is the formula for the row and column that is under attack by the queen so we'll remove underattack
#instead of translating english to logical formula I just implement python to get the formula
#in the following loop I find the slot with similar row and column and store them inside a list then if the board is == to the underattack i just remove that.
def move():
    underAttack = []
    for i in range(len(board)):
        if board[i][1] == queen[1]:
            underAttack.append(board[i])




        elif board[i][2] == queen[2]:

            underAttack.append(board[i])

    for i in underAttack:
        for j in board:
            if i == j:
                board.remove(j)
    # diag is the formula for the diagnoal slot that is under attack




    diag = []

    diagrow = int(queen[1])
    diagcol = int(queen[2])
    for i in range(n):
        diagcol += 1
        diagrow += 1
        diag.append('p' + str(diagrow) + str(diagcol))

        for ele in diag:
            if int(ele[1]) > n or int(ele[1]) < 1 or int(ele[2]) > n or int(ele[2]) < 1:
                diag.remove(ele)
    diagrow = int(queen[1])
    diagcol = int(queen[2])

    for i in range(n):
        if diagrow > 1 and diagcol > 1:
            diagrow -= 1
            diagcol -= 1
            diag.append('p' + str(diagrow) + str(diagcol))

    diagrow = int(queen[1])
    diagcol = int(queen[2])
    for i in range(n):
        if diagrow > 1 and diagcol < n:
            diagrow -= 1
            diagcol += 1
            diag.append('p' + str(diagrow) + str(diagcol))
    diagrow = int(queen[1])
    diagcol = int(queen[2])
    for i in range(n):
        if diagrow < n and diagcol > 1:
            diagrow += 1
            diagcol -= 1
            diag.append('p' + str(diagrow) + str(diagcol))

    diag = set(diag)
    diag = list(diag)

    for i in diag:
        for j in board:
            if i == j:
                board.remove(j)
    return underAttack,diag
cnf = []
temp = []
index = 0
nqueen = 0

for i in original:
    queen = i
    move()
    nqueen += 1
    print(board,queen,nqueen)
    temp.append(queen)
    for num in range(n-2):
        for j in board:
            queen = j
            move()
            nqueen += 1
            print('backtracking',board, queen, nqueen)
            temp.append(queen)

    if len(board) == 0:

        if nqueen == n:
            cnf.append(temp)
            temp = []

        for ele in original:
            board.append(ele)
            nqueen = 0
            temp = []


print()
print('cnf=',cnf)
print(sat(cnf))

if len(cnf) == 0:
    print('Not Solvable')

elif len(cnf) != 0:
    from turtle import *


    speed(0)
    tracer(0)

    penup()
    goto(-300, 300)
    pendown()


    def sq():
        for i in range(4):
            fd(50)
            right(90)
        fd(50)


    for i in range(n):
        for j in range(n):
            det = i + j
            if det % 2 == 0:
                begin_fill()
                sq()
                end_fill()
            else:
                sq()
        bk(50 * n)
        right(90)
        fd(50)
        left(90)
    left(90)
    fd(50 * n)
    right(90)

    slot = cnf[0]
    penup()
    print(slot)
    for ele in slot:
        row = int(ele[1])
        column = int(ele[2])

        bk(30)

        fd(50 * row)
        right(90)

        bk(17)

        fd(50 * column)
        color('red')
        write('Q', font=(20))
        left(90)
        goto(-300, 300)
goto(-450,-300)
write('cnf=')
goto(-400,-300)
write(cnf)
goto(-400,-350)
write(sat(cnf))
done()

# 12 24 31 43
# 1 7 8 14
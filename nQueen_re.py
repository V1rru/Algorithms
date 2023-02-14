# amount of figures and the size of the field (n figures, n*n field)
n = int(input())

# matrix - the chess field
matrix = []

# filling the empty field with 0 values
for i in range(n):
    temp = []
    for j in range(n):
        temp.append(0)
    matrix.append(temp)

# function checks the ability to place a figure
def Checker(str, col):

    # Checking the row (from the left side before the possible figure's place)
    for i in range(col):
        if matrix[str][i] == 1:
            return False
   
    # Checking only the lower-left diagonal
    if str == 0 and col != 0:
        while col != 0 and str != (n - 1):
            col -= 1
            str += 1
            if matrix[str][col] == 1:
                return False

    # Checking only the upper-left diagonal
    if str == (n - 1) and col != 0:
        while col != 0 and str != 0:
            col -= 1
            str -= 1
            if matrix[str][col] == 1:
                return False
        
    # # Checking both the upper-left and lower-left diagonals
    if str != 0 and col != 0:
        strClone = str
        colClone = col
        while col != 0 and str != 0:
            col -= 1
            str -= 1 
            if matrix[str][col] == 1:
                    return False

        while colClone != 0 and strClone != (n - 1):
            colClone -= 1
            strClone += 1
            if matrix[strClone][colClone] == 1:
                return False

    return True

# places the figures on their places
def Positioner(column):
    
    if column >= n:
        return True
    else:
        for string in range(n):
            if Checker(string, column) == True:
                matrix[string][column] = 1
                if Positioner(column + 1) == True:
                    return True 

                matrix[string][column] = 0

        return False

Positioner(0)

for i in range(n):
    tmp = ""
    for j in range(n):
        tmp += str(matrix[i][j]) + " "
    print(tmp)
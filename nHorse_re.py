# The sizes of the field
n = int(input("Enter the size of the field: "))

# The amount of steps made
res = 1

# Matrix - the chess field
matrix = []

# The set of possible movements
mvX = [2, 1, -1, -2, -2, -1, 1, 2]
mvY = [1, 2, 2, 1, -1, -2, -2, -1]

# Filling the empty field with 0 values
for i in range(n):
    temp = []
    for j in range(n):
        temp.append(0)
    matrix.append(temp)

# Function checks the ability to take a place
def Checker(nX, nY):
    if(nX >= 0 and nY >= 0 and nX < n and nY < n and matrix[nX][nY] == 0):
        return True
    return False

# Places the figures on their places
def Positioner(cX, cY, res):
    if res == pow(n, 2):
        return True
    else:
        for i in range(8):
            nX = cX + mvX[i]
            nY = cY + mvY[i]
            if Checker(nX, nY) == True:
                matrix[nX][nY] = res

                if Positioner(nX, nY, res + 1) == True:
                    return True

                matrix[nX][nY] = 0

        return False

# Calling the method
Positioner(0, 0, res)

# Printing the final matrix
print()
print("The result is:")
for i in range(n):
    tmp = ""
    for j in range(n):
        tmp += str(matrix[i][j]) + " "
    print(tmp)
    
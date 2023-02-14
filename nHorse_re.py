# The sizes of the field
n = int(input("Enter the size of the field: "))

# The amount of steps made
res = 0

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
def Checker():


# Places the figures on their places
def Positioner(cX, cY, res):
    if res == pow(n, 2):
        return True
    else:
        for i in range(8):
            nX = cX + mvX[i]
            nY = cY + mvY[i]
            
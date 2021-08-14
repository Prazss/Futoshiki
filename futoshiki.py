grid = 3

f = [[0,0,0],
     [0,0,0],
     [0,0,0]]

conditions = [[0,2,">",1,2],
              [1,0,">",2,0],
              [1,0,">",1,1],
              [1,2,">",2,2]]

def checkConditions():
    
    for c in conditions:
        
        x = f[c[0]][c[1]]
        y = f[c[3]][c[4]]
        z = c[2]

        if(x!=0 and y!=0):          
            if(z == "<"):
                if(x >= y):
                    return False
            else:
                if(x <= y):
                    return False
                    
    return True

def printGrid():

    for i in f:
        for j in i:
            print("\t"+str(j),end="")
        print("\n")

    print("\n")

def checkGrid(row,column,num):

    for x in range(grid):
        if f[row][x]==num:
            return False

    for x in range(grid):
        if f[x][column]==num:
            return False

    return True

def solGrid(row,column):

    if row == grid-1 and column == grid:
        return True

    if column==grid:
        row+=1
        column=0

    if f[row][column]>0:
        return solGrid(row,column+1)

    for num in range(grid):
        if checkGrid(row,column,num+1) and checkConditions():
            f[row][column]=num+1
            if solGrid(row,column+1):
                return True
        f[row][column]=0

    return False

printGrid()
solGrid(0,0)
print("\n\nAfter Solution - \n")
printGrid()

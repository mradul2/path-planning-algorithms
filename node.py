from utils import * 

# Node class for each pixel in the Image matrix 
class Node :
    def __init__(self,row,column):
        self.parent = None 
        # Setting g, h, f as Infinity 
        self.g = 2e50
        self.h = 2e50
        self.f = 2e50
        # By default set Mode of a node is Navigable 
        self.mode = NAVIGABLE
        self.row = row
        self.column = column
    
    # Method for converting the Node into Start Mode 
    def start(self):
        self.mode = START

    # Method for converting the Node into End Node 
    def end(self):
        self.mode = END

    # Method for converting the Node into Obstacle Mode 
    def obstacle(self):
        self.mode = OBSTACLE


# isValid function for checking if a poition for a Node is valid 
def isValid(i, j):
    if i >= 0 and j >= 0 and i < SIZE and j < SIZE:
        return True
    else:
        return False

# Function returns valid obstacle free Neighbours of a particular Node in 4 directions
def neighbours1(A, matrix):
    neighbour = []
    if isValid(A.row,A.column-1) and matrix[A.row][A.column-1].mode != OBSTACLE:
        neighbour.append(matrix[A.row][A.column-1])
    if isValid(A.row,A.column+1) and matrix[A.row][A.column+1].mode != OBSTACLE:
        neighbour.append(matrix[A.row][A.column+1])
    if isValid(A.row-1,A.column) and matrix[A.row-1][A.column].mode != OBSTACLE:
        neighbour.append(matrix[A.row-1][A.column])
    if isValid(A.row+1,A.column) and matrix[A.row+1][A.column].mode != OBSTACLE:
        neighbour.append(matrix[A.row+1][A.column])

    return neighbour

# Function returns valid obstacle free Neighbours of a particular Node in other 4 directions
def neighbours2(A,matrix):
    neighbour = []
    if isValid(A.row-1,A.column+1) and matrix[A.row-1][A.column+1].mode != OBSTACLE:
        neighbour.append(matrix[A.row-1][A.column+1])
    if isValid(A.row-1,A.column-1) and matrix[A.row-1][A.column-1].mode != OBSTACLE:
        neighbour.append(matrix[A.row-1][A.column-1])
    if isValid(A.row+1,A.column+1) and matrix[A.row+1][A.column+1].mode != OBSTACLE:
        neighbour.append(matrix[A.row+1][A.column+1])
    if isValid(A.row+1,A.column-1) and matrix[A.row+1][A.column-1].mode != OBSTACLE:
        neighbour.append(matrix[A.row+1][A.column-1])

    return neighbour


# Heuristic Function calculating Functions :

# Manhattan Distance
def manhattan(A, B):
    return abs(A.row - B.row) + abs(A.column - B.column)

# Euclidean Distance
def euclidean(A, B):
    return math.sqrt((A.row - B.row) ** 2 + (A.column - B.column) ** 2)

# Diagonal Distance
def diagonal(A, B):
    return min(abs(A.row - B.row), abs(A.column - B.column)) * 1.414 + max(abs(A.row - B.row), abs(A.column - B.column)) - min(abs(A.row - B.row), abs(A.column - B.column))


# Function for finding the starting Node in the given Node Matrix : 

def findStart(matrix):
    for i in range(SIZE):
        for j in range(SIZE):
            if matrix[i][j].mode == START:
                return matrix[i][j]


# Function for finding the destination Node in the given Node Matrix
def findEnd(matrix):
    for i in range(SIZE):
        for j in range(SIZE):
            if matrix[i][j].mode == END:
                return matrix[i][j]

# Function constructs Path and calculates Cost of the Path 
def constructPath(start, end, matrix):
    current = end.parent
    ans = 0
    while not current.mode == START:
        current.mode = PATH

        if current.row == current.parent.row or current.column == current.parent.column:
            ans += 1
        else:
            ans += math.sqrt(2)

        current = current.parent
        
    print("Cost of path is " ,ans)
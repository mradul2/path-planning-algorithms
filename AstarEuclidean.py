from node import *

#-----------------------------------ALGORITHM------------------------------------------#

def AstarEuclidean(matrix):

    count = 0

    start = findStart(matrix)
    end = findEnd(matrix)

    start.g = 0
    start.h = 0
    start.f = 0

    PQ = PriorityQueue()
    PQ.put((0, count, start))

    openSet = {start}

    while not PQ.empty():
        f, cnt, current = PQ.get()
        openSet.remove(current)

        

        for neig in neighbours1(current,matrix):
            tempGscore = current.g + 1

            if tempGscore < neig.g:
                neig.parent = current
                neig.g = tempGscore
                neig.f = neig.g + euclidean(neig, end)

                if neig not in openSet:
                    count += 1
                    openSet.add(neig)
                    
                    if neig.mode == END:
                        constructPath(start,neig,matrix)
                        return True
                    else:
                        neig.mode = OPEN
                        PQ.put((neig.f, count, neig))
        if not current.mode == START:
            current.mode = CLOSED


    return False 

#------------------------------------------ Main ----------------------------------------#
matrix = []
for i in range(SIZE):
      matrix.append([])
      for j in range(SIZE):
            matrix[i].append(Node(i,j))


for i in range(SIZE):
      for j in range(SIZE):
            if np.array_equal(IMAGE[i,j],GREEN):
                  matrix[i][j].start()
            elif np.array_equal(IMAGE[i,j],RED):
                  matrix[i][j].end()
            elif np.array_equal(IMAGE[i,j],WHITE):
                  matrix[i][j].obstacle()

      
t0 = time.time()
AstarEuclidean(matrix)
t1 = time.time()
print("Time taken: ", t1-t0)

for i in range(SIZE):
      for j in range(SIZE):
            if matrix[i][j].mode == OPEN:
                  IMAGE[i,j] = BLUE
            elif matrix[i][j].mode == CLOSED:
                  IMAGE[i,j] = ORANGE
            elif matrix[i][j].mode == PATH:
                  IMAGE[i][j] = PURPLE

      


IMAGE = upScale(IMAGE, (1000,1000,3))
cv2.namedWindow("AstarEuclidean")
cv2.imshow("AstarEuclidean",IMAGE)
cv2.waitKey(0)
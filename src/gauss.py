
def _gauss(A):
    m = len(A)
    n = len(A[0])

    for j,row in enumerate(A):
        #diagonal term to be 1
        #by dividing row by diagonal term
        if row[j] != 0:
            divisor = row[j]
            for i, term in enumerate(row):
                row[i] = term / divisor

            #add the other rows to the additive inverse
            #for every row
            for i in range(m):
                if i !=j: #don't do it to row j
                    #calculate the additive inverse
                    addinv = -1*A[i][j]
                    for ind in range(n):
                        #add the corresponding term to the jth row
                        #multiplied by the additive inverse
                        #to the term in the ith row
                        A[i][ind] += addinv*A[j][ind]
    return A

def gauss(A):
    '''Solving a n x n+1 augmented matrix'''
    for j,w in enumerate(A):
        #diagonal term to be 1
        #by dividing row by diagonal term
        if w[j] != 0:
            divisor = w[j]
            for i,v in enumerate(w):
                w[i] = v / divisor

        #add the other rows to additive inverse to make value 0
        rowList = [x for x in range(len(A))]
        rowList.remove(j)
        for i in rowList:
            addinv = -1*A[i][j]
            for ind,value in enumerate(A[i]):
                A[i][ind] = value + addinv*A[j][ind]

    return A

B = [
        [2,1,-1,8],
        [-3, -1, 2, -1],
        [-2, 1, 2, -3],
        ]

print(_gauss(B))

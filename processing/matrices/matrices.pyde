
xmin = -10
xmax = 10

ymin = -10
ymax = 10

rangex = xmax - xmin
rangey = ymax - ymin

fmatrix = [[0,0],[1,0],[1,2],[2,2],[2,3],[1,3],[1,4],[3,4],[3,5],[0,5]]

transformation_matrix = [[0,-1],[1,0]]
transformation_matrix = [[1,0],[0,-1]]
transformation_matrix = [[0,-1],[-1,0]]
transformation_matrix = [[-1,1],[1,1]]

def setup():
    global xscl, yscl
    size(600, 600)
    xscl = width / rangex
    yscl = -height / rangey
    
def draw():
    global xscl, yscl
    background(255)
    translate(width/2, height/2)
    grid(xscl, yscl)
    
    ang = map(mouseX, 0, width, 0, 3*PI)
    rot_matrix = [[cos(ang), -sin(ang)],
                  [sin(ang), cos(ang)]]    
    stroke(0)
    #newmatrix = transpose(multmatrix(transformation_matrix, transpose(fmatrix)))
    newmatrix = transpose(multmatrix(rot_matrix, transpose(fmatrix)))
    graphPoints(fmatrix)
    strokeWeight(2)
    stroke(255, 0, 0)
    graphPoints(newmatrix)

def graphPoints(matrix):
    beginShape()
    for pt in matrix:
        vertex(pt[0]*xscl, pt[1]*yscl)
    endShape(CLOSE)

            
def grid(xscl, yscl):
    #cyan lines
    strokeWeight(1)
    stroke(0, 255, 255)
    for i in range(xmin, xmax+1):
        line(i*xscl, ymin*yscl, i*xscl, ymax*yscl)
        line(xmin*xscl, i*yscl, xmax*xscl, i*yscl)
        
    #black axes
    stroke(0)
    line(0, ymin*yscl, 0, ymax*yscl)
    line(xmin*xscl, 0, xmax*xscl, 0)

def multmatrix(a,b):
    m = len(a) #number of rows in first matrix
    n = len(b[0]) #number of columns in second matrix
    newmatrix = []
    for i in range(m):
        row = []
        #for every column in b
        for j in range(n):
            sum1 = 0
            #for every element in the column
            for k in range(len(b)):
                sum1 += a[i][k]*b[k][j]
            row.append(sum1)
        newmatrix.append(row)
    return newmatrix

def transpose(a):
    output = []
    m = len(a)
    n = len(a[0])
    for i in range(n):
        output.append([])
        for j in range(m):
            #replace a[i][j] with a[j][i]
            output[i].append(a[j][i])
    return output

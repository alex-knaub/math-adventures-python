from math import sqrt, degrees,atan2, sin, cos,radians

xmin=-2
xmax=2

ymin = -2
ymax = 2

rangex = xmax - xmin
rangey = ymax - ymin

def setup():
    global xscl, yscl, rangex, rangey
    
    size(600,600)
    colorMode(HSB)
    noStroke()
    xscl= width / rangex
    yscl= -height / rangey

def draw():
    translate(width/2,height/2)
    #go over all x's and y's on the grid
    for x in arange(xmin,xmax,.01):
        for y in arange(ymin,ymax,.01):
            z=[x,y]
            c = [-0.8, 0.156]
            
            #put it into the julia function
            col=julia(z,c, 100)
            
            #if julia returns 0
            if col == 100:
                fill(0)
            else:
                #map the color from 0 to 100
                #to 0 to 255
                #col1 = map(col,0,100,0,300)
                fill(3*col,255,255)

            rect(x*xscl,y*yscl,1,1)


def arange(start,stop,step):
    '''Returns a list of numbers from 
    start to stop by step '''
    output = []
    x = start
    while x < stop:
        output.append(x)
        x += step
    return output

def julia(z, c, num):
    count = 0
    z1 = z
    count=0
    #define z1 as z
    z1=z
    #iterate num times
    while count <= num:
        #check for divergence
        if magnitude(z1) > 2.0:
        #return the step it diverged on
            return count
        #iterate z
        z1=cAdd(cMult(z1,z1),c)
        count+=1
    #if z hasn't diverged by the end
    return num

def magnitude(z):
    return sqrt(z[0]**2 + z[1]**2)

def cMult(u,v):
    return [u[0] * v[0] - u[1] * v[1], u[1] * v[0] + u[0] * v[1]] 
        
def cAdd(a, b):
    return [a[0] + b[0], a[1] + b[1]]

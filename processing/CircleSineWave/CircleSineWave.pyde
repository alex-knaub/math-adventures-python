r1 = 100 #radius of big circle
r2 = 10  #radius of small circle
t = 0
circleList = []

def setup():
    size(600, 600)
    
def draw():
    global t, circleList
    
    background(200)
    #move to left-center of screen
    translate(width/4, height/2)    
    noFill()
    stroke(0)
    ellipse(0,0, 2*r1, 2*r1)
    
    fill(255, 0, 0) #red
    y = r1*sin(t)
    x = r1*cos(t)
    ellipse(x,y, r2, r2)
    circleList = [y] + circleList[:249]
    
    stroke(0, 255, 0) #green line
    line(x, y, 200, y)
    fill(0, 255, 0) #green
    ellipse(200, y, 10, 10)
    
    for i, c in enumerate(circleList):
        ellipse(200+i, c, 5, 5)
    
    t += 0.05

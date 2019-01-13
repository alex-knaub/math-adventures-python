def setup():
    size(600, 600)
    
def draw():
    translate(width/2, height/2)    
    polygon(5,100)
    
def polygon(sides, sz):
    beginShape()
    step = radians(360/sides)
    for i in range(sides):        
        vertex(sz*cos(step*i), 
               sz*sin(step*i))
    endShape(CLOSE)

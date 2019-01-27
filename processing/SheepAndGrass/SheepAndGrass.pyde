

sheepList = []

def setup():
    size(600, 600)
    
    for i in range(3):
        sheepList.append(Sheep(random(width),
                               random(height)))
    
def draw():
    background(255)
    for sheep in sheepList:
        sheep.update()


class Sheep:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
        self.sz = 10
        
    def update(self):
        move = 10
        self.x = self.x + random(-move, move)
        self.y = self.y + random(-move, move)
        
        fill(255)    
        ellipse(self.x, self.y, self.sz, self.sz)

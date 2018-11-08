from MLP import mlp 


a = mlp(2,3,2)
def setup():
    size(800,800)
    background(51)
    
def draw():
    global a 
    
    a.draw()

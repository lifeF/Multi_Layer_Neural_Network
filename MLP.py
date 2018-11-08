
# NPAL : number of perceptron at layer 
class mlp:
    
    def __init__(self, inputLayer, hiddenLayer , outputLayer):
        # NPAL : number of perceptron at layer 
        self.NPAL =[inputLayer,hiddenLayer ,outputLayer]
        self.state = True
        
        
    def draw(self):
        if self.state :
            points = [[],[],[]]
            for i in range(3):
                fill(200)
                x = (i+1)*width/4
                for j in range(self.NPAL[i]):
                    y = (j+1)*(height-200)/(self.NPAL[i]+1)
                    stroke(200)
                    textAlign(CENTER)
                    text("b",x,y-45)
                    line(x,y,x,y-40)
                    ellipse(x,y,50,50)
                    points[i].append([x,y])
                    
            Layer1 = 0
            Layer2 = 0 
            for i in range(2):
                for a in points[i]:
                    Layer2=0
                    for b in points[i+1]:
                        stroke(200)
                        line(a[0],a[1],b[0],b[1])
                        text("w"+str(Layer1)+","+str(Layer2), (2*a[0]+b[0])/3, (2*a[1]+b[1])/3);
                        Layer2 =Layer2 + 1
                    Layer1 = Layer1+1
                    
            self.state = False 
                

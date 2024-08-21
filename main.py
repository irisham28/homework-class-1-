class stationary():
    def __init__(self,brand,color,size,shape):
        self.brand = brand
        self.color=color
        self.size = size
        self.shape = shape


    def get_color(self):
        return self.color
    
    def set_color(self,new_color):
        self.color = new_color

    def show_stationary(self):
        print("I am a pice of stationary with brand {},  with color {} and the size of a {}, my shape would be a {}.".format(self.brand,self.color,self.size,self.shape))

#child class
class pencil(stationary):
    def __init__(self,brand,color,size,shape,quality):
        stationary.__init__(self,brand,color,size,shape)
        self.quality = quality 

    def show_stationary(self):
        print("I am a piece of stationary with a brand  of {} with color {} and my quality is {}".format(self.brand,self.color,self.quality))

#method
eraser=stationary("castle","blue","small","rectangle")
eraser.show_stationary()
    




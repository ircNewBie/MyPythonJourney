class circle( object):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
        
        
    def add_radius(self, r):
        self.radius = self.radius + r


   

class Car(object):
    def __init__(self,make,model,color):
        self.make=make;
        self.model=model;
        self.color=color;
        self.owner_number=0
    def specs(self):
        print ("Transmission Type:",  self.transmission)  
        print ("Rim Size:", self.rim_size)
        print ("RIm Type:", self.rim_type)
    def car_info(self):
        print("make: ",self.make)
        print("model:", self.model)
        print("color:",self.color)
        print("number of owners:",self.owner_number)
        print("\n")
        
        try:
            self.specs()
        except:
            print("Specs not yet specified")
        
    def sell(self):
        self.owner_number=self.owner_number+1
        
    def change_color(self,new_color):
        self.color = new_color
    def set_specs (self, transType = "", rim_size = "" , rim_type = ""):
        self.transmission = transType
        self.rim_size = rim_size
        self.rim_type = rim_type
    


c1 = circle(5, "red")


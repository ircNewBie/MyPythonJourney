class circle( object):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
        
    def add_radius(self, r):
        self.radius = self.radius + r
        
    def compute_area(self):
        return self.radius*self.radius*3.1416

    self.area = compute_area()



c1 = circle(5, "red")


from turtle import Turtle, Screen
from random import randint, choice as rand_choice

colors = ['blue','red','orange','green','purple']

class MyTurtle(Turtle):
    def random_shape(self, x, y):
        self.color(rand_choice(colors))
        
        self.penup()
        self.setposition(randint(-200, 200), randint(-200, 200))
        self.pendown()
        self.circle(50, steps=randint(4, 12))
    
    
    
    def __init__(self):
        super().__init__()
        self.random_shape(0,0)
        self.onclick(self.random_shape)
       
        
        

        
x = MyTurtle()
z = MyTurtle()





screen = Screen()

screen.mainloop()
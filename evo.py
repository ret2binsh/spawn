import turtle
import random
import os

alive = []

class Organism(object):
    '''Defines an organism object that holds all of the
       common attributes amongst all organisms.'''

    def __init__(self):
        self.body = turtle.Turtle()
        self.body.ht()
        self.body.penup()
        self.body.shape("turtle")
        pos = self._random_xy()
        while pos in alive:
            pos = self._random_xy()
        self.body.setposition(x=pos)

    def _random_xy(self):
        return (random.randint(-360,360),random.randint(-360,360))

    def birth(self):
        if random_chance() < self.birth_chance:
            rand  = random_chance()
            if rand < 10:
                alive.append(random.choice(self.secondary)())
            else:
                alive.append(self.primary())

    def death_check(self):
        if random_chance() < self.death_chance:
            self.body.ht()

class Red(Organism):

    def __init__(self):
        super(Red, self).__init__()
        self.body.color("red")
        self.death_chance = 10
        self.birth_chance = 5
        self.body.st()
        self.primary = Red
        self.secondary = [Blue,Green]

class Blue(Organism):

    def __init__(self):
        super(Blue, self).__init__()
        self.body.color("blue")
        self.death_chance = 10
        self.birth_chance = 5
        self.body.st()
        self.primary = Blue
        self.secondary = [Green]

class Green(Organism):

    def __init__(self):
        super(Green, self).__init__()
        self.body.color("green")
        self.body.turtlesize(2)
        self.death_chance = 5
        self.birth_chance = 5
        self.body.st()
        self.primary = Green
        self.secondary = [Green,Orange]

class Orange(Organism):

    def __init__(self):
        super(Orange, self).__init__()
        self.body.color("white")
        self.death_chance = 5
        self.birth_chance = 10
        self.body.st()
        self.primary = Orange
        self.secondary = [Orange]

class environment(object):
    '''Keeps track of the play environment'''

    def __init__(self):
        self.env = turtle.Screen()
        self.env.setup(width=800,height=800)
        self.env.bgcolor("black")
        self.env.title("EvoLand")

def random_chance():
    r = ord(os.urandom(1))
    return int(r) % 100

if __name__ == "__main__":

    world = environment()
    spawn_chance = 100
    
    for generation in range(1,201):
        world.env.title("Generation %d" % generation)
        if random_chance() < spawn_chance:
            alive.append(Red())

        for o in alive:
            try:
                if o.body.isvisible():
                    o.birth()
                    o.death_check()
            except:
                pass
    count = 0
    red = 0
    blue = 0
    green = 0
    white = 0
    for org in alive:
        try:
            if org.body.isvisible():
                color = org.body.color()[0]
                if color == "red":
                    red = red+1
                elif color == "blue":
                    blue = blue+1
                elif color == "green":
                    green = green+1
                elif color == "white":
                    white = white+1
                count = count+1
        except:
            pass

    print("Total turtles: %d" % count)
    print("Red: %d" % red)
    print("Blue: %d" % blue)
    print("Green: %d" % green)
    print("White: %d" % white)
    raw_input()

import math
import turtle
G = 1

class Sun:
    def __init__(self, name, radius, mass, temp, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.mass = mass
        self.radius = radius
        self.temp = temp
        
        self.turtle = turtle.Turtle()
        self.turtle.shape('circle')
        self.turtle.color('yellow')
        self.turtle.penup()
        self.turtle.goto(self._x, self._y)
   
    def __str__(self):
        return f"Sun {self.name}: Position=({self.x}, {self.y}), Mass={self.mass}, Temp={self.temp}"
    
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

class Planet():
    def __init__(self, name, radius, mass, dist, x, y, vel_x, vel_y, color):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.dist = dist
        self._x = x
        self._y = y
        self._vel_x = float(vel_x)
        self._vel_y = float(vel_y)
        self.color = color
        self.shape = 'circle'
        
        self.turtle = turtle.Turtle()
        self.turtle.shape(self.shape)
        self.turtle.color(self.color)
        self.turtle.penup()
        self.turtle.goto(self.x, self.y)
        
        
    def __str__(self):
        return f"Planet {self.name}: Position=({self.x}, {self.y}), Velocity=({self.vel_x}, {self.vel_y})"
    
    def dist_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y 
        return math.sqrt(dx**2 + dy**2)
    
    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def vel_x(self):
        return self._vel_x

    @vel_x.setter
    def vel_x(self, value):
        self._vel_x = float(value)

    @property
    def vel_y(self):
        return self._vel_y

    @vel_y.setter
    def vel_y(self, value):
        self._vel_y = float(value)
class SolarSystem:
    def __init__(self):
        self.the_sun = None
        self.planets = []
    def add_sun(self, the_sun):
        self.the_sun = the_sun
    def add_planets(self, new_planet):
        if self.the_sun is None:
            raise ValueError("Sun must be added before planets.")
        self.planets.append(new_planet)
    def show_planets(self):
        if not self.planets:
            print("No planets to show.")
            return
    def move_planets(self):
        dt = .001
        for planet in self.planets:
            planet.x += dt * planet.vel_x
            planet.y += dt * planet.vel_y 
                     
            dist_x = self.the_sun.x - planet.x
            dist_y = self.the_sun.y - planet.y
            new_distance = math.sqrt(dist_x**2 + dist_y**2)
            
            acc_x = G * self.the_sun.mass * dist_x / new_distance**3
            acc_y = G * self.the_sun.mass * dist_y / new_distance**3

            planet.vel_x += dt * acc_x
            planet.vel_y += dt * acc_y

class Simulation:
    def __init__(self, solar_system, width, height, steps):
        self.solar_system = solar_system
        self.width = width
        self.height = height
        self.steps = steps

    def run(self):
        print("Simulation running!")
        for _ in range(self.steps):
            self.solar_system.move_planets()
    
if __name__ == '__main__':
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.setup(width=350, height=600)
    
    solar_system = SolarSystem()
    the_sun = Sun("SOL", 5000, 10000000, 5800, 0, 0)
    solar_system.add_sun(the_sun)

    earth = Planet("Earth", 47.5, 1, 1, 50, 0, 1, 2.0, "blue")  
    solar_system.add_planets(earth)

    mars = Planet("Mars", 40.5, 0.1, 1.52, 75, 0, 1, 1.5, "red")  
    solar_system.add_planets(mars)

    simulation = Simulation(solar_system, 500, 500, 2000)
    simulation.run()             
    
    turtle.done()
        
    
    
        

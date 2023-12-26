import push2_python

from Push2 import push
from Push2 import LightItUpButtons
from Grid import Pad
from Grid import GridMap
from Grid import DrawableObjectsRegistry


class FairyLight:
    def __init__(self, grid_map, initial_position=(7, 7), color='green'):
        self.grid_map = grid_map
        self.position = list(initial_position)
        self.color = color

    def move(self, direction):
      #  print("move")
        if direction == 'up':
            self.position[1] = (self.position[1] + 1) % self.grid_map.size
        elif direction == 'down':
            self.position[1] = (self.position[1] - 1) % self.grid_map.size
        elif direction == 'left':
            self.position[0] = (self.position[0] - 1) % self.grid_map.size
        elif direction == 'right':
            self.position[0] = (self.position[0] + 1) % self.grid_map.size
        print(self.position)
        self.draw_to_gridmap()

    def draw_to_gridmap(self):
        self.grid_map.set_desired_color(self.position[0], self.position[1], self.color)
 

# Initialize the grid map with the Push 2 instance
grid_map = GridMap(push)

# Initialize the DrawableObjectsRegistry
drawable_registry = DrawableObjectsRegistry()

fairy_light = FairyLight(grid_map)
drawable_registry.add_object(fairy_light)





#####-- Control handlers



@push2_python.on_button_pressed()
def on_button_pressed(push, button_name):
    grid_map.clear()

    print(f"pressed {button_name}")
    if button_name == 'Page Left':
        fairy_light.move('left')
    elif button_name == 'Page Right':
        fairy_light.move('right')
    elif button_name == 'Octave Down':
        fairy_light.move('down')
    elif button_name == 'Octave Up':
        fairy_light.move('up')
    
    drawable_registry.draw_all(grid_map)

 








class Pad:
    def __init__(self, push, x, y):
        self.push = push
        self.x = x
        self.y = y
        self.current_color = 'black'
        self.desired_color = 'black'

    def set_color(self, color):
        self.desired_color = color

    def render_color(self):
        """ Render the color of the pad on the Push 2 if it has changed. """
   
        if self.desired_color != self.current_color:
            self.push.pads.set_pad_color((self.x, self.y), self.desired_color)
            self.current_color = self.desired_color

    def forced_render_color(self):
        """ Render the color of the pad on the Push 2 if it has changed. """
        self.push.pads.set_pad_color((self.x, self.y), self.desired_color)
        self.current_color = self.desired_color


class GridMap:
    def __init__(self, push, size=8):
        self.push = push
        self.size = size
        self.grid = [[Pad(push, x, y) for y in range(size)] for x in range(size)]
        self.black_init()

    
    def force_set_all_pads_to_color(self, color):
        """ Set all pads on the grid to the specified color. """
        for x in range(self.size):
            for y in range(self.size):
                self.grid[x][y].set_color(color)
                self.grid[x][y].forced_render_color()


    
    def set_desired_color(self, x, y, color):
        """ Set the color of a specific pad using inverted y-axis coordinates. Push 2 lib coordinates are peculiar. 
            Lib counts (0,0 ) coordinates as left top corner and y goes from left to right.  
            Therefore we convert coordinates here in this wrapper.
        """
        self.set_desired_color_push_convention(self.size - 1- y,  x, color)

    def set_desired_color_push_convention(self, x, y, color):
         self.grid[x][y].set_color(color)

    def render(self):
        """ Update the Push 2 grid to match the desired state of each pad. """
        for x in range(self.size):
            for y in range(self.size):
                self.grid[x][y].render_color()
    
    def clear(self):
        for x in range(self.size):
            for y in range(self.size):
                self.grid[x][y].set_color("black")
 

    def black_init(self):
        """ Paint it black""" 
        self.force_set_all_pads_to_color("black")


class DrawableObjectsRegistry:
    def __init__(self):
        self.objects = []

    def add_object(self, obj):
        """ Add an object to the registry. """
        self.objects.append(obj)

    def remove_object(self, obj):
        """ Remove a specific object from the registry. """
        if obj in self.objects:
            self.objects.remove(obj)

    def draw_all(self, grid_map):
        """ Draw all registered objects on the grid. """
        # Clear the grid before drawing
        grid_map.clear()

        # Draw each object
        for obj in self.objects:
         #   print(f"drawing {obj}")
            obj.draw_to_gridmap()

        # Render the updated grid
        grid_map.render()

 



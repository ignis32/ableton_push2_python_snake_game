import push2_python
import time
from Push2 import push
from Push2 import LightItUpButtons
from Grid import Pad
from Grid import GridMap
from Grid import DrawableObjectsRegistry
from snake_led import DisplayManager
import random
import math

high_score = 0
update_interval = 0.5 

class Food:
    def __init__(self, grid_map, color='red'):
        self.grid_map = grid_map
        self.color = color
        self.position = self.random_position()

    def random_position(self):
        """ Generate a random position for the food. """
        x = random.randint(0, self.grid_map.size - 1)
        y = random.randint(0, self.grid_map.size - 1)
        return [x, y]

    def draw_to_gridmap(self):
        """ Draw the food on the grid. """
        self.grid_map.set_desired_color(self.position[0], self.position[1], self.color)

    def reset_position(self, snake_body):
        """ Reset the position of the food to a spot not occupied by the snake. """
        while True:
            self.position = self.random_position()
            if self.position not in snake_body:
                break

class Snake:
    def __init__(self, grid_map, initial_length=3, color='green'):
        self.grid_map = grid_map
        self.color = color
        self.direction = 'up'  # Initial direction
        self.score = 0

        # Calculate the start position for the head in the middle of the grid
        start_x = grid_map.size // 2
        start_y =  initial_length#grid_map.size // 2 + initial_length // 2

        self.body = self.initialize_body((start_x, start_y), initial_length)
   
    @property
    def head_position(self):
        """ Return the position of the snake's head. """
        return self.body[0]

    def initialize_body(self, start_position, length):
        """ Initialize the snake's body. """
        x, y = start_position
        body = []
        for i in range(length):
            # Since the snake extends upwards, decrement y for each new segment
            body_segment = [x, y - i]
            body.append(body_segment)
        return body

    def extend_body(self, initial=False):
        """ Extend the snake body by adding a new segment at the end. """
        tail = self.body[-1].copy()  # Use copy to avoid reference issues
        if initial:
            # During initialization, add segments in the opposite direction of movement
            tail[1] -= 1
        else:
            # After initialization, add segments based on current direction
            if self.direction == 'up':
                tail[1] += 1
            elif self.direction == 'down':
                tail[1] -= 1
            elif self.direction == 'left':
                tail[0] += 1
            elif self.direction == 'right':
                tail[0] -= 1

        # Add the new segment to the snake's body
        self.body.append(tail)

    def move(self):
        """ Move the snake in the current direction with edge warping. """
        head_x, head_y = self.body[0]

        if self.direction == 'up':
            new_head = [head_x, (head_y + 1) % self.grid_map.size]
        elif self.direction == 'down':
            new_head = [head_x, (head_y - 1) % self.grid_map.size]
        elif self.direction == 'left':
            new_head = [(head_x - 1) % self.grid_map.size, head_y]
        elif self.direction == 'right':
            new_head = [(head_x + 1) % self.grid_map.size, head_y]

        # Insert the new head at the beginning of the body list
        self.body.insert(0, new_head)

        # Remove the last segment of the snake's body
        self.body.pop()

    def change_direction(self, new_direction):
        """ Change the snake's direction. """
        #  logic to change direction, ensuring it's not the opposite of current direction
        opposite_directions = {
            'up': 'down',
            'down': 'up',
            'left': 'right',
            'right': 'left'
        }

        if new_direction != opposite_directions[self.direction]:
            self.direction = new_direction

    def grow(self):
        """ Grow the snake by adding a new segment at the end. """
        self.extend_body()
    
    def check_collision_with_body(self):
        """ Check if the snake has collided with itself. """
    
        if self.head_position in self.body[1:]:
            print("SO DEAD BRO")
            snake.__init__(self.grid_map)
            self.grid_map.force_set_all_pads_to_color("yellow")
            time.sleep(1)


    def check_collision_with_food(self, food):
        """ Check if the snake has collided with the food. """
        if self.head_position == food.position:
            
            return True
        return False
    
    def increment_score(self):
        self.score += 1
        global high_score
        if self.score > high_score:
            high_score = self.score

    def draw_to_gridmap(self):
        """ Draw the snake on the grid with the head in yellow and the body in green. """
        # Draw the head segment in yellow
        head_x, head_y = self.body[0]
        self.grid_map.set_desired_color(head_x, head_y, 'yellow')

       # Draw the rest of the body segments in the original color
        for segment in self.body[1:]:
            self.grid_map.set_desired_color(segment[0], segment[1], self.color)


# Initialize the grid map with the Push 2 instance
grid_map = GridMap(push)

# light up controls
push.buttons.set_button_color("Tap Tempo", 'white')  # we can use encoder nearby
push.buttons.set_button_color("Page Left", 'white')  
push.buttons.set_button_color("Page Right", 'white')   
push.buttons.set_button_color("Octave Down", 'white')   
push.buttons.set_button_color("Octave Up", 'white')  

# Initialize the DrawableObjectsRegistry
drawable_registry = DrawableObjectsRegistry()

# Create and add food to the registry
food = Food(grid_map)
drawable_registry.add_object(food)

snake = Snake(grid_map)
drawable_registry.add_object(snake)

drawable_registry.draw_all(grid_map)



# Usage in your game loop
display_manager = DisplayManager(push)

# ... within your game loop
display_manager.draw_scores(snake.score,high_score,update_interval)
#####-- Control handlers

@push2_python.on_button_pressed()
def on_button_pressed(push, button_name):
    try:
        grid_map.clear()

        print(f"pressed {button_name}")
        if button_name == 'Page Left':
            snake.change_direction('left')
        elif button_name == 'Page Right':
            snake.change_direction('right')
        elif button_name == 'Octave Down':
            snake.change_direction('down')
        elif button_name == 'Octave Up':
            snake.change_direction('up')
       # food.reset_position()
       # snake.move()
        snake.check_collision_with_body()

        if snake.check_collision_with_food(food):
            snake.grow()
            food.reset_position(snake.body)
        
        drawable_registry.draw_all(grid_map)
       # print(snake.body)
    except Exception as e:
       print(e)



@push2_python.on_encoder_rotated(push2_python.constants.ENCODER_TEMPO_ENCODER )
def on_encoder1_rotated(push, increment):
    global update_interval
    
    try:
        # Adjust the update interval logarithmically
        adjustment_factor = math.log10(update_interval + 1)
        new_interval = update_interval - increment * 0.05 * adjustment_factor

        # Limit the update interval to not less than 0.1 seconds and not more than 1 second
        update_interval = max(0.1, min(new_interval, 1.0))

        print(f"Adjusted update interval: {update_interval}")
    except Exception as e:
        print(e)
def game_loop():
    last_update_time = time.time()
     # seconds between updates

    while True:
        current_time = time.time()
        if current_time - last_update_time > update_interval:
            try:
                snake.move()
                snake.check_collision_with_body()
                

                if snake.check_collision_with_food(food):
                    snake.grow()
                    food.reset_position(snake.body)
                    snake.increment_score()

                drawable_registry.draw_all(grid_map)
                display_manager.draw_scores(snake.score, high_score,update_interval)  # Update the score display

                last_update_time = current_time

            except Exception as e:
                print(e)

 

game_loop()




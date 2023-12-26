import cairo
import numpy
import push2_python


class DisplayManager:
    def __init__(self, push):
        self.push = push
        self.WIDTH, self.HEIGHT = push2_python.constants.DISPLAY_LINE_PIXELS, push2_python.constants.DISPLAY_N_LINES

    
    def draw_scores(self, current_score, high_score, update_interval):
        """ Draw the current score and high score on the Push 2 display. """
        surface = cairo.ImageSurface(cairo.FORMAT_RGB16_565, self.WIDTH, self.HEIGHT)
        ctx = cairo.Context(surface)

        # Set up text properties
        ctx.set_source_rgb(1, 1, 1)  # White color
        font_size = self.HEIGHT // 6
        ctx.set_font_size(font_size)
        ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)

        # Draw current score
        ctx.move_to(10, font_size * 2)
        ctx.show_text(f"Score: {current_score}")

        # Draw high score
        ctx.move_to(10, font_size * 4)
        ctx.show_text(f"High Score: {high_score}")

        # Draw speed

        # Draw high score
        ctx.move_to(340, font_size * 4)
        ctx.show_text(f"Update interval: {update_interval:.3f}")

        # Convert canvas to numpy array and display it
        buf = surface.get_data()
        frame = numpy.ndarray(shape=(self.HEIGHT, self.WIDTH), dtype=numpy.uint16, buffer=buf)
        frame = frame.transpose()
        self.push.display.display_frame(frame, input_format=push2_python.constants.FRAME_FORMAT_RGB565)


# # Usage in your game loop
# display_manager = DisplayManager(push)

# # ... within your game loop
# display_manager.draw_score(snake.score)
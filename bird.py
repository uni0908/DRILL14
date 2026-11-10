from pico2d import load_image, get_canvas_width
import game_framework

MIN_SPEED = 120.0
MAX_SPEED = 200.0


class Bird:
    image = None

    def __init__(self, x=800, y=500, width=76):
        if Bird.image is None:
            Bird.image = load_image('bird_animation.png')
        self.x, self.y = x, y
        self.width = width
        self.height = width * (Bird.image.h / 3) / (Bird.image.w / 5)
        self.speed = MIN_SPEED
        self.direction = 1

    def update(self):
        dt = game_framework.frame_time
        if dt <= 0:
            return
        left = self.width / 2
        span = get_canvas_width() - self.width
        # Unfold the reflected path, then fold it back into the screen.
        offset = self.x - left
        phase = offset if self.direction == 1 else 2 * span - offset
        phase = (phase + self.speed * dt) % (2 * span)
        self.x = left + (phase if phase < span else 2 * span - phase)
        self.direction = 1 if phase < span else -1

    def draw(self):
        cell_width = self.image.w // 5
        cell_height = self.image.h // 3
        self.image.clip_composite_draw(0, self.image.h - cell_height,
                             cell_width, cell_height,
                             0, '' if self.direction == 1 else 'h',
                             self.x, self.y, self.width, self.height)

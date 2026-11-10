from pico2d import load_image, get_canvas_width
import game_framework

MIN_SPEED = 120.0
MAX_SPEED = 200.0
FRAME_COUNT = 14
FLAP_CYCLES_PER_SECOND = 1.0
FRAMES_PER_SECOND = FRAME_COUNT * FLAP_CYCLES_PER_SECOND


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
        self.frame = 0.0

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
        self.frame = (self.frame + FRAMES_PER_SECOND * dt) % FRAME_COUNT

    def draw(self):
        column = int(self.frame) % 5
        row = int(self.frame) // 5
        # Round each edge independently: the sheet is not evenly divisible.
        left = round(column * self.image.w / 5)
        right = round((column + 1) * self.image.w / 5)
        top = round(row * self.image.h / 3)
        bottom = round((row + 1) * self.image.h / 3)
        self.image.clip_composite_draw(left, self.image.h - bottom,
                             right - left, bottom - top,
                             0, '' if self.direction == 1 else 'h',
                             self.x, self.y, self.width, self.height)

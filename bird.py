from pico2d import load_image


class Bird:
    image = None

    def __init__(self, x=800, y=500, width=76):
        if Bird.image is None:
            Bird.image = load_image('bird_animation.png')
        self.x, self.y = x, y
        self.width = width
        self.height = width * (Bird.image.h / 3) / (Bird.image.w / 5)

    def update(self):
        pass

    def draw(self):
        cell_width = self.image.w // 5
        cell_height = self.image.h // 3
        self.image.clip_draw(0, self.image.h - cell_height,
                             cell_width, cell_height,
                             self.x, self.y, self.width, self.height)

import arcade
import random

SCREEN_WIDTH=800
SCREEN_HEIGHT=600
SCREEN_TITLE="Star Wars"
CRAI=15
ANGLE=20
SPEED=5


class Meteorit(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename, scale)
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = SCREEN_HEIGHT

    def update(self):
        self.center_y -=2
        if self.center_y==0:
            self.center_y = SCREEN_HEIGHT
            self.center_x=random.randint(CRAI,SCREEN_WIDTH-CRAI)
            window.score+=1

class Falcon(arcade.Sprite):
    def __init__(self,filename,scale):
        super().__init__(filename,scale)
        self.center_x=SCREEN_WIDTH/2
        self.center_y=SCREEN_HEIGHT/4

    def update(self):
        self.center_x+=self.change_x
        if self.right>SCREEN_WIDTH-CRAI or self.left <CRAI:
            self.change_x=0

class Game(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width, height, title)
        self.back = arcade.load_texture("background.jpg")
        self.meteorit=Meteorit("meteorit.png",0.8)
        self.falcon=Falcon("falcon.png",0.5)
        self.score = 0
        self.game = True


    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.back)
        self.meteorit.draw()
        self.falcon.draw()


    def update(self, delta_time):
        if self.game:
            self.meteorit.update()
            self.falcon.update()


    def on_key_press(self, key, modifiers):
        if key==arcade.key.LEFT:
            self.falcon.change_x=-SPEED
            self.falcon.angle=ANGLE
        if key==arcade.key.RIGHT:
            self.falcon.change_x=SPEED
            self.falcon.angle = -ANGLE


    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.falcon.change_x = 0
            self.falcon.angle =0



window=Game(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
arcade.run()
import arcade
import random

SCREEN_WIDTH=800
SCREEN_HEIGHT=600
SCREEN_TITLE="Star Wars"
CRAI=15
ANGLE=20
SPEED=5

class Enemy(arcade.Sprite):
    def __init__(self):
        super().__init__("TieFighter.png", 0.2)
        self.change_y=1.5
        self.angle=90

    def update(self):
        self.center_y -= self.change_y
        if self.center_y <0:
            self.kill()

class Laser(arcade.Sprite):
    def __init__(self):
        super().__init__("laser.png",0.8)
        self.center_x=window.falcon.center_x
        self.bottom=window.falcon.top
        self.change_y=5
        self.laser_sound=arcade.load_sound("laser.wav")

    def update(self):
        self.center_y+=self.change_y
        if self.center_y>SCREEN_HEIGHT:
            self.kill()

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
        self.meteorit=Meteorit("meteorit.png",0.2)
        self.falcon=Falcon("falcon.png",0.3)
        self.score = 0
        self.game = True

        self.lasers=arcade.SpriteList()
        self.enemies=arcade.SpriteList()

    def setup(self):
        for i in range(30):
            enemy=Enemy()
            enemy.center_x=random.randint(0, SCREEN_WIDTH)
            enemy.center_y=SCREEN_HEIGHT+i*50
            self.enemies.append(enemy)




    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.back)
        self.meteorit.draw()
        self.falcon.draw()
        self.lasers.draw()
        self.enemies.draw()
        arcade.draw_text(f"Счет:{int(self.score)}", SCREEN_WIDTH/2-20, SCREEN_HEIGHT-20, (250, 250, 250), 20)


    def update(self, delta_time):
        if self.game:
            self.meteorit.update()
            self.falcon.update()
            self.lasers.update()
            self.enemies.update()
            for laser in self.lasers:
                hit_list=arcade.check_for_collision_with_list(laser,self.enemies)
                if hit_list:
                    laser.kill()
                    for enemy in hit_list:
                        enemy.kill()
                        self.score += 1


    def on_key_press(self, key, modifiers):
        if key==arcade.key.LEFT:
            self.falcon.change_x=-SPEED
            self.falcon.angle=ANGLE
        if key==arcade.key.RIGHT:
            self.falcon.change_x=SPEED
            self.falcon.angle = -ANGLE
        if key==arcade.key.SPACE:
            laser=Laser()
            self.lasers.append(laser)
            arcade.play_sound(sound=laser.laser_sound,volume=0.2)


    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.falcon.change_x = 0
            self.falcon.angle =0



window=Game(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
window.setup()
arcade.run()
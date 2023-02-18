import arcade
import random

#Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Fantastic Fish"
SCALING = 2.0

#Classes
class SwimmingSprite(arcade.Sprite):

    def update(self):
        super().update()

        #Remove if off screen
        if self.right < 0:
            self.remove_from_sprite_lists()


class FantasticFish(arcade.Window):

    def __init__(self, width: int, height: int, title: str):
        super().__init__(width, height, title)

        #Sprite list
        self.enemies_list = arcade.SpriteList()
        self.bubbles_list = arcade.SpriteList()
        self.seaweed_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()
        self.score = 0

    def setup(self):
        arcade.set_background_color(arcade.color.DARK_BLUE)
        #The player
        self.player = arcade.Sprite("images/fish.png", SCALING)
        self.player.center_y = self.height / 2
        self.player.left = 10
        self.all_sprites.append(self.player)

        #Spawn shark
        arcade.schedule(self.add_shark, 1.0)

        #Spawn bubble
        arcade.schedule(self.add_bubble, 0.8)

        #Spawn seaweed
        arcade.schedule(self.add_seaweed, 0.8)

        #Backgroudn music
        self.background_music = arcade.load_sound(
            "sounds/Music.mp3"
        )

        #Play music
        arcade.play_sound(self.background_music, volume = 0.1)

        self.collided = False
        self.collision_timer = 0.0

    def add_shark(self, delta_time: float):

        #Shark spawn properties
        shark = SwimmingSprite("images/shark.png", SCALING)
        shark.left = random.randint(self.width, self.width + 10)
        shark.top = random.randint(10, self.height - 10)
        shark.velocity = (random.randint(-200, -50), 0)

        self.enemies_list.append(shark)
        self.all_sprites.append(shark)

    def add_bubble(self, delta_time: float):

        #Bubble spawn properties
        bubble = SwimmingSprite("images/bubble.png", SCALING)
        bubble.left = random.randint(self.width, self.width + 10)
        bubble.top = random.randint(10, self.height - 10)
        bubble.velocity = (random.randint(-300, -50), 0)

        self.bubbles_list.append(bubble)
        self.all_sprites.append(bubble)

    def add_seaweed(self, delta_time: float):

        #Seaweed spawn properties
        seaweed = SwimmingSprite("images/seaweed.png", SCALING)
        seaweed.left = random.randint(self.width, self.width + 10)
        seaweed.top = 70
        seaweed.velocity = (random.randint(-80,-75), 0)

        self.seaweed_list.append(seaweed)
        self.all_sprites.append(seaweed)

    def on_draw(self):
        #Render in the sprites
        arcade.start_render()
        self.all_sprites.draw()
        #Game text
        arcade.draw_text("Score: ",20, 1160, arcade.color.WHITE,16)
        arcade.draw_text(str(self.score), 100, 1160, arcade.color.WHITE,16)
        arcade.draw_text("Move with the WASD keys", 300, 1160, arcade.color.WHITE,16)


    def on_key_press(self, symbol: int, modifiers: int):

        #Movement keys
        if symbol == arcade.key.W:
            self.player.change_y = 250
        if symbol == arcade.key.S:
            self.player.change_y = -250
        if symbol == arcade.key.A:
            self.player.change_x = -250
        if symbol == arcade.key.D:
            self.player.change_x = 250

    def on_key_release(self, symbol: int, modifiers: int):

        #Stop moving
        if (
            symbol == arcade.key.W
            or symbol == arcade.key.S
        ):
            self.player.change_y = 0

        if (
            symbol == arcade.key.A
            or symbol == arcade.key.D
        ):
            self.player.change_x = 0

    def on_update(self, delta_time: float):
        self.score += 1
        if self.collided:
            self.collision_timer += delta_time
            if self.collision_timer > 1:
                arcade.close_window()
            return
        #Game will stop if there is a collision
        if self.player.collides_with_list(self.enemies_list):
            self.collided = True
            self.collision_timer = 0
        #Update all sprites
        for sprite in self.all_sprites:
            sprite.center_x = int(
                sprite.center_x + sprite.change_x * delta_time
            )
            sprite.center_y = int(
                sprite.center_y + sprite.change_y * delta_time
            )
        #Boundaries
        if self.player.top > self.height:
            self.player.top = self.height
        if self.player.right > self.width:
            self.player.right = self.width
        if self.player.bottom < 0:
            self.player.bottom = 0
        if self.player.left < 0:
            self.player.left = 0

#Run game
if __name__ == "__main__":
    fish_game = FantasticFish(
        int(SCREEN_WIDTH * SCALING), int(SCREEN_HEIGHT * SCALING), SCREEN_TITLE
    )
    fish_game.setup()
    arcade.run()

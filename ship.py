from superwires import games


class Ship(games.Sprite):
    image = games.load_image("ship.bmp")
    ROTATION_STEP = 3

    def update(self):
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= Ship.ROTATION_STEP


if __name__ == '_main_':
    print("Its module!")

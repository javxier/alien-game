class GameStats:
    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.reset_stats()
        self.last_ships_left = self.ships_left

    def reset_stats(self): self.ships_left = self.settings.ship_limit
    def ship_hit(self):
        self.ships_left -= 1
        n = self.ships_left
        print(f'SHIP HIT!', end=' ')
        if self.last_ships_left != self.ships_left:
            print(f'{self.ships_left} ship{"s" if n != 1 else ""} left')
            self.last_ships_left = self.ships_left
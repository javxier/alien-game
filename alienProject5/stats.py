import os

class Stats:
    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.reset_stats()
        self.last_ships_left = self.ships_left
        self.score = 0
        self.level = 0
        self.highscore = self.load_high_score()

    def __del__(self): self.save_high_score()    

    def load_high_score(self): 
        try:
            with open("highscore.txt", "r") as f:
                return int(f.read())    
        except:
                return 0
        
    def save_high_score(self):
        try:
            with open("highscore.txt", "w+") as f:
                f.write(str(round(self.highscore, -1)))  # 314.15 --> 310,  (0) --> 314
        except:
            print("highscore.txt not found...")

    def get_score(self): return self.score
    def get_highscore(self): return self.highscore
    def get_level(self): return self.level
    def get_ships_left(self): return self.ships_left
    def reset_stats(self): self.ships_left = self.settings.ship_limit
    def level_up(self): 
        self.level += 1
        print("leveling up: level is now ", self.level)
    def alien_hit(self, alien):
        self.score += alien.points
        self.highscore = max(self.score, self.highscore)
    def ship_hit(self):
        self.ships_left -= 1
        n = self.ships_left
        print(f'SHIP HIT!', end=' ')
        if self.last_ships_left != self.ships_left:
            print(f'{self.ships_left} ship{"s" if n != 1 else ""} left')
            self.last_ships_left = self.ships_left

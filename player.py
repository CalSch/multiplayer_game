import pyray as rl
from game_util import *

player_size=rl.Vector2(30,30)
player_speed=2.5


class Player:
    def __init__(self, pos: rl.Vector2, color: rl.Color):
        self.pos=pos
        self.color=color
        self.old_pos=rl.Vector2(0,0)
        
    def draw(self):
        rl.draw_rectangle(
            int(self.pos.x-player_size.x/2),
            int(self.pos.y-player_size.y),
            int(player_size.x),
            int(player_size.y),
            self.color)
    
    def update(self):
        if rl.is_key_down(rl.KEY_W) or rl.is_key_down(rl.KEY_UP):
            self.pos = addvec(self.pos , rl.Vector2(0, -player_speed))
        if rl.is_key_down(rl.KEY_D) or rl.is_key_down(rl.KEY_RIGHT):
            self.pos = addvec(self.pos , rl.Vector2(player_speed, 0))
        if rl.is_key_down(rl.KEY_A) or rl.is_key_down(rl.KEY_LEFT):
            self.pos = addvec(self.pos , rl.Vector2(-player_speed, 0))
        if rl.is_key_down(rl.KEY_S) or rl.is_key_down(rl.KEY_DOWN):
            self.pos = addvec(self.pos , rl.Vector2(0, player_speed))
        
        self.old_pos=self.pos
            
def get_player_rect(player: Player):
    return rl.Rectangle(
        player.pos.x-player_size.x/2,
        player.pos.y-player_size.y,
        player_size.x,
        player_size.y
    )
import pyray as rl

def addvec(vec1: rl.Vector2, vec2: rl.Vector2):
    return rl.Vector2(
        vec1.x+vec2.x,
        vec1.y+vec2.y
    )
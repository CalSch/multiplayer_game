import os

# set the path before raylib is imported.
os.environ["RAYLIB_BIN_PATH"] = "/home/calvin/Coding/Python/multiplayer_game/raylib-2.0.0-Linux-amd64/lib/"

# import raylibpy as rl
import pyray as rl
import player

rl.init_window(200,200,"bob")

old_mouse_pos=rl.Vector2(0,0)

guy = player.Player(rl.Vector2(50,100),rl.RED)

rl.hide_cursor()

mouse_delta=rl.Vector2(0,0)

rl.set_target_fps(60)

while not rl.window_should_close():


    rl.begin_drawing()
    mouse_delta=rl.get_mouse_delta()
    guy.update()

    rl.clear_background(rl.WHITE)
    
    guy.draw()

    rl.draw_circle(
        int(rl.get_mouse_x()),
        int(rl.get_mouse_y()),
        5,rl.GREEN)

    rl.end_drawing()

    old_mouse_pos=rl.get_mouse_position()

rl.show_cursor()

rl.close_window()
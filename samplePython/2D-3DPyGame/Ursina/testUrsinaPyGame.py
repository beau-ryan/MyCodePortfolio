

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


# --- GAME ENGINE ---
app = Ursina()

# World Setup
window.title = 'Python 3D Open World'
window.borderless = False
window.exit_button.visible = False
window.fps_counter.enabled = True


# Create Ground
Entity(model='plane', scale=100, texture='white_cube', texture_scale=(100,100), color=color.dark_gray, collider='box')



# Environment Lighting
sun = DirectionalLight(parent=camera)
sun.look_at(Vec3(1, -1, 1))
Sky()



app.run()
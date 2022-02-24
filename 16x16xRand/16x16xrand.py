import bpy
import random
from time import sleep

spacing = 2
cube_count = 16
for x in range(0, cube_count):
    sleep(0.05)
    scale = (1, 1, 1)
    for y in range(0, cube_count):
        loc = (x * spacing, y * spacing, 1)
        
        if random.random() < 0.1:
            scale = (1, 1, random.uniform(3, 6))
        bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=loc, scale=scale)
        
        item = bpy.context.object
        if random.random() < 0.2:
            item.data.materials.append(bpy.data.materials["Material.003"])
        else:
            item.data.materials.append(bpy.data.materials["Material.002"])
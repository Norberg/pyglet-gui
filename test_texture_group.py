#!/usr/bin/env python3
"""Test ThemeTextureGroup specifically to find the sorting issue"""

import pyglet
from pyglet import gl

# Import our ThemeTextureGroup
import sys
sys.path.insert(0, '/workspace')
from pyglet_gui.theme.elements import ThemeTextureGroup
from pyglet_gui.manager import ViewerManagerGroup

# Create a simple texture for testing
def create_test_texture():
    # Create a simple 1x1 white texture
    image = pyglet.image.SolidColorImagePattern((255, 255, 255, 255)).create_image(1, 1)
    return image.get_texture()

# Create a batch and test ThemeTextureGroup
batch = pyglet.graphics.Batch()

try:
    # Create the hierarchy like our Manager does
    root_group = ViewerManagerGroup()
    
    # Create a regular Group
    regular_group = pyglet.graphics.Group(order=20, parent=root_group)
    
    # Create a ThemeTextureGroup
    texture = create_test_texture()
    theme_group = ThemeTextureGroup(texture, regular_group)
    
    print(f"✅ Root group: {root_group}")
    print(f"✅ Regular group: {regular_group}")
    print(f"✅ Theme group: {theme_group}")
    
    # Check if they have order attributes
    print(f"✅ root_group.order = {root_group.order}")
    print(f"✅ regular_group.order = {regular_group.order}")
    
    # Check if ThemeTextureGroup has order
    if hasattr(theme_group, 'order'):
        print(f"✅ theme_group.order = {theme_group.order}")
    else:
        print(f"❌ theme_group has no order attribute")
    
    # Test creating vertex lists with these groups
    program = pyglet.graphics.get_default_shader()
    
    # Create vertex list with ThemeTextureGroup
    vertex_list = program.vertex_list(3, gl.GL_TRIANGLES,
                                      batch=batch,
                                      group=theme_group,
                                      position=('f', [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.5, 1.0, 0.0]),
                                      colors=('Bn', [255, 0, 0, 255, 0, 255, 0, 255, 0, 0, 255, 255]),
                                      tex_coords=('f', [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.5, 1.0, 0.0]))
    
    print(f"✅ Vertex list created successfully")
    
    # This is where the error happens - when batch tries to sort
    print("Testing batch._update_draw_list()...")
    batch._update_draw_list()
    print(f"✅ Batch update/sorting works!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
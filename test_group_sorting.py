#!/usr/bin/env python3
"""Test Group sorting behavior in pyglet 2.1+"""

import pyglet
from pyglet import gl

# Create a simple batch and groups to test sorting
batch = pyglet.graphics.Batch()

# Create different types of groups
try:
    # Test if creating Groups with different patterns works
    group1 = pyglet.graphics.Group(order=1)
    group2 = pyglet.graphics.Group(order=2) 
    print(f"✅ Basic Group creation works: {group1}, {group2}")
    
    # Test if they have order attributes
    print(f"✅ group1.order = {group1.order}")
    print(f"✅ group2.order = {group2.order}")
    
    # Test comparison
    print(f"✅ group1 < group2 = {group1 < group2}")
    
    # Test creating a vertex list with groups
    program = pyglet.graphics.get_default_shader()
    
    vertex_list1 = program.vertex_list(3, gl.GL_TRIANGLES,
                                      batch=batch,
                                      group=group1,
                                      position=('f', [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.5, 1.0, 0.0]),
                                      colors=('Bn', [255, 0, 0, 255, 0, 255, 0, 255, 0, 0, 255, 255]))
    
    vertex_list2 = program.vertex_list(3, gl.GL_TRIANGLES,
                                      batch=batch,
                                      group=group2,
                                      position=('f', [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.5, 1.0, 0.0]),
                                      colors=('Bn', [255, 0, 0, 255, 0, 255, 0, 255, 0, 0, 255, 255]))
    
    print(f"✅ Vertex lists created successfully")
    
    # Test if sorting works by trying to update the batch
    batch._update_draw_list()
    print(f"✅ Batch update/sorting works!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
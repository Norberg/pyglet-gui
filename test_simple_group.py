#!/usr/bin/env python3
"""Test simple Group creation to see if our syntax is causing issues"""

import pyglet
from pyglet import gl

try:
    # Test basic Group creation like in documentation
    print("Testing Group creation...")
    
    # Test 1: Basic Group creation (documentation syntax)
    group1 = pyglet.graphics.Group(order=0)
    print(f"✅ Group 1: {group1}")
    print(f"   order: {group1.order}")
    
    # Test 2: Group with parent
    group2 = pyglet.graphics.Group(order=1, parent=group1) 
    print(f"✅ Group 2: {group2}")
    print(f"   order: {group2.order}")
    print(f"   parent: {group2.parent}")
    
    # Test 3: Can we compare them?
    print(f"✅ group1 < group2: {group1 < group2}")
    
    # Test 4: Create batch and vertex lists
    batch = pyglet.graphics.Batch()
    program = pyglet.graphics.get_default_shader()
    
    vlist1 = program.vertex_list(3, gl.GL_TRIANGLES,
                                batch=batch,
                                group=group1,
                                position=('f', [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.5, 1.0, 0.0]),
                                colors=('Bn', [255, 0, 0, 255, 0, 255, 0, 255, 0, 0, 255, 255]))
    
    vlist2 = program.vertex_list(3, gl.GL_TRIANGLES,
                                batch=batch,
                                group=group2,
                                position=('f', [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.5, 1.0, 0.0]),
                                colors=('Bn', [255, 0, 0, 255, 0, 255, 0, 255, 0, 0, 255, 255]))
    
    print("✅ Vertex lists created")
    
    # Test 5: Can batch sort them?
    print("Testing batch._update_draw_list()...")
    batch._update_draw_list()
    print("✅ Batch sorting works!")
    
    print("✅ All tests passed!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
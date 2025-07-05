#!/usr/bin/env python3
"""Test to isolate TextureGroup ordering issue"""

import pyglet
from pyglet import gl

try:
    # Create texture for testing
    texture = pyglet.image.SolidColorImagePattern((255, 255, 255, 255)).create_image(1, 1).get_texture()
    
    # Test 1: Regular Group
    regular_group = pyglet.graphics.Group(order=10)
    print(f"✅ Regular Group: {regular_group}")
    print(f"   Has order: {hasattr(regular_group, 'order')}")
    if hasattr(regular_group, 'order'):
        print(f"   Order value: {regular_group.order}")
        print(f"   Order type: {type(regular_group.order)}")
    
    # Test 2: TextureGroup
    texture_group = pyglet.graphics.TextureGroup(texture, parent=regular_group)
    print(f"\n✅ TextureGroup: {texture_group}")
    print(f"   Has order: {hasattr(texture_group, 'order')}")
    if hasattr(texture_group, 'order'):
        print(f"   Order value: {texture_group.order}")
        print(f"   Order type: {type(texture_group.order)}")
    else:
        print("   ❌ TextureGroup has no order attribute!")
    
    # Test 3: Try to compare them
    print(f"\nTesting comparison...")
    try:
        result = regular_group < texture_group
        print(f"✅ regular_group < texture_group: {result}")
    except Exception as e:
        print(f"❌ Comparison failed: {e}")
    
    try:
        result = texture_group < regular_group  
        print(f"✅ texture_group < regular_group: {result}")
    except Exception as e:
        print(f"❌ Comparison failed: {e}")
    
    # Test 4: Create batch and see if sorting works
    print(f"\nTesting with batch...")
    batch = pyglet.graphics.Batch()
    program = pyglet.graphics.get_default_shader()
    
    # Create vertex lists
    vlist1 = program.vertex_list(3, gl.GL_TRIANGLES,
                                batch=batch,
                                group=regular_group,
                                position=('f', [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.5, 1.0, 0.0]),
                                colors=('Bn', [255, 0, 0, 255, 0, 255, 0, 255, 0, 0, 255, 255]))
    
    vlist2 = program.vertex_list(3, gl.GL_TRIANGLES,
                                batch=batch,
                                group=texture_group,
                                position=('f', [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.5, 1.0, 0.0]),
                                colors=('Bn', [255, 0, 0, 255, 0, 255, 0, 255, 0, 0, 255, 255]),
                                tex_coords=('f', [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.5, 1.0, 0.0]))
    
    print("✅ Vertex lists created")
    
    # Test sorting
    print("Testing batch._update_draw_list()...")
    batch._update_draw_list()
    print("✅ Batch sorting works!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
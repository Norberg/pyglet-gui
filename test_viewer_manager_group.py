#!/usr/bin/env python3
"""Test ViewerManagerGroup specifically to reproduce the sorting issue"""

import pyglet
from pyglet import gl
import sys
sys.path.insert(0, '/workspace')

try:
    # Import our ViewerManagerGroup
    from pyglet_gui.manager import ViewerManagerGroup
    
    print("Testing ViewerManagerGroup creation...")
    
    # Create ViewerManagerGroup like in Manager
    root_group = ViewerManagerGroup()
    print(f"✅ Root group: {root_group}")
    print(f"   Type: {type(root_group)}")
    print(f"   Order: {root_group.order}")
    print(f"   Own order: {root_group.own_order}")
    
    # Create child Groups like in Manager.__init__
    panel_group = pyglet.graphics.Group(order=10, parent=root_group)
    background_group = pyglet.graphics.Group(order=20, parent=root_group)
    foreground_group = pyglet.graphics.Group(order=30, parent=root_group)
    highlight_group = pyglet.graphics.Group(order=40, parent=root_group)
    
    print(f"✅ Panel group: {panel_group}")
    print(f"✅ Background group: {background_group}")
    print(f"✅ Foreground group: {foreground_group}")
    print(f"✅ Highlight group: {highlight_group}")
    
    # Test comparisons
    print("\nTesting comparisons...")
    try:
        print(f"✅ root_group < panel_group: {root_group < panel_group}")
        print(f"✅ panel_group < background_group: {panel_group < background_group}")
        print(f"✅ background_group < foreground_group: {background_group < foreground_group}")
    except Exception as e:
        print(f"❌ Comparison error: {e}")
        import traceback
        traceback.print_exc()
    
    # Test with batch
    print("\nTesting with batch...")
    batch = pyglet.graphics.Batch()
    program = pyglet.graphics.get_default_shader()
    
    # Create vertex lists with different groups
    vlist1 = program.vertex_list(3, gl.GL_TRIANGLES,
                                batch=batch,
                                group=panel_group,
                                position=('f', [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.5, 1.0, 0.0]),
                                colors=('Bn', [255, 0, 0, 255, 0, 255, 0, 255, 0, 0, 255, 255]))
    
    vlist2 = program.vertex_list(3, gl.GL_TRIANGLES,
                                batch=batch,
                                group=background_group,
                                position=('f', [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.5, 1.0, 0.0]),
                                colors=('Bn', [255, 0, 0, 255, 0, 255, 0, 255, 0, 0, 255, 255]))
    
    print("✅ Vertex lists created")
    
    # This is where it might fail
    print("Testing batch._update_draw_list()...")
    batch._update_draw_list()
    print("✅ Batch sorting works!")
    
    print("\n✅ All ViewerManagerGroup tests passed!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
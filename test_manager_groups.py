#!/usr/bin/env python3
"""Test ViewerManagerGroup sorting behavior specifically"""

import pyglet
from pyglet import gl

# Import our ViewerManagerGroup
import sys
sys.path.insert(0, '/workspace')
from pyglet_gui.manager import ViewerManagerGroup

# Create a simple batch to test with
batch = pyglet.graphics.Batch()

try:
    # Create ViewerManagerGroup objects like our Manager does
    root_group = ViewerManagerGroup()
    
    # Create child groups like in Manager.__init__
    panel_group = pyglet.graphics.Group(order=10, parent=root_group)
    background_group = pyglet.graphics.Group(order=20, parent=root_group)
    foreground_group = pyglet.graphics.Group(order=30, parent=root_group)
    highlight_group = pyglet.graphics.Group(order=40, parent=root_group)
    
    print(f"✅ ViewerManagerGroup created: {root_group}")
    print(f"✅ Child groups created: {panel_group}, {background_group}")
    
    # Test our group properties
    print(f"✅ root_group.order = {root_group.order}")
    print(f"✅ root_group.own_order = {root_group.own_order}")
    print(f"✅ panel_group.order = {panel_group.order}")
    
    # Test creating vertex lists like our elements do
    program = pyglet.graphics.get_default_shader()
    
    vertex_list1 = program.vertex_list(3, gl.GL_TRIANGLES,
                                      batch=batch,
                                      group=panel_group,
                                      position=('f', [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.5, 1.0, 0.0]),
                                      colors=('Bn', [255, 0, 0, 255, 0, 255, 0, 255, 0, 0, 255, 255]))
    
    vertex_list2 = program.vertex_list(3, gl.GL_TRIANGLES,
                                      batch=batch,
                                      group=background_group,
                                      position=('f', [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.5, 1.0, 0.0]),
                                      colors=('Bn', [255, 0, 0, 255, 0, 255, 0, 255, 0, 0, 255, 255]))
    
    print(f"✅ Vertex lists created successfully")
    
    # This is where the error happens - when batch tries to sort
    print("Testing batch._update_draw_list()...")
    batch._update_draw_list()
    print(f"✅ Batch update/sorting works!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
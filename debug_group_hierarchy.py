#!/usr/bin/env python3
"""Debug Group hierarchy to find the sorting issue"""

import pyglet
from pyglet import gl

# Import everything we need
import sys
sys.path.insert(0, '/workspace')

try:
    # Set up display
    window = pyglet.window.Window(640, 480, resizable=True, vsync=True)
    batch = pyglet.graphics.Batch()
    
    # Create theme like in button_focus.py
    from pyglet_gui.theme import Theme
    
    theme = Theme({
        "font": "Lucida Grande",
        "font_size": 12,
        "gui_color": [255, 255, 255, 255],
        "text_color": [255, 255, 255, 255],
        "button": {
            "up": {
                "image": {
                    "source": "button.png",
                    "frame": [6, 6, 3, 3],
                    "padding": [12, 12, 4, 2]
                }
            }
        }
    }, resources_path='examples/../theme/')
    
    print("✅ Theme created successfully")
    
    # Create UI elements step by step and debug each
    from pyglet_gui.gui import Label, FocusButton
    from pyglet_gui.containers import VerticalContainer
    from pyglet_gui.manager import Manager
    
    print("Creating Label...")
    label = Label("Test Label")
    print(f"✅ Label created: {label}")
    
    print("Creating FocusButton...")
    button = FocusButton("Test Button")
    print(f"✅ FocusButton created: {button}")
    
    print("Creating VerticalContainer...")
    container = VerticalContainer([label, button])
    print(f"✅ VerticalContainer created: {container}")
    
    print("Creating Manager...")
    manager = Manager(container, window=window, batch=batch, theme=theme)
    print(f"✅ Manager created: {manager}")
    
    # Now let's analyze the batch's groups
    print("\n🔍 Analyzing batch groups:")
    
    # Get all groups from batch
    groups_found = set()
    
    # Iterate through vertex lists to find groups
    for domain in batch.group_map.values():
        for group in domain.allocator.groups.keys():
            groups_found.add(group)
            print(f"  Found group: {group}")
            print(f"    Type: {type(group)}")
            if hasattr(group, 'order'):
                print(f"    Order: {group.order} (type: {type(group.order)})")
            else:
                print(f"    No order attribute!")
            if hasattr(group, 'parent'):
                print(f"    Parent: {group.parent}")
            print()
    
    print(f"Total groups found: {len(groups_found)}")
    
    # Try to manually sort groups to see what happens
    print("\n🔍 Testing manual sorting of found groups:")
    groups_list = list(groups_found)
    
    for i, group1 in enumerate(groups_list):
        for j, group2 in enumerate(groups_list):
            if i != j:
                try:
                    result = group1 < group2
                    print(f"  {group1} < {group2} = {result}")
                except Exception as e:
                    print(f"  ❌ Error comparing {group1} < {group2}: {e}")
    
    print("\n🔍 Testing batch._update_draw_list()...")
    batch._update_draw_list()
    print("✅ Batch update works!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
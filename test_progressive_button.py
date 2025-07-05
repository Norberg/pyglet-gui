#!/usr/bin/env python3
"""Progressive test building up to full button_focus.py to isolate the issue"""

import pyglet
from pyglet import gl
import sys
sys.path.insert(0, '/workspace')

try:
    # Set up display first
    window = pyglet.window.Window(640, 480, resizable=True, vsync=True)
    batch = pyglet.graphics.Batch()
    
    print("✅ Window and batch created")
    
    # Create theme
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
    
    print("✅ Theme created")
    
    # Test 1: Just Label
    from pyglet_gui.gui import Label
    from pyglet_gui.manager import Manager
    
    print("\nTest 1: Just Label")
    label = Label("Test Label")
    manager1 = Manager(label, window=window, batch=batch, theme=theme)
    print("✅ Label + Manager created")
    
    # Test batch sorting
    batch._update_draw_list()
    print("✅ Batch sorting works with Label")
    
    # Test 2: Add FocusButton
    print("\nTest 2: Add FocusButton")
    from pyglet_gui.gui import FocusButton
    button = FocusButton("Test Button")
    
    # Delete old manager first
    manager1.delete()
    
    # Create new manager with button
    manager2 = Manager(button, window=window, batch=batch, theme=theme)
    print("✅ FocusButton + Manager created")
    
    # Test batch sorting
    batch._update_draw_list()
    print("✅ Batch sorting works with FocusButton")
    
    # Test 3: Add VerticalContainer
    print("\nTest 3: Add VerticalContainer")
    from pyglet_gui.containers import VerticalContainer
    
    # Delete old manager
    manager2.delete()
    
    container = VerticalContainer([
        Label("Try (SHIFT+)TAB and ENTER"),
        FocusButton("Button 1")
    ])
    
    manager3 = Manager(container, window=window, batch=batch, theme=theme)
    print("✅ VerticalContainer + Manager created")
    
    # Test batch sorting - this might be where it fails
    print("Testing batch sorting with container...")
    batch._update_draw_list()
    print("✅ Batch sorting works with VerticalContainer")
    
    # Test 4: Multiple buttons like in original
    print("\nTest 4: Multiple buttons like original")
    manager3.delete()
    
    container_full = VerticalContainer([
        Label("Try (SHIFT+)TAB and ENTER"),
        FocusButton("Button 1"),
        FocusButton("Button 2"),
        FocusButton("Button 3")
    ])
    
    manager4 = Manager(container_full, window=window, batch=batch, theme=theme)
    print("✅ Full container + Manager created")
    
    # Test batch sorting - this might be where it fails
    print("Testing batch sorting with full container...")
    batch._update_draw_list()
    print("✅ Batch sorting works with full container!")
    
    print("\n🎉 All tests passed! The issue might be with event loop or drawing...")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
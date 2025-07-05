#!/usr/bin/env python3
"""Minimal test replicating button_focus.py to find the Group sorting issue"""

import pyglet
from pyglet import gl

# Import everything we need
import sys
sys.path.insert(0, '/workspace')

try:
    # Set up display first
    window = pyglet.window.Window(640, 480, resizable=True, vsync=True)
    batch = pyglet.graphics.Batch()
    
    @window.event
    def on_draw():
        window.clear()
        batch.draw()
    
    # Create theme like in button_focus.py
    from pyglet_gui.theme import Theme
    
    theme = Theme({
        "font": "Lucida Grande",
        "font_size": 12,
        "font_size_small": 10,
        "gui_color": [255, 255, 255, 255],
        "disabled_color": [160, 160, 160, 255],
        "text_color": [255, 255, 255, 255],
        "focus_color": [255, 255, 255, 64],
        "button": {
            "down": {
                "focus": {
                    "image": {
                        "source": "button-highlight.png",
                        "frame": [8, 6, 2, 2],
                        "padding": [18, 18, 8, 6]
                    }
                },
                "image": {
                    "source": "button-down.png",
                    "frame": [6, 6, 3, 3],
                    "padding": [12, 12, 4, 2]
                },
                "text_color": [0, 0, 0, 255]
            },
            "up": {
                "focus": {
                    "image": {
                        "source": "button-highlight.png",
                        "frame": [8, 6, 2, 2],
                        "padding": [18, 18, 8, 6]
                    }
                },
                "image": {
                    "source": "button.png",
                    "frame": [6, 6, 3, 3],
                    "padding": [12, 12, 4, 2]
                }
            }
        }
    }, resources_path='examples/../theme/')
    
    print("✅ Theme created successfully")
    
    # Create a simple Label first
    from pyglet_gui.gui import Label
    label = Label("Test Label")
    
    print("✅ Label created successfully")
    
    # Create a Manager with just the label
    from pyglet_gui.manager import Manager
    manager = Manager(label, window=window, batch=batch, theme=theme)
    
    print("✅ Manager created successfully")
    
    # Test batch sorting manually first
    print("Testing batch._update_draw_list()...")
    batch._update_draw_list()
    print("✅ Batch update/sorting works!")
    
    print("✅ Starting pyglet.app.run() - this may trigger the error...")
    
    # Schedule a function to exit after a short time
    def exit_after_delay(dt):
        print("✅ App ran successfully, exiting...")
        pyglet.app.exit()
    
    pyglet.clock.schedule_once(exit_after_delay, 1.0)
    
    # This is where the error should occur if it's going to happen
    pyglet.app.run()
    
    print("✅ All tests passed!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
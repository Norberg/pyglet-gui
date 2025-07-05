#!/usr/bin/env python3
"""
Focused test to verify our Batch API fix works.
This specifically tests the vertex_list creation without display issues.
"""

import sys
import os

# Mock the display to avoid "No standard config is available" errors
import unittest.mock

# Add the workspace to path so we can import pyglet_gui
sys.path.insert(0, '/workspace')

def test_batch_api_fix():
    """Test that our Batch API fix works by creating vertex lists."""
    print("🧪 Testing Batch API fix...")
    
    try:
        # First, let's mock the display-related stuff that causes problems
        with unittest.mock.patch('pyglet.gl._create_shadow_window'):
            import pyglet
            
            # Create the basic pyglet objects we need
            batch = pyglet.graphics.Batch()
            group = pyglet.graphics.Group(order=0)
            
            print("✅ Created Batch and Group successfully")
            
            # Test the vertex_list creation with batch parameter
            # This is what our fixed code does
            try:
                vertex_data = (10, 15, 30, 35, 50, 55, 70, 75)
                color_data = (255, 0, 0, 255) * 2
                
                vlist = pyglet.graphics.vertex_list(
                    4,  # vertex count
                    ('v2i', vertex_data),
                    ('c4B', color_data),
                    batch=batch,
                    group=group
                )
                
                print("✅ vertex_list(batch=batch, group=group) creation successful!")
                print(f"   Created vertex list with {len(vertex_data)//2} vertices")
                
                # Test that we can access the vertex data
                if hasattr(vlist, 'vertices'):
                    print("✅ Vertex list has 'vertices' attribute")
                else:
                    print("❌ Vertex list missing 'vertices' attribute")
                    return False
                
                # Clean up
                vlist.delete()
                print("✅ Vertex list deletion successful")
                
                return True
                
            except Exception as e:
                print(f"❌ vertex_list creation failed: {e}")
                return False
                
    except Exception as e:
        print(f"❌ Basic pyglet setup failed: {e}")
        return False


def test_element_creation_syntax():
    """Test that our elements.py code compiles and can be instantiated."""
    print("\n🧪 Testing element creation syntax...")
    
    try:
        # Mock display to avoid config issues
        with unittest.mock.patch('pyglet.gl._create_shadow_window'):
            import pyglet
            from pyglet_gui.theme.elements import GraphicElement, TextureGraphicElement
            
            # Create basic objects
            batch = pyglet.graphics.Batch()
            group = pyglet.graphics.Group()
            color = (255, 255, 255, 255)
            
            # Create a mock texture
            class MockTexture:
                def __init__(self):
                    self.width = 32
                    self.height = 32
                    self.tex_coords = [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0]
            
            mock_texture = MockTexture()
            
            print("✅ Basic setup completed")
            
            # Test that our classes can be instantiated (this will call _load())
            try:
                # This would fail with the old Batch.add() API
                texture_element = TextureGraphicElement(mock_texture, color, batch, group)
                print("✅ TextureGraphicElement creation successful!")
                
                # Clean up
                if texture_element._vertex_list:
                    texture_element.unload()
                    print("✅ TextureGraphicElement cleanup successful")
                
                return True
                
            except Exception as e:
                print(f"❌ Element creation failed: {e}")
                print(f"   This suggests our Batch API fix may need adjustment")
                return False
                
    except Exception as e:
        print(f"❌ Element testing setup failed: {e}")
        return False


def main():
    """Run the batch fix verification tests."""
    print("🚀 Testing Batch API fix")
    print("=" * 50)
    
    tests = [
        test_batch_api_fix,
        test_element_creation_syntax,
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"❌ Test {test.__name__} failed with exception: {e}")
    
    print("\n" + "=" * 50)
    print(f"📊 Batch Fix Test Results: {passed}/{total} passed")
    
    if passed == total:
        print("\n🎉 BATCH API FIX VERIFIED!")
        print("✅ vertex_list(batch=batch) approach works correctly")
        print("✅ Elements can be created without Batch.add() errors")
        print("\n🔧 Ready to test with actual pyglet GUI!")
    else:
        print(f"\n❌ {total - passed} tests failed.")
        print("   The Batch API fix may need further adjustment.")
    
    return passed == total


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
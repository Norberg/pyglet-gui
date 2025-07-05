#!/usr/bin/env python3
"""
Script to automatically apply pyglet2+ compatibility fixes to pyglet-gui
Run this after cloning the original repository.
"""

import os
import sys
import shutil
from pathlib import Path
import re

def apply_setup_py_fix():
    """Update setup.py with new version requirements"""
    setup_file = "setup.py"
    if not os.path.exists(setup_file):
        print(f"❌ {setup_file} not found")
        return False
    
    with open(setup_file, 'r') as f:
        content = f.read()
    
    # Apply fixes
    content = re.sub(r'pyglet>=1\.\d+', 'pyglet>=2.0', content)
    content = re.sub(r"version='0\.1'", "version='0.2'", content)
    
    with open(setup_file, 'w') as f:
        f.write(content)
    
    print("✅ Updated setup.py")
    return True

def apply_gui_py_fix():
    """Update gui.py with weight parameter instead of bold"""
    gui_file = "pyglet_gui/gui.py"
    if not os.path.exists(gui_file):
        print(f"❌ {gui_file} not found")
        return False
    
    with open(gui_file, 'r') as f:
        content = f.read()
    
    # Replace Label constructor
    old_constructor = '''class Label(Viewer):
    def __init__(self, text="", bold=False, italic=False,
                 font_name=None, font_size=None, color=None, path=None):
        Viewer.__init__(self)
        self.text = text
        self.bold = bold'''
    
    new_constructor = '''class Label(Viewer):
    def __init__(self, text="", weight=None, italic=False,
                 font_name=None, font_size=None, color=None, path=None):
        Viewer.__init__(self)
        self.text = text
        self.weight = weight'''
    
    content = content.replace(old_constructor, new_constructor)
    
    # Replace pyglet.text.Label call
    old_label_call = '''self.label = pyglet.text.Label(self.text,
                                       bold=self.bold,'''
    new_label_call = '''self.label = pyglet.text.Label(self.text,
                                       weight=self.weight,'''
    
    content = content.replace(old_label_call, new_label_call)
    
    with open(gui_file, 'w') as f:
        f.write(content)
    
    print("✅ Updated pyglet_gui/gui.py")
    return True

def apply_text_input_fix():
    """Update text_input.py with correct IncrementalTextLayout arguments"""
    text_input_file = "pyglet_gui/text_input.py"
    if not os.path.exists(text_input_file):
        print(f"❌ {text_input_file} not found")
        return False
    
    with open(text_input_file, 'r') as f:
        content = f.read()
    
    # Fix IncrementalTextLayout constructor
    old_layout = '''self._text_layout = pyglet.text.layout.IncrementalTextLayout(
            self._document, needed_width, needed_height,
            multiline=False, **self.get_batch('foreground'))'''
    
    new_layout = '''self._text_layout = pyglet.text.layout.IncrementalTextLayout(
            self._document, 
            x=0, y=0, z=0,
            width=needed_width, height=needed_height,
            multiline=False, **self.get_batch('foreground'))'''
    
    content = content.replace(old_layout, new_layout)
    
    # Fix InputLabel constructor
    old_input_label = '''self._label = InputLabel(self._document.text,
                                 multiline=False,
                                 width=self.width-self._padding*2,
                                 color=theme['text_color'],
                                 font_name=theme['font'],
                                 font_size=theme['font_size'],
                                 **self.get_batch('foreground'))'''
    
    new_input_label = '''self._label = InputLabel(
            text=self._document.text,
            x=0, y=0, z=0,
            width=self.width-self._padding*2,
            multiline=False,
            color=theme['text_color'],
            font_name=theme['font'],
            font_size=theme['font_size'],
            **self.get_batch('foreground'))'''
    
    content = content.replace(old_input_label, new_input_label)
    
    with open(text_input_file, 'w') as f:
        f.write(content)
    
    print("✅ Updated pyglet_gui/text_input.py")
    return True

def apply_document_fix():
    """Update document.py with correct IncrementalTextLayout arguments"""
    document_file = "pyglet_gui/document.py"
    if not os.path.exists(document_file):
        print(f"❌ {document_file} not found")
        return False
    
    with open(document_file, 'r') as f:
        content = f.read()
    
    # Fix IncrementalTextLayout constructor
    old_layout = '''self._content = pyglet.text.layout.IncrementalTextLayout(self._document,
                                                                 self.content_width, self.max_height,
                                                                 multiline=True, **self.get_batch('background'))'''
    
    new_layout = '''self._content = pyglet.text.layout.IncrementalTextLayout(
            self._document,
            x=0, y=0, z=0,
            width=self.content_width, height=self.max_height,
            multiline=True, **self.get_batch('background'))'''
    
    content = content.replace(old_layout, new_layout)
    
    with open(document_file, 'w') as f:
        f.write(content)
    
    print("✅ Updated pyglet_gui/document.py")
    return True

def update_readme():
    """Update README.md with new requirements"""
    readme_file = "README.md"
    if not os.path.exists(readme_file):
        print(f"❌ {readme_file} not found")
        return False
    
    with open(readme_file, 'r') as f:
        content = f.read()
    
    # Update Python version requirements
    content = re.sub(r'Python \d+\.\d+\+', 'Python 3.6+', content)
    
    # Update pyglet version requirements
    content = re.sub(r'pyglet \d+\.\d+\+', 'pyglet 2.0+', content)
    
    # Update installation instructions
    content = re.sub(
        r'pip install --upgrade http://pyglet.googlecode.com/archive/tip.zip',
        'pip install pyglet>=2.0',
        content
    )
    
    with open(readme_file, 'w') as f:
        f.write(content)
    
    print("✅ Updated README.md")
    return True

def apply_ordered_group_fix():
    """Fix OrderedGroup removal in pyglet 2.1+ - replace with Group(order=X)"""
    files_to_fix = [
        "pyglet_gui/manager.py",
        "pyglet_gui/scrollable.py", 
        "tests/test_theme.py"
    ]
    
    fixed_count = 0
    
    for file_path in files_to_fix:
        if not os.path.exists(file_path):
            print(f"⚠️ {file_path} not found, skipping...")
            continue
            
        try:
            with open(file_path, 'r') as f:
                content = f.read()
            
            original_content = content
            
            # Fix ViewerManagerGroup inheritance
            if "class ViewerManagerGroup(pyglet.graphics.OrderedGroup):" in content:
                content = content.replace(
                    "class ViewerManagerGroup(pyglet.graphics.OrderedGroup):",
                    "class ViewerManagerGroup(pyglet.graphics.Group):"
                )
            
            # Fix ViewerManagerGroup constructor
            if "pyglet.graphics.OrderedGroup.__init__(self, self._get_next_top_order(), parent)" in content:
                content = content.replace(
                    "pyglet.graphics.OrderedGroup.__init__(self, self._get_next_top_order(), parent)",
                    "pyglet.graphics.Group.__init__(self, order=self._get_next_top_order(), parent=parent)"
                )
            
            # Fix comparison methods
            content = content.replace(
                "return pyglet.graphics.OrderedGroup.__eq__(self, other)",
                "return pyglet.graphics.Group.__eq__(self, other)"
            )
            content = content.replace(
                "return pyglet.graphics.OrderedGroup.__lt__(self, other)",
                "return pyglet.graphics.Group.__lt__(self, other)"
            )
            
            # Fix OrderedGroup creation patterns
            content = content.replace(
                "pyglet.graphics.OrderedGroup(10, self.root_group)",
                "pyglet.graphics.Group(order=10, parent=self.root_group)"
            )
            content = content.replace(
                "pyglet.graphics.OrderedGroup(20, self.root_group)",
                "pyglet.graphics.Group(order=20, parent=self.root_group)"
            )
            content = content.replace(
                "pyglet.graphics.OrderedGroup(30, self.root_group)",
                "pyglet.graphics.Group(order=30, parent=self.root_group)"
            )
            content = content.replace(
                "pyglet.graphics.OrderedGroup(40, self.root_group)",
                "pyglet.graphics.Group(order=40, parent=self.root_group)"
            )
            content = content.replace(
                "pyglet.graphics.OrderedGroup(0, self.root_group)",
                "pyglet.graphics.Group(order=0, parent=self.root_group)"
            )
            
            # Fix test OrderedGroup
            content = content.replace(
                "pyglet.graphics.OrderedGroup(1)",
                "pyglet.graphics.Group(order=1)"
            )
            
            if content != original_content:
                with open(file_path, 'w') as f:
                    f.write(content)
                print(f"✅ Fixed OrderedGroup usage in {file_path}")
                fixed_count += 1
            else:
                print(f"ℹ️ No OrderedGroup changes needed in {file_path}")
                
        except Exception as e:
            print(f"❌ Error fixing OrderedGroup in {file_path}: {e}")
            return False
    
    if fixed_count > 0:
        print(f"✅ Fixed OrderedGroup in {fixed_count} files")
        return True
    else:
        print("ℹ️ No OrderedGroup fixes needed")
        return True

def apply_batch_add_fix():
    """Fix Batch.add() API change in elements.py"""
    print("🔧 Applying Batch.add() → ShaderProgram.vertex_list() API fix...")
    
    elements_file = "pyglet_gui/theme/elements.py"
    if not os.path.exists(elements_file):
        print(f"❌ {elements_file} not found")
        return
    
    # The complete fixed file content using shader-based approach
    fixed_content = '''from abc import abstractmethod

import pyglet
from pyglet import gl
from ..core import Rectangle


class ThemeTextureGroup(pyglet.graphics.TextureGroup):
    """
    ThemeTextureGroup, in addition to setting the texture, also ensures that
    we map to the nearest texel instead of trying to interpolate from nearby
    texels. This prevents 'blooming' along the edges.
    """

    def set_state(self):
        super(ThemeTextureGroup, self).set_state()
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_NEAREST)


class GraphicElement(Rectangle):
    def __init__(self, color, batch, group, width=0, height=0):
        Rectangle.__init__(self, width=width, height=height)
        self._color = color
        self._batch = batch
        self._group = group
        self._vertex_list = None
        self._load()

    @abstractmethod
    def _load(self):
        assert self._vertex_list is None
        # Get the default shader program and use it to create vertex list
        program = pyglet.graphics.get_default_shader()
        self._vertex_list = program.vertex_list(12, gl.GL_LINES,
                                               batch=self._batch,
                                               group=self._group,
                                               position=('i', self._get_vertices()),
                                               colors=('B', self._color * 12))

    @abstractmethod
    def _get_vertices(self):
        x1, y1 = int(self._x), int(self._y)
        x2, y2 = x1 + int(self.width), y1 + int(self.height)
        return (x1, y1, x2, y1, x2, y1, x2, y2,
                x2, y2, x1, y2, x1, y2, x1, y1,
                x1, y1, x2, y2, x1, y2, x2, y1)

    def unload(self):
        self._vertex_list.delete()
        self._vertex_list = None
        self._group = None

    def get_content_region(self):
        return self._x, self._y, self.width, self.height

    def get_content_size(self, width, height):
        return width, height

    def get_needed_size(self, content_width, content_height):
        return content_width, content_height

    def update(self, x, y, width, height):
        self.set_position(x, y)
        self.width, self.height = width, height

        if self._vertex_list is not None:
            self._vertex_list.position = self._get_vertices()


class TextureGraphicElement(GraphicElement):
    def __init__(self, texture, color, batch, group):
        self.texture = texture
        GraphicElement.__init__(self,
                                color,
                                batch,
                                ThemeTextureGroup(texture, group),
                                texture.width, texture.height)

    def _load(self):
        assert self._vertex_list is None
        # Get the default shader program and use it to create vertex list
        program = pyglet.graphics.get_default_shader()
        self._vertex_list = program.vertex_list(4, gl.GL_TRIANGLES,
                                               batch=self._batch,
                                               group=self._group,
                                               position=('i', self._get_vertices()),
                                               colors=('B', self._color * 4),
                                               tex_coords=('f', self.texture.tex_coords))

    def _get_vertices(self):
        x1, y1 = int(self._x), int(self._y)
        x2, y2 = x1 + int(self.width), y1 + int(self.height)
        return x1, y1, x2, y1, x2, y2, x1, y2


class FrameTextureGraphicElement(GraphicElement):
    def __init__(self, outer_texture, inner_texture, margins, padding, color, batch, group):
        self.outer_texture = outer_texture
        self.inner_texture = inner_texture
        self.margins = margins
        self.padding = padding
        GraphicElement.__init__(self,
                                color,
                                batch,
                                ThemeTextureGroup(outer_texture, group),
                                outer_texture.width,
                                outer_texture.height)

    def _load(self):
        assert self._vertex_list is None

        # 36 vertices: 4 for each of the 9 rectangles.
        # Get the default shader program and use it to create vertex list
        program = pyglet.graphics.get_default_shader()
        self._vertex_list = program.vertex_list(36, gl.GL_TRIANGLES,
                                               batch=self._batch,
                                               group=self._group,
                                               position=('i', self._get_vertices()),
                                               colors=('B', self._color * 36),
                                               tex_coords=('f', self._get_tex_coords()))

    def _get_tex_coords(self):
        x1, y1 = self.outer_texture.tex_coords[0:2]  # outer's lower left
        x4, y4 = self.outer_texture.tex_coords[6:8]  # outer's upper right
        x2, y2 = self.inner_texture.tex_coords[0:2]  # inner's lower left
        x3, y3 = self.inner_texture.tex_coords[6:8]  # inner's upper right
        return (x1, y1, x2, y1, x2, y2, x1, y2,  # bottom left
                x2, y1, x3, y1, x3, y2, x2, y2,  # bottom
                x3, y1, x4, y1, x4, y2, x3, y2,  # bottom right
                x1, y2, x2, y2, x2, y3, x1, y3,  # left
                x2, y2, x3, y2, x3, y3, x2, y3,  # center
                x3, y2, x4, y2, x4, y3, x3, y3,  # right
                x1, y3, x2, y3, x2, y4, x1, y4,  # top left
                x2, y3, x3, y3, x3, y4, x2, y4,  # top
                x3, y3, x4, y3, x4, y4, x3, y4)  # top right

    def _get_vertices(self):
        left, right, top, bottom = self.margins
        x1, y1 = int(self._x), int(self._y)
        x2, y2 = x1 + int(left), y1 + int(bottom)
        x3 = x1 + int(self.width) - int(right)
        y3 = y1 + int(self.height) - int(top)
        x4, y4 = x1 + int(self.width), y1 + int(self.height)
        return (x1, y1, x2, y1, x2, y2, x1, y2,  # bottom left
                x2, y1, x3, y1, x3, y2, x2, y2,  # bottom
                x3, y1, x4, y1, x4, y2, x3, y2,  # bottom right
                x1, y2, x2, y2, x2, y3, x1, y3,  # left
                x2, y2, x3, y2, x3, y3, x2, y3,  # center
                x3, y2, x4, y2, x4, y3, x3, y3,  # right
                x1, y3, x2, y3, x2, y4, x1, y4,  # top left
                x2, y3, x3, y3, x3, y4, x2, y4,  # top
                x3, y3, x4, y3, x4, y4, x3, y4)  # top right

    def get_content_region(self):
        left, right, top, bottom = self.padding
        return (self._x + left, self._y + bottom,
                self.width - left - right, self.height - top - bottom)

    def get_content_size(self, width, height):
        left, right, top, bottom = self.padding
        return width - left - right, height - top - bottom

    def get_needed_size(self, content_width, content_height):
        left, right, top, bottom = self.padding
        return (max(content_width + left + right, self.outer_texture.width),
                max(content_height + top + bottom, self.outer_texture.height))
'''
    
    with open(elements_file, 'w') as f:
        f.write(fixed_content)
    
    print(f"✅ Updated {elements_file}")

def main():
    """Apply all pyglet2+ compatibility fixes"""
    print("🚀 Starting pyglet2+ compatibility fixes for pyglet-gui")
    print("=" * 60)
    
    # Apply all fixes in order
    apply_setup_py_fix()
    apply_gui_py_fix()
    apply_text_input_fix()
    apply_document_fix()
    apply_ordered_group_fix()
    apply_batch_add_fix()  # Updated Batch API fix with ShaderProgram
    update_readme()
    
    print("\n" + "=" * 60)
    print("✅ All pyglet2+ compatibility fixes applied successfully!")
    print("\n📋 Summary of changes:")
    print("   • Updated setup.py: pyglet>=2.0, version 0.2")
    print("   • Fixed Label constructor: bold → weight parameter")
    print("   • Fixed IncrementalTextLayout constructor argument order")
    print("   • Fixed InputLabel constructor for pyglet 2.1+")
    print("   • Fixed OrderedGroup → Group(order=X) usage")
    print("   • Fixed Batch.add() → ShaderProgram.vertex_list() API")
    print("   • Updated README.md requirements")
    
    print("\n🧪 Next steps:")
    print("   1. Test with: python test_pyglet2_compatibility.py")
    print("   2. Run examples: python test_examples.py")
    print("   3. Install: pip install -e . pyglet>=2.0")

if __name__ == "__main__":
    main()
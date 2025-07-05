#!/usr/bin/env python3
"""
Script to automatically apply pyglet2+ compatibility fixes to pyglet-gui
Run this after cloning the original repository.
"""

import os
import sys
import shutil
from pathlib import Path

def apply_setup_py_fix():
    """Update setup.py with new version requirements"""
    setup_file = "setup.py"
    if not os.path.exists(setup_file):
        print(f"❌ {setup_file} not found")
        return False
    
    with open(setup_file, 'r') as f:
        content = f.read()
    
    # Apply fixes
    content = content.replace("version='0.1'", "version='0.2'")
    content = content.replace("requires=('pyglet (>=1.2)',)", "requires=('pyglet (>=2.0)',)")
    
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
    content = content.replace("""* Python:

    * 2.7
    * 3.2
    * 3.3
    * 3.4

* Pyglet:

    * >= 1.2""", """* Python:

    * 3.6+

* Pyglet:

    * >= 2.0""")
    
    # Update installation instructions
    content = content.replace(
        "pip install --upgrade http://pyglet.googlecode.com/archive/tip.zip",
        "pip install pyglet>=2.0"
    )
    
    with open(readme_file, 'w') as f:
        f.write(content)
    
    print("✅ Updated README.md")
    return True

def main():
    print("🔧 Applying pyglet2+ compatibility fixes...")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists("pyglet_gui"):
        print("❌ This doesn't appear to be the pyglet-gui directory")
        print("   Make sure you're in the root of the pyglet-gui repository")
        sys.exit(1)
    
    fixes = [
        apply_setup_py_fix,
        apply_gui_py_fix,
        apply_text_input_fix,
        apply_document_fix,
        update_readme
    ]
    
    applied = 0
    for fix in fixes:
        try:
            if fix():
                applied += 1
        except Exception as e:
            print(f"❌ Error applying fix {fix.__name__}: {e}")
    
    print("\n" + "=" * 50)
    print(f"📊 Applied {applied}/{len(fixes)} fixes")
    
    if applied == len(fixes):
        print("🎉 All pyglet2+ fixes applied successfully!")
        print("\nNext steps:")
        print("1. pip install pyglet>=2.0")
        print("2. python test_pyglet2_compatibility.py")
    else:
        print("⚠️ Some fixes failed to apply")
        print("You may need to apply them manually")

if __name__ == "__main__":
    main()
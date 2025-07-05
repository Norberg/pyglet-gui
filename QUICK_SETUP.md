# 🚀 Quick Setup Guide - Pyglet2+ Compatible pyglet-gui

## Option 1: Auto-apply fixes to original repo (Recommended)

```bash
# 1. Clone original repo
git clone https://github.com/jorgecarleitao/pyglet-gui.git
cd pyglet-gui

# 2. Download and run the auto-fix script
curl -O https://raw.githubusercontent.com/your-repo/apply_pyglet2_fixes.py  # Replace with actual URL
python apply_pyglet2_fixes.py

# 3. Download test files
curl -O https://raw.githubusercontent.com/your-repo/test_pyglet2_compatibility.py
curl -O https://raw.githubusercontent.com/your-repo/test_examples.py

# 4. Install pyglet 2.0+ and test
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
pip install pyglet>=2.0
python test_pyglet2_compatibility.py
```

## Option 2: Manual file download

If you can't use the auto-script, download these files manually and replace them in the pyglet-gui directory:

### Core Files to Replace:
1. **setup.py** - Updated version requirements
2. **README.md** - Updated compatibility info  
3. **pyglet_gui/gui.py** - Fixed Label with weight parameter
4. **pyglet_gui/text_input.py** - Fixed IncrementalTextLayout
5. **pyglet_gui/document.py** - Fixed IncrementalTextLayout

### Test Files to Add:
1. **test_pyglet2_compatibility.py** - Main compatibility test
2. **test_examples.py** - Example runner test

## Option 3: Copy-paste manual fixes

If auto-script doesn't work, apply these changes manually:

### Fix 1: setup.py
```python
# Change line ~5:
requires=('pyglet (>=2.0)',)  # Was: >=1.2

# Change line ~4:
version='0.2'  # Was: 0.1
```

### Fix 2: pyglet_gui/gui.py (Line ~44)
```python
# OLD:
def __init__(self, text="", bold=False, italic=False, ...)

# NEW:
def __init__(self, text="", weight=None, italic=False, ...)
```

```python
# OLD (Line ~65):
self.label = pyglet.text.Label(self.text, bold=self.bold, ...)

# NEW:
self.label = pyglet.text.Label(self.text, weight=self.weight, ...)
```

### Fix 3: pyglet_gui/text_input.py (Line ~49)
```python
# OLD:
self._text_layout = pyglet.text.layout.IncrementalTextLayout(
    self._document, needed_width, needed_height,
    multiline=False, **self.get_batch('foreground'))

# NEW:
self._text_layout = pyglet.text.layout.IncrementalTextLayout(
    self._document, 
    x=0, y=0, z=0,
    width=needed_width, height=needed_height,
    multiline=False, **self.get_batch('foreground'))
```

### Fix 4: pyglet_gui/document.py (Line ~53)
```python
# OLD:
self._content = pyglet.text.layout.IncrementalTextLayout(
    self._document, self.content_width, self.max_height,
    multiline=True, **self.get_batch('background'))

# NEW:
self._content = pyglet.text.layout.IncrementalTextLayout(
    self._document,
    x=0, y=0, z=0,
    width=self.content_width, height=self.max_height,
    multiline=True, **self.get_batch('background'))
```

## Quick Test

Once you have the updated code:

```bash
# Install pyglet 2.0+
pip install pyglet>=2.0

# Run compatibility test
python test_pyglet2_compatibility.py

# Expected output:
# 🎉 All tests passed! Pyglet2+ compatibility looks good!
```

## Need Help?

If you encounter issues:

1. **Check pyglet version**: `python -c "import pyglet; print(pyglet.version)"`
2. **Check Python version**: `python --version` (needs 3.6+)
3. **Run tests with verbose output**: Tests will show detailed error messages

## Files You Need

### Essential Files (Updated):
- `setup.py` ✅
- `README.md` ✅  
- `pyglet_gui/gui.py` ✅
- `pyglet_gui/text_input.py` ✅
- `pyglet_gui/document.py` ✅

### Test Files (New):
- `test_pyglet2_compatibility.py` ➕
- `test_examples.py` ➕

### Documentation (New):
- `CHANGELOG.md` ➕
- `PYGLET2_MIGRATION_NOTES.md` ➕

That's it! The library should now work with pyglet 2.0+.
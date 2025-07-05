# Pyglet2+ Migration Notes

## Summary
The migration from pyglet 1.x to pyglet 2+ revealed **significant API breaking changes** that required comprehensive updates. While the most critical issues have been addressed, some areas still require careful testing and potentially further updates.

## ✅ Issues Fixed

### 1. Text Layout Constructor Arguments (CRITICAL)
**Problem**: `IncrementalTextLayout` constructor argument order completely changed in pyglet 2.1+

**Old (pyglet 1.x)**:
```python
IncrementalTextLayout(document, width, height, multiline=False, ...)
```

**New (pyglet 2.1+)**:
```python  
IncrementalTextLayout(document, x, y, z, width, height, anchor_x, anchor_y, rotation, ...)
```

**Files Fixed**:
- `pyglet_gui/text_input.py` line 49-52
- `pyglet_gui/document.py` line 53-55

**Impact**: Without this fix, **all text input and document widgets would crash** on creation.

### 2. Label API Updates
**Problem**: `bold` parameter deprecated in favor of `weight`

**Fixed**:
- `pyglet_gui/gui.py`: Updated Label class constructor
- `pyglet_gui/text_input.py`: Updated InputLabel constructor with new argument order

### 3. Version Requirements
- Updated minimum pyglet version: `>=1.2` → `>=2.0`
- Dropped Python 2.7 support
- Updated README and setup.py

## ⚠️ Remaining Risks & Areas Needing Testing

### 1. Internal Graphics API Usage (`override.py`)
**Risk Level**: HIGH 🔴

**Problem**: 
```python
# This code uses internal pyglet APIs:
for vlist in self._vertex_lists:    # Internal API
    # ... vertex manipulation
pyglet.text.Label._update(self)    # Internal method
```

**Potential Issues**:
- `_vertex_lists` attribute may not exist in pyglet 2+
- `_update()` method signature may have changed
- Vertex list structure may have changed

**Testing Required**: 
- Test `InputLabel` text clipping functionality
- Test with long text that exceeds input field width
- Monitor for `AttributeError` or `TypeError` exceptions

### 2. Layout Update Methods
**Risk Level**: MEDIUM 🟡

**Locations**:
- `text_input.py`: `begin_update()`/`end_update()` calls
- `document.py`: Text layout positioning

**Potential Issues**:
- Methods may have been deprecated
- Signature changes
- Performance implications

### 3. Event Handling Changes
**Risk Level**: MEDIUM 🟡

**Areas to Test**:
- Mouse scroll events (`on_mouse_scroll`)
- Widget event dispatching
- Event return values and propagation

**Pyglet 2.1+ Changes**:
- Widget events now pass widget instance as first argument
- Some event signatures may have changed

### 4. Graphics Batch/Group API
**Risk Level**: LOW 🟢

**Areas**:
- `OrderedGroup` usage in `manager.py` and `scrollable.py`
- Batch drawing methods
- Group ordering and hierarchy

## 🧪 Testing Strategy

### Essential Tests
1. **Text Input Widget**:
   ```python
   # Test basic functionality
   text_input = TextInput("Test text", length=20)
   # Test focus gain/loss
   # Test typing and editing
   # Test text overflow/clipping
   ```

2. **Document Widget**:
   ```python
   # Test document creation and display
   doc = Document("Long text content...", width=200, height=100)
   # Test scrolling
   # Test text layout
   ```

3. **Label Rendering**:
   ```python
   # Test various label configurations
   label1 = Label("Test", weight="bold")
   label2 = Label("Test", weight="normal")
   ```

### Runtime Error Monitoring
Monitor for these specific errors:
- `AttributeError: '_Label' object has no attribute '_vertex_lists'`
- `TypeError` in text layout positioning
- Graphics rendering errors
- Event handling exceptions

### Performance Testing
- Text rendering performance
- Layout update performance
- Memory usage patterns

## 🔧 Potential Additional Fixes Needed

### If Internal API Issues Occur
If `_vertex_lists` or `_update()` methods cause issues, consider:

1. **Remove Custom Clipping**: Simplify `InputLabel` to use standard pyglet functionality
2. **Alternative Clipping**: Use pyglet 2+ recommended approaches for text clipping
3. **Fallback Implementation**: Detect pyglet version and use appropriate methods

### Example Defensive Code:
```python
class InputLabel(pyglet.text.Label):
    def _update(self):
        try:
            # Try new pyglet 2+ approach
            super()._update()
        except (AttributeError, TypeError):
            # Fallback for compatibility
            self._layout()
```

## 📋 Pre-Release Checklist

- [ ] Install pyglet 2.0+ in clean environment
- [ ] Run all examples without errors
- [ ] Test text input functionality thoroughly
- [ ] Test document scrolling and display
- [ ] Verify label rendering with different weights
- [ ] Test on multiple platforms (Windows, macOS, Linux)
- [ ] Performance benchmark vs pyglet 1.x version
- [ ] Memory leak testing for text components

## 🚀 Recommended Next Steps

1. **Immediate**: Test with real pyglet 2.0+ installation
2. **Short-term**: Address any runtime errors found in testing
3. **Medium-term**: Refactor `override.py` to avoid internal APIs
4. **Long-term**: Consider pyglet 2.1+ specific optimizations

## 📚 Resources

- [Pyglet 2.1+ Migration Guide](https://pyglet.readthedocs.io/en/development/programming_guide/migration.html)
- [Pyglet 2.1+ Text API Documentation](https://pyglet.readthedocs.io/en/latest/modules/text.html)
- [Pyglet Graphics API Changes](https://pyglet.readthedocs.io/en/latest/modules/graphics.html)
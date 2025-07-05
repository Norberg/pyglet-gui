# Changelog

## Version 0.2 - pyglet2+ Compatibility Update

### ⚠️ MAJOR BREAKING CHANGES
This update addresses **critical compatibility issues** with pyglet 2.0+. The previous version would **fail to run** with pyglet 2.0+ due to multiple API changes.

### Critical Issues Fixed

1. **Graphics API Overhaul** (CRITICAL - BLOCKING):
   - Fixed `OrderedGroup` removal - replaced with `Group(order=X)` in pyglet 2.1+
   - Updated `ViewerManagerGroup` inheritance from `OrderedGroup` to `Group`
   - Fixed all group creation calls in `manager.py` and `scrollable.py`
   - **Without this fix**: Complete import failure - library wouldn't load at all

2. **Text Layout API Overhaul** (CRITICAL):
   - Fixed `IncrementalTextLayout` constructor argument order in `text_input.py` and `document.py`
   - Updated from old format: `(document, width, height, ...)` 
   - Updated to new format: `(document, x, y, z, width, height, anchor_x, anchor_y, rotation, ...)`
   - **Without this fix**: Text input and document widgets would crash on creation

3. **Label API Updates**:
   - Replaced deprecated `bold` parameter with `weight` parameter in `gui.py`
   - Updated `InputLabel` constructor to use new argument order with explicit positioning
   - **Without this fix**: Text rendering would use deprecated API

4. **Minimum Version Requirements Updated**:
   - **pyglet**: Updated from `>=1.2` to `>=2.0`
   - **Python**: Dropped Python 2.7 support, now requires Python 3.6+

### Breaking Changes Summary

| Component | Issue | Fix |
|-----------|-------|-----|
| **Graphics Groups** | `OrderedGroup` removed | Use `Group(order=X)` |
| **Text Layouts** | Constructor args reordered | Add `x, y, z` positioning |
| **Labels** | `bold` parameter deprecated | Use `weight` parameter |
| **Python** | 2.7 no longer supported | Requires 3.6+ |

### Files Modified
- `setup.py` - Updated version requirements
- `README.md` - Updated compatibility information  
- `pyglet_gui/gui.py` - Fixed Label constructor (bold → weight)
- `pyglet_gui/text_input.py` - Fixed IncrementalTextLayout and InputLabel constructors
- `pyglet_gui/document.py` - Fixed IncrementalTextLayout constructor
- `pyglet_gui/manager.py` - Fixed OrderedGroup → Group with order parameter
- `pyglet_gui/scrollable.py` - Fixed OrderedGroup → Group with order parameter
- `tests/test_theme.py` - Updated test to use Group instead of OrderedGroup

### Remaining Compatibility Concerns

⚠️ **WARNING**: The following areas may still have compatibility issues and need further testing:

1. **Internal Graphics API Usage** (`override.py`):
   - Uses internal pyglet APIs like `_vertex_lists` and `_update()` 
   - These may have changed or been removed in pyglet 2+
   - May cause runtime errors in InputLabel text clipping functionality

2. **Layout Update Methods**:
   - Uses `begin_update()`/`end_update()` methods that may have changed
   - Found in text layout and label positioning code

3. **Event Handling**:
   - Mouse scroll events and other event signatures may have changed
   - Widget event dispatching may need updates for pyglet 2.1+

### Migration Guide

**For Library Users:**
- Ensure Python 3.6+ and pyglet 2.0+
- Replace `Label(text, bold=True)` with `Label(text, weight="bold")`
- Test text input and document widgets thoroughly
- No manual changes needed for Group/OrderedGroup (handled internally)

**For Library Developers:**
- Review `override.py` for potential internal API breakage
- Test all GUI components with pyglet 2.0+ 
- Monitor for runtime errors in text rendering and event handling
- Update any custom Groups to use `pyglet.graphics.Group(order=X)` syntax

### Testing Status
- ✅ Basic syntax compatibility verified (OrderedGroup fix applied)
- ✅ Major import blocking issues resolved
- ⚠️ **Full runtime testing with real pyglet 2+ installation needed**
- ⚠️ **InputLabel clipping functionality needs verification**

### Compatibility Matrix
- **pyglet**: 2.0, 2.1+ (2.2+ compatibility unknown)
- **Python**: 3.6, 3.7, 3.8, 3.9, 3.10, 3.11+
- **Platforms**: Windows, macOS, Linux

---

## Version 0.1 - Original Release
- Initial release with pyglet 1.2+ support
- Python 2.7 and 3.x support
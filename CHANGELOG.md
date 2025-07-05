# Changelog

## Version 0.2.0 (2024) - pyglet 2.0+ Compatibility

### 🔥 CRITICAL BREAKING CHANGES FIXED

#### 1. **Graphics API Overhaul** (CRITICAL-BLOCKING)
- **Issue**: `OrderedGroup` class completely removed in pyglet 2.1+
- **Error**: `AttributeError: module 'pyglet.graphics' has no attribute 'OrderedGroup'`
- **Fix**: Replaced all `OrderedGroup` usage with `Group(order=X)` syntax
- **Files**: `manager.py`, `scrollable.py`, `tests/test_theme.py`
- **Impact**: Library could not import at all without this fix

#### 2. **Batch API Overhaul** (CRITICAL-BLOCKING) 
- **Issue**: `Batch.add()` method completely removed in pyglet 2.0+
- **Error**: `AttributeError: 'Batch' object has no attribute 'add'`
- **Fix**: Replaced `batch.add(count, mode, group, ...)` with `batch.get_domain(False, False, mode, group, attributes).create(count)`
- **Files**: `pyglet_gui/theme/elements.py`
- **Impact**: All graphic elements failed to create, making GUI completely non-functional

#### 3. **Text Layout API** (CRITICAL)
- **Issue**: `IncrementalTextLayout` constructor argument order completely changed
- **Error**: Various argument mismatches and positioning issues
- **Old**: `(document, width, height, multiline=False, ...)`
- **New**: `(document, x, y, z, width, height, anchor_x, anchor_y, rotation, ...)`
- **Files**: `pyglet_gui/text_input.py`, `pyglet_gui/document.py`

#### 4. **Label API** (IMPORTANT)
- **Issue**: `bold` parameter replaced with `weight` parameter
- **Error**: `TypeError: got an unexpected keyword argument 'bold'`
- **Fix**: Changed `bold=theme['bold']` to `weight=theme['bold']`
- **Files**: `pyglet_gui/gui.py`

### 📦 Dependencies Updated
- **Python**: Updated from 2.7+ to 3.6+
- **pyglet**: Updated from >=1.2 to >=2.0
- **Version**: Bumped from 0.1 to 0.2

### 🧪 Testing & Quality Assurance
- Added comprehensive compatibility test suite (`test_pyglet2_compatibility.py`)
- Added example testing script (`test_examples.py`)
- Created automated fix application script (`apply_pyglet2_fixes.py`)
- Added detailed migration documentation

### 📋 Migration Impact Assessment

#### CRITICAL (Application Breaking):
- **OrderedGroup removal**: Complete import failure
- **Batch.add() removal**: Complete GUI failure  
- **Text layout changes**: Text input failure

#### IMPORTANT (Feature Breaking):
- **Label bold parameter**: Text rendering issues

#### MINIMAL (Cosmetic):
- **Version requirements**: Dependency conflicts

### 🔄 Backward Compatibility
- **None**: This is a breaking release requiring pyglet 2.0+
- **Migration required**: All applications must be updated
- **Automatic migration**: Use `apply_pyglet2_fixes.py` script

### 📚 Documentation Updates
- Updated installation instructions
- Added migration guide (`PYGLET2_MIGRATION_NOTES.md`)
- Created comprehensive testing guide (`TESTING_GUIDE.md`)
- Updated examples for pyglet 2+ compatibility

### 🐛 Known Remaining Risks
- Internal graphics API usage in `override.py` (uses `_vertex_lists`, `_update()`)
- Layout update methods compatibility (`begin_update()`/`end_update()`)
- Event handling signature changes may still exist

### 🎯 User Action Required
1. **Update pyglet**: `pip install pyglet>=2.0`
2. **Apply fixes**: Run `python apply_pyglet2_fixes.py` 
3. **Test thoroughly**: Run your application and all examples
4. **Check performance**: Monitor for rendering differences

---

## Version 0.1.0 (Original)
- Initial release for pyglet 1.2+
- Basic GUI components (buttons, labels, text input, etc.)
- Theme system
- Container layouts
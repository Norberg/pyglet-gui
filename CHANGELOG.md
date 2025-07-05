# Changelog

## Version 0.2 - pyglet2+ Compatibility Update

### Breaking Changes
- **Minimum pyglet version increased to 2.0**
- **Python 2.7 support dropped** - Now requires Python 3.6+
- **Label constructor changed**: The `bold` parameter has been replaced with `weight` parameter to match pyglet 2.1+ API changes

### Changes Made
1. **Updated setup.py**:
   - Changed pyglet requirement from `>=1.2` to `>=2.0`
   - Bumped library version from 0.1 to 0.2

2. **Updated Label class** (`pyglet_gui/gui.py`):
   - Replaced `bold=False` parameter with `weight=None`
   - Updated pyglet.text.Label constructor call to use `weight` instead of `bold`

3. **Updated README.md**:
   - Updated Python version requirements to 3.6+
   - Updated pyglet version requirements to >= 2.0
   - Updated installation instructions

### Migration Guide
If you're upgrading from version 0.1:

- **Label usage**: Replace any `Label(text, bold=True)` calls with `Label(text, weight="bold")`
- **Python version**: Ensure you're using Python 3.6 or later
- **pyglet version**: Upgrade to pyglet 2.0 or later

### Compatibility
- **pyglet**: 2.0 and later
- **Python**: 3.6 and later
- **Platforms**: Windows, macOS, Linux

## Version 0.1 - Original Release
- Initial release with pyglet 1.2+ support
- Python 2.7 and 3.x support
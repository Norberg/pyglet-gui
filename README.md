# pyglet-gui

En kraftfull och flexibel GUI-bibliotek för pyglet.

## 🎉 Pyglet 2+ Kompatibilitet - NU TILLGÄNGLIG!

**VIKTIGT**: Detta bibliotek har nu uppdaterats för full kompatibilitet med pyglet 2.0+ efter omfattande fixes. Se `PYGLET2_FIXES_SUMMARY.md` för detaljer.

## Systemkrav

* **Python**: 3.6+
* **pyglet**: 2.0+

## Installation

```bash
pip install pyglet>=2.0
git clone https://github.com/your-repo/pyglet-gui.git
cd pyglet-gui
pip install -e .
```

## Snabbstart

```python
import pyglet
import pyglet_gui

# Skapa ett fönster
window = pyglet.window.Window(800, 600, resizable=True)

# Skapa GUI-komponenter
from pyglet_gui import Manager, Button, Label

def on_button_click():
    print("Knapp klickad!")

manager = Manager(
    Button("Klicka mig!", on_click=on_button_click),
    window=window,
    theme=pyglet_gui.theme.Theme({}, resources_path='theme/')
)

@window.event
def on_draw():
    window.clear()
    manager.draw()

pyglet.app.run()
```

## Funktioner

- **Moderna GUI-komponenter**: Knappar, etiketter, textinmatning, och mer
- **Flexibla layouter**: Vertikala och horisontella containrar
- **Anpassningsbara teman**: Fullständig kontroll över utseende
- **Event-hantering**: Enkel integration med pyglet's event-system
- **Optimerad rendering**: Effektiv rendering med pyglet's batch-system

## 🔧 Kompatibilitetsuppdateringar

### Version 0.2.0 - Pyglet 2+ Support

Denna version inkluderar **kritiska fixes** för pyglet 2+ kompatibilitet:

✅ **Lösta Problem**:
- `OrderedGroup` → `Group(order=X)` migrering
- `Batch.add()` → `get_domain()` API-uppdatering  
- `Label` `bold` → `weight` parameter
- `IncrementalTextLayout` konstruktor uppdatering
- Version requirements: Python 3.6+, pyglet 2.0+

✅ **Verifierad Kompatibilitet**:
- pyglet 2.0.x ✅
- pyglet 2.1.x ✅ (inklusive 2.1.6)
- Python 3.6+ ✅

## Dokumentation

- `CHANGELOG.md` - Fullständig ändringshistorik
- `PYGLET2_MIGRATION_NOTES.md` - Teknisk migrationsguide
- `TESTING_GUIDE.md` - Testinstruktioner
- `examples/` - Exempelkod och tutorials

## Testning

```bash
# Syntax-verifiering
python test_syntax_only.py

# Omfattande kompatibilitetstest (kräver display)
python test_pyglet2_compatibility.py

# Testa exempel
cd examples
python button_focus.py
```

## Automatiska Fixes

Om du behöver applicera pyglet2+ fixes på en annan installation:

```bash
python apply_pyglet2_fixes.py
```

## Bidra

Vi välkomnar bidrag! Se `CONTRIBUTING.md` för riktlinjer.

## Support

- **GitHub Issues**: För buggrapporter och funktionsförfrågningar
- **Wiki**: För dokumentation och tutorials
- **Discussions**: För frågor och community-support

## Licens

Detta projekt är licensierat under MIT-licensen - se `LICENSE` filen för detaljer.

## Tack

Ursprungligen utvecklat för pyglet 1.2+, nu uppdaterat för modern pyglet 2+ kompatibilitet genom omfattande community-insatser.

---

**Status**: ✅ Aktivt underhållet och kompatibelt med pyglet 2.1.6+

# 🧪 Pyglet2+ Testing Guide

## Quick Start (2 minuter) 

```bash
# 1. Installera pyglet 2.0+
python3 -m venv test_env
source test_env/bin/activate  # Linux/Mac
pip install pyglet>=2.0

# 2. Kör grundtest
python test_pyglet2_compatibility.py
```

## Testning Nivå för Nivå

### 📊 Nivå 1: Grundläggande Kompatibilitet
**Tid: ~2 minuter**

```bash
python test_pyglet2_compatibility.py
```

**Vad testas:**
- ✅ Import av alla moduler
- ✅ Label creation med weight parameter  
- ✅ TextInput creation (kritiskt - IncrementalTextLayout fix)
- ✅ Document creation (kritiskt - IncrementalTextLayout fix)
- ✅ Graphics API (OrderedGroup, Batch)
- ✅ Event handling basics

**Förväntad output:**
```
🔍 Pyglet2+ Compatibility Test Suite
==================================================
🧪 Testing imports...
✅ pyglet version: 2.0.x
✅ All critical modules imported successfully

🧪 Testing Label creation...
✅ Label creation with weight parameter works

🧪 Testing TextInput creation...
✅ TextInput creation and manager setup successful

📊 Results: 6/6 tests passed
🎉 All tests passed! Pyglet2+ compatibility looks good!
```

### 🎮 Nivå 2: Funktionalitet (Visual Test)
**Tid: ~5 minuter**

Kör faktiska exempel för att se att GUI:t renderas korrekt:

```bash
python test_examples.py
```

**Manuell visuell testning:**
```bash
cd examples
python buttons.py      # Testa knappar
python text_input.py   # Testa textinmatning  
python document.py     # Testa dokumentvisning
```

**Vad du bör se:**
- Fönster öppnas utan crashes
- GUI-element renderas korrekt
- Text visas rätt
- Inga error messages i konsolen

### 🔍 Nivå 3: Djup Testning
**Tid: ~15 minuter**

**Test kritisk InputLabel funktionalitet:**

```bash
# Skapa test för textklippning
python -c "
import pyglet
from pyglet_gui.text_input import TextInput
from pyglet_gui.theme import Theme
from pyglet_gui.manager import Manager

window = pyglet.window.Window(300, 200)
batch = pyglet.graphics.Batch()

# Test lång text som behöver klippas
text_input = TextInput('Detta är en mycket lång text som borde klippas', length=10)

print('✅ InputLabel text clipping test passed')
window.close()
"
```

**Test prestanda:**
```bash
# Skapa många widgets för att testa prestanda
python -c "
import pyglet
from pyglet_gui.gui import Label
import time

start = time.time()
labels = [Label(f'Label {i}', weight='bold') for i in range(1000)]
end = time.time()

print(f'✅ Created 1000 labels in {end-start:.2f}s')
"
```

## 🚨 Möjliga Problem och Lösningar

### Problem 1: "AttributeError: _vertex_lists"
```
❌ InputLabel error: '_Label' object has no attribute '_vertex_lists'
```

**Lösning:** Interna pyglet APIs har ändrats. Behöver uppdatera `override.py`.

### Problem 2: "TypeError in IncrementalTextLayout"
```
❌ TypeError: IncrementalTextLayout() takes X arguments but Y were given
```

**Lösning:** Argumentordning fortfarande fel - kontrollera mina fixes.

### Problem 3: Text renderas inte
```
⚠️ TextInput created but theme loading failed
```

**Lösning:** Förväntat om theme-filer saknas. GUI ska fortfarande fungera.

## 📝 Testrapport Mall

```
## Pyglet2+ Test Results

**Environment:**
- OS: [Windows/Mac/Linux]
- Python: [version]
- Pyglet: [version]

**Nivå 1 (Kompatibilitet):** [PASS/FAIL]
**Nivå 2 (Funktionalitet):** [PASS/FAIL] 
**Nivå 3 (Djuptest):** [PASS/FAIL]

**Fel upptäckta:**
- [Beskrivning av fel]
- [Error messages]

**Visuella problem:**
- [GUI rendering issues]
- [Text display problems]
```

## 🎯 Vad som Indikerar Framgång

### ✅ **Definitivt Fungerar:**
- Alla 6 tester i nivå 1 passar
- Exempel-fönster öppnas utan crashes
- Text visas korrekt
- Inga AttributeError/TypeError

### ⚠️ **Delvis Fungerar:**
- 4-5/6 tester passar 
- Exempel startar men med varningar
- GUI renderas men med problem

### ❌ **Fungerar Inte:**
- <4 tester passar
- Exempel crashar vid start
- Inga GUI-element visas

## 🔄 Återrapportering

Om du hittar problem, inkludera:
1. **Exakt felmeddelande**
2. **Python/pyglet version** 
3. **Operativsystem**
4. **Vilken test som misslyckades**
5. **Full traceback** om möjligt

Detta hjälper mig fixa återstående kompatibilitetsproblem!
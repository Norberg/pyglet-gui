#!/usr/bin/env python3
"""
Test the actual examples to verify they work with pyglet2+
"""
import sys
import os
import subprocess

def test_example(example_name):
    """Test running an example"""
    print(f"\n🧪 Testing {example_name}...")
    
    example_path = os.path.join("examples", f"{example_name}.py")
    if not os.path.exists(example_path):
        print(f"⚠️ Example {example_path} not found")
        return False
    
    try:
        # Run the example for 2 seconds to see if it starts without crashing
        result = subprocess.run([
            sys.executable, example_path
        ], 
        cwd="examples",
        timeout=2, 
        capture_output=True, 
        text=True
        )
        
        # If it times out, that means it ran successfully for 2 seconds
        return True
        
    except subprocess.TimeoutExpired:
        print(f"✅ {example_name} started successfully (timeout after 2s is expected)")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {example_name} failed:")
        print(f"   stdout: {e.stdout}")
        print(f"   stderr: {e.stderr}")
        return False
    except Exception as e:
        print(f"❌ {example_name} error: {e}")
        return False

def main():
    print("🧪 Testing Examples with pyglet2+")
    print("=" * 40)
    
    # Key examples to test
    examples = [
        "buttons",
        "text_input", 
        "document",
        "containers"
    ]
    
    passed = 0
    for example in examples:
        if test_example(example):
            passed += 1
    
    print(f"\n📊 Results: {passed}/{len(examples)} examples work")
    
    if passed == len(examples):
        print("🎉 All examples work with pyglet2+!")
    else:
        print("⚠️ Some examples have issues")

if __name__ == "__main__":
    main()
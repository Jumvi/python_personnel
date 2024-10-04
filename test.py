import sys
print(sys.path)

try:
    from app import app
    print("Import successful")
except ImportError as e:
    print(f"Import failed: {e}")
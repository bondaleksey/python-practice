from pathlib import Path

print(f"{Path('spam')/'bacon'/'eggs'}")
print(f"{Path('spam')/Path('bacon/eggs')}")
print(f"{Path('spam')/Path('bacon','eggs')}")

print(Path.home())
print(Path.cwd())

#!/usr/bin/env python3
"""
Migrate existing problem's python/solution.py to root directory and rename to solution-python.py
Remove empty python/ folders
"""

import os
import shutil
from pathlib import Path


def migrate_problem_structure(problem_dir):
    """Migrate structure of a single problem"""
    problem_path = Path(problem_dir)
    python_dir = problem_path / 'python'
    
    if not python_dir.exists():
        return False, "No python folder"
    
    moved_files = []
    
    # Migrate all Python files
    for py_file in python_dir.glob('*.py'):
        if py_file.name == 'solution.py':
            # Rename main solution file to solution-python.py
            new_name = 'solution-python.py'
        else:
            # Keep other files with -python suffix
            name_parts = py_file.stem, py_file.suffix
            new_name = f"{name_parts[0]}-python{name_parts[1]}"
        
        new_path = problem_path / new_name
        shutil.move(str(py_file), str(new_path))
        moved_files.append(f"{py_file.name} -> {new_name}")
    
    # Remove empty python folder
    try:
        python_dir.rmdir()
        return True, f"Migrated files: {', '.join(moved_files)}"
    except OSError:
        return False, f"python folder not empty, migrated files: {', '.join(moved_files)}"


def main():
    """Migrate all problems"""
    project_root = Path(__file__).parent.parent
    problems_dir = project_root / 'problems'
    
    if not problems_dir.exists():
        print("❌ problems folder does not exist")
        return
    
    migrated_count = 0
    skipped_count = 0
    
    for problem_folder in sorted(problems_dir.iterdir()):
        if problem_folder.is_dir() and problem_folder.name.startswith(('00001', '00020', '00021', '00026', '00088')):
            success, message = migrate_problem_structure(problem_folder)
            if success:
                print(f"✅ {problem_folder.name}: {message}")
                migrated_count += 1
            else:
                print(f"⚠️  {problem_folder.name}: {message}")
                skipped_count += 1
    
    print(f"\n🎉 Migration complete!")
    print(f"✅ Successfully migrated: {migrated_count} problems")
    print(f"⚠️  Skipped: {skipped_count} problems")
    
    # Update project structure description
    print("\n📝 New file structure:")
    print("problems/")
    print("├── 00001-two-sum/")
    print("│   ├── README.md")
    print("│   └── solution-python.py")
    print("├── 00020-valid-parentheses/")
    print("│   ├── README.md")
    print("│   ├── solution-python.py")
    print("│   └── alt1_counter-python.py")
    print("└── ...")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
將現有題目的 python/solution.py 遷移到根目錄並重命名為 solution-python.py
移除空的 python/ 資料夾
"""

import os
import shutil
from pathlib import Path


def migrate_problem_structure(problem_dir):
    """遷移單個題目的結構"""
    problem_path = Path(problem_dir)
    python_dir = problem_path / 'python'
    
    if not python_dir.exists():
        return False, "沒有 python 資料夾"
    
    moved_files = []
    
    # 遷移所有 Python 檔案
    for py_file in python_dir.glob('*.py'):
        if py_file.name == 'solution.py':
            # 主要解答檔案重命名為 solution-python.py
            new_name = 'solution-python.py'
        else:
            # 其他檔案保持原名但加上 -python 後綴
            name_parts = py_file.stem, py_file.suffix
            new_name = f"{name_parts[0]}-python{name_parts[1]}"
        
        new_path = problem_path / new_name
        shutil.move(str(py_file), str(new_path))
        moved_files.append(f"{py_file.name} -> {new_name}")
    
    # 移除空的 python 資料夾
    try:
        python_dir.rmdir()
        return True, f"遷移檔案: {', '.join(moved_files)}"
    except OSError:
        return False, f"python 資料夾不為空，已遷移檔案: {', '.join(moved_files)}"


def main():
    """遷移所有題目"""
    project_root = Path(__file__).parent.parent
    problems_dir = project_root / 'problems'
    
    if not problems_dir.exists():
        print("❌ problems 資料夾不存在")
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
    
    print(f"\n🎉 遷移完成！")
    print(f"✅ 成功遷移: {migrated_count} 個題目")
    print(f"⚠️  跳過: {skipped_count} 個題目")
    
    # 更新專案結構說明
    print("\n📝 新的檔案結構:")
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

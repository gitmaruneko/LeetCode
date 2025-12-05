#!/usr/bin/env python3
"""
LeetCode Practice Statistics Tool
Automatically count completed problems and progress
"""

import os
import re
from collections import defaultdict


def scan_problems(problems_dir):
    """Scan problems directory, count completed problems"""
    stats = {
        'easy': 0,
        'medium': 0,
        'hard': 0,
        'total': 0,
        'problems': []
    }
    
    # Scan difficulty folders
    for difficulty in ['easy', 'medium', 'hard']:
        diff_path = os.path.join(problems_dir, difficulty)
        if not os.path.exists(diff_path):
            continue
            
        files = os.listdir(diff_path)
        # Only count code files (exclude note files)
        code_files = [f for f in files if not f.endswith('-notes.md')]
        
        stats[difficulty] = len(set(f.split('-')[0] for f in code_files if '-' in f))
    
    stats['total'] = stats['easy'] + stats['medium'] + stats['hard']
    return stats


def update_readme(readme_path, stats):
    """Update statistics in README.md"""
    if not os.path.exists(readme_path):
        return
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update statistics table
    table_pattern = r'(\| 難度 \| 已解決 \| 總題數 \|\n\|------|--------|--------\|\n)(\| Easy \| )\d+(\| \d+ \|\n)(\| Medium \| )\d+(\| \d+ \|\n)(\| Hard \| )\d+(\| \d+ \|\n)(\| \*\*總計\*\* \| \*\*)\d+(\*\* \| \*\*)\d+(\*\* \|)'
    
    replacement = f'\\g<1>\\g<2>{stats["easy"]}\\g<3>\\g<4>{stats["medium"]}\\g<5>\\g<6>{stats["hard"]}\\g<7>\\g<8>{stats["total"]}\\g<9>{stats["total"]}\\g<10>'
    
    new_content = re.sub(table_pattern, replacement, content)
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)


def main():
    """Main function"""
    project_root = os.path.dirname(os.path.abspath(__file__))
    problems_dir = os.path.join(project_root, 'problems')
    readme_path = os.path.join(project_root, 'README.md')
    
    # Count problems
    stats = scan_problems(problems_dir)
    
    # Display statistics
    print("=== LeetCode Practice Statistics ===")
    print(f"Easy: {stats['easy']}")
    print(f"Medium: {stats['medium']}")
    print(f"Hard: {stats['hard']}")
    print(f"Total: {stats['total']}")
    
    # Update README
    update_readme(readme_path, stats)
    print("\nREADME.md updated!")


if __name__ == "__main__":
    main()

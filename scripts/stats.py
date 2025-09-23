#!/usr/bin/env python3
"""
LeetCode 練習統計工具
自動統計已完成的題目數量和進度
"""

import os
import re
from collections import defaultdict


def scan_problems(problems_dir):
    """掃描 problems 目錄，統計已完成的題目"""
    stats = {
        'easy': 0,
        'medium': 0,
        'hard': 0,
        'total': 0,
        'problems': []
    }
    
    # 掃描各難度資料夾
    for difficulty in ['easy', 'medium', 'hard']:
        diff_path = os.path.join(problems_dir, difficulty)
        if not os.path.exists(diff_path):
            continue
            
        files = os.listdir(diff_path)
        # 只計算程式碼檔案（不包含筆記檔）
        code_files = [f for f in files if not f.endswith('-notes.md')]
        
        stats[difficulty] = len(set(f.split('-')[0] for f in code_files if '-' in f))
    
    stats['total'] = stats['easy'] + stats['medium'] + stats['hard']
    return stats


def update_readme(readme_path, stats):
    """更新 README.md 中的統計資訊"""
    if not os.path.exists(readme_path):
        return
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 更新統計表格
    table_pattern = r'(\| 難度 \| 已解決 \| 總題數 \|\n\|------|--------|--------\|\n)(\| Easy \| )\d+(\| \d+ \|\n)(\| Medium \| )\d+(\| \d+ \|\n)(\| Hard \| )\d+(\| \d+ \|\n)(\| \*\*總計\*\* \| \*\*)\d+(\*\* \| \*\*)\d+(\*\* \|)'
    
    replacement = f'\\g<1>\\g<2>{stats["easy"]}\\g<3>\\g<4>{stats["medium"]}\\g<5>\\g<6>{stats["hard"]}\\g<7>\\g<8>{stats["total"]}\\g<9>{stats["total"]}\\g<10>'
    
    new_content = re.sub(table_pattern, replacement, content)
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)


def main():
    """主函數"""
    project_root = os.path.dirname(os.path.abspath(__file__))
    problems_dir = os.path.join(project_root, 'problems')
    readme_path = os.path.join(project_root, 'README.md')
    
    # 統計題目
    stats = scan_problems(problems_dir)
    
    # 顯示統計結果
    print("=== LeetCode 練習統計 ===")
    print(f"簡單題目: {stats['easy']}")
    print(f"中等題目: {stats['medium']}")
    print(f"困難題目: {stats['hard']}")
    print(f"總計: {stats['total']}")
    
    # 更新 README
    update_readme(readme_path, stats)
    print("\nREADME.md 已更新！")


if __name__ == "__main__":
    main()

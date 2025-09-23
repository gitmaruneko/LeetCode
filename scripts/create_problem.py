#!/usr/bin/env python3
"""
快速創建新 LeetCode 題目檔案的工具
"""

import os
import sys
import re


def create_problem_files(problem_num, title, difficulty, language='python'):
    """創建新題目的檔案"""
    
    # 格式化題目編號
    problem_num_str = f"{int(problem_num):04d}"
    
    # 將標題轉換為檔案名格式
    title_slug = re.sub(r'[^\w\s-]', '', title.lower())
    title_slug = re.sub(r'[-\s]+', '-', title_slug).strip('-')
    
    # 確定資料夾路徑
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    difficulty_dir = os.path.join(project_root, 'problems', difficulty.lower())
    
    if not os.path.exists(difficulty_dir):
        os.makedirs(difficulty_dir)
    
    # 檔案名稱
    base_name = f"{problem_num_str}-{title_slug}"
    
    # 根據語言選擇副檔名
    extensions = {
        'python': 'py',
        'javascript': 'js',
        'java': 'java',
        'cpp': 'cpp'
    }
    
    code_file = os.path.join(difficulty_dir, f"{base_name}-{language}.{extensions.get(language, 'py')}")
    notes_file = os.path.join(difficulty_dir, f"{base_name}-notes.md")
    
    # 讀取模板
    template_dir = os.path.join(project_root, 'templates')
    
    # 創建程式碼檔案
    if language == 'python':
        template_file = os.path.join(template_dir, 'python-template.py')
        if os.path.exists(template_file):
            with open(template_file, 'r', encoding='utf-8') as f:
                template_content = f.read()
            
            # 替換模板內容
            code_content = template_content.replace('{題號}', problem_num)
            code_content = code_content.replace('{題目名稱}', title)
            code_content = code_content.replace('{url-slug}', title_slug)
        else:
            code_content = f'# {problem_num}. {title}\n\nclass Solution:\n    def solve(self):\n        pass\n'
    
    # 創建筆記檔案
    notes_template_file = os.path.join(template_dir, 'notes-template.md')
    if os.path.exists(notes_template_file):
        with open(notes_template_file, 'r', encoding='utf-8') as f:
            notes_template = f.read()
        
        # 替換模板內容
        difficulty_emoji = {'easy': '✅', 'medium': '🟡', 'hard': '🔴'}
        notes_content = notes_template.replace('{題號}', problem_num)
        notes_content = notes_content.replace('{題目名稱}', title)
        notes_content = notes_content.replace('{難度等級}', f"{difficulty_emoji.get(difficulty.lower(), '❓')} {difficulty.title()}")
    else:
        notes_content = f'# {problem_num}. {title}\n\n## 題目描述\n\n## 解題思路\n\n## 複雜度分析\n\n'
    
    # 寫入檔案
    with open(code_file, 'w', encoding='utf-8') as f:
        f.write(code_content)
    
    with open(notes_file, 'w', encoding='utf-8') as f:
        f.write(notes_content)
    
    print(f"✅ 已創建檔案:")
    print(f"   程式碼: {code_file}")
    print(f"   筆記: {notes_file}")


def main():
    """主函數"""
    if len(sys.argv) < 4:
        print("使用方法: python create_problem.py <題號> <題目標題> <難度> [語言]")
        print("範例: python create_problem.py 20 'Valid Parentheses' easy python")
        sys.exit(1)
    
    problem_num = sys.argv[1]
    title = sys.argv[2]
    difficulty = sys.argv[3]
    language = sys.argv[4] if len(sys.argv) > 4 else 'python'
    
    create_problem_files(problem_num, title, difficulty, language)


if __name__ == "__main__":
    main()

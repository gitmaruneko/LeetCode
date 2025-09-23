#!/usr/bin/env python3
"""
同步 meta.yaml 資訊到 README.md
將結構化的元數據整合到各題目的 README 中
"""

import os
import yaml
import re
from pathlib import Path


def sync_meta_to_readme(problem_dir):
    """將 meta.yaml 的資訊同步到 README.md"""
    meta_file = os.path.join(problem_dir, 'meta.yaml')
    readme_file = os.path.join(problem_dir, 'README.md')
    
    if not os.path.exists(meta_file) or not os.path.exists(readme_file):
        return False
    
    # 讀取 meta.yaml
    with open(meta_file, 'r', encoding='utf-8') as f:
        meta = yaml.safe_load(f)
    
    # 讀取現有 README
    with open(readme_file, 'r', encoding='utf-8') as f:
        readme_content = f.read()
    
    # 構建資訊卡片
    difficulty_emoji = {'easy': '🟢', 'medium': '🟡', 'hard': '🔴'}
    difficulty_display = f"{difficulty_emoji.get(meta['difficulty'], '❓')} **{meta['difficulty'].title()}**"
    tags_display = ' '.join([f"`{tag}`" for tag in meta.get('tags', [])])
    
    info_card = f"""> **題目資訊**  
> 🔗 [LeetCode](https://leetcode.com/problems/{meta['url_slug']}/) | 🎯 {difficulty_display} | 🏷️ {tags_display} | 📅 {meta['date_solved']}"""
    
    # 檢查是否已存在資訊卡片
    title_pattern = rf"# {meta['id']}\. {re.escape(meta['title'])}"
    
    if re.search(r'> \*\*題目資訊\*\*', readme_content):
        # 替換現有的資訊卡片
        info_pattern = r'> \*\*題目資訊\*\*.*?(?=\n\n|\n#|\Z)'
        new_content = re.sub(info_pattern, info_card, readme_content, flags=re.DOTALL)
    else:
        # 在標題後添加資訊卡片
        title_match = re.search(title_pattern, readme_content)
        if title_match:
            insert_pos = title_match.end()
            new_content = (readme_content[:insert_pos] + 
                          f"\n\n{info_card}\n" + 
                          readme_content[insert_pos:])
        else:
            return False
    
    # 添加學習筆記區塊（如果不存在）
    if '## 學習筆記' not in new_content and meta.get('notes'):
        notes_section = f"\n\n## 學習筆記\n\n{meta['notes']}"
        new_content += notes_section
    
    # 寫回檔案
    with open(readme_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True


def main():
    """同步所有題目的 meta.yaml 到 README.md"""
    project_root = Path(__file__).parent.parent
    problems_dir = project_root / 'problems'
    
    if not problems_dir.exists():
        print("❌ problems 資料夾不存在")
        return
    
    synced_count = 0
    for problem_folder in problems_dir.iterdir():
        if problem_folder.is_dir():
            if sync_meta_to_readme(problem_folder):
                print(f"✅ 同步完成: {problem_folder.name}")
                synced_count += 1
            else:
                print(f"⚠️  跳過: {problem_folder.name} (缺少必要檔案)")
    
    print(f"\n🎉 同步完成！共處理 {synced_count} 個題目")


if __name__ == "__main__":
    main()

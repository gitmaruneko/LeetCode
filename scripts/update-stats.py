#!/usr/bin/env python3
"""
LeetCode 練習統計工具
基於新的專案結構：以題目為中心的組織方式
自動統計已完成的題目數量和進度
"""

import os
import yaml
import re
from collections import defaultdict, Counter
from datetime import datetime


def parse_frontmatter(readme_content):
    """解析 README 中的 YAML frontmatter"""
    if not readme_content.startswith('---'):
        return None
    
    # 找到第二個 --- 的位置
    end_marker = readme_content.find('---', 3)
    if end_marker == -1:
        return None
    
    frontmatter_text = readme_content[3:end_marker].strip()
    try:
        return yaml.safe_load(frontmatter_text)
    except yaml.YAMLError:
        return None


def scan_problems(problems_dir):
    """掃描 problems 目錄，從 README frontmatter 統計已完成的題目"""
    stats = {
        'easy': 0,
        'medium': 0,
        'hard': 0,
        'total': 0,
        'problems': [],
        'languages': Counter(),
        'tags': Counter(),
        'recent_problems': []
    }
    
    if not os.path.exists(problems_dir):
        return stats
    
    # 掃描所有題目資料夾
    problem_dirs = [d for d in os.listdir(problems_dir) 
                   if os.path.isdir(os.path.join(problems_dir, d)) and re.match(r'\d{5}-', d)]
    
    for problem_dir in sorted(problem_dirs):
        problem_path = os.path.join(problems_dir, problem_dir)
        readme_file = os.path.join(problem_path, 'README.md')
        
        if not os.path.exists(readme_file):
            continue
        
        try:
            with open(readme_file, 'r', encoding='utf-8') as f:
                readme_content = f.read()
            
            # 解析 frontmatter
            meta_data = parse_frontmatter(readme_content)
            if not meta_data:
                continue
            
            problem_info = {
                'id': meta_data.get('id', 0),
                'title': meta_data.get('title', ''),
                'difficulty': meta_data.get('difficulty', 'unknown'),
                'languages': meta_data.get('languages', []),
                'tags': meta_data.get('tags', []),
                'date_solved': meta_data.get('date_solved', ''),
                'folder': problem_dir
            }
            
            stats['problems'].append(problem_info)
            
            # 統計難度
            difficulty = problem_info['difficulty'].lower()
            if difficulty in ['easy', 'medium', 'hard']:
                stats[difficulty] += 1
            
            # 統計語言
            for lang in problem_info['languages']:
                stats['languages'][lang] += 1
            
            # 統計標籤
            for tag in problem_info['tags']:
                if tag not in ['tag1', 'tag2', 'tag3']:  # 過濾模板標籤
                    stats['tags'][tag] += 1
            
            # 收集最近問題
            if problem_info['date_solved']:
                stats['recent_problems'].append(problem_info)
        
        except Exception as e:
            print(f"⚠️  讀取 {readme_file} 時出錯: {e}")
            continue
    
    stats['total'] = len(stats['problems'])
    
    # 按日期排序最近問題
    stats['recent_problems'].sort(key=lambda x: x['date_solved'], reverse=True)
    stats['recent_problems'] = stats['recent_problems'][:10]  # 只保留最近10個
    
    return stats


def generate_index_by_difficulty(stats):
    """生成按難度分類的索引"""
    index_content = "# LeetCode 題目索引 - 按難度分類\n\n"
    
    difficulties = ['easy', 'medium', 'hard']
    difficulty_names = {'easy': '簡單', 'medium': '中等', 'hard': '困難'}
    difficulty_emojis = {'easy': '✅', 'medium': '🟡', 'hard': '🔴'}
    
    for difficulty in difficulties:
        problems = [p for p in stats['problems'] if p['difficulty'] == difficulty]
        if not problems:
            continue
        
        index_content += f"## {difficulty_emojis[difficulty]} {difficulty_names[difficulty]} ({len(problems)} 題)\n\n"
        index_content += "| 題號 | 題目 | 語言 | 標籤 |\n"
        index_content += "|------|------|------|------|\n"
        
        for problem in sorted(problems, key=lambda x: x['id']):
            languages = ', '.join(problem['languages'])
            tags = ', '.join([tag for tag in problem['tags'] if tag not in ['tag1', 'tag2', 'tag3']])
            folder_link = f"./problems/{problem['folder']}"
            
            index_content += f"| {problem['id']} | [{problem['title']}]({folder_link}) | {languages} | {tags} |\n"
        
        index_content += "\n"
    
    return index_content


def generate_index_by_tags(stats):
    """生成按標籤分類的索引"""
    if not stats['tags']:
        return ""
    
    index_content = "# LeetCode 題目索引 - 按標籤分類\n\n"
    
    for tag, count in stats['tags'].most_common():
        if tag in ['tag1', 'tag2', 'tag3']:  # 跳過模板標籤
            continue
        
        problems = [p for p in stats['problems'] if tag in p['tags']]
        if not problems:
            continue
        
        index_content += f"## {tag} ({count} 題)\n\n"
        index_content += "| 題號 | 題目 | 難度 | 語言 |\n"
        index_content += "|------|------|------|------|\n"
        
        for problem in sorted(problems, key=lambda x: x['id']):
            difficulty_emoji = {'easy': '✅', 'medium': '🟡', 'hard': '🔴'}.get(problem['difficulty'], '❓')
            languages = ', '.join(problem['languages'])
            folder_link = f"./problems/{problem['folder']}"
            
            index_content += f"| {problem['id']} | [{problem['title']}]({folder_link}) | {difficulty_emoji} {problem['difficulty'].title()} | {languages} |\n"
        
        index_content += "\n"
    
    return index_content


def update_readme(readme_path, stats):
    """更新主 README.md 中的統計資訊"""
    if not os.path.exists(readme_path):
        return
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 更新統計表格 - 簡化版本
    stats_section = f"""## 統計資訊

| 難度 | 已解題數 |
|------|----------|
| 🟢 Easy | {stats["easy"]} |
| 🟡 Medium | {stats["medium"]} |
| 🔴 Hard | {stats["hard"]} |
| **總計** | **{stats["total"]}** |"""

    # 替換統計資訊區塊
    stats_pattern = r'## 統計資訊.*?(?=\n## [^#]|\n\n## [^#]|\Z)'
    new_content = re.sub(stats_pattern, stats_section, content, flags=re.DOTALL)
    
    # 更新最近練習表格 - 只顯示最近 3 題
    if stats['recent_problems']:
        recent_section = "\n\n## 最近練習\n\n"
        recent_section += "| 題號 | 題目 | 難度 | 完成日期 |\n"
        recent_section += "|------|------|------|----------|\n"
        
        for problem in stats['recent_problems'][:3]:  # 只顯示最近3個
            difficulty_emoji = {'easy': '🟢', 'medium': '🟡', 'hard': '🔴'}.get(problem['difficulty'], '❓')
            folder_link = f"./problems/{problem['folder']}"
            
            recent_section += f"| {problem['id']} | [{problem['title']}]({folder_link}) | {difficulty_emoji} {problem['difficulty'].title()} | {problem['date_solved']} |\n"
        
        # 替換最近練習區塊
        recent_pattern = r'\n## 最近練習.*?(?=\n## [^#]|\Z)'
        new_content = re.sub(recent_pattern, recent_section, new_content, flags=re.DOTALL)
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)


def main():
    """主函數"""
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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
    
    if stats['languages']:
        print(f"\n語言統計: {dict(stats['languages'])}")
    
    if stats['tags']:
        top_tags = dict(stats['tags'].most_common(5))
        print(f"熱門標籤: {top_tags}")
    
    # 更新 README
    update_readme(readme_path, stats)
    print(f"\n✅ README.md 已更新！")
    
    # 生成索引檔案
    index_dir = os.path.join(project_root, 'docs')
    if not os.path.exists(index_dir):
        os.makedirs(index_dir)
    
    # 按難度索引
    difficulty_index = generate_index_by_difficulty(stats)
    with open(os.path.join(index_dir, 'index-by-difficulty.md'), 'w', encoding='utf-8') as f:
        f.write(difficulty_index)
    print("✅ 已生成按難度分類的索引")
    
    # 按標籤索引
    tags_index = generate_index_by_tags(stats)
    if tags_index:
        with open(os.path.join(index_dir, 'index-by-tags.md'), 'w', encoding='utf-8') as f:
            f.write(tags_index)
        print("✅ 已生成按標籤分類的索引")


if __name__ == "__main__":
    main()

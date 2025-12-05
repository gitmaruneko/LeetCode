#!/usr/bin/env python3
"""
LeetCode Practice Statistics Tool
Based on new project structure: problem-centric organization
Automatically count completed problems and progress
"""

import os
import yaml
import re
from collections import defaultdict, Counter
from datetime import datetime


def parse_frontmatter(readme_content):
    """Parse YAML frontmatter from README"""
    if not readme_content.startswith('---'):
        return None
    
    # Find the second --- position
    end_marker = readme_content.find('---', 3)
    if end_marker == -1:
        return None
    
    frontmatter_text = readme_content[3:end_marker].strip()
    try:
        return yaml.safe_load(frontmatter_text)
    except yaml.YAMLError:
        return None


def scan_problems(problems_dir):
    """Scan problems directory, count completed problems from README frontmatter"""
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
    
    # Scan all problem folders
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
            
            # Parse frontmatter
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
            
            # Count by difficulty
            difficulty = problem_info['difficulty'].lower()
            if difficulty in ['easy', 'medium', 'hard']:
                stats[difficulty] += 1
            
            # Count by language
            for lang in problem_info['languages']:
                stats['languages'][lang] += 1
            
            # Count by tags
            for tag in problem_info['tags']:
                if tag not in ['tag1', 'tag2', 'tag3']:  # Filter template tags
                    stats['tags'][tag] += 1
            
            # Collect recent problems
            if problem_info['date_solved']:
                stats['recent_problems'].append(problem_info)
        
        except Exception as e:
            print(f"⚠️  Error reading {readme_file}: {e}")
            continue
    
    stats['total'] = len(stats['problems'])
    
    # Sort recent problems by date
    stats['recent_problems'].sort(key=lambda x: x['date_solved'], reverse=True)
    stats['recent_problems'] = stats['recent_problems'][:10]  # Keep only latest 10
    
    return stats


def generate_index_by_difficulty(stats):
    """Generate index classified by difficulty"""
    index_content = "# LeetCode Problem Index - By Difficulty\n\n"
    
    difficulties = ['easy', 'medium', 'hard']
    difficulty_names = {'easy': 'Easy', 'medium': 'Medium', 'hard': 'Hard'}
    difficulty_emojis = {'easy': '✅', 'medium': '🟡', 'hard': '🔴'}
    
    for difficulty in difficulties:
        problems = [p for p in stats['problems'] if p['difficulty'] == difficulty]
        if not problems:
            continue
        
        index_content += f"## {difficulty_emojis[difficulty]} {difficulty_names[difficulty]} ({len(problems)} problems)\n\n"
        index_content += "| ID | Problem | Languages | Tags |\n"
        index_content += "|------|------|------|------|\n"
        
        for problem in sorted(problems, key=lambda x: x['id']):
            languages = ', '.join(problem['languages'])
            tags = ', '.join([tag for tag in problem['tags'] if tag not in ['tag1', 'tag2', 'tag3']])
            folder_link = f"./problems/{problem['folder']}"
            
            index_content += f"| {problem['id']} | [{problem['title']}]({folder_link}) | {languages} | {tags} |\n"
        
        index_content += "\n"
    
    return index_content


def generate_index_by_tags(stats):
    """Generate index classified by tags"""
    if not stats['tags']:
        return ""
    
    index_content = "# LeetCode Problem Index - By Tags\n\n"
    
    for tag, count in stats['tags'].most_common():
        if tag in ['tag1', 'tag2', 'tag3']:  # Skip template tags
            continue
        
        problems = [p for p in stats['problems'] if tag in p['tags']]
        if not problems:
            continue
        
        index_content += f"## {tag} ({count} problems)\n\n"
        index_content += "| ID | Problem | Difficulty | Languages |\n"
        index_content += "|------|------|------|------|\n"
        
        for problem in sorted(problems, key=lambda x: x['id']):
            difficulty_emoji = {'easy': '✅', 'medium': '🟡', 'hard': '🔴'}.get(problem['difficulty'], '❓')
            languages = ', '.join(problem['languages'])
            folder_link = f"./problems/{problem['folder']}"
            
            index_content += f"| {problem['id']} | [{problem['title']}]({folder_link}) | {difficulty_emoji} {problem['difficulty'].title()} | {languages} |\n"
        
        index_content += "\n"
    
    return index_content


def update_readme(readme_path, stats):
    """Update statistics in main README.md"""
    if not os.path.exists(readme_path):
        return
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update statistics table - simplified version
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
    """Main function"""
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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
    
    if stats['languages']:
        print(f"\nLanguage stats: {dict(stats['languages'])}")
    
    if stats['tags']:
        top_tags = dict(stats['tags'].most_common(5))
        print(f"Popular tags: {top_tags}")
    
    # Update README
    update_readme(readme_path, stats)
    print(f"\n✅ README.md updated!")
    
    # Generate index files
    index_dir = os.path.join(project_root, 'docs')
    if not os.path.exists(index_dir):
        os.makedirs(index_dir)
    
    # Index by difficulty
    difficulty_index = generate_index_by_difficulty(stats)
    with open(os.path.join(index_dir, 'index-by-difficulty.md'), 'w', encoding='utf-8') as f:
        f.write(difficulty_index)
    print("✅ Generated index by difficulty")
    
    # Index by tags
    tags_index = generate_index_by_tags(stats)
    if tags_index:
        with open(os.path.join(index_dir, 'index-by-tags.md'), 'w', encoding='utf-8') as f:
            f.write(tags_index)
        print("✅ Generated index by tags")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Sync meta.yaml information to README.md
Integrate structured metadata into each problem's README
"""

import os
import yaml
import re
from pathlib import Path


def sync_meta_to_readme(problem_dir):
    """Sync meta.yaml information to README.md"""
    meta_file = os.path.join(problem_dir, 'meta.yaml')
    readme_file = os.path.join(problem_dir, 'README.md')
    
    if not os.path.exists(meta_file) or not os.path.exists(readme_file):
        return False
    
    # Read meta.yaml
    with open(meta_file, 'r', encoding='utf-8') as f:
        meta = yaml.safe_load(f)
    
    # Read existing README
    with open(readme_file, 'r', encoding='utf-8') as f:
        readme_content = f.read()
    
    # Build info card
    difficulty_emoji = {'easy': '🟢', 'medium': '🟡', 'hard': '🔴'}
    difficulty_display = f"{difficulty_emoji.get(meta['difficulty'], '❓')} **{meta['difficulty'].title()}**"
    tags_display = ' '.join([f"`{tag}`" for tag in meta.get('tags', [])])
    
    info_card = f"""> **Problem Information**  
> 🔗 [LeetCode](https://leetcode.com/problems/{meta['url_slug']}/) | 🎯 {difficulty_display} | 🏷️ {tags_display} | 📅 {meta['date_solved']}"""
    
    # Check if info card already exists
    title_pattern = rf"# {meta['id']}\. {re.escape(meta['title'])}"
    
    if re.search(r'> \*\*Problem Information\*\*', readme_content) or re.search(r'> \*\*題目資訊\*\*', readme_content):
        # Replace existing info card
        info_pattern = r'> \*\*(?:Problem Information|題目資訊)\*\*.*?(?=\n\n|\n#|\Z)'
        new_content = re.sub(info_pattern, info_card, readme_content, flags=re.DOTALL)
    else:
        # Add info card after title
        title_match = re.search(title_pattern, readme_content)
        if title_match:
            insert_pos = title_match.end()
            new_content = (readme_content[:insert_pos] + 
                          f"\n\n{info_card}\n" + 
                          readme_content[insert_pos:])
        else:
            return False
    
    # Add learning notes section (if doesn't exist)
    if '## Learning Notes' not in new_content and '## 學習筆記' not in new_content and meta.get('notes'):
        notes_section = f"\n\n## Learning Notes\n\n{meta['notes']}"
        new_content += notes_section
    
    # Write back to file
    with open(readme_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True


def main():
    """Sync all problems' meta.yaml to README.md"""
    project_root = Path(__file__).parent.parent
    problems_dir = project_root / 'problems'
    
    if not problems_dir.exists():
        print("❌ problems folder does not exist")
        return
    
    synced_count = 0
    for problem_folder in problems_dir.iterdir():
        if problem_folder.is_dir():
            if sync_meta_to_readme(problem_folder):
                print(f"✅ Synced: {problem_folder.name}")
                synced_count += 1
            else:
                print(f"⚠️  Skipped: {problem_folder.name} (missing required files)")
    
    print(f"\n🎉 Sync complete! Processed {synced_count} problems")


if __name__ == "__main__":
    main()

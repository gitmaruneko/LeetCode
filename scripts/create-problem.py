#!/usr/bin/env python3
"""
Quick LeetCode problem file creator
Based on new project structure: problem-centric organization
"""

import os
import sys
import re
import yaml
from datetime import datetime


def kebab_case(text):
    """Convert text to kebab-case format"""
    # Remove special characters, keep letters, numbers, spaces, hyphens
    text = re.sub(r'[^\w\s-]', '', text.lower())
    # Replace spaces and multiple hyphens with single hyphen
    text = re.sub(r'[-\s]+', '-', text)
    # Remove leading and trailing hyphens
    return text.strip('-')


def create_problem_structure(problem_id, title, difficulty, languages=['python'], topics=None):
    """Create complete structure for new problem"""
    
    # Format problem ID (5 digits)
    problem_id_str = f"{int(problem_id):05d}"
    
    # Convert title to kebab-case
    title_slug = kebab_case(title)
    url_slug = title_slug  # URL slug usually matches kebab-case title
    
    # Create problem folder
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    problem_dir = os.path.join(project_root, 'problems', f"{problem_id_str}-{title_slug}")
    
    if os.path.exists(problem_dir):
        print(f"❌ Error: Problem folder already exists: {problem_dir}")
        return
    
    os.makedirs(problem_dir)
    print(f"✅ Created problem folder: {problem_dir}")
    
    # No longer creating language subfolders, create language-specific files in root
    
    # Create README.md (using YAML frontmatter to integrate all information)
    difficulty_emoji = {'easy': '🟢', 'medium': '🟡', 'hard': '🔴'}
    difficulty_display = f"{difficulty_emoji.get(difficulty.lower(), '❓')} **{difficulty.title()}**"
    
    # Use provided topics or default values
    if topics and len(topics) > 0:
        default_topics = topics
        default_tags = topics  # tags use same topics
    else:
        default_topics = ["Topic 1", "Topic 2"]
        default_tags = ["Tag 1", "Tag 2"]
    tags_display = ' '.join([f"`{tag}`" for tag in default_tags])
    
    date_str = datetime.now().strftime('%Y-%m-%d')
    
    readme_content = f"""---
id: {problem_id}
title: "{title}"
url_slug: "{url_slug}"
difficulty: "{difficulty.lower()}"
tags: {default_tags}
topics: {default_topics}
date_created: "{date_str}"
date_solved: "{date_str}"
languages: {languages}
notes: "待填入解題心得和筆記"
---

# {problem_id}. {title}

> **題目資訊**  
> 🔗 [LeetCode](https://leetcode.com/problems/{url_slug}/) | 🎯 {difficulty_display} | 🏷️ {tags_display} | 📅 {date_str}

## 題目描述

[待填入題目描述]

## 解題思路

### 方法一：

[待填入解題思路]

1. [步驟1]
2. [步驟2]
3. [步驟3]

## 複雜度分析

### 方法
- **時間複雜度**：O(?)
- **空間複雜度**：O(?)

## 學習筆記

待填入解題心得和筆記
"""
    
    readme_file = os.path.join(problem_dir, 'README.md')
    with open(readme_file, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    print(f"✅ Created README file: {readme_file}")
    
    # Create solution files for each language
    for lang in languages:
        if lang == 'python':
            create_python_solution(problem_dir, problem_id, title, url_slug, default_topics)
        elif lang == 'cpp':
            create_cpp_solution(problem_dir, problem_id, title, url_slug, default_topics)
        elif lang == 'javascript':
            create_js_solution(problem_dir, problem_id, title, url_slug, default_topics)
    
    print(f"\n🎉 Problem {problem_id}. {title} created successfully!")
    print(f"📁 Folder: {problem_dir}")


def create_python_solution(problem_dir, problem_id, title, url_slug, topics=None):
    """Create Python solution file"""
    # Create solution-python.py directly in problem root directory
    
    # Format topics
    if topics and len(topics) > 0:
        tags_str = ', '.join(topics)
    else:
        tags_str = 'To be filled'
    
    solution_content = f'''"""
{problem_id}. {title}
https://leetcode.com/problems/{url_slug}/

Time Complexity: O(?)
Space Complexity: O(?)

Tags: {tags_str}
"""

class Solution:
    def solve(self, param):

        pass


def test_solution():
    """測試函數"""
    solution = Solution()
    
    test_cases = [
        # (input, expected_output),
        # 範例：(example_input, expected_result),
    ]
    
    for i, (input_data, expected) in enumerate(test_cases):
        result = solution.solve(input_data)
        print(f"Test {{i+1}}: input={{input_data}} -> {{result}} (Expected: {{expected}})")
        assert result == expected, f"Test {{i+1}} failed"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
'''
    
    solution_file = os.path.join(problem_dir, 'solution-python.py')
    with open(solution_file, 'w', encoding='utf-8') as f:
        f.write(solution_content)
    print(f"✅ Created Python solution: {solution_file}")


def create_cpp_solution(problem_dir, problem_id, title, url_slug, topics=None):
    """Create C++ solution file"""
    cpp_dir = os.path.join(problem_dir, 'cpp')
    
    # Format topics
    if topics and len(topics) > 0:
        tags_str = ', '.join(topics)
    else:
        tags_str = 'To be filled'
    
    solution_content = f'''/*
{problem_id}. {title}
https://leetcode.com/problems/{url_slug}/

Time Complexity: O(?)
Space Complexity: O(?)

Tags: {tags_str}
*/

#include <vector>
#include <iostream>
using namespace std;

class Solution {{
public:
    // [待填入返回類型] solve([待填入參數類型] param) {{
    //     // [待填入解題思路]
    //     return [待填入返回值];
    // }}
}};

// 測試函數
int main() {{
    Solution solution;
    
    // 測試用例
    // [待填入測試用例]
    
    cout << "All tests passed!" << endl;
    return 0;
}}
'''
    
    solution_file = os.path.join(cpp_dir, 'solution.cpp')
    with open(solution_file, 'w', encoding='utf-8') as f:
        f.write(solution_content)
    print(f"✅ Created C++ solution: {solution_file}")


def create_js_solution(problem_dir, problem_id, title, url_slug, topics=None):
    """Create JavaScript solution file"""
    js_dir = os.path.join(problem_dir, 'javascript')
    
    # Format topics
    if topics and len(topics) > 0:
        tags_str = ', '.join(topics)
    else:
        tags_str = 'To be filled'
    
    solution_content = f'''/**
 * {problem_id}. {title}
 * https://leetcode.com/problems/{url_slug}/
 * 
 * Time Complexity: O(?)
 * Space Complexity: O(?)
 * 
 * Tags: {tags_str}
 */

/**
 * [待填入解題思路描述]
 * @param {{[參數類型]}} param [參數描述]
 * @return {{[返回類型]}} [返回值描述]
 */
var solve = function(param) {{
    // [待填入解題邏輯]
}};

// 測試函數
function testSolution() {{
    const testCases = [
        // [input, expected_output],
        // 範例：[example_input, expected_result],
    ];
    
    testCases.forEach((testCase, i) => {{
        const [input, expected] = testCase;
        const result = solve(input);
        console.log(`Test ${{i+1}}: input=${{JSON.stringify(input)}} -> ${{JSON.stringify(result)}} (Expected: ${{JSON.stringify(expected)}})`);
        console.assert(JSON.stringify(result) === JSON.stringify(expected), `Test ${{i+1}} failed`);
    }});
    
    console.log("All tests passed!");
}}

// 執行測試
testSolution();
'''
    
    solution_file = os.path.join(js_dir, 'solution.js')
    with open(solution_file, 'w', encoding='utf-8') as f:
        f.write(solution_content)
    print(f"✅ Created JavaScript solution: {solution_file}")


def main():
    """Main function"""
    if len(sys.argv) < 4:
        print("Usage: python create-problem.py <problem_id> <title> <difficulty> [lang1,lang2,...] [--topics topic1,topic2,...]")
        print("Example: python create-problem.py 20 'Valid Parentheses' easy python,cpp")
        print("Example (with topics): python create-problem.py 20 'Valid Parentheses' easy --topics Array,Hash Table")
        print("Supported languages: python, cpp, javascript")
        sys.exit(1)
    
    problem_id = sys.argv[1]
    title = sys.argv[2]
    difficulty = sys.argv[3]
    
    # Parse language parameters and topics
    languages = ['python']  # Default
    topics = None
    
    i = 4
    while i < len(sys.argv):
        if sys.argv[i] == '--topics':
            if i + 1 < len(sys.argv):
                topics = [t.strip() for t in sys.argv[i + 1].split(',')]
                i += 2
            else:
                print("❌ --topics parameter requires a list of tags")
                sys.exit(1)
        else:
            languages = [lang.strip() for lang in sys.argv[i].split(',')]
            i += 1
    
    # Validate languages
    supported_languages = {'python', 'cpp', 'javascript'}
    invalid_languages = set(languages) - supported_languages
    if invalid_languages:
        print(f"❌ Unsupported languages: {', '.join(invalid_languages)}")
        print(f"Supported languages: {', '.join(supported_languages)}")
        sys.exit(1)
    
    create_problem_structure(problem_id, title, difficulty, languages, topics)


if __name__ == "__main__":
    main()

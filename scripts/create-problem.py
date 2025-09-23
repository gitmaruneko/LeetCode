#!/usr/bin/env python3
"""
快速創建新 LeetCode 題目檔案的工具
基於新的專案結構：以題目為中心的組織方式
"""

import os
import sys
import re
import yaml
from datetime import datetime


def kebab_case(text):
    """將文本轉換為 kebab-case 格式"""
    # 移除特殊字符，保留字母、數字、空格、連字符
    text = re.sub(r'[^\w\s-]', '', text.lower())
    # 將空格和多個連字符替換為單個連字符
    text = re.sub(r'[-\s]+', '-', text)
    # 移除開頭和結尾的連字符
    return text.strip('-')


def create_problem_structure(problem_id, title, difficulty, languages=['python']):
    """創建新題目的完整結構"""
    
    # 格式化題目編號 (4位數)
    problem_id_str = f"{int(problem_id):05d}"
    
    # 轉換標題為 kebab-case
    title_slug = kebab_case(title)
    url_slug = title_slug  # URL slug 通常與 kebab-case 標題相同
    
    # 創建題目資料夾
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    problem_dir = os.path.join(project_root, 'problems', f"{problem_id_str}-{title_slug}")
    
    if os.path.exists(problem_dir):
        print(f"❌ 錯誤：題目資料夾已存在: {problem_dir}")
        return
    
    os.makedirs(problem_dir)
    print(f"✅ 創建題目資料夾: {problem_dir}")
    
    # 不再創建語言子資料夾，直接在根目錄創建語言特定檔案
    
    # 創建 README.md（使用 YAML frontmatter 整合所有資訊）
    difficulty_emoji = {'easy': '🟢', 'medium': '🟡', 'hard': '🔴'}
    difficulty_display = f"{difficulty_emoji.get(difficulty.lower(), '❓')} **{difficulty.title()}**"
    
    # 預設標籤和相關題目
    default_tags = ["待填入標籤1", "待填入標籤2"]
    tags_display = ' '.join([f"`{tag}`" for tag in default_tags])
    
    date_str = datetime.now().strftime('%Y-%m-%d')
    
    readme_content = f"""---
id: {problem_id}
title: "{title}"
url_slug: "{url_slug}"
difficulty: "{difficulty.lower()}"
tags: {default_tags}
topics: ["待填入主題1", "待填入主題2"]
date_created: "{date_str}"
date_solved: "{date_str}"
languages: {languages}
notes: "待填入解題心得和筆記"
related_problems:
  - id: 0
    title: "相關題目1"
  - id: 0
    title: "相關題目2"
---

# {problem_id}. {title}

> **題目資訊**  
> 🔗 [LeetCode](https://leetcode.com/problems/{url_slug}/) | 🎯 {difficulty_display} | 🏷️ {tags_display} | 📅 {date_str}

## 題目描述

[待填入題目描述]

## 解題思路

### 方法一：[解法名稱]

[待填入解題思路]

**算法步驟：**
1. [步驟1]
2. [步驟2]
3. [步驟3]

## 複雜度分析

### 方法一
- **時間複雜度**：O(?)
- **空間複雜度**：O(?)

## 相關標籤

- `待填入標籤1`
- `待填入標籤2`

## 相關題目

- [相關題目1](../相關連結1)
- [相關題目2](../相關連結2)

## 學習筆記

待填入解題心得和筆記
"""
    
    readme_file = os.path.join(problem_dir, 'README.md')
    with open(readme_file, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    print(f"✅ 創建README檔案: {readme_file}")
    
    # 為每種語言創建解答檔案
    for lang in languages:
        if lang == 'python':
            create_python_solution(problem_dir, problem_id, title, url_slug)
        elif lang == 'cpp':
            create_cpp_solution(problem_dir, problem_id, title, url_slug)
        elif lang == 'javascript':
            create_js_solution(problem_dir, problem_id, title, url_slug)
    
    print(f"\n🎉 題目 {problem_id}. {title} 創建完成！")
    print(f"📁 資料夾: {problem_dir}")


def create_python_solution(problem_dir, problem_id, title, url_slug):
    """創建 Python 解答檔案"""
    # 直接在題目根目錄創建 solution-python.py
    
    solution_content = f'''"""
{problem_id}. {title}
https://leetcode.com/problems/{url_slug}/

Time Complexity: O(?)
Space Complexity: O(?)

Tags: [待填入標籤]
"""

class Solution:
    def solve(self, param):
        """
        [待填入解題思路描述]
        
        Args:
            param: [參數描述]
            
        Returns:
            [返回值描述]
        """
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
    print(f"✅ 創建Python解答: {solution_file}")


def create_cpp_solution(problem_dir, problem_id, title, url_slug):
    """創建 C++ 解答檔案"""
    cpp_dir = os.path.join(problem_dir, 'cpp')
    
    solution_content = f'''/*
{problem_id}. {title}
https://leetcode.com/problems/{url_slug}/

Time Complexity: O(?)
Space Complexity: O(?)

Tags: [待填入標籤]
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
    print(f"✅ 創建C++解答: {solution_file}")


def create_js_solution(problem_dir, problem_id, title, url_slug):
    """創建 JavaScript 解答檔案"""
    js_dir = os.path.join(problem_dir, 'javascript')
    
    solution_content = f'''/**
 * {problem_id}. {title}
 * https://leetcode.com/problems/{url_slug}/
 * 
 * Time Complexity: O(?)
 * Space Complexity: O(?)
 * 
 * Tags: [待填入標籤]
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
    print(f"✅ 創建JavaScript解答: {solution_file}")


def main():
    """主函數"""
    if len(sys.argv) < 4:
        print("使用方法: python create-problem.py <題號> <題目標題> <難度> [語言1,語言2,...]")
        print("範例: python create-problem.py 20 'Valid Parentheses' easy python,cpp")
        print("支援的語言: python, cpp, javascript")
        sys.exit(1)
    
    problem_id = sys.argv[1]
    title = sys.argv[2]
    difficulty = sys.argv[3]
    
    # 解析語言參數
    languages = ['python']  # 預設
    if len(sys.argv) > 4:
        languages = [lang.strip() for lang in sys.argv[4].split(',')]
    
    # 驗證語言
    supported_languages = {'python', 'cpp', 'javascript'}
    invalid_languages = set(languages) - supported_languages
    if invalid_languages:
        print(f"❌ 不支援的語言: {', '.join(invalid_languages)}")
        print(f"支援的語言: {', '.join(supported_languages)}")
        sys.exit(1)
    
    create_problem_structure(problem_id, title, difficulty, languages)


if __name__ == "__main__":
    main()

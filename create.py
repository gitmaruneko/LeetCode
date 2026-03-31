#!/usr/bin/env python3
"""
Simplified LeetCode Problem Creator
Usage: python create.py 1408
"""

import sys
import subprocess
import requests
import re
import html
import ast


def get_leetcode_problem_info(problem_id):
    """Fetch problem information from LeetCode GraphQL API (including topics)"""
    
    # LeetCode GraphQL endpoint
    url = "https://leetcode.com/graphql"
    
    # First, get all problems list to find titleSlug
    all_problems_query = """
    query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
        problemsetQuestionList: questionList(
            categorySlug: $categorySlug
            limit: $limit
            skip: $skip
            filters: $filters
        ) {
            questions: data {
                questionId
                questionFrontendId
                title
                titleSlug
                difficulty
            }
        }
    }
    """
    
    # Get detailed problem information (including topics)
    detail_query = """
    query questionData($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            questionId
            questionFrontendId
            title
            titleSlug
            difficulty
            content
            metaData
            topicTags {
                name
                slug
            }
        }
    }
    """
    
    try:
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0'
        }
        
        # Step 1: Find the problem's titleSlug
        payload = {
            "query": all_problems_query,
            "variables": {
                "categorySlug": "",
                "skip": 0,
                "limit": 3000,
                "filters": {}
            }
        }
        
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        data = response.json()
        
        title_slug = None
        if 'data' in data and 'problemsetQuestionList' in data['data']:
            questions = data['data']['problemsetQuestionList']['questions']
            
            for q in questions:
                if q['questionFrontendId'] == str(problem_id):
                    title_slug = q['titleSlug']
                    break
        
        if not title_slug:
            return None
        
        # Step 2: Get detailed information (including topics)
        detail_payload = {
            "query": detail_query,
            "variables": {
                "titleSlug": title_slug
            }
        }
        
        detail_response = requests.post(url, json=detail_payload, headers=headers, timeout=10)
        detail_data = detail_response.json()
        
        if 'data' in detail_data and 'question' in detail_data['data']:
            q = detail_data['data']['question']
            topics = [tag['name'] for tag in q.get('topicTags', [])]
            
            return {
                'id': q['questionFrontendId'],
                'title': q['title'],
                'difficulty': q['difficulty'].lower(),
                'topics': topics,
                'titleSlug': q['titleSlug'],
                'content': q.get('content') or '',
                'metaData': q.get('metaData') or '{}'
            }
        
        return None
        
    except Exception as e:
        print(f"⚠️  Unable to fetch problem information from LeetCode: {e}")
        return None


def _safe_eval_literal(text):
    """Convert LeetCode literal text to Python value."""
    normalized = text.strip()
    normalized = re.sub(r'\btrue\b', 'True', normalized, flags=re.IGNORECASE)
    normalized = re.sub(r'\bfalse\b', 'False', normalized, flags=re.IGNORECASE)
    normalized = re.sub(r'\bnull\b', 'None', normalized, flags=re.IGNORECASE)
    return ast.literal_eval(normalized)


def _extract_param_names(meta_data):
    """Extract ordered parameter names from LeetCode metadata JSON."""
    try:
        import json
        parsed = json.loads(meta_data or '{}')
        params = parsed.get('params') or []
        names = [p.get('name') for p in params if p.get('name')]
        return names
    except Exception:
        return []


def _extract_examples_from_content(content):
    """Extract (input, output) strings from question HTML content."""
    blocks = re.findall(r'<pre>(.*?)</pre>', content or '', flags=re.IGNORECASE | re.DOTALL)
    examples = []

    for block in blocks:
        text = re.sub(r'<br\s*/?>', '\n', block, flags=re.IGNORECASE)
        text = re.sub(r'<[^>]+>', '', text)
        text = html.unescape(text)
        text = text.replace('\r\n', '\n').replace('\r', '\n')

        m = re.search(r'Input:\s*(.*?)\s*Output:\s*(.*?)(?:\n\s*Explanation:|\n\s*Constraints:|$)', text, flags=re.DOTALL)
        if not m:
            continue

        input_text = m.group(1).strip()
        output_text = m.group(2).strip()
        examples.append((input_text, output_text))

    return examples


def _parse_input_values(input_text, param_names):
    """Parse LeetCode input expression into Python args."""
    if not param_names:
        return None

    values = []
    for i, name in enumerate(param_names):
        if i + 1 < len(param_names):
            next_name = re.escape(param_names[i + 1])
            pattern = rf'{re.escape(name)}\s*=\s*(.*?)(?=,\s*{next_name}\s*=|$)'
        else:
            pattern = rf'{re.escape(name)}\s*=\s*(.*)$'

        m = re.search(pattern, input_text, flags=re.DOTALL)
        if not m:
            return None

        raw_value = m.group(1).strip()
        try:
            values.append(_safe_eval_literal(raw_value))
        except Exception:
            return None

    return values


def _parse_expected_output(output_text):
    """Parse expected return value from LeetCode output expression."""
    output_text = output_text.strip()

    # For in-place array problems LeetCode may show: "2, nums = [1,2,_]"
    first_part = output_text.split(',', 1)[0].strip()

    for candidate in (output_text, first_part):
        try:
            return _safe_eval_literal(candidate)
        except Exception:
            continue

    return None


def build_python_test_cases(content, meta_data):
    """Build Python test cases as list[(input_data, expected)]."""
    param_names = _extract_param_names(meta_data)
    if not param_names:
        return []

    parsed_cases = []
    for input_text, output_text in _extract_examples_from_content(content):
        values = _parse_input_values(input_text, param_names)
        expected = _parse_expected_output(output_text)

        if values is None or expected is None:
            continue

        input_data = values[0] if len(values) == 1 else tuple(values)
        parsed_cases.append((input_data, expected))

    return parsed_cases


def populate_python_test_cases(problem_id, title_slug, test_cases):
    """Inject extracted test cases into generated solution-python.py."""
    if not test_cases:
        return

    problem_dir = f"problems/{int(problem_id):05d}-{title_slug}"
    solution_file = f"{problem_dir}/solution-python.py"

    try:
        with open(solution_file, 'r', encoding='utf-8') as f:
            content = f.read()

        formatted_cases = []
        for input_data, expected in test_cases:
            formatted_cases.append(f"        ({repr(input_data)}, {repr(expected)}),")

        replacement = "\n".join([
            "    test_cases = [",
            *formatted_cases,
            "    ]"
        ])

        updated = re.sub(
            r"    test_cases = \[\n(?:.|\n)*?    \]",
            replacement,
            content,
            count=1,
            flags=re.DOTALL,
        )

        with open(solution_file, 'w', encoding='utf-8') as f:
            f.write(updated)

        print(f"✅ Auto-filled test cases: {solution_file}")
    except Exception as e:
        print(f"⚠️  Unable to auto-fill test cases: {e}")


def create_problem(problem_id):
    """Create LeetCode problem structure"""
    
    print(f"🔍 Querying LeetCode problem #{problem_id} information...")
    
    # Try to fetch problem information from LeetCode
    info = get_leetcode_problem_info(problem_id)
    
    if info:
        print(f"✅ Found problem: {info['title']}")
        print(f"   Difficulty: {info['difficulty']}")
        if info.get('topics'):
            print(f"   Tags: {', '.join(info['topics'])}")
        
        # Call the original create-problem.py script with topics
        cmd = [
            sys.executable,
            'scripts/create-problem.py',
            str(problem_id),
            info['title'],
            info['difficulty']
        ]
        
        # If topics available, pass as additional arguments
        if info.get('topics'):
            cmd.append('--topics')
            cmd.append(','.join(info['topics']))
        
    else:
        # If API fails, prompt user for manual input
        print(f"❌ Unable to automatically fetch information for problem #{problem_id}")
        print(f"\nPlease run manually:")
        print(f'python scripts/create-problem.py {problem_id} "Problem Title" difficulty')
        return False
    
    # Execute creation script
    print(f"\n🚀 Creating problem structure...")
    result = subprocess.run(cmd, capture_output=False)

    if result.returncode == 0 and info:
        test_cases = build_python_test_cases(info.get('content', ''), info.get('metaData', '{}'))
        populate_python_test_cases(problem_id, info['titleSlug'], test_cases)
    
    return result.returncode == 0


def main():
    if len(sys.argv) < 2:
        print("Usage: python create.py <problem_number>")
        print("Example: python create.py 1408")
        sys.exit(1)
    
    try:
        problem_id = int(sys.argv[1])
    except ValueError:
        print("❌ Error: Problem number must be an integer")
        sys.exit(1)
    
    success = create_problem(problem_id)
    
    if success:
        print("\n✅ Problem created successfully!")
    else:
        print("\n❌ Problem creation failed")
        sys.exit(1)


if __name__ == '__main__':
    main()

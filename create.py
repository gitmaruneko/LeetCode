#!/usr/bin/env python3
"""
Simplified LeetCode Problem Creator
Usage: python create.py 1408
"""

import sys
import subprocess
import requests
import re


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
                'titleSlug': q['titleSlug']
            }
        
        return None
        
    except Exception as e:
        print(f"⚠️  Unable to fetch problem information from LeetCode: {e}")
        return None


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

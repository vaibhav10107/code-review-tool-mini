from typing import List, Tuple

def review_code_snippet(snippet: str) -> List[Tuple[int, str]]:
    issues = []
    lines = snippet.split('\n')
    for i, line in enumerate(lines):
        if 'TODO' in line:
            issues.append((i+1, 'TODO found'))
        if 'print' in line:
            issues.append((i+1, 'Print statement found'))
    return issues

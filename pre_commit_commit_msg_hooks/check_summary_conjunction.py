"""
Check the summary does not contain conjugated sentences.

Searches for occurrences of 'and', 'nor', and 'or' and fails if found.
"""
from pre_commit_commit_msg_hooks.common import get_commit_msg_lines


def main():
    summary, _ = get_commit_msg_lines()
    conjuctions = [
        'and',
        'nor',
        'but',
        'or',
        'yet',
        'so',
    ]
    words = summary.split()
    for word in words:
        if word in conjuctions:
            print(summary)
            print(f"Conjunction '{word}' found in summary.")
            return 1

    return 0


if __name__ == '__main__':
    SystemExit(main())

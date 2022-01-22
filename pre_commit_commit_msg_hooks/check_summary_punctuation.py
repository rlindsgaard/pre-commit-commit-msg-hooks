"""
Check the summary does not end with punctuation.

Checks the last character against ``string.punctuation`` and fails
on match.
"""
from pre_commit_commit_msg_hooks.common import get_commit_msg_lines


def main():
    summary, _ = get_commit_msg_lines()
    from string import punctuation
    if summary[-1] in punctuation:
        print(summary)
        print(f'Summary is punctuated.')
        return 1

    return 0


if __name__ == '__main__':
    SystemExit(main())

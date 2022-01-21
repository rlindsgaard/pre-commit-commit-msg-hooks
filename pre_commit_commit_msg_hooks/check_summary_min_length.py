"""Check the summary is at least 6 characters."""
from pre_commit_commit_msg_hooks.common import get_commit_msg_lines


def main():
    summary, _ = get_commit_msg_lines()
    limit = 6
    summary_len = len(summary)
    if summary_len < limit:
        print(summary)
        print(f'Summary too short. {summary_len} < {limit}.')
        return 1

    return 0


if __name__ == '__main__':
    SystemExit(main())

"""Check lines in the description are not more than 72 characters."""
from pre_commit_commit_msg_hooks.common import get_commit_msg_lines


def main():
    _, description = get_commit_msg_lines()

    if not description:
        return

    limit = 72
    retval = 0

    for line in description:
        line_len = len(line)
        if line_len > limit:
            print(line)
            print(f'Line exceeds limit. {line_len} > {limit}')
            retval = 1

    return retval


if __name__ == '__main__':
    SystemExit(main())

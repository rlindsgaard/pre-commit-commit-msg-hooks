"""Check the second line of the commit message is blank."""
from pre_commit_commit_msg_hooks.common import get_commit_msg_lines


def main():
    _, description = get_commit_msg_lines()

    if not description:
        return

    if description[0] != '':
        print(description[0])
        print('Second line not empty.')
        return 1

    return 0

if __name__ == '__main__':
    SystemExit(main())

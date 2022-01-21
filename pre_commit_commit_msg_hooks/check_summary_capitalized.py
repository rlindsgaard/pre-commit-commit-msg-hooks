"""Check the summary starts with a capital letter."""
from pre_commit_commit_msg_hooks.common import get_commit_msg_lines


def main():
    summary, _ = get_commit_msg_lines()
    first_word = summary.split()[0]
    if first_word != first_word.capitalize():
        print(summary)
        print(f'Summary not capitalized.')
        return 1

    return 0


if __name__ == '__main__':
    SystemExit(main())

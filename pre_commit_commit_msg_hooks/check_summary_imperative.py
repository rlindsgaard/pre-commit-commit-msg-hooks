"""
Check the summary starts with a verb.

Searches a wordlist comprised of > 6000 verbs. The check fails
if not found.
"""
from pre_commit_commit_msg_hooks.common import get_commit_msg_lines
import os

here = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(here, 'verbs-wordlist.txt'), mode='r') as f:
    verbs = [l.strip().lower() for l in f.readlines()]


def main():
    summary, _ = get_commit_msg_lines()

    first_word = summary.split()[0]

    if first_word.lower() not in verbs:
        print(summary)
        print('Summary not imperative tense.')
        return 1

    return 0


if __name__ == '__main__':
    SystemExit(main())

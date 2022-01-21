import sys

def get_commit_msg_lines():
    filename = sys.argv[1]

    with open(filename, mode='r') as f:
        tmpfile = f.readlines()

    lines = [l.strip() for l in tmpfile]
    summary = lines[0]

    # We don't want to work on git's auto-generated messages
    if summary.startswith('squash!') or summary.startswith('fixup!'):
        return None, None

    description = []
    if len(lines) > 1:
        description = lines[1:]

    return summary, description

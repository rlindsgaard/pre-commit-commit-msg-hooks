###########################
pre-commit-commit-msg-hooks
###########################

A collection of checks for the commit-msg for pre-commit.

The hooks in this repository makes it possible to check for the
rules defined by https://commit.style/.::

   Commit message style guide for Git

   The first line of a commit message serves as a summary.  When displayed
   on the web, it's often styled as a heading, and in emails, it's
   typically used as the subject.  As such, you should capitalize it and
   omit any trailing punctuation.  Aim for about 50 characters, give or
   take, otherwise it may be painfully truncated in some contexts.  Write
   it, along with the rest of your message, in the imperative tense: "Fix
   bug" and not "Fixed bug" or "Fixes bug".  Consistent wording makes it
   easier to mentally process a list of commits.

   Oftentimes a subject by itself is sufficient.  When it's not, add a
   blank line (this is important) followed by one or more paragraphs hard
   wrapped to 72 characters.  Git is strongly opinionated that the author
   is responsible for line breaks; if you omit them, command line tooling
   will show it as one extremely long unwrapped line.  Fortunately, most
   text editors are capable of automating this.

   :q


And then some.

All hooks can be used from the command line as well.

Usage
=====
Configure https://pre-commit.com for checking compliance with
https://commit.style

.. code-block::
    :name: .pre-commit-config.yaml

    repos:
      - repo: ../pre-commit-commit-msg-hooks
        rev: 0.1.0
        hooks:
          - id: check-description-max-length
          - id: check-second-line-empty
          - id: check-summary-capitalized
          - id: check-summary-imperative
          - id: check-summary-max-length
          - id: check-summary-punctuation


Available Hooks
===============

check-description-max-length
----------------------------

Check lines in the description are not more than 72 characters.


check-second-line-empty
-----------------------

Check the second line of the commit message is blank.


check-summary-conjunction
-------------------------

Check the summary does not contain conjugated sentences.

Searches for occurrences of 'and', 'nor', and 'or' and fails if found.


check-summary-imperative
------------------------

Check the summary starts with a verb.

Searches a wordlist comprised of > 6000 verbs. The check fails
if not found.

.. note::
    The wordlist is comprised of different lists but as terminology
    evolves, the list is incomplete. If you find anything missing,
    please amend `verbs-wordlist.txt <https://github.com/rlindsgaard/
    pre-commit-commit-msg-hooks/blob/master/pre_commit_commit_msg_hooks/
    verbs-wordlist.txt>`_
    and issue a Pull Request.


check-summary-capitalized
-------------------------

Check the summary starts with a capital letter.


check-summary-max-length
------------------------

Check the summary is not more than 54 characters.

.. note::
    https://commit.style says `Aim for about 50 characters, give
    or take`. 54 gives a little more lee-way.


check-summary-min-length
------------------------

Check the summary is at least 6 characters.


check-summary-punctuation
-------------------------

Check the summary does not end with punctuation.

Checks the last character against `string.punctuation <
https://docs.python.org/3/library/string.html#string.punctuation>`_
and fails on match.

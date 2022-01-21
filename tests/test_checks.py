import os.path

from pre_commit_commit_msg_hooks import (
    check_description_max_length,
    check_second_line_empty,
    check_summary_conjunction,
    check_summary_imperative,
    check_summary_capitalized,
    check_summary_max_length,
    check_summary_min_length,
    check_summary_punctuation,
)
import pytest
from unittest.mock import ANY

here = os.path.dirname(os.path.abspath(__file__))
examples = os.path.join(here, '..', 'examples')

@pytest.mark.parametrize('check', [
    check_description_max_length,
    check_second_line_empty,
    check_summary_conjunction,
    check_summary_imperative,
    check_summary_capitalized,
    check_summary_max_length,
    check_summary_min_length,
    check_summary_punctuation,
])
def test_good_commit_msg(check, mocker):
    patch_args(check.__name__, mocker, 'good_commit_msg')
    assert check.main() == 0


@pytest.mark.parametrize('check,commit_msg,expect_err', [
    (
        check_description_max_length,
        'description_too_long',
        [ANY, 'Line exceeds limit. 135 > 72'],
    ),
    (
        check_second_line_empty,
        'second_line_not_empty',
        [ANY, 'Second line not empty.'],
    ),
    (
        check_summary_conjunction,
        'conjunction_in_summary',
        [ANY, "Conjunction 'and' found in summary."],

    ),
    (
        check_summary_imperative,
        'summary_not_imperative',
        [ANY, 'Summary not imperative tense.'],
    ),
    (
        check_summary_capitalized,
        'summary_not_capitalized',
        [ANY, 'Summary not capitalized.'],
    ),
    (
        check_summary_max_length,
        'summary_too_long',
        [ANY, 'Summary too long. 62 > 54.'],
    ),
    (
        check_summary_min_length,
        'summary_too_short',
        [ANY, 'Summary too short. 5 < 6.'],
    ),
    (
        check_summary_punctuation,
        'punctuated_summary',
        [ANY, 'Summary is punctuated.'],
    ),
])
def test_checks_fail(
    check, commit_msg, expect_err, capsys, mocker
):
    patch_args(check.__name__, mocker, commit_msg)
    assert check.main() == 1
    captured = capsys.readouterr()
    assert captured.out.splitlines() == expect_err


def patch_args(test_name, mocker, commit_msg_filename):
    mocker.patch(
        'sys.argv',
        [
            test_name,
            os.path.join(examples, f'{commit_msg_filename}.txt')
        ]
    )

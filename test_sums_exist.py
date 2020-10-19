import pytest

from sums_exist import no_sums_exist


@pytest.mark.parametrize(
    "numbers_to_check, expected",
    [
        # Tests from specification
        ([4, 5, 15, 2, 8], True),
        ([8, 7, 5, 3], False),
        # Examples which satisfy the criteria
        ([3, 3, 3], True),
        ([200, 99, 99, 2], True),
        ([-6, -3, -7, 2, 11], True),
        ([-3, 9, 10] + [18] * 20, True),
        # Examples which do not satisfy the criteria
        ([4, 4, 8], False),
        ([68, 200, 99, 3, 65, 101], False),
        ([68, 200, 100, 100, 3, 9], False),
        ([-3, -6, -3, 2, 9], False),
        ([-3, 9, 10, 19, 30] + [18] * 20, False),
        # Boundary tests
        ([], True),
    ]
)
def test_sums_exist(numbers_to_check, expected):
    assert no_sums_exist(numbers_to_check) == expected

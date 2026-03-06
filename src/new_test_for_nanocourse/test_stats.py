import pytest
from new_package_for_nanocourse.stats import mean


def test_mean_happy_path(sample_values):
    assert mean(sample_values) == 2.0


def test_mean_empty_raises():
    with pytest.raises(ValueError):
        mean([])

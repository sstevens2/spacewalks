import pytest
from eva_data_analysis import (
    text_to_duration,
    calculate_crew_size
)

def test_text_to_duration_integer():
    input_value = "10:00"
    assert text_to_duration(input_value) == 10

def test_text_to_duration_float():
    assert text_to_duration("10:15") == 10.25

def test_text_to_duration_irrational():
    assert text_to_duration("10:20") == pytest.approx(10.33333)

@pytest.mark.parametrize("input_value, expected_result", [
    ("Valentina Tereshokova;", 1),
    ("Judith Resnik; Sally Ride;", 2)
])
def test_calculate_crew_size(input_value, expected_result):
    actual_result = calculate_crew_size(input_value)
    assert actual_result == expected_result

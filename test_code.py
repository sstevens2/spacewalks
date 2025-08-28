from eva_data_analysis import text_to_duration

def test_text_to_duration_integer():
    input_value = "10:00"
    assert text_to_duration(input_value) == 10

def test_text_to_duration_float():
    assert text_to_duration("10:15") == 10.25

def test_text_to_duration_irrational():
    assert abs(text_to_duration("10:20") - 10.33333) < 1e-5
    assert text_to_duration("10:20") == 10 + 1/3

test_text_to_duration_integer()
test_text_to_duration_float()
test_text_to_duration_irrational()

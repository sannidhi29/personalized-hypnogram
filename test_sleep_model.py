from sleep_model import (
    convert_to_minutes,
    calculate_sleep_duration,
    generate_sleep_cycles,
    build_hypnogram_data
)

def test_convert_to_minutes():
    assert convert_to_minutes("00:00") == 0
    assert convert_to_minutes("01:30") == 90
    assert convert_to_minutes("23:00") == 1380

def test_calculate_sleep_duration_same_day():
    assert calculate_sleep_duration("01:00", "05:00") == 240

def test_calculate_sleep_duration_overnight():
    assert calculate_sleep_duration("23:00", "07:00") == 480
    assert calculate_sleep_duration("23:00", "06:00") == 420

def test_generate_sleep_cycles_short_sleep():
    stages = generate_sleep_cycles(240)
    assert len(stages) == 16

def test_generate_sleep_cycles_normal_sleep():
    stages = generate_sleep_cycles(480)
    assert len(stages) == 32
    assert "REM" in stages
    assert "N3" in stages

def test_build_hypnogram_data():
    stages = ["N1", "N2", "N3", "REM"]
    times, values = build_hypnogram_data(stages)

    assert times == [0, 15, 30, 45]
    assert values == [3, 2, 1, 4]

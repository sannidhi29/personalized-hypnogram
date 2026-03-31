import matplotlib.pyplot as plt

def get_time_input():
    sleep_time = input("Enter sleep time (HH:MM): ")
    wake_time = input("Enter wake time (HH:MM): ")
    return sleep_time, wake_time

def convert_to_minutes(time_str):
    hours, minutes = map(int, time_str.split(":"))
    return hours * 60 + minutes

def calculate_sleep_duration(sleep_time, wake_time):
    sleep_min = convert_to_minutes(sleep_time)
    wake_min = convert_to_minutes(wake_time)

    if wake_min < sleep_min:
        wake_min += 24 * 60

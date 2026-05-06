import matplotlib.pyplot as plt

def get_time_input():
    sleep_time = input("Enter sleep time (HH:MM): ")
    wake_time = input("Enter wake time (HH:MM): ")
    return sleep_time, wake_time

def convert_to_minutes(time_str):
    hours, minutes = time_str.split(":")
    hours = int(hours)
    minutes = int(minutes)
    total_minutes = hours * 60 + minutes
    return total_minutes

def calculate_sleep_duration(sleep_time, wake_time):
    sleep_min = convert_to_minutes(sleep_time)
    wake_min = convert_to_minutes(wake_time)

    if wake_min < sleep_min:
        wake_min = wake_min + 24 * 60

    duration = wake_min - sleep_min
    return duration

def generate_sleep_cycles(total_minutes):
    stages = []
    minutes_used = 0
    cycle_number = 1

    while minutes_used < total_minutes:
        if cycle_number <= 2:
            cycle = ["N1", "N2", "N3", "N3", "N2", "REM"]
        elif cycle_number <= 4:
            cycle = ["N1", "N2", "N2", "N3", "N2", "REM"]
        else:
            cycle = ["N1", "N2", "N2", "REM", "REM", "REM"]

        for stage in cycle:
            if minutes_used >= total_minutes:
                break
                
            stages.append(stage)
            minutes_used = minutes_used + 15

        cycle_number = cycle_number + 1

    return stages

def build_hypnogram_data(stages):
    stage_values = {
        "REM": 4,
        "N1": 3,
        "N2": 2,
        "N3": 1
    }

    times = []
    values = []

    for i in range(len(stages)):
        times.append(i * 15)
        values.append(stage_values[stages[i]])

    return times, values

def plot_sleep_architecture(times, values):
    plt.plot(times, values, marker="o")

    plt.yticks([1, 2, 3, 4], ["N3", "N2", "N1", "REM"])
    plt.xlabel("Minutes After Falling Asleep")
    plt.ylabel("Sleep Stage")
    plt.title("Personalized Sleep Architecture Hypnogram")

    plt.gca().invert_yaxis()
    plt.grid(True)
    plt.show()

def main():
    sleep_time, wake_time = get_time_input()

    total_minutes = calculate_sleep_duration(sleep_time, wake_time)
    print("Total sleep duration:", total_minutes, "minutes")

    cycles = total_minutes / 90
    print("Approximate number of 90-minute cycles:", round(cycles, 1))

    stages = generate_sleep_cycles(total_minutes)
    print("Generated sleep stages:")
    print(stages)

    times, values = build_hypnogram_data(stages)
    plot_sleep_architecture(times, values)

main()

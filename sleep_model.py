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

    plt.yticks(
        [1, 2, 3, 4],
        ["N3: Deep Sleep", "N2: Light Sleep", "N1: Lightest Sleep", "REM: Dream Sleep"]
    )

    plt.xlabel("Minutes After Falling Asleep")
    plt.ylabel("Predicted Sleep Stage")
    plt.title("Personalized Sleep Architecture Hypnogram")

    plt.gca().invert_yaxis()
    plt.grid(True)
    plt.tight_layout()
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

    evaluate_sleep_quality(total_minutes, stages)

    times, values = build_hypnogram_data(stages)
    explain_hypnogram()
    plot_sleep_architecture(times, values)

def explain_hypnogram():
    
    print("\nHow to read the hypnogram:")
    print("The x-axis shows minutes after falling asleep.")
    print("The y-axis shows the predicted sleep stage.")
    print("N3 is deep sleep, which is more common earlier in the night.")
    print("REM is dream-associated sleep, which is more common later in the night.")
    print("Each point on the graph represents a 15-minute block of sleep.\n")

def evaluate_sleep_quality(total_minutes, stages):
    """
    Give a simple educational sleep quality summary.

    This is not a medical diagnosis. It uses sleep duration and the
    simulated stage pattern to give the user an easy-to-understand summary.
    """
    total_hours = total_minutes / 60

    rem_count = stages.count("REM")
    n3_count = stages.count("N3")

    rem_minutes = rem_count * 15
    n3_minutes = n3_count * 15

    print("\nSleep Quality Summary:")

    if total_hours < 6:
        print("Your sleep duration is short.")
        print("This may not give your body enough time for full sleep cycles.")
    elif total_hours < 7:
        print("Your sleep duration is slightly below the common adult recommendation.")
        print("You may get some full cycles, but more sleep may be helpful.")
    elif total_hours <= 9:
        print("Your sleep duration is in a healthy general range for many adults.")
        print("Your simulated pattern includes time for both deep sleep and REM sleep.")
    else:
        print("Your sleep duration is longer than average for many adults.")
        print("Long sleep is not always bad, but consistently needing very long sleep may be worth paying attention to.")

    print("\nEstimated stage totals:")
    print("REM sleep:", rem_minutes, "minutes")
    print("Deep sleep (N3):", n3_minutes, "minutes")

    if n3_minutes == 0:
        print("Your model did not include much deep sleep, likely because the sleep duration was very short.")
    elif rem_minutes == 0:
        print("Your model did not include much REM sleep, likely because the sleep duration was very short.")
    else:
        print("This model includes both deep sleep and REM sleep, which are important parts of a complete sleep cycle.")

    print("\nNote: This is a simplified educational model, not a medical sleep assessment.")

if __name__ == "__main__":
    main()

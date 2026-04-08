# personalized-sleep-cycle
This project generates a simple personalized sleep architecture (hypnogram) graph based on a user’s sleep and wake times. It simulates typical ~90-minute sleep cycles and models changes in sleep stages (N1, N2, N3, REM) across the night. Users input their sleep schedule, and the program calculates predicted sequences and durations of sleep stages and visualizes the results as a graph. The goal of the project is to demonstrate how sleep patterns can be modeled computationally, using 6 Python functions, so that users can have a visual representation of their circadian rhythm. 

a. get_time_input(): Promotes user to enter their sleep and wake times in HH:MM format, collecting input needed to generate personalized sleep cycle.

b. convert_to_minutes(time_str): Converts a time string to total number of minutes after midnight, standardizing time values so they can be used for calculations.

c. calculate_sleep_duration(sleep_time, wake_time): Calculates total sleep duration in minutes based on user input. Correctly handles cases where sleep period crosses midnight.

d. generate_sleep_cycles(total_minutes): Generates sequence of sleep stages based on ~90-minute cycles. Models realistic patterns where deep sleep is more common early and REM increases later.

e. build_hypnogram_data(stages): Converts sleep stage labels into numerical values for plotting, allowing stages to be visualized on a graph.

f. plot_sleep_architecture(times, stages): Creates hypnogram showing how sleep stages change over time. Displays time on the x-axis and sleep stages on the y-axis.


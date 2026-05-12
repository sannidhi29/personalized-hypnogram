# personalized-sleep-cycle

This project generates a simple personalized sleep architecture (hypnogram) graph based on a user’s sleep and wake times. It simulates typical ~90-minute sleep cycles and models changes in sleep stages (N1, N2, N3, REM) across the night. Users input their sleep schedule, and the program calculates predicted sequences and durations of sleep stages and visualizes the results as a graph. 

## What is sleep architecture?

Sleep architecture refers to the pattern of sleep stages that occur across a night of sleep. A typical night includes repeated sleep cycles that last about 90 minutes. Earlier in the night, deep sleep stages such as N3 are more common. Later in the night, REM sleep becomes more common.

This project uses a simplified model of that pattern:

- Early cycles include more N3 deep sleep.
- Middle cycles include more N2 sleep and some N3 sleep.
- Later cycles include more REM sleep.
- Each simulated sleep stage block represents 15 minutes.

This model is not meant to be a clinical sleep prediction tool. Instead, it is a simple computational demonstration of how sleep stages can be represented and visualized using Python.

## Project features

The goal of the project is to demonstrate how sleep patterns can be modeled computationally, using 6 Python functions, so that users can have a visual representation of their circadian rhythm. 

a. get_time_input(): Promotes user to enter their sleep and wake times in HH:MM format, collecting input needed to generate personalized sleep cycle.

b. convert_to_minutes(time_str): Converts a time string to total number of minutes after midnight, standardizing time values so they can be used for calculations.

c. calculate_sleep_duration(sleep_time, wake_time): Calculates total sleep duration in minutes based on user input. Correctly handles cases where sleep period crosses midnight.

d. generate_sleep_cycles(total_minutes): Generates sequence of sleep stages based on ~90-minute cycles. Models realistic patterns where deep sleep is more common early and REM increases later.

e. build_hypnogram_data(stages): Converts sleep stage labels into numerical values for plotting, allowing stages to be visualized on a graph.

f. plot_sleep_architecture(times, stages): Creates hypnogram showing how sleep stages change over time. Displays time on the x-axis and sleep stages on the y-axis.

## Installation

This project uses two Python packages:

- matplotlib
- pytest

These packages are listed in the `requirements.txt` file.

To install them:

1. Download or clone this project from GitHub.
2. Open the project folder on your computer.
3. Open the terminal in that folder.
4. Type this command: pip install -r requirements.txt


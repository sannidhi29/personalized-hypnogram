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

## Installation & Running Instructions

This project uses two Python packages:

- matplotlib to create the sleep architecture graph
- pytest to run the tests

These packages are listed in the `requirements.txt` file.

To install them:

1. Download or clone this project from GitHub.
2. Open the project folder on your computer. You should see these files:
     - README.md
     - requirements.txt
     - sleep_model.py
     - test_sleep_model.py
4. Open the terminal in the same folder as sleep_model.py
5. Type this command to install the packages: pip install -r requirements.txt

To run the project:

1. Type in terminal: python sleep_model.py
2. The program will ask you to enter your sleep time and wake time.
     - Use 24-hour time in HH:MM format

## How to interpret the graph

The graph is called a hypnogram. It shows the predicted sleep stage at different points during the night.

- The x-axis shows minutes after falling asleep.
- The y-axis shows the predicted sleep stage.
- N1 is the lightest sleep stage.
- N2 is light sleep.
- N3 is deep sleep.
- REM is dream-associated sleep.

In this simplified model, deep sleep is more common earlier in the night, while REM sleep becomes more common later in the night. Each point on the graph represents a 15-minute block of sleep.

## Limitations

This project is a simplified educational model. Real sleep architecture is influenced by many factors, including age, health, circadian rhythm, sleep quality, stress, medication, and sleep disorders. This program does not use real sleep data and should not be used for medical or clinical purposes.

## References

Carskadon, M. A., & Dement, W. C. (2011). Normal human sleep: An overview. In Principles and Practice of Sleep Medicine.

National Institute of Neurological Disorders and Stroke. (n.d.). Brain basics: Understanding sleep. National Institutes of Health. https://www.ninds.nih.gov/health-information/public-education/brain-basics/brain-basics-understanding-sleep




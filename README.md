# personalized-sleep-cycle
This project generates a simple personalized sleep architecture (hypnogram) graph based on a user’s sleep and wake times. It simulates typical ~90-minute sleep cycles and models changes in sleep stages (N1, N2, N3, REM) across the night. Users input their sleep schedule, and the program calculates predicted sequences and durations of sleep stages and visualizes the results as a graph. The goal of the project is to demonstrate how sleep patterns can be modeled computationally, using 3 Python functions, so that users can have a visual representation of their circadian rhythm. 

a. process_sleep_schedule(): 
This function will take the user's sleep time and wake time as input and calculate the total sleep duration in minutes. If the wake time is earlier    than the sleep time (for example, sleeping at 23:00 and waking at 07:00), the function will correctly treat the sleep period as crossing midnight and compute the duration accordingly.

b. generate_sleep_cycles(): 
This function will simulate sleep cycles across the night and assign durations for each sleep stage (N1, N2, N3, REM) based on typical ~90-minute cycles. It will adjust the stages so that deeper sleep (N3) occurs more in earlier cycles and REM sleep becomes longer in later cycles.

c. plot_sleep_architecture(): 
This function will create a hypnogram graph showing how sleep stages change over time during the night and display the visualization. The graph will plot time on the x-axis and sleep stages on the y-axis so the user can clearly see the structure of their simulated sleep cycles.


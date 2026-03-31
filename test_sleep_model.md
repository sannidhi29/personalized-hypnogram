To test the program:

1. Run sleep_model.py
2. Enter:
   Sleep time: 23:00
   Wake time: 07:00

Expected output:

- Program calculates 480 minutes of sleep
- Generates ~5 sleep cycles
- Displays a graph with labeled sleep stages

Additional tests:

Short sleep duration:
Input: 01:00 --> 05:00
Expected: Program calculates a short sleep period (~4 hours) and generates fewer sleep cycles.
  
Long sleep duration:
Input: 22:00 --> 10:00
Expected: Program calculates a long sleep period (~12 hours) and generates more sleep cycles.
  
Crossing midnight (exception):
Input: 23:00 --> 06:00
Expected: Program correctly handles overnight sleep by accounting for the next day and returns ~7 hours of sleep instead of -17.

# Arduino Distance-Time Graphing and Statistical Analysis

This project involves creating a distance-time graph using an Arduino Uno and an ultrasonic sensor. Additionally, it includes statistical analysis such as calculating the mean, standard deviation, maximum, and minimum values of the collected data.

## Usage

1. Upload the Arduino sketch provided (`setup.ino`) to your Arduino Uno.
2. Run the Python script (`data_analysis.py`) on your computer to collect data from the Arduino Uno via serial communication and perform statistical analysis.
   Launch the Streamlit app (`streamlit_app.py`) to visualize the distance-time graph and view the statistical analysis results.

## Files

- `distance_time_graph.ino`: Arduino sketch for collecting distance data and sending it over serial.
- `data_analysis.py`: Python script for receiving data from the Arduino Uno, performing statistical analysis, and saving the results.
- `streamlit_app.py`: Streamlit web application for visualizing the distance-time graph and displaying statistical analysis results.

## Hardware Setup

Connect the ultrasonic sensor to the Arduino Uno as follows:

- VCC pin of the sensor to 5V pin of the Arduino Uno
- TRIG pin of the sensor to digital pin 9 of the Arduino Uno
- ECHO pin of the sensor to digital pin 10 of the Arduino Uno
- GND pin of the sensor to GND pin of the Arduino Uno

## Required Libraries

Before running the code, make sure to install the necessary Python libraries:

```bash
pip install pandas
pip install streamlit
pip install pyserial







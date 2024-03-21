import serial
import time
import streamlit as st
import pandas as pd


def clear_data():
    distance_data.clear()

try:
    ser = serial.Serial('COM5', 9600)
except serial.SerialException as e:
    st.error(f"Failed to open serial port: {e}")
    st.stop()

DATA = st.empty()
try:
    distance_data = [] 
    line_chart_placeholder = st.empty() 
    df_placeholder = st.empty()  

    while True:
        if ser.in_waiting > 0:
            distance = ser.readline().decode('utf-8').rstrip()
            distance_data.append(float(distance))
            

           
            DATA.text("Distance: {} cm".format(distance))  
            line_chart_placeholder.line_chart(distance_data)
            
            df = pd.DataFrame({'Distance (cm)': distance_data})
            df_placeholder.dataframe(df.describe())

                
                
            

except KeyboardInterrupt:
    ser.close()

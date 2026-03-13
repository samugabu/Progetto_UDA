import serial
import csv
import time
from datetime import datetime
import dearpygui.dearpygui as dpg

porta = 'COM4'
bound_rate = 9600
file = "monitoraggio_temperature.csv"

with open(file, "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "Temperature"])

ser = serial.Serial(porta, bound_rate, timeout=0.1)

data_x = [] 
data_y = []
start_time = time.time()

def update_data():
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').strip()
        
        if not line:
            return

        timestamp = datetime.now().strftime("%H:%M:%S")
        
        if "Temperature:" in line:
            val_str = line.replace("Temperature:", "").strip()
            temp = float(val_str)
            with open(file, mode='a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([timestamp, temp])
            print(f"{timestamp} -> {temp} °C")
            
            elapsed = time.time() - start_time
            data_x.append(elapsed)
            data_y.append(temp)
            
            if len(data_x) > 50:
                data_x.pop(0)
                data_y.pop(0)
            
            dpg.set_value("series_tag", [list(data_x), list(data_y)])
            dpg.set_value("temp_text", f"Temp: {temp} °C")
            dpg.fit_axis_data("x_axis")
            dpg.fit_axis_data("y_axis")
           
        elif "," in line:
            parti = line.split(",")
            with open(file, mode='a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([timestamp] + parti)
            print(f"{timestamp} -> {line}")

dpg.create_context()
dpg.create_viewport(title='Monitoraggio', width=850, height=850)

with dpg.window(label="Dati Seriale", width=800, height=800):
    dpg.add_text("In attesa di dati...", tag="temp_text")
    with dpg.plot(label="Grafico Temperatura", height=300, width=-1):
        dpg.add_plot_axis(dpg.mvXAxis, label="Secondi", tag="x_axis")
        dpg.add_plot_axis(dpg.mvYAxis, label="°C", tag="y_axis")
        dpg.add_line_series(data_x, data_y, tag="series_tag", parent="y_axis")

dpg.setup_dearpygui()
dpg.show_viewport()

while dpg.is_dearpygui_running():
    update_data()
    dpg.render_dearpygui_frame()

dpg.destroy_context()
ser.close()

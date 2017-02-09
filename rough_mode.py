# rough_mode.py
# Mónica Milán (@mncmilan)
# mncmilan@gmail.com
# http://steelhummingbird.blogspot.com.es/

# This code obtains acceleration data from eZ430-Chronos watch by Texas Instruments, then it eliminates the noise in X
# and Y axis and it only considers the movement in the axis where there's an acceleration change bigger than a defined
# threshold, setting the other one constant at the initial value. Thus only rough or high range hand movements are
# detected. Finally it plots the resulting values.

import time
import matplotlib.pyplot as plt
from libs import communications, filterings, graphics, modes, datalog

communication = communications.CommunicationManager()
filtering = filterings.FilteringManager()
graphic = graphics.GraphicsManager()
report = datalog.DatalogManager()
mode = modes.ModesManager()


class RoughMovement():
    communication.open_serial_port()

    watch_samples_counter = -1

    x_axis_acceleration = []
    y_axis_acceleration = []

    x_axis_limited_acceleration = [0]
    y_axis_limited_acceleration = [0]

    x_limited_ = 0
    y_limited_ = 0

    graphic.set_plot_parameters()

    while True:
        bytesToRead = communication.send_data_request()
        inbyte = communication.read_data(bytesToRead)

        if (bytesToRead >= 7 and inbyte[3] == 1) or (bytesToRead == 14 and inbyte[10] == 1):
            watch_samples_counter += 1

            x_axis_acceleration.append(inbyte[bytesToRead-3])
            filtering.filter_acceleration(x_axis_acceleration, watch_samples_counter)
            y_axis_acceleration.append(inbyte[bytesToRead-2])
            filtering.filter_acceleration(y_axis_acceleration, watch_samples_counter)

            x_limited, y_limited = mode.rough_movement_limitation(x_axis_acceleration, y_axis_acceleration, watch_samples_counter)
            x_axis_limited_acceleration.append(x_limited)
            y_axis_limited_acceleration.append(y_limited_)

        plt.pause(0.01)  # 10ms

        if x_axis_limited_acceleration[watch_samples_counter]==0 or y_axis_limited_acceleration[watch_samples_counter]==0:
            time.sleep(0.5)

    communication.close_serial_port()

# single_axis_mode.py
# Mónica Milán (@mncmilan)
# mncmilan@gmail.com
# http://steelhummingbird.blogspot.com.es/

# This code obtains acceleration data from eZ430-Chronos watch by Texas Instruments, then it eliminates the noise in X
# and Y axis and it only considers the movement in the axis where there's a bigger acceleration change, setting the
# other one constant at the initial value. Finally it plots the resulting values.

import matplotlib.pyplot as plt
from libs import communications, filterings, graphics, modes, datalog

communication = communications.CommunicationManager()
filtering = filterings.FilteringManager()
graphic = graphics.GraphicsManager()
report = datalog.DatalogManager()
mode = modes.ModesManager()


class SingleAxisMovement():
    communication.open_serial_port()

    watch_samples_counter = -1

    x_axis_acceleration = []
    y_axis_acceleration = []

    x_axis_limited_acceleration = 0
    y_axis_limited_acceleration = 0

    graphic.set_plot_parameters()

    while True:
        bytes_to_read = communication.send_data_request()
        inbyte = communication.read_data(bytes_to_read)

        if (bytes_to_read >= 7 and inbyte[3] == 1) or (bytes_to_read == 14 and inbyte[10] == 1):
            watch_samples_counter += 1

            x_axis_acceleration.append(inbyte[bytes_to_read-3])
            filtering.filter_acceleration(x_axis_acceleration, watch_samples_counter)
            y_axis_acceleration.append(inbyte[bytes_to_read-2])
            filtering.filter_acceleration(y_axis_acceleration, watch_samples_counter)

            x_axis_limited_acceleration, y_axis_limited_acceleration = mode.single_axis_limitation(x_axis_acceleration, y_axis_acceleration, watch_samples_counter)
            graphic.plot_data(x_axis_limited_acceleration, y_axis_limited_acceleration)

        plt.pause(0.01)  # 10ms

    communication.close_serial_port()

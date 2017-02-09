# graphics.py
# Mónica Milán (@mncmilan)
# mncmilan@gmail.com
# http://steelhummingbird.blogspot.com.es/

# Library that contains all necessary methods in order to plot acceleration data obtained from eZ430-Chronos.

import matplotlib.pyplot as plt


class GraphicsManager():

    def plot_data(self, x_axis_acceleration, y_axis_acceleration):
        dot.set_xdata(x_axis_acceleration)
        dot.set_ydata(y_axis_acceleration)

    def plot_close(self):
        plt.close()

    def set_plot_parameters(self):
        global fig
        global ax
        fig, ax = plt.subplots()
        ax.set_xlim(-128,128)
        ax.set_ylim(-128,128)
        global dot
        dot, = ax.plot(0,0,'ro',markersize=20, color='c')

    def change_color(self):
        ax.set_axis_bgcolor('paleturquoise')

    def restore_color(self):
        ax.set_axis_bgcolor('white')


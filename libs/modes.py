# modes.py
# Mónica Milán (@mncmilan)
# mncmilan@gmail.com
# http://steelhummingbird.blogspot.com.es/

# Library that contains all necessary methods in order to filter acceleration data obtained from eZ430-Chronos.

from libs import graphics

graph = graphics.GraphicsManager()


class ModesManager():

    def rough_movement_limitation(self, x_acc, y_acc, samples_counter):

        xnew, ynew = self.single_axis_limitation(x_acc, y_acc, samples_counter)

        if xnew < -30:
            xnew = -127
        elif xnew > 30:
            xnew = 127
        else:
            xnew = 0

        if ynew < -30:
            ynew = -127
        elif ynew > 30:
            ynew = 127
        else:
            ynew = 0

        graph.plot_data(xnew, ynew)

        return xnew, ynew,

    def single_axis_limitation(self, x_axis_acceleration, y_axis_acceleration, watch_samples_counter):
        if abs(x_axis_acceleration[watch_samples_counter])>abs(y_axis_acceleration[watch_samples_counter]) \
                and abs(x_axis_acceleration[watch_samples_counter-1])>abs(y_axis_acceleration[watch_samples_counter-1]):
            ynew = 0
            return x_axis_acceleration[watch_samples_counter], ynew
        else:
            xnew = 0
            return xnew, y_axis_acceleration[watch_samples_counter]


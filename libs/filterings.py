# filterings.py
# Mónica Milán (@mncmilan)
# mncmilan@gmail.com
# http://steelhummingbird.blogspot.com.es/

# Library that contains all necessary methods in order to filter acceleration data obtained from eZ430-Chronos.

class FilteringManager:

    def data_availability(self,bytes_to_read,inbyte):
        enter = 0
        if bytes_to_read == 7:
            if inbyte[4] == 0 and inbyte[5] and inbyte[6] == 0:
                enter = False
            else:
                enter = True
        elif bytes_to_read == 14:
            if inbyte[11] == 0 and inbyte[12] == 0 and inbyte[13] == 0:
                enter = False
            else:
                enter = True
        return enter

    def filter_acceleration(self, x_axis_acceleration, x_samples_counter):
        if x_axis_acceleration[x_samples_counter] <= 6:  # threshold
            x_axis_acceleration[x_samples_counter] = 0
        elif x_axis_acceleration[x_samples_counter]-x_axis_acceleration[x_samples_counter-1] <= 5:
            x_axis_acceleration[x_samples_counter] = x_axis_acceleration[x_samples_counter]
        if x_axis_acceleration[x_samples_counter] > 127:  # sign in order to direction
            x_axis_acceleration[x_samples_counter] = (255 - x_axis_acceleration[x_samples_counter] + 1) * -1

    def handside_mode(self, x_axis_acceleration, y_axis_acceleration, handside):
        if handside is 'left':
            x_axis_acceleration = x_axis_acceleration * -1
            y_axis_acceleration = y_axis_acceleration * -1
        return x_axis_acceleration, y_axis_acceleration

    def handside_mode_3_axis(self, x_axis_acceleration, y_axis_acceleration, z_axis_acceleration, handside):
        if handside is 'right':
            z_axis_acceleration = z_axis_acceleration * -1
        if handside is 'left':
            y_axis_acceleration = y_axis_acceleration * -1
        return x_axis_acceleration, y_axis_acceleration, z_axis_acceleration
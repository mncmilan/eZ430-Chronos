# communications.py
# Mónica Milán (@mncmilan)
# mncmilan@gmail.com
# http://steelhummingbird.blogspot.com.es/

# Library that contains all necessary methods in order to enable communications between PC and eZ430-Chronos.

import serial

s = serial.Serial('COM4', baudrate=115200,timeout=None)  # open serial port


class CommunicationManager():

    def open_serial_port(self):
        s.write(bytearray([255, 7, 3]))  # starting communications with serial port

    def send_data_request(self):
        s.write(bytearray([255, 8, 7, 0, 0, 0, 0]))  # acceleration data request
        bytesToRead = s.inWaiting()
        return bytesToRead

    def read_from_labVIEW_request(self):
        bytes_to_read = s.inWaiting()
        inbyte = s.read(bytes_to_read)
        return bytes_to_read, inbyte

    def read_data(self, bytes_to_read):
        inbyte = s.read(bytes_to_read)
        return inbyte

    def close_serial_port(self):
        s.write(bytearray([255, 9, 3]))  # stop transmitting
        s.close()

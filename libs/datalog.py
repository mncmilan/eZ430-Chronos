# datalog.py
# Mónica Milán (@mncmilan)
# mncmilan@gmail.com
# http://steelhummingbird.blogspot.com.es/

# Library that contains all necessary methods in order to store data in a text file.

class DatalogManager():

    def record_data(self, filename, parameter, x_axis_acceleration, y_axis_acceleration, z_axis_acceleration):
        archi = open('data/' + filename, 'a')
        data= str(parameter) + '       ' + str(x_axis_acceleration) + '      ' + str(y_axis_acceleration)+ '      ' + str(z_axis_acceleration)
        archi.write(data)
        archi.write('\n')
        archi.close()

    def create_file(self,filename):
        archi = open('data/'+filename, 'w')
        archi.close()

    def record_for_training(self,x_axis_acceleration, y_axis_acceleration, z_axis_acceleration):
        archi = open('data/pos_centered_clap.csv', 'a')
        data =  str(x_axis_acceleration) + ';' + str(y_axis_acceleration) + ';' + str(z_axis_acceleration)+';'
        archi.write(data)
        archi.close()

    def next_line(self):
        archi = open('data/pos_centered_clap.csv', 'a')
        archi.write('\n')
        archi.close()

    def record_probabilities(self, prediction, probability,position):
        archi = open('data/probabilities.txt', 'a')
        data = str(prediction) + '         ' + str(probability[0][0])+ '         ' + str(probability[0][-1])+ '         ' + str(position)
        archi.write(data)
        archi.write('\n')
        archi.close()
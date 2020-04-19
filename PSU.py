import serial
import time

class PSU():

    ser = None

    def __init__(self, com):

        self.com = com

        self.ser = serial.Serial()

        self.ser.port = self.com
        self.ser.baudrate = 9600
        self.ser.parity = serial.PARITY_NONE
        self.ser.bytesize = serial.EIGHTBITS
        self.ser.stopbits = serial.STOPBITS_ONE
        self.ser.timeout = 1

    def identyfication(self):
        try:
            self.ser.open()
            self.ser.write('*IDN?'.encode())
            time.sleep(0.1)
            received = self.ser.read(100)
            return received
        except serial.SerialException as se:
            print(str(se))
            received = None
            return received

if __name__ == '__main__':
    psu = PSU('COM9')
    identyficator = psu.identyfication()
    print(identyficator)


# ser.write('VSET1:3.3'.encode())
# time.sleep(0.1)
# received = ser.read(100)
#
# ser.write('OUT0'.encode())
# time.sleep(0.1)
# received = ser.read(100)
from PSU_Control.PSU import PSU
import time

if __name__ == '__main__':
    psu = PSU('COM9')
    help(PSU)
    identyficator = psu.identyfication()
    print(identyficator)

    try:
        psu.setVoltage(3.3)
    except TypeError as tp:
        print(str(tp))
    except ValueError as ve:
        print(str(ve))

    try:
        psu.setCurrent(1.1)
    except TypeError as tp:
        print(str(tp))
    except ValueError as ve:
        print(str(ve))

    time.sleep(0.5)

    print(psu.getSet_Voltage())
    print(psu.getSet_Current())

    print(f'Supplied voltage is equal to {psu.getActual_Voltage()}')
    print(f'Supplied current is equal to {psu.getActual_Current()}')

    psu.output_on()
    time.sleep(2)
    psu.output_off()
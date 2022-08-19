import pyfirmata

comport = 'COM5'

board = pyfirmata.Arduino(comport)

enA = board.get_pin('d:6:o')
in1 = board.get_pin('d:7:o') 
in2 = board.get_pin('d:8:o')
in3 = board.get_pin('d:9:o')
in4 = board.get_pin('d:10:o')
enB = board.get_pin('d:11:o')

def led(total):
    if total == 0:
        enA.write(0)
        in1.write(0)
        in2.write(0)
        in3.write(0)
        in4.write(0)
        enB.write(0)


    elif total == 1:
        enA.write(1)
        in1.write(0)
        in2.write(1)
        in3.write(0)
        in4.write(1)
        enB.write(1)

    elif total == 2:
        enA.write(1)
        in1.write(1)
        in2.write(0)
        in3.write(1)
        in4.write(0)
        enB.write(1)

    elif total == 3:
        enA.write(0)
        in1.write(0)
        in2.write(0)
        in3.write(0)
        in4.write(1)
        enB.write(1)

    elif total == 4:
        enA.write(1)
        in1.write(0)
        in2.write(1)
        in3.write(0)
        in4.write(0)
        enB.write(0)

    else:
        enA.write(0)
        in1.write(0)
        in2.write(0)
        in3.write(0)
        in4.write(0)
        enB.write(0)

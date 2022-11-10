import pyfirmata

comport = 'COM5'

board = pyfirmata.Arduino(comport)

enA = board.get_pin('d:9:o')
in1 = board.get_pin('d:8:o') 
in2 = board.get_pin('d:7:o')
in3 = board.get_pin('d:11:o')
in4 = board.get_pin('d:12:o')
enB = board.get_pin('d:10:o')

def direction(total):

    if total >= 1 and total < 37:  #extreme left
        enA.write(1)
        in1.write(1)
        in2.write(0)
        in3.write(0)
        in4.write(1)
        enB.write(1)


    elif total >= 37 and total < 72:  #left
        enA.write(0)
        in1.write(0)
        in2.write(0)
        in3.write(0)
        in4.write(1)
        enB.write(1)

    elif total >= 72 and total <= 90:  #forward
        enA.write(1)
        in1.write(0)
        in2.write(1)
        in3.write(0)
        in4.write(1)
        enB.write(1)

    elif total >= -89 and total < -72:  #forward
        enA.write(1)
        in1.write(0)
        in2.write(1)
        in3.write(0)
        in4.write(1)
        enB.write(1)

    elif total >=  -72 and total < -37:  #right
        enA.write(1)
        in1.write(0)
        in2.write(1)
        in3.write(0)
        in4.write(0)
        enB.write(0)

    elif total >=  -37 and total < -1:  #extreme right
        enA.write(1)
        in1.write(0)
        in2.write(1)
        in3.write(1)
        in4.write(0)
        enB.write(1)

    else:  #stop
        enA.write(0)
        in1.write(0)
        in2.write(0)
        in3.write(0)
        in4.write(0)
        enB.write(0)

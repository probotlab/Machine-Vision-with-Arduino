import pygame
import pyfirmata

comport = 'COM5'

board = pyfirmata.Arduino(comport)

enA1 = board.get_pin('d:6:o')
in11 = board.get_pin('d:4:o')
in12 = board.get_pin('d:3:o')
in13 = board.get_pin('d:2:o')
in14 = board.get_pin('d:13:o')
enB1 = board.get_pin('d:5:o')
enA2 = board.get_pin('d:10:o')
in21 = board.get_pin('d:12:o')
in22 = board.get_pin('d:11:o')
in23 = board.get_pin('d:8:o')
in24 = board.get_pin('d:7:o')
enB2 = board.get_pin('d:9:o')

def init():
    pygame.init()
    win = pygame.display.set_mode((150, 150))

def getKey(keyName):
    ans = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True
    pygame.display.update()
    return ans

def main():
    if getKey("w"):
        enA1.write(1)
        in11.write(1)
        in12.write(0)
        in13.write(0)
        in14.write(1)
        enB1.write(1)
        enA2.write(1)
        in21.write(1)
        in22.write(0)
        in23.write(1)
        in24.write(0)
        enB2.write(1)

    elif getKey("s"):
        enA1.write(1)
        in11.write(0)
        in12.write(1)
        in13.write(1)
        in14.write(0)
        enB1.write(1)
        enA2.write(1)
        in21.write(0)
        in22.write(1)
        in23.write(0)
        in24.write(1)
        enB2.write(1)

    elif getKey("a"):
        enA1.write(1)
        in11.write(1)
        in12.write(0)
        in13.write(1)
        in14.write(0)
        enB1.write(1)
        enA2.write(1)
        in21.write(0)
        in22.write(1)
        in23.write(1)
        in24.write(0)
        enB2.write(1)

    elif getKey("d"):
        enA1.write(1)
        in11.write(0)
        in12.write(1)
        in13.write(0)
        in14.write(1)
        enB1.write(1)
        enA2.write(1)
        in21.write(1)
        in22.write(0)
        in23.write(0)
        in24.write(1)
        enB2.write(1)

    else:
        enA1.write(0)
        in11.write(0)
        in12.write(0)
        in13.write(0)
        in14.write(0)
        enB1.write(0)
        enA2.write(0)
        in21.write(0)
        in22.write(0)
        in23.write(0)
        in24.write(0)
        enB2.write(0)

if __name__ == '__main__':
    init()
    while True:
        main()

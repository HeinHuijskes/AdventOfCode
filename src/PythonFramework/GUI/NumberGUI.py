import sys

sys.path.append("../AdventOfCode")
sys.path.append("../AdventOfCode/src")
sys.path.append("../AdventOfCode/src/GUI_Framework")
sys.path.append("../AdventOfCode/src/GUI_Framework/Framework")
sys.path.append("../AdventOfCode/src/GUI_Framework/Framework/src")

from time import sleep
from threading import Thread
import pygame

from src.GUI_Framework.Framework.src.algorithm import Algorithm
from src.GUI_Framework.Framework.src.controller import Controller
from src.GUI_Framework.Framework.src.controller import Drawable
from src.GUI_Framework.Framework.src.parameters import Parameters

def getNumberGUI():
    controller = Controller(NumberGUIParameters(), buttons=[])
    return NumberGUI(controller)

class NumberGUIParameters(Parameters):
    def __init__(self) -> None:
        super().__init__(title="Number GUI")

class NumberGUI(Algorithm):

    numbers: list[int] = []
    number: Drawable
    run = True
    delay = False

    def drawNumber(self):
        self.controller.ui.clearOutputScreen()
        if len(self.numbers) > 0:
            self.number.value = self.numbers.pop(0)
        if self.number.value != None:
            self.number.draw(self.controller.ui)

    def __init__(self, controller: Controller) -> None:
        super().__init__(controller)
        width = self.controller.ui.settings.width // 2
        height = self.controller.ui.settings.height // 2
        self.number = Drawable((width, height), size=(1,1), drawType='text')
        self.number.fontSize = 100


    def update(self, value):
        self.numbers.append(str(value))

    def loop_updater():
        pass

    def runGUI(self):
        self.controller.ui.drawTopText(f'Number GUI', 1)
        self.controller.setDrawables([self.number])

        self.controller.redrawDrawables()
        while self.run or len(self.numbers) > 0:
            self.drawNumber()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.controller.checkMouseEvent(pygame.mouse.get_pos())
            if self.controller.timer.runTimer:
                self.controller.showTimer()
            pygame.display.flip()
            self.controller.clock.tick(60)
        print('quitting')
        # pygame.display.quit()
        # pygame.quit()
        sleep(.1)

        # while self.run:
        #     print(self.number.value, len(self.numbers))
        #     if self.delay:
        #         sleep(0.1)
        #     self.drawNumber()


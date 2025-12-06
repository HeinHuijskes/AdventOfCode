from src.PythonFramework.GUI.NumberGUI import getNumberGUI
from src.GUI_Framework.Framework.src.controller import Controller
from enum import Enum

class GUI_GETTER:
    class GUI_OPTIONS(Enum):
        NUMBER = 'Number'

    def getGui(self, type):
        if type not in [x.value for x in self.GUI_OPTIONS]:
            raise(ValueError)
        if type == self.GUI_OPTIONS.NUMBER.value:
            print('yes')
            return getNumberGUI()

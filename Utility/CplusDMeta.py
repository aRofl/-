from PyQt5.QtWidgets import QWidget
from abc import ABCMeta

QtWrapperType = type(QWidget)

class CplusDMeta(QtWrapperType, ABCMeta):
    pass
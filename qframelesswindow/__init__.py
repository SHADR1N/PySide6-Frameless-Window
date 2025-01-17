"""
PySide6-Frameless-Window
======================
A cross-platform frameless window based on PySide6, support Win32, Linux and macOS.

Documentation is available in the docstrings and
online at https://pyqt-frameless-window.readthedocs.io.

Examples are available at https://github.com/zhiyiYo/PyQt-Frameless-Window/tree/master/examples.

:copyright: (c) 2021 by zhiyiYo.
:license: GPLv3, see LICENSE for more details.
"""

__version__ = "0.0.1"

import sys

from PySide6.QtWidgets import QDialog, QMainWindow

from .titlebar import TitleBar, TitleBarButton, SvgTitleBarButton, StandardTitleBar, TitleBarBase

if sys.platform == "win32":
    from .windows import AcrylicWindow
    from .windows import WindowsFramelessWindow as FramelessWindow
    from .windows import WindowsWindowEffect as WindowEffect
elif sys.platform == "darwin":
    from .mac import AcrylicWindow
    from .mac import MacFramelessWindow as FramelessWindow
    from .mac import MacWindowEffect as WindowEffect
else:
    from .linux import LinuxFramelessWindow as FramelessWindow
    from .linux import LinuxWindowEffect as WindowEffect

    AcrylicWindow = FramelessWindow


class FramelessDialog(QDialog, FramelessWindow):
    """ Frameless dialog """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.titleBar.minBtn.hide()
        self.titleBar.maxBtn.hide()
        self.titleBar.setDoubleClickEnabled(False)
        self.windowEffect.disableMaximizeButton(self.winId())


class FramelessMainWindow(QMainWindow):
    """ Frameless main window """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.frameless = FramelessWindow(self)

        attributes = vars(self.frameless)

        # Переопределить атрибуты в текущем экземпляре
        for attr_name, attr_value in attributes.items():
            setattr(self, attr_name, attr_value)

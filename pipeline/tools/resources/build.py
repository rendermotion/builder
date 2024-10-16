from PySide6 import QtCore
from PySide6.QtUiTools import QUiLoader
from builder import pipeline
from PySide6.QtCore import QIODevice


print(pipeline.__path__[0])
ui_file = f'{pipeline.__path__[0]}\\tools\\resources\\build_form.ui'

print(ui_file)
file = QtCore.QFile()
file.setFileName(ui_file)
file.open(QIODevice.ReadOnly)
QUiLoader.load(file)
# file.close()

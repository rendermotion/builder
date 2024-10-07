from PySide2 import QtCore
from PySide2.QtUiTools import QUiLoader
from builder import pipeline
from PySide2.QtCore import QIODevice


print(pipeline.__path__[0])
ui_file = f'{pipeline.__path__[0]}\\tools\\resources\\build_form.ui'

print(ui_file)
file = QtCore.QFile()
file.setFileName(ui_file)
file.open(QIODevice.ReadOnly)
QUiLoader.load(file)
# file.close()

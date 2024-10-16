import maya.cmds as cmds
import maya.OpenMayaUI as mui
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6 import __version__
from shiboken6 import wrapInstance
from builder.pipeline.tools.UI import buildForm
import maya.mel as mel
from builder.pipeline.mgear import io
from builder.pipeline import environment
from RMPY.core import data_save_load

import importlib
from builder.pipeline import pipe_config
from builder.pipeline import environment
import os
import pkgutil
from pathlib import Path

importlib.reload(io)
importlib.reload(pipe_config)
importlib.reload(environment)
importlib.reload(buildForm)
importlib.reload(data_save_load)


class BuildStep(QListWidgetItem):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.evaluate = None

    def toggle_item(self):
        print(self.flags() & Qt.ItemIsEnabled)
        if Qt.ItemIsEnabled in self.flags():
            self.setFlags(self.flags() & ~Qt.ItemIsEnabled)
        else:
            self.setFlags(self.flags() | Qt.ItemIsEnabled)

    @property
    def is_enabled(self):
        print(self.flags() & Qt.ItemIsEnabled)
        if Qt.ItemIsEnabled in self.flags():
            return True
        else:
            return False

def getMayaWindow():
    ptr = mui.MQtUtil.mainWindow()
    return wrapInstance(int(ptr), QMainWindow)


class Main(MayaQWidgetDockableMixin, QDialog):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent=getMayaWindow())
        self.build_step_list = []
        self.env = environment.Environment()
        self.ui = buildForm.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle('bgb Short Pipe')
        self.ui.save_guides_button.clicked.connect(io.export_template)
        self.ui.save_skin_button.clicked.connect(data_save_load.save_skin_cluster)
        self.ui.load_skin_button.clicked.connect(data_save_load.load_skin_cluster)
        self.ui.save_shapes_button.clicked.connect(data_save_load.save_curve)
        self.ui.load_shapes_button.clicked.connect(data_save_load.load_curves)
        self.ui.save_reference_file_btn.clicked.connect(self.save_reference_file)

        for index, each in enumerate(self.env.asset_list):
            self.ui.comboBox.insertItem(index, each)
        self.ui.comboBox.currentIndexChanged.connect(self.update_env)
        self.ui.listWidget.itemDoubleClicked.connect(self.build_clicked)
        self.ui.file_name_lineEdit.setText('reference_points')
        self.add_build_steps()

    def update_env(self):
        # print(f'the index changed {self.ui.comboBox.currentIndex()}')
        # print(self.env.asset_list[self.ui.comboBox.currentIndex()])
        self.ui.listWidget.clear()
        self.env.asset = self.env.asset_list[self.ui.comboBox.currentIndex()]
        self.build_step_list = []
        self.add_build_steps()

    def save_reference_file(self):
        data_save_load.export_maya_file(file_name=self.ui.file_name_lineEdit.text())

    def build_clicked(self):
        index = 0
        run_till = self.ui.listWidget.currentItem()
        if run_till.is_enabled:
            if run_till.evaluate is not None:
                index = self.ui.listWidget.currentRow()
            else:
                print('run button evaluate is none')
        else:
            print('button not enabled')
            return

        for each_widget in self.build_step_list[:index+1]:
            if each_widget.is_enabled:
                if each_widget.evaluate:
                    each_widget.evaluate()
                each_widget.toggle_item()

    def add_build_steps(self):
        self.env.import_environment_modules()
        from pprint import pprint as pp
        pp(self.env.build_config_file.build)

        if self.env.build_config_file:
            for each in self.env.build_config_file.build_order:
                self.build_step_list.append(BuildStep(each))
                for step_text, step_function in self.env.build_config_file.build[each]:
                    self.build_step_list.append(BuildStep(f'    {step_text}'))
                    self.build_step_list[-1].evaluate = self.env.get_variables_from_path(step_function[0])

        for each in self.build_step_list:
            self.ui.listWidget.addItem(each)


if __name__ == '__main__':
    w = Main()
    w.show()

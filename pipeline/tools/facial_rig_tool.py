import sys
import maya.cmds as cmds
import maya.OpenMayaUI as mui
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from shiboken6 import wrapInstance
from builder.pipeline.tools.UI import facialRigForm
import maya.mel as mel
import os
import pymel.core as pm
from RMPY import RMblendShapesTools
from builder.pipeline import environment
from RMPY.snippets import blendshape_extraction
from RMPY.snippets import blendshape_split
import importlib
from RMPY.rig import rigBlendShapeControls
from RMPY.rig import rigFacial
reload(blendshape_extraction)
reload(blendshape_split)



def getMayaWindow():
    ptr = mui.MQtUtil.mainWindow()
    return wrapInstance(int(ptr), QMainWindow)


class Main(MayaQWidgetDockableMixin, QDialog):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent=getMayaWindow())
        self.ui = facialRigForm.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle('FacialRig')

        self.env = environment.Environment()
        self.dictionary = None
        facial_definition = self.env.get_variables_from_path(environment.pipe_config.facial_definition)
        if 'definition' in dir(facial_definition):
            self.dictionary = facial_definition.definition
            self.prefix_geometry_list = facial_definition.prefix_geometry_list
        else:
            print(f'no definition found on {facial_definition.__file__}')

        from pprint import pprint as pp
        self.ui.CheckBtn.clicked.connect(self.check_button_pressed)
        # self.ui.ImportFacialInterfaceBtn.clicked.connect(self.ImportFacialInterfaceBtnPressed)
        # self.ui.DeleteAttributesBtn.clicked.connect(self.deleteAttributes)
        self.ui.ListCBx.currentIndexChanged.connect(self.combo_box_changed)
        self.ui.renameRightBtn.clicked.connect(self.rename_right_btn)
        self.ui.LinkAllBtn.clicked.connect(self.link_all_dictionaries)
        self.ui.createMissingBtn.clicked.connect(self.create_missing_shapes)

        self.ui.extract_blendshapes_btn.clicked.connect(self.extract_blendShapes)
        self.ui.copy_vertex_position_btn.clicked.connect(self.copy_vertex_position)
        self.ui.split_by_axis_btn.clicked.connect(self.split_by_axis)

        self.ui.build_facial_controls_btn.clicked.connect(self.build_facial_controls)
        self.ui.connectRigBtn.clicked.connect(self.connect_to_rig)

        self.ui.UseSufixChkBx.stateChanged.connect(self.use_sufix_chk_bx_state_changed)
        for eachItem in sorted(self.dictionary):
            self.ui.ListCBx.addItem(eachItem)
        self.ui.LinkSelectedBtn.clicked.connect(self.connect_dictionary)
        self.Manager = RMblendShapesTools.BSManager()

        self.ui.PrefixLineEdit.textChanged.connect(self.check_button_pressed)

    def build_facial_controls(self):
        rigBlendShapeControls.RigBlendShapeControls(root='C_facialControls_reference_pnt')

    def connect_to_rig(self):
        rigFacial.RigFacial(self.dictionary, prefix_geometry_list=self.prefix_geometry_list)

    def extract_blendShapes(self):
        selection = pm.ls(selection=True)
        if len(selection) > 1:
            for each in selection[1:]:
                blendshape_extraction.duplicate_targets(prefix=str(each), geometry_node = selection[0], duplicated_object = each)
        else:
            blendshape_extraction.duplicate_targets()

    def copy_vertex_position(self):
        selection = pm.ls(selection=True)
        blendshape_split.copy_vertex_position(*selection)

    def split_by_axis(self):
        selection = pm.ls(selection=True)
        if pm.objExists('character'):
            blendshape_split.split_blendshape('character', str(selection[0]))
        else:
            print('no base "character" geo exists')

    def use_sufix_chk_bx_state_changed(self):
        if self.ui.UseSufixChkBx.checkState() == Qt.CheckState.Checked:
            self.ui.PrefixLineEdit.setEnabled(True)
        else:
            self.ui.PrefixLineEdit.setDisabled(True)
        self.check_button_pressed()

    def rename_right_btn(self):
        selection = cmds.ls(selection=True)
        for i in selection:
            cmds.rename(i, "R" + i[1:-1])

    def combo_box_changed(self):
        self.check_button_pressed()

    def connect_dictionary(self):
        if self.ui.PrefixLineEdit.isEnabled():
            object_name_prefix = self.ui.PrefixLineEdit.text()
        else:
            object_name_prefix = ''

        link_dictionary = self.dictionary[self.ui.ListCBx.currentText()]
        self.Manager.AppyBlendShapeDefinition(link_dictionary,  objectPrefix=object_name_prefix)

    def create_missing_shapes(self):
        self.check_button_pressed()
        sufix = self.ui.PrefixLineEdit.text()
        if sufix:
            base_geo = sufix
        else:
            base_geo = self.dictionary[self.ui.ListCBx.currentText()]['baseMesh']
        if pm.objExists(base_geo):
            for each in range(self.ui.listWidget.count()):
                current_item = self.ui.listWidget.item(each)
                pm.duplicate(base_geo, name=current_item.text())
            self.check_button_pressed()
        else:
            print("base object {} doesn't exists".format(base_geo))

    def link_all_dictionaries(self):
        if self.ui.PrefixLineEdit.isEnabled():
            object_name_prefix = self.ui.PrefixLineEdit.text()
        else:
            object_name_prefix = ''

        for eachDic in self.dictionary:
            self.Manager.AppyBlendShapeDefinition(self.dictionary[eachDic],  objectPrefix=object_name_prefix)

    def check_button_pressed(self):
        if self.ui.PrefixLineEdit.isEnabled():
            object_name_prefix = self.ui.PrefixLineEdit.text()
        else:
            object_name_prefix = ''
        self.ui.listWidget.clear()
        each_dic = self.dictionary[self.ui.ListCBx.currentText()]
        # for eachDefinition in eachDic:
        # print(eachDefinition)
        if each_dic['type'] == 'blend_shape_definition':
            array_prefix = []
            if each_dic['isSymetrical']:
                array_prefix = "LR"
                for eachPrefix in array_prefix:
                    for eachBlendShape in sorted(each_dic['blendShapes']):
                        if not cmds.objExists('{}{}{}'.format(eachPrefix, eachBlendShape[1:], object_name_prefix)):
                            self.ui.listWidget.addItem('{}{}{}'.format(eachPrefix, eachBlendShape[1:], object_name_prefix))
            else:
                for eachBlendShape in sorted(each_dic['blendShapes']):
                    if not cmds.objExists('{}{}'.format(eachBlendShape, object_name_prefix)):
                        self.ui.listWidget.addItem('{}{}'.format(eachBlendShape, object_name_prefix))


if __name__ == '__main__':
    w = Main()
    w.show()

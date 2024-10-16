# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_FacialRig.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(275, 417)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.CheckBtn = QtWidgets.QPushButton(self.groupBox)
        self.CheckBtn.setMaximumSize(QtCore.QSize(70, 16777215))
        self.CheckBtn.setObjectName("CheckBtn")
        self.horizontalLayout.addWidget(self.CheckBtn)
        self.ListCBx = QtWidgets.QComboBox(self.groupBox)
        self.ListCBx.setObjectName("ListCBx")
        self.horizontalLayout.addWidget(self.ListCBx)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.LinkAllBtn = QtWidgets.QPushButton(self.groupBox)
        self.LinkAllBtn.setObjectName("LinkAllBtn")
        self.horizontalLayout_2.addWidget(self.LinkAllBtn)
        self.LinkSelectedBtn = QtWidgets.QPushButton(self.groupBox)
        self.LinkSelectedBtn.setObjectName("LinkSelectedBtn")
        self.horizontalLayout_2.addWidget(self.LinkSelectedBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.UseSufixChkBx = QtWidgets.QCheckBox(self.groupBox)
        self.UseSufixChkBx.setObjectName("UseSufixChkBx")
        self.horizontalLayout_3.addWidget(self.UseSufixChkBx)
        self.PrefixLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.PrefixLineEdit.setEnabled(False)
        self.PrefixLineEdit.setObjectName("PrefixLineEdit")
        self.horizontalLayout_3.addWidget(self.PrefixLineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.renameRightBtn = QtWidgets.QPushButton(self.groupBox)
        self.renameRightBtn.setObjectName("renameRightBtn")
        self.horizontalLayout_4.addWidget(self.renameRightBtn)
        self.createMissingBtn = QtWidgets.QPushButton(self.groupBox)
        self.createMissingBtn.setObjectName("createMissingBtn")
        self.horizontalLayout_4.addWidget(self.createMissingBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.copy_vertex_position_btn = QtWidgets.QPushButton(self.groupBox)
        self.copy_vertex_position_btn.setObjectName("copy_vertex_position_btn")
        self.horizontalLayout_5.addWidget(self.copy_vertex_position_btn)
        self.extract_blendshapes_btn = QtWidgets.QPushButton(self.groupBox)
        self.extract_blendshapes_btn.setObjectName("extract_blendshapes_btn")
        self.horizontalLayout_5.addWidget(self.extract_blendshapes_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.build_facial_controls_btn = QtWidgets.QPushButton(self.groupBox)
        self.build_facial_controls_btn.setObjectName("build_facial_controls_btn")
        self.horizontalLayout_6.addWidget(self.build_facial_controls_btn)
        self.connectRigBtn = QtWidgets.QPushButton(self.groupBox)
        self.connectRigBtn.setObjectName("connectRigBtn")
        self.horizontalLayout_6.addWidget(self.connectRigBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.split_by_axis_btn = QtWidgets.QPushButton(self.groupBox)
        self.split_by_axis_btn.setObjectName("split_by_axis_btn")
        self.verticalLayout_2.addWidget(self.split_by_axis_btn)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Blendshape creation tools"))
        self.CheckBtn.setText(_translate("Form", "Check"))
        self.LinkAllBtn.setText(_translate("Form", "Link all"))
        self.LinkSelectedBtn.setText(_translate("Form", "Link selected"))
        self.UseSufixChkBx.setText(_translate("Form", "UseSufix"))
        self.renameRightBtn.setText(_translate("Form", "Rename right"))
        self.createMissingBtn.setText(_translate("Form", "Create  missing as proxy"))
        self.copy_vertex_position_btn.setText(_translate("Form", "Copy vertex position"))
        self.extract_blendshapes_btn.setText(_translate("Form", "Extract blendshapes"))
        self.build_facial_controls_btn.setText(_translate("Form", "Build facial controls"))
        self.connectRigBtn.setText(_translate("Form", "Connect to rig"))
        self.split_by_axis_btn.setText(_translate("Form", "Split by axis"))

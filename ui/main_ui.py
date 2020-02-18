# -*- coding: utf-8 -*-
__author__ = "yangtao"


import sys
import datetime
import os

from PySide2 import QtWidgets
from PySide2 import QtGui




class Unpack_Widget(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Unpack_Widget, self).__init__(parent=parent)
        self.setWindowTitle("释放")
        self.setMinimumWidth(400)

        self.pack_dir_edit = QtWidgets.QLineEdit()
        self.pack_dir_edit.setPlaceholderText("输入“包文件”夹路径")
        self.resolve_button = QtWidgets.QPushButton("解析")
        self.pack_dir_layout = QtWidgets.QHBoxLayout()
        self.pack_dir_layout.addWidget(self.pack_dir_edit)
        self.pack_dir_layout.addWidget(self.resolve_button)

        self.map_layout = QtWidgets.QFormLayout()

        # 开始
        self.start_button = QtWidgets.QPushButton("释放")
        self.start_button.setEnabled(False)

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.addLayout(self.pack_dir_layout)
        self.main_layout.addLayout(self.map_layout)
        self.main_layout.addWidget(self.start_button)

        self.start_button.clicked.connect(lambda: self.close())

    def get_map(self, map_label):
        drives_map = {}
        for l in map_label:
            value = self.findChild(QtWidgets.QLineEdit, l).text()
            drives_map[l] = value
        return drives_map

    def add_map(self, map_label):
        self.remove_map()
        if map_label:
            for l in map_label:
                label = QtWidgets.QLabel("%s >>> "%l)
                edit = QtWidgets.QLineEdit()
                edit.setObjectName(l)
                self.map_layout.addRow(label, edit)
            self.start_button.setEnabled(True)

    def remove_map(self):
        for row in range(self.map_layout.rowCount()):
            self.map_layout.removeRow(0)
        self.start_button.setEnabled(False)


class Pack_Widget(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Pack_Widget, self).__init__(parent=parent)
        self.setWindowTitle("打包")
        self.setMinimumWidth(400)

        file_name_label = QtWidgets.QLabel("Nuke工程文件")
        self.file_name_edit = QtWidgets.QLineEdit()
        export_dir_label = QtWidgets.QLabel("输出路径")
        self.export_dir_edit = QtWidgets.QLineEdit()

        # 开始
        self.start_button = QtWidgets.QPushButton("打包")

        self.main_layout = QtWidgets.QFormLayout(self)
        self.main_layout.addRow(file_name_label, self.file_name_edit)
        self.main_layout.addRow(export_dir_label, self.export_dir_edit)
        self.main_layout.addRow(self.start_button)

        self.start_button.clicked.connect(lambda :self.close())


class Mian_Widget(QtWidgets.QWidget):
    def __init__(self):
        super(Mian_Widget, self).__init__()
        self.setWindowIcon(QtWidgets.QApplication.style().standardIcon(QtWidgets.QStyle.SP_TitleBarCloseButton))
        self.setWindowTitle("DZL Nuke 工程打包工具 by yangtao")
        self.setMinimumWidth(485)

        # 信息框
        self.info_edit = QtWidgets.QTextEdit()
        self.info_edit.setWordWrapMode(QtGui.QTextOption.NoWrap)

        # 打包，释放按钮
        self.pack_button = QtWidgets.QPushButton("打包")
        self.pack_button.setObjectName("pack_project")
        self.pack_button.setIcon(QtWidgets.QApplication.style().standardIcon(QtWidgets.QStyle.SP_ArrowDown))
        self.unpack_button = QtWidgets.QPushButton("释放")
        self.unpack_button.setObjectName("unpack_project")
        self.unpack_button.setIcon(QtWidgets.QApplication.style().standardIcon(QtWidgets.QStyle.SP_ArrowUp))

        expand_button_layout = QtWidgets.QHBoxLayout()
        expand_button_layout.addWidget(self.pack_button)
        expand_button_layout.addWidget(self.unpack_button)

        # 打包，释放 UI
        self.pack_widget = Pack_Widget(self)
        self.unpack_widget = Unpack_Widget(self)
        #self.unpack_widget.add_map(["a", "b", "c", "d"])
        #self.unpack_widget.setHidden(True)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(self.info_edit)
        main_layout.addLayout(expand_button_layout)

        # connect
        self.pack_button.clicked.connect(self.show_pack_widget)
        self.unpack_button.clicked.connect(self.show_pack_widget)

    def set_button_enabled(self, status):
        self.pack_button.setEnabled(status)
        self.unpack_button.setEnabled(status)

    def add_info(self, text, add_time_line=True):
        current_info = self.info_edit.toPlainText()
        if add_time_line:
            time_line = "%s:\n"%datetime.datetime.now().strftime("%H:%M:%S")
        else:
            time_line = ""
        new_info = current_info + time_line + text
        self.info_edit.setText("%s\n"%new_info)
        self.info_edit.moveCursor(QtGui.QTextCursor.End)

    def show_pack_widget(self):
        if self.sender().objectName() == "pack_project":
            self.pack_widget.show()
            self.unpack_widget.close()

        if self.sender().objectName() == "unpack_project":
            self.pack_widget.close()
            self.unpack_widget.show()




if __name__ == "__main__":
    app = QtWidgets.QApplication()
    mw = Mian_Widget()
    mw.show()
    sys.exit(app.exec_())
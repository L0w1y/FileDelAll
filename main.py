import os
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from inspect import getsourcefile
from os.path import abspath
from data import ui


# region UI
class Interface(QMainWindow):
    def __init__(self):
        super(Interface, self).__init__()
        self.ui = ui.Ui_MainWindow()
        self.ui.setupUi(self)

        # while editiong texts - checks the proceedd status
        self.ui.Extentions_LineEdit.textEdited.connect(self.Checks)
        self.ui.RootFolder_LineEdit.textEdited.connect(self.Checks)

        # on click - do something
        self.ui.ChooseFolderButton.clicked.connect(self.ChooseFolder)
        self.ui.StartDelete_Button.clicked.connect(self.Process)

    def ChooseFolder(self):
        path = QFileDialog.getExistingDirectory(caption="Выберите корневую папку")
        self.ui.RootFolder_LineEdit.setText(path)

    def Process(self):
        FileDeleteAll(path=self.ui.RootFolder_LineEdit.text(), extentions=self.ui.Extentions_LineEdit.text(),
                      delete_cfiles=self.ui.SaveTemporaryFiles_Checkbox.isChecked(),
                      cache_path=os.path.dirname(abspath(getsourcefile(lambda: 0))))

        self.ui.Extentions_LineEdit.setText("")
        self.ui.RootFolder_LineEdit.setText("")

    def Checks(self):
        if len(self.ui.RootFolder_LineEdit.text()) > 3 and len(self.ui.Extentions_LineEdit.text()) > 2:
            self.ui.StartDelete_Button.setEnabled(True)
        else:
            self.ui.StartDelete_Button.setEnabled(False)

def Start():
    app = QApplication(sys.argv)
    window = Interface()
    window.show()
    sys.exit(app.exec())
# endregion

# region DeleteAllFile
def FileDeleteAll(path:str, extentions:str, cache_path:str, delete_cfiles:bool) -> None:
    if os.path.exists(path) and os.path.exists(cache_path):
        os.system(f"where /r {os.path.normpath(path)} {extentions} >> {cache_path}\\.temp.txt")
    with open(f"{cache_path}\\.temp.txt", "r") as files:
        files = files.read()
        files = files.split("\n")
        for i in files:
            print(f"Процесс: {files.index(i)+1} / {len(files)}")
            if files.index(i) != len(files)-1 and os.path.exists(i) and os.path.isfile(i):
                os.system(f"del {i}")

    if delete_cfiles:
        os.system(f"del {cache_path}\\.temp.txt")
# endregion

if __name__ == '__main__':
    Start()

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QListWidgetItem, QMessageBox
from EditDialog import Ui_Dialog

class EditDialog(QDialog):
    def __init__(self, TypeS, *args, **kwargs) :
        super().__init__(*args, **kwargs)
    
    
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.ui.btnAdd.clicked.connect(self.accept)
        self.ui.btnCancel.clicked.connect(self.reject)

        print(TypeS)

        for r in TypeS.values():
            self.ui.cmbTypeS.addItem(r.title, r)


    def get_data(self):
        return{
            "TypeS_id": self.ui.cmbTypeS.currentData().id,
            "object": self.ui.lObject.text(),
            "sCount": self.ui.lsCount.text(),
            "sCaseCount": self.ui.lsCaseCount.text(),
            "year": self.ui.lYear.text()
        }
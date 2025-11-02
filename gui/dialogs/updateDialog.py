
from dialogs.EditDialogCode import EditDialog

class UpdateDialog(EditDialog):
    def __init__(self, TypeS, init_data, *args, **kwargs):
        super().__init__(TypeS,  *args, **kwargs)

        self.ui.btnAdd.setText('Изменить')

        self.ui.cmbTypeS.setEnabled(False)

        TypeSname = TypeS[init_data.TypeS_id].title     
        self.ui.cmbTypeS.setCurrentText(TypeSname)

        self.ui.lObject.setText(str(init_data.object))
        self.ui.lsCount.setText(str(init_data.sCount))
        self.ui.lsCaseCount.setText(str(init_data.sCaseCount))
        self.ui.lYear.setText(str(init_data.year))
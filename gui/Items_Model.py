from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QListWidgetItem, QMessageBox
from PySide6 import QtCore
from PySide6 import QtWidgets

class ItemsModel(QtCore.QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._items = []
        self._typeS = {}
        self._headers = ["ID", "Вид страхования", "Объект", "Кол-во договоров", "Кол-во случаев", "Год"]

    def setItems(self, items):
        self.beginResetModel()
        self._items = items
        self.endResetModel()

    def setTypeS(self, typeS):
        self.beginResetModel()
        self._typeS = typeS
        self.endResetModel()

    def rowCount(self, parent=QtCore.QModelIndex()) -> int:
        return len(self._items)

    def columnCount(self, parent=QtCore.QModelIndex()) -> int:
        return len(self._headers)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if not index.isValid() or not (0 <= index.row() < len(self._items)):
            return None

        item = self._items[index.row()]
        col = index.column()

        if role == QtCore.Qt.DisplayRole:
            if col == 0:
                return str(item.id)
            elif col == 1:
                typeS_item = self._typeS.get(item.TypeS_id)
                return typeS_item.title if typeS_item else "N/A"
            elif col==2:
                return str(item.object)
            elif col == 3:
                return str(item.sCount)
            elif col == 4:
                return str(item.sCaseCount)
            elif col == 5:
                return str(item.year)
        elif role == QtCore.Qt.ItemDataRole.UserRole:
            return item
        
        return None

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                if 0 <= section < len(self._headers):
                    return self._headers[section]
        return None
    
    def headerData(self, section: int, 
                  orientation: QtCore.Qt.Orientation,
                  role=QtCore.Qt.ItemDataRole.DisplayRole):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            if orientation == QtCore.Qt.Orientation.Horizontal:
                headers = {
                    0: 'ID',
                    1: 'Вид страхования',
                    2: 'Объект',
                    3: 'Кол-во договоров', 
                    4: 'Кол-во случаев',
                    5: 'Год'
                }
                return headers.get(section, "")
        return None
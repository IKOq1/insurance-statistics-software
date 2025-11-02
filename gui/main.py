from statistics import *
import sys
import os
import PySide6
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QListWidgetItem, QMessageBox
from PySide6 import QtCore
from PySide6 import QtWidgets

#mb error

from dialogs.EditDialogCode import EditDialog


from MainWindow import Ui_MainWindow
from EditDialog import Ui_Dialog
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

from data.typeS_information_info import typeS_information_info
from data.fetch_object_info import fetch_object_info
from data.insert_information_info import insert_information_info
from data.delete_information_info import delete_information_info
from data.update_information_info import update_information_info
from data.create_session import create_session
from data.fetch_information_info import fetch_information_info
from dialogs.updateDialog import UpdateDialog
from pathlib import Path
import subprocess
from PySide6 import QtCharts

#чтобы получить доступ к дргуми файлам
PROJECT_ROOT = Path(__file__).parent.parent  
sys.path.append(str(PROJECT_ROOT))

from Items_Model import ItemsModel
from gui.data.compute_statistics import compute_statistics
from gui.charts.create_bar_chart import create_bar_chart
from gui.charts.create_pie_chart import create_pie_chart
from gui.charts.create_bar_chart2 import create_bar_chart2


    #politech
dirname = os.path.dirname(PySide6.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()


        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.model= ItemsModel() #инициализация табл
        self.ui.tblView.setModel(self.model)

        #vneshnii vid tabl
        self.ui.tblView.horizontalHeader().setStretchLastSection(True)
        self.ui.tblView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.ui.tblView.setSelectionMode(QtWidgets.QTableView.SingleSelection)


        #вызываем функции

        self.load_TypeS()
        self.load_object()
        self.load_information()

        

        self.ui.cmbTypeS.currentIndexChanged.connect(self.load_information)
        self.ui.cmbObject.currentIndexChanged.connect(self.load_information)
        self.ui.btnAdd.clicked.connect(self.onBtnAdd)
        self.ui.btnDelete.clicked.connect(self.onBtnDelete)
        self.ui.btnChange.clicked.connect(self.onBtnChange)
        self.ui.btnStartBot.clicked.connect(self.onBtnStartBot)
        self.ui.btnUpdateWidget.clicked.connect(self.onBtnUpdateWidget)


    def onBtnStartBot(self):
        pbot = Path(__file__).parent.parent
        bot = pbot / 'bot' / 'tgBot.py'

        subprocess.Popen(
            ['python', str(bot)],
                          creationflags=subprocess.CREATE_NEW_CONSOLE) #запустить тг бот 


    def onBtnUpdateWidget(self): #перегрузить
        self.load_information()
        self.load_object()


    def onBtnChange(self):
        item = self.ui.tblView.currentIndex()
        init_data = item.data (QtCore.Qt.ItemDataRole.UserRole)
        
        dialog = UpdateDialog(self.TypeS, init_data)
        r = dialog.exec()
        if r == 0:
            return
        
        data = dialog.get_data()
        

        with create_session() as s:
            update_information_info(s, data, init_data)


        self.load_information()
        self.load_object()
    
    


    def onBtnDelete(self):
        item =self.ui.tblView.currentIndex()
        data = item.data(QtCore.Qt.ItemDataRole.UserRole)

        r = QMessageBox.question(self, "Потверждение", "Точно ли хотите удалить?")
        if r == QMessageBox.StandardButton.Yes:    
            
            
            with create_session() as s:
                delete_information_info(s, data)
            
            
            self.load_information()
            self.load_object()
        else:
            return

    def onBtnAdd(self):
        
        dialog = EditDialog(self.TypeS)
        r = dialog.exec()

        if r==0:
            return

        
        
        #вытаскиваем данные

        data = dialog.get_data()
        with create_session() as s:
            insert_information_info(s, data)
        
        
        #вызываем чтобы обновился списочек
        self.load_information()
        self.load_object()
    
    


    def load_information(self):

        TypeS_data=self.ui.cmbTypeS.currentData()
        
            #проверка на отсутствие значения
        
        if TypeS_data:
            typeS_id = self.ui.cmbTypeS.currentData().id
        else:
            typeS_id=0
        object_text = self.ui.cmbObject.currentText()

            #фильтруем объект страхования 
            #причем фильтруем в форме тернарного оператора, про который я только что узнал
        
        object_filter = object_text if object_text!= "Объект страхования" else None


            #Чистим
        # self.ui.lstWidget.clear()
        self.rows = []

        with create_session() as s:

            rows = fetch_information_info(s, typeS_id, object_filter)



            for r in rows:

                self.rows.append(r)

        #statistics
        self.show_statisctics()

        #graph1
        self.draw_bar_chart2()
        self.draw_pie_chart()
        self.draw_bar_chart()
        self.model.setItems(self.rows)
        self.ui.tblView.setColumnWidth(0, 30)
        self.ui.tblView.setColumnWidth(1, 170)
        self.ui.tblView.setColumnWidth(5, 30)
        self.ui.tblView.setColumnWidth(3, 120)
    
                                                    #podgruzjat types
    def load_TypeS(self):
        self.TypeS = {}
        with create_session() as s:
            
            
            rows = typeS_information_info(s)
            for r in rows:
                self.TypeS[r.id] = r 
            
            
            #добавим прочерк  
        self.ui.cmbTypeS.addItem("Вид страхования")

        for r in self.TypeS.values():
            self.ui.cmbTypeS.addItem(r.title ,r )

        self.model.setTypeS(self.TypeS)

        #zapusk
    
                                                                            #statistics
    def show_statisctics(self):
        text  = compute_statistics(self.rows, self.TypeS)
        self.ui.lblStatistics.setText(text)
    
                                                            #работа с объектом страхования
    def load_object(self):
        
            #блочим сигнал чтобы интефейс не вылетал (не вызывал себя постоянно)
        self.ui.cmbObject.blockSignals(True)
        
            #чистим
        self.ui.cmbObject.clear()


        #снова пустно знач
        self.ui.cmbObject.addItem("Объект страхования")

        with create_session() as s:
            rows = fetch_object_info(s)

            for r in rows:
                self.ui.cmbObject.addItem(str(r.object))
        
            #разблокируем сигналы после циклирования
        self.ui.cmbObject.blockSignals(False)

                                                                    #graph3

    def draw_bar_chart(self):
        chart = create_bar_chart(self.rows, self.TypeS)
        self.ui.chartView3.setChart(chart)
    
                                                                    #graph2
    def draw_pie_chart(self):
        chart = create_pie_chart(self.rows, self.TypeS)
        self.ui.chartView2.setChart(chart)
                                                                    #graph1
    def draw_bar_chart2(self):
        chart = create_bar_chart2(self.rows, self.TypeS)
        self.ui.chartView1.setChart(chart)
    
# основная болванка

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
from PySide6 import QtCharts
from PySide6 import QtCore, QtGui


def create_bar_chart(rows, TypeS):
    
    data_by_TypeS = {}
    year = set()


    for row in rows:
        # if row.TypeS_id in TypeS:
            items = data_by_TypeS.setdefault(row.TypeS_id, {})
            items[row.year] = items.get(row.year, 0) + row.sCount
            year.add(row.year)

    series = QtCharts.QHorizontalBarSeries()

    for TypeS_id, TypeS_data in data_by_TypeS.items():
        TypeS_title = TypeS[TypeS_id].title
        bar_set = QtCharts.QBarSet(TypeS_title)
        for i in year:
                value = TypeS_data.get(i, 0)
                bar_set.append(value)
        bar_set.setLabelColor('#2b3d40')
        series.append(bar_set)
        
    series.setLabelsVisible(True)
    series.setLabelsPosition(QtCharts.QAbstractBarSeries.LabelsPosition.LabelsOutsideEnd)
    series.setLabelsPrecision(15)

    chart= QtCharts.QChart()
    chart.setAnimationOptions(QtCharts.QChart.AnimationOption.SeriesAnimations)
    chart.addSeries(series)
    chart.createDefaultAxes()
        

    axis = QtCharts.QBarCategoryAxis()
    axis.append([str(i) for i in year])
    chart.setAxisY(axis, series)
    chart.axes(QtCore.Qt.Horizontal)[0].setTitleText("Количество договоров")

    chart.setMargins(QtCore.QMargins(50, 20, 50, 20))


    return chart

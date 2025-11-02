from statistics import mean
from PySide6 import QtCharts


def create_pie_chart(rows, TypeS):
    data_by_TypeS ={}
    for row in rows:
        items = data_by_TypeS.setdefault(row.TypeS_id, [])
        items.append(row)
        
    series = QtCharts.QPieSeries()
        
    for TypeS_id, TypeS_data in data_by_TypeS.items():
        TypeS_name = TypeS[TypeS_id].title
        avg = int(mean([i.sCount for i in TypeS_data]))
        series.append(f'{TypeS_name}', avg)
            

    series.setLabelsVisible(True)


    chart = QtCharts.QChart()
    chart.addSeries(series)

    return chart
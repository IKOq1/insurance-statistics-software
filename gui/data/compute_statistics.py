


from statistics import mean


def compute_statistics(rows, TypeS):
        max_rows = max(rows, key = lambda row: row.sCount)
        min_rows = min(rows, key = lambda row: row.sCount)
        
        avr_value = int(mean([i.sCount for i in rows]))
        avr_value2 = int(mean([i.sCaseCount for i in rows]))

        TypeSmax_name = TypeS[max_rows.TypeS_id].title
        TypeSmin_name = TypeS[min_rows.TypeS_id].title
        


        text = f"""
        Наибольшее количество договоров составило <b style = "color:#03c2fc; font-size: 13px">{max_rows.sCount}</b> в <b style="color:#03c2fc">{max_rows.year}</b><br> и присущим ему видом страхования было <b style= "color:#03c2fc">{TypeSmax_name}</b>.
        <hr> 
        Наименьшее количество страховых случаев составило <b style = "color:#6e6aa3;font-size: 13px">{min_rows.sCount}</b> в <b style= "color:#6e6aa3">{min_rows.year}</b><br> и присущим ему видом страхования было <b style= "color:#6e6aa3">{TypeSmin_name}</b> .
        <hr>
        Среднее значение количества <b style = "color:#979ccf">договоров</b> составило <span style = "background: #757ee0">{avr_value}</span>
        <hr>
        Среднее значение количества <b style = "color:#979ccf">страховых случаев</b> составило <span style = "background: #4a4875">{avr_value2}</span>
        """

        return text
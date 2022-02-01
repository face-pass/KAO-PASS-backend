from datetime import date, datetime

def getJsonDict(column, row):

    row_list = []
    column_list = []

    for c in range(len(column)):
        column_quant = column[c]
        for cq in range(len(column_quant)):
            column_list.append(column[c][cq])
    
    for r in range(len(row)):
        row_list.append(row[r][0])

    json_dict = dict(zip(row_list, column_list))

    return json_dict

def json_serial(obj):
    # 日付型の場合には、文字列に変換します
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    # 上記以外はサポート対象外.
    raise TypeError ("Type %s not serializable" % type(obj))
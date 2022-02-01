import json
import logging
import azure.functions as func
from shared_code.json_module import getJsonDict, json_serial
from shared_code.DB import MySQL

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # リクエスト
    table = req.form.get("table")

    if not table:
        func.HttpResponse("Table is required!!", status_code=400)
    
    mysql = MySQL

    column, row = mysql.select_all(table)

    json_dict = getJsonDict(column, row)

    with open('/tmp/student.json','w'):
        json.dumps({"*studnet_list*":[json_dict]}, indent=4, default=json_serial, ensure_ascii=False)

    return func.HttpResponse('/tmp/student.json', status_code=200)

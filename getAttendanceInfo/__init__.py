import logging
import azure.functions as func
from shared_code.create_json import create_json
from shared_code.DB import MySQL

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # リクエスト
    table = req.form.get("table")

    if not table:
        func.HttpResponse("Table is required!!", status_code=400)
    
    mysql = MySQL

    data = mysql.select_all(table)

    jsons = create_json(data)

    for json in jsons:
        json_data = {
            "*studentlist*":[
                json
            ]
        }

    with open('./tmp/student.json','w') as f:
        json.dump(json_data, f, ensure_ascii=False)

    return func.HttpResponse('./tmp/student.json', status_code=200)

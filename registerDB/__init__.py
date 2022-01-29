import logging
import azure.functions as func
from shared_code.DB import MySQL
from shared_code.connectStorage import connect_blob
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    storage_name = os.environ["STORAGE"]

    # リクエスト
    img_file = req.files['img']
    name = req.form.get('name')
    Major = req.form.get('Major')
    person_id = req.form.get('person_id')
    Mail = req.form.get('Mail')
    table = req.form.get('table')

    if not img_file:
        func.HttpResponse("Image files is required!!", status_code=400)
    elif not name or not Mail:
        func.HttpResponse("You have not entered either your name or email address, or both. Please enter.", status_code=401)
    elif not Major or not person_id:
        func.HttpResponse("The major name, person ID number, or both have not been entered. Please enter.", status_code=401)
    else:

        service = connect_blob()

        # upload blob
        container = table # ここはのちにテーブルの名前(ログインしているユーザー名_授業名)にする

        try:
            service.create_container(container,public_access="container")
        except:
            logging.error("Image container is already exist")
            pass
        
        blob_client = service.get_blob_client(container=container, blob=img_file.filename)
        blob_client.upload_blob(img_file, overwrite=True)

        logging.info('succes')

        # urlの作成
        blob_url = f"https://{storage_name}.blob.core.windows.net/{container}/{img_file.filename}"

        mysql = MySQL

        mysql.register(table, blob_url, name, Major, person_id, Mail)

        return func.HttpResponse('Student registration is complete.', status_code=200)

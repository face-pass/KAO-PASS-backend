import os
import logging
import azure.functions as func
from faceAPI.similar_faces import similar_face

def main(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")

    """
    フロントエンドからBlobに保存された画像の前処理
    """    
    # ファイル名からテーブル名を抜き取る
    table_name = os.path.splitext(os.path.basename(myblob.name))[0]
    logging.info(table_name)

    # 画像をリストに保存する
    image_list = []
    image_list.append(myblob.uri)
    
    # リサイズした画像をFaceAPIに送る
    similar_face(image_list, table_name)
    logging.info(f"updating {table_name} was success")
    
    logging.info("success")

"""送られてきた画像と登録されている画像を比較して同じ顔の人がいるかいないかを判別する"""
from shared_code.connectFaceAPI import connectFaceAPI
from shared_code.DB import MySQL
from shared_code.delete_blob import delete
import logging

def similar_face(request_img, table):

    student_id = []

    # connect FaceAPI client
    face_client = connectFaceAPI()

    mysql = MySQL()
    logging.info("Connected")

    # get student id parametar from table by dic
    # get student Image data from table by list
    dic, image_list = mysql.getProperty(table)
    # logging.info("got property!")
    # logging.info(dic)
    # logging.info(image_list)

    # analitics Image data by faceAPI and return student_id
    for x in range(len(image_list)):
        detect_face = face_client.face.detect_with_url(image_list[x], "detection_03")
        face_id = detect_face[0].face_id

        face_list_key = x + 1

        for img in request_img:
            detect_req_face = face_client.face.detect_with_url(url=img, detection_model="detection_03")
            face_req_id = list(map(lambda x: x.face_id, detect_req_face))

            similar_faces = face_client.face.find_similar(face_id=face_id, face_ids=face_req_id)
            if similar_faces:
                student_id.append(dic[face_list_key])
                verify_result = face_client.face.verify_face_to_face(face_id1=face_id, face_id2=face_req_id[0])
                logging.info("find similar_faces {} = {}. confidence: {}%".format(image_list[x], img, int(verify_result.confidence * 100)))
                break
            else:
                continue
    
    # 送られてきた画像を削除
    delete()

    mysql.upDate(table, student_id)
    
    mysql.sendMail(table)
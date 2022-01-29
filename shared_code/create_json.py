import json

def create_json(data):

    student_list = []

    for x in range(len(data)):
        json_list = {
            "id": data[x][0],
            "image": data[x][1],
            "name": data[x][2],
            "class": data[x][3],
            "number": data[x][4],
            "mail": data[x][5]
        }


        student_list.append(json_list)
    

    return student_list
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
import os

def connectFaceAPI():
    # This key will serve all examples in this document.
    KEY = os.environ['APIKEY']
    

    # This endpoint will be used in all examples in this quickstart.
    ENDPOINT = os.environ['ENDPOINT']


    # Create an authenticated FaceClient.
    face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

    return face_client
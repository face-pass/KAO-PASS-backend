from azure.storage.blob import BlobServiceClient
import os

def connect_blob():
    connect_str = os.environ['AzureWebJobsStorage']
    service = BlobServiceClient.from_connection_string(connect_str)
    return service
from .connectStorage import connect_blob
import logging

def delete():

    service = connect_blob()

    container_client = service.get_container_client("image")

    blob_list = container_client.list_blobs()

    for blob in blob_list:
        container_client.delete_blob(blob)
        logging.info(f"delete {blob} file")
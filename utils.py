from google.cloud import storage
import os

def initialize_bucket(credentials_path, bucket_name, create_bucket=False):
    '''
    function to access the data stored in a Google Storage bucket
    IN:
    credentials_path: local where the JSON file with the credentials is stored
    create_bucket: if the bucket needs to be created
    bucket_name: name of the bucket that is going to be accessed

    OUT:
    client: client initialized
    bucket: 
    '''

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path

    client = storage.Client()
    bucket = client.bucket(bucket_name)
    
    if create_bucket:
        bucket.location = 'US-EAST1'
        bucket.create()

    return client, bucket
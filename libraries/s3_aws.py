''' Módulo para administración de Amazon S3 Bucket '''

import os
from dotenv import load_dotenv
import boto3

class AdminS3AWS():
    ''' Clase para administrar Amazon S3 Bucket '''

    def __init__(self):
        # pylint: disable=invalid-name
        env_path = "/app/.env"
        load_dotenv(env_path)
        self.client_s3 = boto3.client(
            's3',
            aws_access_key_id=os.getenv('ERP_AWS_ACCESS_KEY_ID', ""),
            aws_secret_access_key=os.getenv('ERP_AWS_SECRET_ACCESS_KEY', ""),
            region_name=os.getenv('ERP_AWS_DEFAULT_REGION', "")
        )
        self.resource_s3 = boto3.resource(
            's3',
            aws_access_key_id=os.getenv('ERP_AWS_ACCESS_KEY_ID', ""),
            aws_secret_access_key=os.getenv('ERP_AWS_SECRET_ACCESS_KEY', ""),
            region_name=os.getenv('ERP_AWS_DEFAULT_REGION', "")
        )
        self.environment = os.getenv('APP_SETTINGS', "")
        self.bucket_name = os.getenv('ERP_AWS_BUCKET_NAME', "")

    def check_file(self, filename):
        ''' Verifica si existe el archivo '''
        if self.environment == "" or self.bucket_name == "":
            return False
        filename = '%s/%s' % (self.environment, filename)
        results = self.client_s3.list_objects(Bucket=self.bucket_name, Prefix=filename)
        return 'Contents' in results

    def upload_file(self, filepath, filename):
        ''' Sube un archivo '''
        fullpath = "/app" + filepath
        new_filepath = '%s/%s' % (self.environment, filename)
        self.client_s3.upload_file(fullpath, self.bucket_name, new_filepath)

    def get_object(self, filepath):
        ''' Lee y retorna el contenido en formato de objeto de archivo '''
        filename = '%s/%s' % (self.environment, filepath)
        object_s3 = self.resource_s3.Object(self.bucket_name, filename)
        return object_s3

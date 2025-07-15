# file_uploader.py MinIO Python SDK example
import os

from dotenv import load_dotenv
from minio import Minio
from minio.error import S3Error


load_dotenv()

class MinioFileUploader:
    def __init__(self):
        # Create a client with the MinIO server playground, its access key
        # and secret key.
        self.client = Minio("play.min.io",
            access_key=os.environ.get("MINIO_ACCESS_KEY", "Q3AM3UQ867SPQQA43P2F"),
            secret_key=os.environ.get("MINIO_SECRET_KEY", "zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG"),
        )

    def upload_file(self, bucket_name=None, source_file=None, destination_file=None):
        """
        Uploads a file to a MinIO bucket, creating the bucket if it does not exist.
        :param bucket_name: Name of the bucket to upload to.
        :param source_file: Path to the local file to upload.
        :param destination_file: Name of the file in the bucket.
        """
        # Make the bucket if it doesn't exist.
        try:
            found = self.client.bucket_exists(bucket_name)
            if not found:
                self.client.make_bucket(bucket_name)
                print("Created bucket", bucket_name)
            else:
                print("Bucket", bucket_name, "already exists")

            # Upload the file, renaming it in the process
            self.client.fput_object(
                bucket_name, destination_file, source_file,
            )
            print(
                source_file, "successfully uploaded as object",
                destination_file, "to bucket", bucket_name,
            )
        except S3Error as err:
            print("Error occurred.", err)
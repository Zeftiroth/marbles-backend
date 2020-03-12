import boto3
import botocore
from config import Config

s3 = boto3.client(
    "s3",
    aws_access_key_id=Config.AWS_ACCESS_KEY,
    aws_secret_access_key=Config.AWS_SECRET_KEY
)


def upload_file_to_s3(file, ori_file, acl="public-read"):
    try:
        s3.upload_file(
            file,
            Config.AWS_BUCKET_NAME,
            ori_file.filename,
            ExtraArgs={
                "ACL": acl,
                "ContentType": ori_file.content_type
            }
        )

        return True

    except Exception as e:

        return False


import logging
import boto3
from botocore.exceptions import ClientError


def bucket_exists(bucket_name):
    """Determine whether bucket_name exists and the user has permission to access it

    :param bucket_name: string
    :return: True if the referenced bucket_name exists, otherwise False
    """

    s3 = boto3.client('s3')
    try:
        response = s3.head_bucket(Bucket=bucket_name)
    except ClientError as e:
        logging.debug(e)
        return False
    return True


def main():
    """Exercise bucket_exists()"""

    # Assign this value before running the program
    test_bucket_name = 'rahulb-test-bucket'

    # Set up logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')

    # Check if the bucket exists
    if bucket_exists(test_bucket_name):
        logging.info(f'{test_bucket_name} exists and you have permission to access it.')
    else:
        logging.info(f'{test_bucket_name} does not exist or '
                     f'you do not have permission to access it.')

if __name__ == '__main__':
    main()

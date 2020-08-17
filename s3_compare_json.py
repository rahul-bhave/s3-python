"""
This file will contain following 3 methods:
1. Read the json file from the S3 bucket and convert the json in the dict object.
3. Compare the json.dict with predefined.dict using deepdiff.
"""
import boto3
import collections
import deepdiff
import json
import logging
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import conf.aws_configuration_conf as aws_conf
from pythonjsonlogger import jsonlogger

# logging
log_handler = logging.StreamHandler()
log_handler.setFormatter(jsonlogger.JsonFormatter())
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)

#setting environment variable
os.environ["AWS_ACCOUNT_ID"]= aws_conf.AWS_ACCOUNT_ID
os.environ['AWS_DEFAULT_REGION'] = aws_conf.AWS_DEFAULT_REGION
os.environ['AWS_ACCESS_KEY_ID'] = aws_conf.AWS_ACCESS_KEY_ID
os.environ['AWS_SECRET_ACCESS_KEY'] = aws_conf.AWS_SECRET_ACCESS_KEY

#Declaring expecte json format
expected_dict = json.loads("""[{
   "MessageAttributes":{
      "quantity":{
         "Type":"Number",
         "Value":"100"
      }
   }
}]""")

class s3utilities():
    # class to write s3 utilities
    logger = logging.getLogger(__name__)
    s3_bucket = "compare-json"
    key = 'sample.json'

    def __init__(self):
        # initialising the class
        self.logger.info(f's3 utilities activated')

    def get_s3_bucket_json_dict(self):
        # Method to which will read the json file from the s3 bucket
        # Convert the json file to dictionary
        s3_client = boto3.client('s3')
        response = s3_client.get_object(Bucket=self.s3_bucket, Key=self.key)
        print(f'printing{response}')
        sample_json = ""
        for line in response["Body"].iter_lines():
            sample_json += line.decode("utf-8")
        sample_dict = json.loads(sample_json)
        print(f'printing sample dict {sample_dict}')

        return sample_dict


    def compare_with_expected_dict(self, expected_dict):
        # Method to compare expected dict and actual dict
        sample_dict = self.get_s3_bucket_json_dict()
        diff = deepdiff.DeepDiff(expected_dict, sample_dict)

        return diff


if __name__ == "__main__":
    # Testing s3utilities

    print(f'Testing s3utilities class')
    s3utilities = s3utilities()
    print(f'sample_dict')
    diff = s3utilities.compare_with_expected_dict(expected_dict)
    print(f'actual diff is {diff}')

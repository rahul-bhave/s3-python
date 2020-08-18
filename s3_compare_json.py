"""
This file will contain following  methods:
1. Get Response s3 client object.
2. Convert response into dict object.
3. Get Response dict object.
4. Get expected dict from json stored as expected json.
5. Compare Response dict and expected dict using deepdiff.
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
from pprint import pprint

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


class s3utilities():
    # class to write s3 utilities
    logger = logging.getLogger(__name__)
    s3_bucket = "compare-json"
    key = 'sample.json'
    template_directory = 'samples'

    def __init__(self):
        # initialising the class
        self.logger.info(f's3 utilities activated')

    def get_response(self, bucket, key):
        # Get Response s3 client object
        s3_client = boto3.client('s3')
        response = s3_client.get_object(Bucket=bucket, Key=key)

        return response

    def convert_dict_from_response(self,response):
        # Convert response into dict object
        response_json = ""
        for line in response["Body"].iter_lines():
            response_json += line.decode("utf-8")
        response_dict = json.loads(response_json)

        return response_dict

    def get_response_dict(self):
        # Get Response dict object
        response = self.get_response(self.s3_bucket,self.key)
        response_dict = self.convert_dict_from_response(response)

        return response_dict

    def get_expected_dict(self):
        # Get expected dict from json stored as expected json
        current_directory = os.path.dirname(os.path.realpath(__file__))
        message_template = os.path.join(current_directory,self.template_directory,'expected_message.json')
        with open(message_template,'r') as fp:
            expected_dict = json.loads(fp.read())

        return expected_dict

    def compare_dict(self):
        # Compare Response dict and expected dict using deepdiff
        response_dict = self.get_response_dict()
        expected_dict = self.get_expected_dict()
        diff = deepdiff.DeepDiff(expected_dict, response_dict, verbose_level=0)

        return diff

if __name__ == "__main__":
    # Testing s3utilities
    s3utilities = s3utilities()
    diff = s3utilities.compare_dict()
    pprint(f'Actual diff is {diff}')

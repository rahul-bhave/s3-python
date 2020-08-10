# s3-python
 
Compare json stored in the s3 bucket with pre-defined json format using deepdiff

Recently, I got a chance to work on the amazon s3 bucket, where I compared the JSON files stored in the s3 bucket with the pre-defined data structure stored as a dictionary object, using deepdiff. I can't actually replicate, the entire system but for the demo purpose, I am comparing json file stored in s3 bucket with pre-defined json format using deepdiff. I

Flow:
1. Read the json file from the S3 bucket.
2. Convert the json in the dict object.
3. Compare the json.dict with predefined.dict using deepdiff.

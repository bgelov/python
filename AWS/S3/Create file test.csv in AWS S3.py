#Create file test.csv in AWS S3

import boto3

s3 = boto3.resource('s3')
object = s3.Object('antismilebot-whitelist', 'test.csv')
s3_body = 'test test test'
object.put(Body=s3_body)
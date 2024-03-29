#Add item to list AWS DynamoDB
#key - chat_id
#list - chat_whitelist

import boto3
from boto3.dynamodb.conditions import Key

dynamodb_client = boto3.client('dynamodb', region_name='us-west-2')
dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
table = dynamodb.Table('antiSmileBot')

def add_user_to_chat_whitelist(chat_id, user_id):
    response = table.update_item(
        Key={
            "chat_id": chat_id
        },
        UpdateExpression="SET chat_whitelist = list_append(chat_whitelist, :i)",
        ExpressionAttributeValues={
            ':i': [user_id],
        },
        ReturnValues="UPDATED_NEW"
    )
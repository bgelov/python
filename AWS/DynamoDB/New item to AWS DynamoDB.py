#New item to AWS DynamoDB
import boto3
from boto3.dynamodb.conditions import Key

dynamodb_client = boto3.client('dynamodb', region_name='us-west-2')
dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
table = dynamodb.Table('antiSmileBot')

def new_chat_id(chat_id, chat_admins, chat_autoreply, chat_whitelist):
    response = table.put_item(
        Item = {
         "chat_id": chat_id,
         "chat_admins": chat_admins,
         "chat_autoreply": chat_autoreply,
         "chat_whitelist": chat_whitelist
        }
    )
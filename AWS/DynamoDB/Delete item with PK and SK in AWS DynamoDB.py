#Delete item with PK and SK in AWS DynamoDB
import boto3
from boto3.dynamodb.conditions import Key

dynamodb_client = boto3.client('dynamodb', region_name='us-west-2')
dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
table_whitelist = dynamodb.Table('antiSmileBot')

# Remove user from whitelist
# chat_id partition key and from_id sort key. In this case we write in json both keys
# https://beabetterdev.com/2022/04/22/how-to-delete-an-item-in-a-dynamodb-table-with-boto3/
def rem_from_whitelist(chat_id, sender_from):
    chat_id_str = str(chat_id)
    sender_from_str = str(sender_from)
    response = table_whitelist.delete_item(
        Key = {
         "chat_id": chat_id_str,
         "from_id": sender_from_str
        }
    )
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return True
    else:
        return False
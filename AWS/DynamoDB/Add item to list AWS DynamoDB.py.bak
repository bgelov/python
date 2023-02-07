#Add item to list AWS DynamoDB
#key - chat_id
#list - chat_whitelist

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
import json
import boto3


def lambda_handler(event, context):

    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Cars')
    
    try:
        response = table.delete_item(Key = event.get('Key'))
        
    except:
        return "Error deleting item"
    

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }

import json
import boto3

def lambda_handler(event, context):
        
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Cars')
    CarID = event['CarID']
    
    
    response = table.get_item(
        Key = {
            'CarID': CarID,
        }
    )
    
    Item = response['Item']
    
    return{
        'body' : json.dumps(Item)
    }
    

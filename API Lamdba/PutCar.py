import json
import boto3

def lambda_handler(event, context):
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Cars')
    exc = None
    
    print(event.get('Item'))
    
    response = table.put_item(Item=event.get('Item'))
        
    
    return{
        'status': 200,
        'response' : response
        }
    
   
    


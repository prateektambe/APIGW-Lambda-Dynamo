import boto3
dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(
    TableName : 'Cars',
    KeySchema=[
        {
            'AttributeName': 'CarID',
            'KeyType': 'HASH'
        }
    ],

    AttributeDefinitions=[

        {
            'AttributeName': 'CarID',
            'AttributeType': 'N'
        },

        {
            'AttributeName': 'Manufacturer',
            'AttributeType': 'S'
        },

        {
            'AttributeName': 'Model',
            'AttributeType': 'S'
        },
        
        {
            'AttributeName': 'Year',
            'AttributeType': 'S'
        },
    ],

    ProvisionedThroughput={

        'ReadCapacityUnits' : 2,
        'WriteCapacityUnits' : 2
    }
)
